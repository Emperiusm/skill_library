#!/usr/bin/env python3
"""Scan YouTube channels for recent tooling/workflow videos.

Usage: python3 scan_youtube.py [days]   (default: youtube.yaml window_days)
Reads youtube.yaml next to this skill. Outputs ranked JSON to stdout.

Design (measured 2026-10-23, not assumed):
- Relevance search (ytsearch) is useless for freshness: its top results
  are years-old popular videos; a 30-day match-filter over 15 candidates
  yielded zero, and each candidate costs ~5s to extract.
- --dateafter on search results silently returns nothing, and this
  yt-dlp build has no date-sorted search.
- Channel /videos feeds ARE newest-first and list in ~2s per channel
  (flat playlist: id, title, duration, views; no dates). So: list each
  configured channel's newest few, fully extract only those (metadata
  only, no media downloads), and filter by upload_date client-side.
Deep analysis stays with the video-summarizer skill, exactly like Reddit
candidates go to the audit step.

yt-dlp binary: the video-summarizer venv's (its certifi bundle carries
the sandbox egress CA; see AGENTS.md), then ~/.local/bin, then PATH.
"""
import datetime
import json
import os
import subprocess
import sys

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YTDLP_CANDIDATES = [
    os.path.expanduser("~/workspace/skills/video-summarizer/.venv/bin/yt-dlp"),
    os.path.expanduser("~/.local/bin/yt-dlp"),
    "yt-dlp",
]

TOOLING_TERMS = [
    "workflow", "pipeline", "tutorial", "how to", "breakdown", "technique",
    "procedural", "geometry nodes", "shader", "rigging", "retopology",
    "baking", "comfyui", "houdini", "blender", "godot", "unreal", "unity",
    "substance", "gaussian", "photogrammetry", "vfx", "real-time",
    "realtime", "export", "import", "automation", "scripting", "addon",
    "plugin", "tips", "deep dive", "behind the scenes", "devlog",
]
NOISE_TERMS = [
    "gameplay", "let's play", "lets play", "walkthrough", "speedrun",
    "trailer", "teaser", "reaction", "tier list", "giveaway", "shorts",
    "live stream", "livestream", "podcast",
]


def load_config():
    cfg = {"window_days": 14, "per_channel_newest": 6, "min_duration_secs": 240,
           "channels": []}
    path = os.path.join(SKILL_DIR, "youtube.yaml")
    section = None
    with open(path) as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            if s.startswith("channels:"):
                section = "channels"
                continue
            if section == "channels" and s.startswith("- "):
                cfg["channels"].append(s[2:].strip().strip('"').strip("'"))
                continue
            section = None
            for key in ("window_days", "per_channel_newest", "min_duration_secs"):
                if s.startswith(key + ":"):
                    cfg[key] = int(s.split(":", 1)[1])
    return cfg


def find_ytdlp():
    for cand in YTDLP_CANDIDATES:
        if os.path.sep in cand:
            if os.path.isfile(cand):
                return cand
        else:
            return cand
    return None


def run_ytdlp(ytdlp, args, timeout=300):
    proc = subprocess.run([ytdlp] + args, capture_output=True, text=True, timeout=timeout)
    entries = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    warning = None
    if proc.returncode != 0 and not entries:
        warning = (proc.stderr or "").strip().splitlines()[-1] if proc.stderr else "yt-dlp failed"
    return entries, warning


def score(entry):
    title = (entry.get("title") or "").lower()
    desc = (entry.get("description") or "").lower()
    s = 0
    for term in TOOLING_TERMS:
        if term in title:
            s += 3
        elif term in desc:
            s += 1
    for term in NOISE_TERMS:
        if term in title:
            s -= 4
    views = entry.get("view_count") or 0
    if views >= 10000:
        s += 2
    elif views >= 1000:
        s += 1
    return s


def channel_url(handle):
    handle = handle.strip()
    if handle.startswith("http"):
        return handle.rstrip("/") + ("" if handle.endswith("/videos") else "/videos")
    return f"https://www.youtube.com/@{handle.lstrip('@')}/videos"


def main():
    cfg = load_config()
    days = int(sys.argv[1]) if len(sys.argv) > 1 else cfg["window_days"]
    cutoff = (datetime.date.today() - datetime.timedelta(days=days)).strftime("%Y%m%d")
    ytdlp = find_ytdlp()
    if not ytdlp:
        print(json.dumps({"error": "yt-dlp not found"}))
        return 1
    seen = {}
    warnings = []
    for handle in cfg["channels"]:
        flat, warning = run_ytdlp(ytdlp, [
            "-j", "--flat-playlist", "--no-warnings",
            "--playlist-end", str(cfg["per_channel_newest"]),
            channel_url(handle),
        ], timeout=120)
        if warning:
            warnings.append(f"{handle}: {warning}")
            continue
        fresh_ids = [
            e["id"] for e in flat
            if e.get("id") and (e.get("duration") or 0) >= cfg["min_duration_secs"]
        ]
        if not fresh_ids:
            continue
        urls = [f"https://www.youtube.com/watch?v={vid}" for vid in fresh_ids]
        entries, warning = run_ytdlp(ytdlp, ["-j", "--no-warnings", "--skip-download"] + urls)
        if warning:
            warnings.append(f"{handle}: {warning}")
            continue
        for e in entries:
            vid = e.get("id")
            if not vid or vid in seen:
                continue
            if (e.get("upload_date") or "00000000") < cutoff:
                continue
            seen[vid] = {
                "id": vid,
                "title": e.get("title"),
                "channel": e.get("channel") or e.get("uploader"),
                "url": f"https://www.youtube.com/watch?v={vid}",
                "upload_date": e.get("upload_date"),
                "duration_secs": e.get("duration"),
                "view_count": e.get("view_count"),
                "description_snippet": (e.get("description") or "")[:400],
                "source_channel": handle,
                "score": score(e),
            }
    ranked = sorted(seen.values(), key=lambda v: (-v["score"], -(v["view_count"] or 0)))
    print(json.dumps({
        "source": "youtube",
        "window_days": days,
        "channels_scanned": len(cfg["channels"]),
        "videos_found": len(ranked),
        "warnings": warnings,
        "videos": ranked,
    }, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
