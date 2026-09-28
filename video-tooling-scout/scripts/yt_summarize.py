#!/usr/bin/env python3
"""yt_summarize.py -- one-command video summarization pipeline.

Usage:
    python3 bin/yt_summarize.py "<url>" [--out DIR] [--lang en]
        [--cookies F] [--frames N] [--quality high|mid|low]
        [--model large-v3-turbo] [--hq-frames] [--watch]
        [--watch-interval 600] [--watch-timeout 21600]
        [--no-transcribe] [--no-frames] [--force]

The whole interface is a single link. Pipeline:
  1. Metadata + captions via yt_extract.py (innertube, ~1s).
  2. Live detection. Active/upcoming lives report status and stop,
     unless --watch polls until the VOD is ready.
  3. Frames: storyboard sprites (fast). Full-res ffmpeg frames from
     downloaded video when available or when --hq-frames is set.
  4. Transcript: captions when present, else download (--quality high)
     and local faster-whisper transcription.
  5. One structured result.json with evidence sources, status,
     timings, and failure reasons.

Idempotent: re-running with the same --out reuses completed steps
unless --force is given. Partial downloads resume via yt-dlp.
No live browser is used at any step.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import time

BIN = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(BIN)
VENV_PY = os.path.join(SKILL_DIR, ".venv", "bin", "python")
YTDLP = shutil.which("yt-dlp") or os.path.join(SKILL_DIR, ".venv", "bin", "yt-dlp")
SYS_PY = "python3"
LIVE_STATES = ("is_live", "is_upcoming")


def run(cmd, timeout=None):
    """Run a command. Returns (rc, stdout, stderr); timeouts and
    crashes become structured results, never exceptions."""
    try:
        p = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=timeout)
        return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()
    except subprocess.TimeoutExpired as e:
        out = (e.stdout or "")
        out = out.decode() if isinstance(out, bytes) else out
        return 124, out.strip(), f"timed out after {timeout}s"
    except Exception as e:  # noqa: BLE001
        return 127, "", f"failed to run: {str(e)[:200]}"


def run_json(cmd, timeout=None):
    rc, out, err = run(cmd, timeout)
    if rc != 0 and not out:
        return {"ok": False, "error": err[-300:] or f"exit {rc}"}
    try:
        d = json.loads(out)
        if isinstance(d, dict):
            return d
        return {"ok": False, "error": "non-dict JSON output"}
    except Exception:  # noqa: BLE001
        return {"ok": False, "error": (err or out)[-300:] or "bad JSON"}


def video_id(url):
    for pat in (r"[?&]v=([\w-]{6,})", r"youtu\.be/([\w-]{6,})",
                r"/shorts/([\w-]{6,})", r"/live/([\w-]{6,})"):
        m = re.search(pat, url)
        if m:
            return m.group(1)
    return None


def is_youtube(url):
    return "youtube.com" in url or "youtu.be" in url


def live_status(url, timeout=60):
    """Fast live check via yt-dlp android client. Never raises."""
    if not is_youtube(url):
        return "not_live"
    rc, out, err = run(
        [YTDLP, "--extractor-args", "youtube:player_client=android",
         "--print", "%(live_status)s", "--skip-download", "--no-warnings",
         url],
        timeout=timeout)
    s = (out or "").strip().splitlines()
    s = s[0].strip() if s else ""
    return s if s in ("is_live", "is_upcoming", "was_live", "not_live",
                      "postlive") else "unknown"


def wait_for_vod(url, interval, timeout):
    """Poll until the video is no longer live. Returns final status."""
    start = time.time()
    while True:
        st = live_status(url)
        if st not in LIVE_STATES:
            return st
        if time.time() - start >= timeout:
            return "watch_timeout"
        time.sleep(interval)


def adaptive_frame_count(duration_s):
    base = (duration_s or 600) // 120
    return max(12, min(24, base))


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"ok": False,
                          "error": "usage: yt_summarize.py <url> [options]"}))
        return 2
    url = sys.argv[1]
    outdir, lang, cookies = None, "en", None
    frames_n, quality, model = None, "high", "large-v3-turbo"
    hq_frames, watch = False, False
    watch_interval, watch_timeout = 600, 21600
    no_transcribe, no_frames, force = False, False, False
    args, i = sys.argv[2:], 0
    while i < len(args):
        a = args[i]
        if a == "--out" and i + 1 < len(args):
            outdir, i = args[i + 1], i + 2
        elif a == "--lang" and i + 1 < len(args):
            lang, i = args[i + 1], i + 2
        elif a == "--cookies" and i + 1 < len(args):
            cookies, i = args[i + 1], i + 2
        elif a == "--frames" and i + 1 < len(args):
            frames_n, i = int(args[i + 1]), i + 2
        elif a == "--quality" and i + 1 < len(args):
            quality, i = args[i + 1], i + 2
        elif a == "--model" and i + 1 < len(args):
            model, i = args[i + 1], i + 2
        elif a == "--watch-interval" and i + 1 < len(args):
            watch_interval, i = int(args[i + 1]), i + 2
        elif a == "--watch-timeout" and i + 1 < len(args):
            watch_timeout, i = int(args[i + 1]), i + 2
        elif a == "--hq-frames":
            hq_frames, i = True, i + 1
        elif a == "--watch":
            watch, i = True, i + 1
        elif a == "--no-transcribe":
            no_transcribe, i = True, i + 1
        elif a == "--no-frames":
            no_frames, i = True, i + 1
        elif a == "--force":
            force, i = True, i + 1
        else:
            i += 1

    vid = video_id(url) or "video"
    if not outdir:
        outdir = os.path.join(SKILL_DIR, "work", vid)
    os.makedirs(outdir, exist_ok=True)
    result_path = os.path.join(outdir, "result.json")
    if os.path.exists(result_path) and not force:
        print(open(result_path).read())
        return 0

    t0 = time.time()
    timings, failures = {}, []
    result = {"ok": True, "url": url, "video_id": vid,
              "completed_at": None}

    # ---- 1. metadata + captions -------------------------------------
    t = time.time()
    meta_cmd = [SYS_PY, os.path.join(BIN, "yt_extract.py"), url,
                "--out", outdir, "--lang", lang]
    if cookies:
        meta_cmd += ["--cookies", cookies]
    meta = run_json(meta_cmd, timeout=120)
    timings["extract_s"] = round(time.time() - t, 1)
    if not meta.get("ok"):
        result.update({"ok": False, "error": meta.get("error"),
                       "failures": [{"step": "extract",
                                     "error": meta.get("error")}]})
        finish(result, result_path, outdir)
        return 0
    result.update({k: meta.get(k) for k in
                   ("title", "uploader", "duration_s", "description",
                    "keywords", "view_count", "thumbnail")})
    duration_s = meta.get("duration_s")
    if frames_n is None:
        frames_n = adaptive_frame_count(duration_s)

    # ---- 2. live detection ------------------------------------------
    t = time.time()
    lstatus = live_status(url)
    timings["live_check_s"] = round(time.time() - t, 1)
    if lstatus in LIVE_STATES and watch:
        t = time.time()
        lstatus = wait_for_vod(url, watch_interval, watch_timeout)
        timings["watch_s"] = round(time.time() - t, 1)
    result["live_status"] = lstatus
    if lstatus in LIVE_STATES:
        result.update({
            "status": "live",
            "transcript": {"source": "none", "reason": "video is live"},
            "frames": {"source": "none", "reason": "video is live"},
            "note": ("Video is currently live (HLS throttled to ~0.05x "
                     "realtime, unusable). Re-run with --watch or after "
                     "the stream ends and the VOD is processed.")})
        finish(result, result_path, outdir, timings, failures)
        return 0
    if lstatus == "watch_timeout":
        result.update({
            "ok": False, "status": "watch_timeout",
            "error": "live stream did not end within --watch-timeout"})
        finish(result, result_path, outdir, timings, failures)
        return 0

    # ---- 3. transcript: captions or local transcription --------------
    transcript = {"source": "none", "segments": [], "segment_count": 0}
    media_file = None
    subs = meta.get("subtitles") or []
    if subs and not no_transcribe:
        transcript = {"source": "captions",
                      "caption_track": meta.get("caption_track"),
                      "segments": subs, "segment_count": len(subs)}
    elif not no_transcribe:
        t = time.time()
        dl_cmd = [SYS_PY, os.path.join(BIN, "yt_download.py"), url,
                  "--out", outdir, "--quality", quality, "--timeout", "1800"]
        if cookies:
            dl_cmd += ["--cookies", cookies]
        dl = run_json(dl_cmd, timeout=1900)
        timings["download_s"] = round(time.time() - t, 1)
        if dl.get("ok"):
            media_file = dl["file"]
            result["media_file"] = media_file
            t = time.time()
            tr = run_json(
                [VENV_PY, os.path.join(BIN, "yt_transcribe.py"),
                 media_file, "--model", model, "--lang", lang],
                timeout=5400)
            timings["transcribe_s"] = round(time.time() - t, 1)
            if tr.get("ok"):
                transcript = {
                    "source": "local-whisper", "model": model,
                    "detected_language": tr.get("detected_language"),
                    "segments": tr.get("segments", []),
                    "segment_count": tr.get("segment_count", 0)}
                with open(os.path.join(outdir, "transcript.json"),
                          "w") as fh:
                    json.dump(transcript, fh, ensure_ascii=False)
            else:
                failures.append({"step": "transcribe",
                                 "error": tr.get("error")})
        else:
            failures.append({"step": "download", "error": dl.get("error")})
    result["transcript"] = transcript

    # ---- 4. frames ----------------------------------------------------
    frames = {"source": "none", "files": [], "frame_count": 0}
    if not no_frames:
        t = time.time()
        frames_dir = os.path.join(outdir, "frames")
        fr_cmd = [SYS_PY, os.path.join(BIN, "yt_frames.py"), url,
                  "--out", frames_dir, "--count", str(frames_n)]
        # Prefer full-res video frames when we already downloaded media,
        # or when the caller explicitly asked for HQ frames (downloads).
        if hq_frames and not media_file:
            dl2 = run_json(
                [SYS_PY, os.path.join(BIN, "yt_download.py"), url,
                 "--out", outdir, "--quality", quality, "--timeout", "1800"],
                timeout=1900)
            if dl2.get("ok"):
                media_file = dl2["file"]
                result["media_file"] = media_file
            else:
                failures.append({"step": "download_for_frames",
                                 "error": dl2.get("error")})
        if media_file and os.path.exists(media_file):
            fr_cmd += ["--from-video", media_file]
        fr = run_json(fr_cmd, timeout=600)
        timings["frames_s"] = round(time.time() - t, 1)
        if fr.get("ok"):
            frames = {"source": fr.get("source"),
                      "files": fr.get("frames", []),
                      "frame_count": fr.get("frame_count", 0),
                      "note": fr.get("note")}
        else:
            failures.append({"step": "frames", "error": fr.get("error")})
    result["frames"] = frames

    result["status"] = ("complete" if transcript["segment_count"] or
                        frames["frame_count"] else "metadata_only")
    finish(result, result_path, outdir, timings, failures)
    return 0


def finish(result, result_path, outdir, timings=None, failures=None):
    import time as _t
    if timings is not None:
        result["timings_s"] = timings
    if failures:
        result["failures"] = failures
    result["completed_at"] = _t.time()
    result["workdir"] = outdir
    try:
        with open(result_path, "w") as fh:
            json.dump(result, fh, ensure_ascii=False)
    except Exception:  # noqa: BLE001
        pass
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
