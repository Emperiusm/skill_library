#!/usr/bin/env python3
"""Scan configured subreddits for video posts about tooling/pipelines.

Usage: python3 scan_videos.py [days]   (default 30)
Reads subreddits.yaml next to this skill. Outputs ranked JSON to stdout.
Source: Arctic Shift public API (same as reddit-outreach scan.py).
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VIDEO_DOMAINS = ("youtube.com/watch", "youtu.be/", "vimeo.com")


def load_subs():
    subs, days, min_score, max_deep = [], 30, 20, 8
    cfg = os.path.join(SKILL_DIR, "subreddits.yaml")
    try:
        in_subs = False
        with open(cfg) as f:
            for line in f:
                s = line.strip()
                if s.startswith("subreddits:"):
                    in_subs = True
                    continue
                if in_subs:
                    if s.startswith("- "):
                        subs.append(s[2:].strip())
                    elif s and not s.startswith("#"):
                        in_subs = False
                if s.startswith("days:"):
                    days = int(s.split(":")[1])
                if s.startswith("min_score:"):
                    min_score = int(s.split(":")[1])
                if s.startswith("max_deep_analysis:"):
                    max_deep = int(s.split(":")[1])
    except FileNotFoundError:
        pass
    return subs or ["blender", "gamedev"], days, min_score, max_deep


# Keywords that signal pipeline/tooling content (not just "look at my render").
TOOLING_KEYWORDS = [
    "blender", "ue5", "unreal", "unity", "godot", "pipeline", "workflow",
    "procedural", "houdini", "substance", "painter", "designer", "rig",
    "retopo", "retopology", "uv", "unwrap", "lod", "nanite", "bake",
    "baking", "sculpt", "zbrush", "marmoset", "rizom", "xatlas",
    "comfyui", "stable diffusion", "trellis", "tripo", "hunyuan",
    "text-to-3d", "image-to-3d", "mesh", "texture", "pbr", "material",
    "addon", "add-on", "plugin", "script", "automation", "batch",
    "geometry nodes", "shader", "optix", "kitbash", "photogrammetry",
    "gaussian splat", "nerf", "mocap", "mixamo", "marvelous",
    "world machine", "gaea", "terrain", "netcode", "rollback",
    "deterministic", "fixed point", "server", "backend", "ci/cd",
]

BASE = "https://arctic-shift.photon-reddit.com/api/posts/search"


def fetch(sub, after_epoch):
    q = urllib.parse.urlencode({
        "subreddit": sub, "limit": 100, "sort": "desc",
        "after": str(after_epoch),
    })
    req = urllib.request.Request(
        BASE + "?" + q,
        headers={"User-Agent": "Mozilla/5.0 (compatible; video-tooling-scout/1.0)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r).get("data", [])


def is_video_post(p):
    url = (p.get("url") or "").lower()
    if any(d in url for d in VIDEO_DOMAINS):
        return True
    if p.get("is_video"):
        return True
    media = p.get("media") or {}
    if isinstance(media, dict) and media.get("reddit_video"):
        return True
    return False


def main():
    subs, default_days, min_score, max_deep = load_subs()
    days = int(sys.argv[1]) if len(sys.argv) > 1 else default_days
    after = int(time.time()) - days * 86400
    out = []
    for sub in subs:
        try:
            posts = fetch(sub, after)
        except Exception as e:
            print(json.dumps({"warning": f"{sub}: {e}"}))
            continue
        for p in posts:
            if p.get("removed_by_category") or p.get("stickied"):
                continue
            if not is_video_post(p):
                continue
            score = p.get("score") or 0
            if score < min_score:
                continue
            text = (p.get("title", "") + " " + (p.get("selftext") or "")).lower()
            hits = sorted({k for k in TOOLING_KEYWORDS if k in text})
            # relevance = tooling keyword hits weighted by engagement.
            # Pure-sim / eye-candy posts with zero tooling signal get their
            # engagement contribution slashed so they can't outrank real
            # tooling content on votes alone .
            engagement = min(score, 500) / 50.0
            if not hits:
                engagement *= 0.2
            relevance = len(hits) * 10 + engagement
            out.append({
                "subreddit": p.get("subreddit"),
                "title": p.get("title"),
                "author": p.get("author"),
                "url": p.get("url"),
                "permalink": "https://www.reddit.com" + p.get("permalink", ""),
                "created_utc": p.get("created_utc"),
                "num_comments": p.get("num_comments"),
                "score": score,
                "tooling_hits": hits,
                "relevance": round(relevance, 1),
                "selftext_snippet": (p.get("selftext") or "")[:300],
            })
    out.sort(key=lambda x: x["relevance"], reverse=True)
    print(json.dumps({
        "meta": {"days": days, "subs": subs, "min_score": min_score,
                 "video_posts": len(out), "deep_analysis_cap": max_deep},
        "videos": out,
    }, indent=1))


if __name__ == "__main__":
    main()
