#!/usr/bin/env python3
"""yt_extract.py -- summarize a video from just its URL. No live browser, no user effort.

Usage:
    yt_extract.py <url> [--out DIR] [--lang en] [--cookies cookies.txt]

YouTube path (primary): YouTube's own innertube player API with an Android
client profile, which is not bot-blocked. Returns title, author, duration,
description, keywords, view count, thumbnail, and caption tracks; captions are
fetched as timedtext XML and parsed into timestamped segments.

Other sites: yt-dlp (metadata + subtitles). YouTube with --cookies also works
via yt-dlp when innertube lacks something.

Prints JSON to stdout:
    {"ok": true, "title": ..., "duration_s": ..., "uploader": ...,
     "description": ..., "keywords": [...], "view_count": ...,
     "subtitles": [{"start": 12.3, "text": "..."}], "source": "innertube"}
or {"ok": false, "error": "..."}.

Requires: yt-dlp only for non-YouTube URLs (pip install yt-dlp).
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request

BIN = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(BIN)
# yt-dlp may live only in the skill venv (cron workers don't inherit PATH).
YTDLP = shutil.which("yt-dlp") or os.path.join(SKILL_DIR, ".venv", "bin", "yt-dlp")

INNERTUBE_KEY = "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
ANDROID_UA = "com.google.android.youtube/20.10.38 (Linux; U; Android 14)"


def http_get(url, headers=None, timeout=20):
    req = urllib.request.Request(url, headers=headers or {"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def http_post_json(url, payload, headers=None, timeout=25):
    data = json.dumps(payload).encode()
    h = {"Content-Type": "application/json", "User-Agent": UA}
    h.update(headers or {})
    req = urllib.request.Request(url, data=data, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def video_id(url):
    m = re.search(r"[?&]v=([\w-]{6,})", url)
    if m:
        return m.group(1)
    m = re.search(r"youtu\.be/([\w-]{6,})", url)
    if m:
        return m.group(1)
    m = re.search(r"/shorts/([\w-]{6,})", url)
    if m:
        return m.group(1)
    return None


def oembed_meta(url):
    """Title + author over plain HTTP; never bot-blocked."""
    try:
        q = urllib.parse.urlencode({"url": url, "format": "json"})
        d = json.loads(http_get(f"https://www.youtube.com/oembed?{q}").decode())
        return {"title": d.get("title", ""), "uploader": d.get("author_name", ""),
                "thumbnail": d.get("thumbnail_url", ""), "url": url}
    except Exception:
        return None


def innertube_player(vid, lang="en"):
    payload = {
        "videoId": vid,
        "context": {"client": {
            "clientName": "ANDROID", "clientVersion": "20.10.38",
            "androidSdkVersion": 34, "hl": lang, "gl": "US",
        }},
    }
    return http_post_json(
        f"https://www.youtube.com/youtubei/v1/player?key={INNERTUBE_KEY}",
        payload, headers={"User-Agent": ANDROID_UA})


def parse_timedtext(xml_text):
    """<p t="ms" d="ms">text</p> -> [{start, text}]."""
    out, seen = [], set()
    for m in re.finditer(r'<p t="(\d+)" d="\d+"[^>]*>(.*?)</p>', xml_text, re.S):
        start = int(m.group(1)) / 1000.0
        text = html.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))
        text = re.sub(r"\s+", " ", text).strip()
        if text and text not in seen:
            seen.add(text)
            out.append({"start": round(start, 1), "text": text})
    return out


def pick_track(tracks, lang="en"):
    def score(c):
        lc = c.get("languageCode", "")
        kind = c.get("kind", "manual")
        s = 0
        if lc == lang:
            s += 10
        elif lc.split("-")[0] == lang.split("-")[0]:
            s += 5
        if kind != "asr":
            s += 3
        return s
    cands = [c for c in tracks if c.get("baseUrl")]
    return max(cands, key=score) if cands else None


def youtube_extract(url, lang="en"):
    vid = video_id(url)
    if not vid:
        return None, "not a recognized YouTube URL"
    try:
        d = innertube_player(vid, lang)
    except Exception as e:  # noqa: BLE001
        return None, f"innertube player failed: {str(e)[:150]}"
    if d.get("playabilityStatus", {}).get("status") not in ("OK",):
        reason = d.get("playabilityStatus", {}).get("reason", "")
        return None, f"video not playable: {reason[:150]}"
    vd = d.get("videoDetails", {})
    tracks = d.get("captions", {}).get(
        "playerCaptionsTracklistRenderer", {}).get("captionTracks", [])
    subtitles, track_used = [], None
    track = pick_track(tracks, lang)
    if track:
        try:
            xml_text = http_get(track["baseUrl"],
                                headers={"User-Agent": UA}).decode("utf-8", "replace")
            subtitles = parse_timedtext(xml_text)
            track_used = f"{track.get('languageCode')}/{track.get('kind', 'manual')}"
        except Exception:  # noqa: BLE001 - captions optional, metadata still good
            subtitles = []
    try:
        duration = int(vd.get("lengthSeconds") or 0) or None
    except (ValueError, TypeError):
        duration = None
    info = {
        "ok": True,
        "title": vd.get("title", ""),
        "duration_s": duration,
        "uploader": vd.get("author", ""),
        "url": f"https://www.youtube.com/watch?v={vid}",
        "description": (vd.get("shortDescription", "") or "")[:2000],
        "keywords": vd.get("keywords", []),
        "view_count": vd.get("viewCount"),
        "thumbnail": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
        "subtitles": subtitles,
        "subtitle_count": len(subtitles),
        "caption_track": track_used,
        "source": "innertube",
    }
    if not subtitles:
        info["transcript_hint"] = ("This video has no caption tracks available "
                                   "(none published, or auto-captions not generated).")
    return info, None


# ---------------------------------------------------------------- yt-dlp path

def run(cmd, timeout=90):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def ytdlp_extract(url, outdir, lang="en", cookies=None):
    base = [YTDLP, "--skip-download", "--no-warnings"]
    if cookies:
        base += ["--cookies", cookies]
    p = run(base + ["--print", "%(title)s\t%(duration)s\t%(uploader)s\t%(webpage_url)s",
                    "--print", "%(description)s",
                    url])
    if p.returncode != 0:
        return None, (p.stderr or p.stdout or "unknown error")[-400:]
    lines = (p.stdout or "").strip().splitlines()
    parts = lines[0].split("\t") if lines else []
    try:
        dur = int(float(parts[1])) if len(parts) > 1 and parts[1] not in ("NA", "None", "") else None
    except (ValueError, IndexError):
        dur = None
    subs = None
    try:
        p2 = run(base + ["--write-auto-subs", "--write-subs", "--sub-langs", lang,
                         "--sub-format", "vtt",
                         "--output", os.path.join(outdir, "subs.%(ext)s"), url],
                 timeout=120)
        for f in os.listdir(outdir):
            if f.startswith("subs.") and f.endswith(".vtt"):
                subs = parse_vtt(os.path.join(outdir, f))
                break
    except Exception:  # noqa: BLE001
        subs = None
    return {
        "ok": True,
        "title": parts[0] if parts else "",
        "duration_s": dur,
        "uploader": parts[2] if len(parts) > 2 else "",
        "url": parts[3] if len(parts) > 3 else url,
        "description": (lines[1] if len(lines) > 1 else "")[:2000],
        "subtitles": subs or [],
        "subtitle_count": len(subs or []),
        "source": "yt-dlp" + ("+cookies" if cookies else ""),
    }, None


def parse_vtt(path):
    out, seen = [], set()
    ts_re = re.compile(r"(\d+:)?(\d+):(\d+)\.(\d+)")

    def to_s(m):
        h = int(m.group(1).rstrip(":")) if m.group(1) else 0
        return h * 3600 + int(m.group(2)) * 60 + int(m.group(3)) + int(m.group(4)) / 1000.0

    cur_start, buf = None, []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if "-->" in line:
                m = ts_re.search(line)
                if m:
                    if cur_start is not None and buf:
                        text = " ".join(buf)
                        if text not in seen:
                            seen.add(text)
                            out.append({"start": round(cur_start, 1), "text": text})
                    cur_start, buf = to_s(m), []
            elif line and not line.startswith("WEBVTT") and not line.startswith("NOTE") \
                    and not re.match(r"^\d+$", line):
                clean = re.sub(r"<[^>]+>", "", line)
                if clean and (not buf or buf[-1] != clean):
                    buf.append(clean)
    if cur_start is not None and buf:
        text = " ".join(buf)
        if text not in seen:
            out.append({"start": round(cur_start, 1), "text": text})
    return out


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"ok": False, "error": "usage: yt_extract.py <url> [--out DIR] [--lang en] [--cookies F]"}))
        return 2
    url, outdir, lang, cookies = sys.argv[1], None, "en", None
    args, i = sys.argv[2:], 0
    while i < len(args):
        if args[i] == "--out" and i + 1 < len(args):
            outdir, i = args[i + 1], i + 2
        elif args[i] == "--lang" and i + 1 < len(args):
            lang, i = args[i + 1], i + 2
        elif args[i] == "--cookies" and i + 1 < len(args):
            cookies, i = args[i + 1], i + 2
        else:
            i += 1

    is_yt = "youtube.com" in url or "youtu.be" in url
    if is_yt and not cookies:
        info, err = youtube_extract(url, lang)
        if info is not None:
            print(json.dumps(info, ensure_ascii=False))
            return 0
        # innertube failed: keep the error, try oEmbed for at least title/author
        oe = oembed_meta(url)
        if oe:
            oe.update({"ok": True, "duration_s": None, "subtitles": [],
                       "subtitle_count": 0, "source": "oembed",
                       "note": f"innertube failed ({err}); metadata via oEmbed only"})
            print(json.dumps(oe, ensure_ascii=False))
            return 0
        print(json.dumps({"ok": False, "error": err}))
        return 0

    tmp = outdir or tempfile.mkdtemp(prefix="yt_extract_")
    os.makedirs(tmp, exist_ok=True)
    info, err = ytdlp_extract(url, tmp, lang, cookies)
    if info is None and is_yt:
        oe = oembed_meta(url)
        if oe:
            oe.update({"ok": True, "duration_s": None, "subtitles": [],
                       "subtitle_count": 0, "source": "oembed",
                       "note": "yt-dlp blocked; metadata via oEmbed only"})
            print(json.dumps(oe, ensure_ascii=False))
            return 0
    if info is None:
        print(json.dumps({"ok": False, "error": err}))
        return 0
    print(json.dumps(info, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
