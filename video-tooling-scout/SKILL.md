---
name: "video_tooling_scout"
description: "Scout tooling videos on Reddit: pulls video posts from configured subreddits, summarizes each with the video-summarizer skill, extracts every tool/pipeline mentioned, and diffs it against every repo pipeline inventory (Aegis primary) to produce per-repo have-vs-need lists with gap recommendations. Trigger on requests to scan subreddits for tooling videos, audit video tooling against a repo, or compare found tools to an existing pipeline."
---

# Video Tooling Scout

## Purpose
Turn "what are other people using to make game assets?" into a maintained,
evidence-based answer. The bot watches configured subreddits for video posts,
extracts the tooling each video demonstrates (software, plugins, pipeline
stages, automation), and compares it against the pipeline inventory of every
one of Ehsan's repos (`references/*-pipeline-inventory.md`; Aegis is the
default/primary comparison). Output is per-repo have-vs-need plus recommended
gaps, so Ehsan can audit whether he needs a tool for a project or just keeps
it on the side as known.

## Workflow
1. **Scan** (`bin/scan_videos.py [days]`): pulls recent posts from the
   subreddits in `subreddits.yaml` via the Arctic Shift public API, keeps
   video posts (YouTube / Vimeo / native Reddit video), scores them by
   tooling relevance x engagement (zero-tooling-signal posts are downweighted
   regardless of engagement), and prints ranked JSON to stdout.
2. **Summarize** each top video with the deepened pipeline FIRST (the
   Cinematic Cavern recovery on 2026-09-27 proved this is what reaches
   FULL depth; captions/metadata are the fallback, not the default).
   The pipeline scripts live in this repo under
   `video-tooling-scout/scripts/` (`yt_download.py`, `yt_transcribe.py`,
   `yt_frames.py`, `yt_summarize.py`); local-machine setup is in
   `video-tooling-scout/LOCAL_SETUP.md`. Note: the sandbox cannot complete
   the Whisper model download (its network approval fires one card per
   HTTP request, and the model fetch makes hundreds), so local
   transcription is a local-machine step; the sandbox runs download +
   frames and falls back to captions/metadata for text.
   - **YouTube/Vimeo, deepened attempt first:** `python3
     scripts/yt_download.py "<url>" --out
     work/<video_id> --quality high` (if it times out, retry once with
     `--continue`; the .part file resumes), then
     `.venv/bin/python
     scripts/yt_transcribe.py
     work/<video_id>/media.* --model large-v3-turbo`, then `python3
     scripts/yt_frames.py "<url>" --out
     work/<video_id>/frames --from-video work/<video_id>/media.mp4 --count
     12`. Read the transcript and review the frames yourself; never invent
     transcript lines, values, or parameters, and never describe frames you
     did not read. A partial download is still usable: ffprobe the .part
     file and transcribe/frame-extract what downloaded.
   - **Fallback (captions/metadata only):** if the download fails, stalls
     with zero progress for 5+ minutes, or hits ANY approval gate, kill the
     process immediately with `process.kill` and never retry that video
     this run. Then run `python3
     scripts/yt_summarize.py "<url>"
     --no-frames` and read `work/<video_id>/result.json` yourself; never
     invent transcript lines or tool mentions.
   - **Native Reddit video (v.redd.it):** the video file itself is a short
     clip; the tooling signal is in the post text and comments. Pull full
     post text from the scan output and top comments with
     `bin/fetch_comments.py <post_id>[:num_comments] [...]` (post id = base-36
     id in the permalink; append `:num_comments` from the scan output so the
     script can detect Arctic Shift coverage gaps). When Arctic Shift returns
     zero comments for a post that has some, the script falls back to old
     Reddit JSON then the PullPush API automatically. Also pull metadata for
     any YouTube demo/tutorial links found in the comments: they often
     contain the real breakdown.
3. **Extract tooling** per video as a full-depth workflow audit (Cinematic Cavern
   standard). The exemplar is
   `~/workspace/user/files/cinematic-cavern-workflow-guide.md`; the public
   repo's worked skill `skills/cinematic-cavern/SKILL.md` is the same format.
   Every audit follows this canonical format:

   ```markdown
   ## <N>. "<Video title>" (<Creator>)

   Source: <URL> | <duration> | r/<sub> post <post_id> (score <n>)

   Tools used: <exact tools, versions, plugins>

   This audit reconstructs the exact workflow shown in the video, step by
   step, so another agent can follow the same process. Every phase has three
   parts: **Do** (the action), **Check** (how the human verifies it), and
   **Why** (the principle). The video's core method is: <one sentence>.

   ### Phase 1: <Name>

   **Do**
   1. <action>

   **Check**
   - <how the human verifies it>

   **Why**
   <the principle>

   ### The human method, distilled
   1. <decision habit, quoted where the creator stated it>

   **Depth status:** FULL | DEPTH-LIMITED (<why>) | NO-TOOLING (<why>)
   ```

   Required: exact tools used; exact parameters, brush names, values, costs,
   benchmarks, and quoted principles wherever the captions/comments/metadata
   support them. Never invent transcript lines or parameters; label
   inferences clearly. When captions are unavailable, mark that audit
   `DEPTH-LIMITED`, explain why, and note whether the depth-escalation
   option (media download) is enabled for this run and what it would take
   to reach FULL.
4. **Diff against every repo inventory** (`references/*-pipeline-inventory.md`):
   produce one have-vs-need table per repo. Aegis
   (`aegis-pipeline-inventory.md`) is the primary comparison and its table
   comes first; 2d3d, desktop-city, and solarempire follow. Mark each found
   tool/stage HAVE (repo already does this), PARTIAL (repo has a weaker/manual
   version), or NEED (repo lacks it). Do not mark HAVE on proxy evidence;
   verify against the audit or the repo tree via the GitHub skill. A tool can
   be NEED for one repo and HAVE for another; say so in each table.
5. **Gap alerts** (`references/p1-gaps.md`): check every extracted tool
   against the known P1/P2 gaps by keyword AND by meaning (a tool that fills
   the described need counts even if the wording differs). Matches go in a
   "Gap alerts" section at the very top of the report AND at the top of the
   chat summary to Ehsan. Do not bury them in the tables.
6. **Watchlist trending** (`bin/trend_watchlist.py`): after extraction, run
   `python3 bin/trend_watchlist.py --date YYYY-MM-DD "<tool 1>" "<tool 2>" ...`
   with every extracted tool name. The script compares them against
   `references/tooling-watchlist.md` (case-insensitive, token-overlap),
   appends "seen again <date>" to reappearing rows in place, and prints a
   "Watchlist trending" snippet: paste it into the report verbatim.
7. **Write the report** to `~/workspace/your_files/video-tooling-scout/`
   as `have-vs-need-YYYY-MM-DD.md` with the Output Contract below, and append
   genuinely new tools to `references/tooling-watchlist.md` (the keep-on-the-side list).

## Output Contract
Every run delivers:
- Gap alerts (from `p1-gaps.md` matches), first in the report and first in
  the chat summary.
- Videos scanned (count, subreddits, date range) and videos deeply analyzed
  (title, channel, URL, duration).
- Tooling extracted per video, each with a source quote or frame note.
- Per-repo have-vs-need tables (Aegis first): Tool/stage | Found in (video)
  | Status (HAVE/PARTIAL/NEED) | Repo evidence | Recommendation
  (adopt now / backlog / watchlist / skip + why).
- Watchlist trending snippet (from `bin/trend_watchlist.py`).
- Gap recommendations: the 3-5 highest-leverage NEEDs, each with what it
  replaces or unblocks in the repo pipeline and a concrete next step.
- Explicit non-goals: tools found but correctly skipped, with one-line reasons.

## Operating Rules
- No live browser anywhere in this loop. Reddit via Arctic Shift API
  (PullPush API as the comments fallback), videos via the video-summarizer
  skill (plain HTTP + local tools).
- **Depth mode (media download).** The deepened pipeline (download +
  local transcribe + frame review) is attempted FIRST for every
  YouTube/Vimeo video, per workflow step 2; captions/metadata are the
  fallback when the download fails or is blocked. Every run declares one
  mode at the start; Ehsan chooses the mode when the run is set up, and it
  is stated in the run report. Modes:
  - `off`: captions and metadata only; no downloads attempted.
    DEPTH-LIMITED audits stay limited. The conservative option; default
    only if Ehsan says so.
  - `ask` (interactive/chat runs only): the deepened attempt runs for each
    video only after Ehsan approves it in chat first ("this one needs a
    download to transcribe, approve?"). If he says no or doesn't answer,
    fall back to metadata + description and move on.
  - `pre-approved`: Ehsan grants a standing allowance of up to N media
    downloads per run (default 2, his call). The run attempts the deepened
    pipeline first for the top candidates without per-video prompts,
    highest relevance first. This is the default for scheduled/cron runs
    once Ehsan enables it.
  Hard limits regardless of mode: cap 3 media downloads per run, never
  download the same video twice in one run. Local transcription (Whisper
  model weights) is a local-machine step per LOCAL_SETUP.md: the sandbox
  cannot complete the model download because its network approval fires
  one card per HTTP request and the model fetch makes hundreds, an
  uncompletable loop. Never attempt a model download from the sandbox;
  kill it immediately if one starts. In the sandbox, the deepened pipeline
  is download + frame review, with captions/metadata as the text fallback. The
  approval-gate rule below is absolute: if ANY download hits
  `pending_user_confirmation` or an approval card, kill the process
  immediately with `process.kill` and skip that video; never retry it, never
  queue it for later in the run. A repeated approval prompt from the same
  host is a hard stop for that host for the rest of the run. Pre-approval
  covers the skill's own decision to download; it can never bypass a
  runtime approval gate, so worst case a blocked download is skipped, never
  a loop.
- **Approval rule: scheduled runs are strict, interactive runs allow exceptions.**
  Scheduled/cron runs: never trigger approval requests. The run's
  configured depth mode governs downloads (`off` = none; `pre-approved` =
  up to N deepened attempts, highest relevance first). If any command hits
  an approval gate (`pending_user_confirmation` or an approval card), kill
  the process immediately with `process.kill` and skip that item; never
  retry it. If the same host prompts more than 3 times in one run, stop
  hitting that host entirely for the rest of the run. Surface skipped items
  and the host in the report.
- **Interactive exception (chat runs only, never cron).** When Ehsan is
  present in chat, the depth mode defaults to `ask`: the deepened attempt
  runs for a video only with his explicit per-video go-ahead in chat first.
  Cap 3 downloads per run. The per-host 3-prompt kill guard still applies,
  so the worst case is a handful of taps, never a loop.
- Comparison target defaults to all four inventories with Aegis primary.
  When Ehsan names a single repo, lead with that repo's table but still run
  the others. Never reuse one repo's inventory for a different repo; if an
  inventory is missing or stale, re-derive it from that repo's audit first.
- A tool is HAVE only with repo evidence (file path, CI workflow, or audit
  citation). "Probably has it" is NEED until verified.
- Keep per-video cost sane: captions/metadata first, always. Cap deep
  analysis at 8 videos per run unless Ehsan asks for more.
- The watchlist (`tooling-watchlist.md`) is append-only institutional memory:
  never delete an entry, only annotate it (adopted, superseded, skipped,
  seen-again dates). `p1-gaps.md` is maintained the same way: annotate
  resolved/deprioritized gaps with a date, never delete rows.
- Honor the reddit-outreach hard lines if any step touches posting or
  commenting: this skill never posts, comments, or votes. It only reads.
