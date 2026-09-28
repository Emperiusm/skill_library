#!/usr/bin/env python3
"""yt_frames.py -- extract evenly-spaced visual frames from a YouTube video.

High-quality default: storyboard sprites (no download). For full-resolution
frames, download --quality high and use --from-video:

    python3 bin/yt_frames.py <url> --out DIR --from-video DIR/media.mp4 --count 12

Storyboard usage:
    python3 bin/yt_frames.py <url> --out DIR [--count 12]

Writes DIR/frame_000.jpg ... and prints JSON:
    {"ok": true, "frames": ["DIR/frame_000.jpg", ...], "frame_count": 12,
     "source": "storyboard" | "video"}

Requires: yt-dlp, Pillow (system python has both), ffmpeg for --from-video.
"""
import io
import json
import os
import shutil
import subprocess
import sys
import urllib.request

BIN = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(BIN)
YTDLP = shutil.which("yt-dlp") or os.path.join(SKILL_DIR, ".venv", "bin", "yt-dlp")

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"


def storyboard_info(url):
    p = subprocess.run(
        [YTDLP, "--extractor-args", "youtube:player_client=android",
         "--dump-json", "--skip-download", url],
        capture_output=True, text=True, timeout=60)
    if p.returncode != 0:
        return None, (p.stderr or "")[-200:]
    try:
        d = json.loads(p.stdout)
    except Exception:
        return None, "bad info json"
    # Prefer the largest storyboard (sb0 > sb1 > sb2).
    cands = [f for f in d.get("formats", [])
             if f.get("format_id", "").startswith("sb")]
    order = {"sb0": 0, "sb1": 1, "sb2": 2}
    cands.sort(key=lambda f: order.get(f.get("format_id"), 9))
    if not cands:
        return None, "no storyboards available"
    return cands[0], None


def extract_from_video(media, outdir, count):
    """High-quality frames via ffmpeg thumbnails from downloaded video."""
    try:
        p = subprocess.run(
            ["ffprobe", "-hide_banner", "-loglevel", "error",
             "-show_entries", "format=duration", "-of",
             "default=noprint_wrappers=1:nokey=1", media],
            capture_output=True, text=True, timeout=30)
        duration = float((p.stdout or "0").strip() or 0)
    except Exception:
        duration = 0
    if duration <= 0:
        return []
    saved = []
    for i in range(count):
        # Evenly spaced, skip first/last 2% to avoid black frames.
        t = duration * (0.02 + 0.96 * i / max(count - 1, 1))
        path = os.path.join(outdir, f"frame_{len(saved):03d}.jpg")
        p = subprocess.run(
            ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
             "-ss", str(round(t, 1)), "-i", media,
             "-frames:v", "1", "-q:v", "2", path],
            capture_output=True, text=True, timeout=60)
        if p.returncode == 0 and os.path.exists(path):
            saved.append(path)
    return saved


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"ok": False, "error": "usage: yt_frames.py <url> --out DIR [--count 12]"}))
        return 2
    url, outdir, count, from_video = sys.argv[1], None, 12, None
    args, i = sys.argv[2:], 0
    while i < len(args):
        if args[i] == "--out" and i + 1 < len(args):
            outdir, i = args[i + 1], i + 2
        elif args[i] == "--count" and i + 1 < len(args):
            count, i = int(args[i + 1]), i + 2
        elif args[i] == "--from-video" and i + 1 < len(args):
            from_video, i = args[i + 1], i + 2
        else:
            i += 1
    if not outdir:
        print(json.dumps({"ok": False, "error": "--out DIR is required"}))
        return 0
    os.makedirs(outdir, exist_ok=True)

    if from_video and os.path.exists(from_video):
        saved = extract_from_video(from_video, outdir, count)
        if saved:
            print(json.dumps({"ok": True, "frames": saved,
                              "frame_count": len(saved), "source": "video",
                              "note": f"{len(saved)} high-res frames from downloaded video"}))
        else:
            print(json.dumps({"ok": False, "error": "ffmpeg frame extraction failed"}))
        return 0

    sb, err = storyboard_info(url)
    if sb is None:
        print(json.dumps({"ok": False, "error": err}))
        return 0
    try:
        from PIL import Image
    except ImportError:
        print(json.dumps({"ok": False, "error": "Pillow not installed"}))
        return 0

    rows, cols = sb.get("rows", 5), sb.get("columns", 5)
    tw, th = sb.get("width", 160), sb.get("height", 90)
    frags = sb.get("fragments") or []
    template = sb.get("url", "")
    total = len(frags) * rows * cols
    if total == 0:
        print(json.dumps({"ok": False, "error": "empty storyboard"}))
        return 0

    # Evenly spaced thumbnail indexes across the whole video.
    want = sorted({round(i * (total - 1) / max(count - 1, 1)) for i in range(count)})
    # Group wanted indexes by sprite.
    per_sprite = rows * cols
    by_sprite = {}
    for w in want:
        by_sprite.setdefault(w // per_sprite, []).append(w % per_sprite)

    saved = []
    for sidx, cells in sorted(by_sprite.items()):
        sprite_url = template.replace("$M", str(sidx))
        try:
            req = urllib.request.Request(sprite_url, headers={"User-Agent": UA})
            raw = urllib.request.urlopen(req, timeout=30).read()
            sprite = Image.open(io.BytesIO(raw)).convert("RGB")
        except Exception:
            continue
        for cidx, w in zip(cells, [x for x in want if x // per_sprite == sidx]):
            r, c = divmod(cidx, cols)
            thumb = sprite.crop((c * tw, r * th, (c + 1) * tw, (r + 1) * th))
            # Upscale small thumbs for vision models (high-quality path).
            if tw < 320:
                thumb = thumb.resize((tw * 3, th * 3), Image.LANCZOS)
            path = os.path.join(outdir, f"frame_{len(saved):03d}.jpg")
            thumb.save(path, "JPEG", quality=95)
            saved.append(path)
    print(json.dumps({"ok": True, "frames": saved, "frame_count": len(saved),
                      "source": "storyboard",
                      "note": f"{len(saved)} evenly spaced frames from {total} storyboard thumbnails"}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
