# Running the deepened pipeline locally

The scout's deepened pipeline (download, local transcribe, frame extract)
runs on any machine with Python 3.10+ and ffmpeg. The sandbox this repo's
automation runs in cannot do the transcription step: its network approval
system fires one approval card per HTTP request, and the Whisper model
download makes hundreds of them, so it can never complete there. On your
own machine there is no such gate. Set it up once, then it just works.

## One-time setup

```bash
# from the repo root
cd video-tooling-scout

python3 -m venv .venv
.venv/bin/pip install yt-dlp faster-whisper
# ffmpeg: apt install ffmpeg / brew install ffmpeg / choco install ffmpeg

# one-time Whisper model download (~800 MB, cached in ~/.cache/huggingface)
.venv/bin/python scripts/yt_transcribe.py --help >/dev/null
# or explicitly:
# .venv/bin/python -c "from faster_whisper import WhisperModel; WhisperModel('large-v3-turbo', device='cpu', compute_type='int8')"
```

Verify the model is cached:

```bash
ls ~/.cache/huggingface/hub/ | grep -i large-v3-turbo
```

## The deepened pipeline (per video)

```bash
ID=<video_id>   # e.g. m9oxz99Ysp0
URL="https://youtu.be/$ID"

# 1. download (resume with --continue if it stalls; .part files resume)
.venv/bin/python scripts/yt_download.py "$URL" --out work/$ID --quality high

# 2. transcribe locally (no API keys, no uploads, CPU)
.venv/bin/python scripts/yt_transcribe.py work/$ID/media.mp4 --model large-v3-turbo > work/$ID/transcript.json

# 3. extract 12 frames from the downloaded media
.venv/bin/python scripts/yt_frames.py "$URL" --out work/$ID/frames --from-video work/$ID/media.mp4 --count 12
```

Then read `work/$ID/transcript.json` and review the frames in
`work/$ID/frames/` yourself, and deepen the skill's audit with a
`## Video-observed evidence` section. Never invent transcript lines or
describe frames you did not read.

## Captions/metadata fallback

If a download fails or the video is gone, fall back without the media:

```bash
.venv/bin/python scripts/yt_summarize.py "$URL" --no-frames
```

and read `work/$ID/result.json`.

## Notes

- `--quality high` caps at 720p: enough for legible on-screen parameters,
  small enough to move fast.
- `--model base` or `--model tiny` are fine for quick drafts; large-v3-turbo
  is the quality default.
- A partial download is still usable: ffprobe the .part file and
  transcribe/extract frames from what downloaded.
