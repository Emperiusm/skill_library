#!/usr/bin/env python3
"""yt_transcribe.py -- local speech-to-text fallback for videos with no captions.

Usage:
    .venv/bin/python bin/yt_transcribe.py <media.mp4> [--model large-v3-turbo] [--lang en] [--vad]

Extracts 16kHz mono audio with ffmpeg, transcribes with faster-whisper (CPU),
prints JSON: {"segments": [{"start": 1.2, "end": 3.4, "text": "..."}], ...}

High-quality default: large-v3-turbo (~800MB, downloaded once to
~/.cache/huggingface). Use --model base or tiny only for quick drafts.
--vad enables Silero VAD (helps noisy speech, hurts music).
"""
import json
import os
import subprocess
import sys
import tempfile

# httpx (via huggingface_hub) crashes parsing this environment's no_proxy
# value ("[::1]" -> "Invalid port"). It is only used for localhost bypass;
# dropping it is safe for model downloads.
for _v in ("no_proxy", "NO_PROXY"):
    os.environ.pop(_v, None)


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"ok": False, "error": "usage: yt_transcribe.py <media> [--model base] [--lang en]"}))
        return 2
    media = sys.argv[1]
    model, lang, vad, beam = "large-v3-turbo", "en", False, 10
    args, i = sys.argv[2:], 0
    while i < len(args):
        if args[i] == "--model" and i + 1 < len(args):
            model, i = args[i + 1], i + 2
        elif args[i] == "--lang" and i + 1 < len(args):
            lang, i = args[i + 1], i + 2
        elif args[i] == "--beam" and i + 1 < len(args):
            beam, i = int(args[i + 1]), i + 2
        elif args[i] == "--vad":
            vad, i = True, i + 1
        else:
            i += 1
    if not os.path.exists(media):
        print(json.dumps({"ok": False, "error": f"media not found: {media}"}))
        return 0
    wav = os.path.join(tempfile.mkdtemp(prefix="yt_tr_"), "audio.wav")
    p = subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
         "-i", media, "-ar", "16000", "-ac", "1", wav],
        capture_output=True, text=True)
    if p.returncode != 0 or not os.path.exists(wav):
        print(json.dumps({"ok": False, "error": f"ffmpeg audio extract failed: {p.stderr[-300:]}"}))
        return 0
    try:
        from faster_whisper import WhisperModel
        wm = WhisperModel(model, device="cpu", compute_type="int8")
        segments, info = wm.transcribe(wav, language=lang, beam_size=beam,
                                       vad_filter=vad,
                                       condition_on_previous_text=True)
        out = [{"start": round(s.start, 1), "end": round(s.end, 1),
                "text": s.text.strip()} for s in segments
               if s.text.strip()]
        print(json.dumps({"ok": True, "model": model,
                          "detected_language": info.language,
                          "segments": out, "segment_count": len(out)},
                         ensure_ascii=False))
    except Exception as e:  # noqa: BLE001
        print(json.dumps({"ok": False, "error": f"transcription failed: {str(e)[:300]}"}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
