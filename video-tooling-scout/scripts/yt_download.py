#!/usr/bin/env python3
"""yt_download.py -- download a YouTube video's media without a browser.

Usage:
    python3 bin/yt_download.py <url> --out DIR [--quality low|mid|high] [--timeout 300]

quality low: smallest format with audio (best for transcription).
quality mid: ~360p (storyboard fallback for frames).
quality high: ~720p (best for high-quality frame extraction and transcription).

Uses yt-dlp with the Android player-client profile, which is not bot-blocked.
Prints JSON: {"ok": true, "file": "DIR/<name>.mp4", ...}
Live streams download via HLS and may stall; a timeout reports ok:false
instead of hanging forever.
"""
import json
import os
import shutil
import subprocess
import sys

BIN = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(BIN)
YTDLP = shutil.which("yt-dlp") or os.path.join(SKILL_DIR, ".venv", "bin", "yt-dlp")

FORMATS = {"low": "worst[acodec!=none]/worst",
           "mid": "bv*[height<=360]+ba/b[height<=360]/bv*+ba/b",
           "high": "bv*[height<=720]+ba/b[height<=720]/bv*+ba/b"}


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"ok": False, "error": "usage: yt_download.py <url> --out DIR [--quality low|mid]"}))
        return 2
    url, outdir, quality, timeout, cookies = sys.argv[1], None, "low", 300, None
    args, i = sys.argv[2:], 0
    while i < len(args):
        if args[i] == "--out" and i + 1 < len(args):
            outdir, i = args[i + 1], i + 2
        elif args[i] == "--quality" and i + 1 < len(args):
            quality, i = args[i + 1], i + 2
        elif args[i] == "--timeout" and i + 1 < len(args):
            timeout, i = int(args[i + 1]), i + 2
        elif args[i] == "--cookies" and i + 1 < len(args):
            cookies, i = args[i + 1], i + 2
        else:
            i += 1
    if not outdir:
        print(json.dumps({"ok": False, "error": "--out DIR is required"}))
        return 0
    os.makedirs(outdir, exist_ok=True)
    fmt = FORMATS.get(quality, FORMATS["low"])
    cmd = [YTDLP, "--extractor-args", "youtube:player_client=android",
           "--continue", "--retries", "10", "--retry-sleep", "5",
           "--concurrent-fragments", "8"]
    if cookies:
        cmd += ["--cookies", cookies]
    cmd += ["-f", fmt, "-o", os.path.join(outdir, "media.%(ext)s"), url]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        print(json.dumps({"ok": False, "error": f"download timed out after {timeout}s "
                          "(live streams often stall; storyboards still work for frames)"}))
        return 0
    files = [os.path.join(outdir, f) for f in os.listdir(outdir)
             if f.startswith("media.") and not f.endswith(".part")]
    if p.returncode != 0 or not files:
        err = (p.stderr or "")[-300:]
        print(json.dumps({"ok": False, "error": f"download failed: {err}"}))
        return 0
    f = max(files, key=os.path.getsize)
    print(json.dumps({"ok": True, "file": f,
                      "size_bytes": os.path.getsize(f), "quality": quality}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
