---
name: "video_tooling_scout"
description: "Scout tooling videos on Reddit: pulls video posts from configured subreddits, summarizes each from captions/metadata, extracts every tool/pipeline mentioned, and diffs it against your pipeline inventories to produce have-vs-need lists with gap recommendations. Trigger on requests to scan subreddits for tooling videos, audit video tooling against a pipeline, or compare found tools to an existing pipeline."
---

# Video Tooling Scout

## Purpose
Turn "what are other people using to make game assets?" into a maintained,
evidence-based answer. The scout watches configured subreddits for video
posts, extracts the tooling each video demonstrates (software, plugins,
pipeline stages, automation), and compares it against your pipeline
inventories (`references/*-pipeline-inventory.md`; your primary inventory is
the default comparison). Output is per-inventory have-vs-need plus
recommended gaps, so you can audit whether you need a tool for a project or
just keep it on the side as known.

## Workflow
1. **Scan** (`bin/scan_videos.py [days]`): pulls recent posts from the
   subreddits in `subreddits.yaml` via the Arctic Shift public API, keeps
   video posts (YouTube / Vimeo / native Reddit video), scores them by
   tooling relevance x engagement (zero-tooling-signal posts are downweighted
   regardless of engagement), and prints ranked JSON to stdout.
2. **Summarize** each top video. Two paths, both captions/metadata only
   (see the no-approval rule below):
   - **YouTube/Vimeo:** a captions-first summarizer of your choice,
     e.g. `<your-summarizer> "<url>"`. Read its result yourself; never invent
     transcript lines or tool mentions. If a video has no captions, use its
     metadata + description and move on, unless the interactive exception
     below applies.
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
3. **Extract tooling** per video: named software, plugins/add-ons, pipeline
   stages (modeling, retopo, UV, bake, rig, LOD, QA, engine import), and any
   automation (scripts, CI, batch processing). Record one quote or frame
   reference per claim.
4. **Diff against every pipeline inventory**
   (`references/*-pipeline-inventory.md`): produce one have-vs-need table per
   inventory. Your primary inventory's table comes first; additional
   inventories follow. Mark each found tool/stage HAVE (the pipeline already
   does this), PARTIAL (the pipeline has a weaker/manual version), or NEED
   (the pipeline lacks it). Do not mark HAVE on proxy evidence; verify
   against the repo tree or its audit. A tool can be NEED for one inventory
   and HAVE for another; say so in each table.
5. **Gap alerts** (`references/p1-gaps.md`): check every extracted tool
   against the known P1/P2 gaps by keyword AND by meaning (a tool that fills
   the described need counts even if the wording differs). Matches go in a
   "Gap alerts" section at the very top of the report AND at the top of the
   operator's chat summary. Do not bury them in the tables.
6. **Watchlist trending** (`bin/trend_watchlist.py`): after extraction, run
   `python3 bin/trend_watchlist.py --date YYYY-MM-DD "<tool 1>" "<tool 2>" ...`
   with every extracted tool name. The script compares them against
   `references/tooling-watchlist.md` (case-insensitive, token-overlap),
   appends "seen again <date>" to reappearing rows in place, and prints a
   "Watchlist trending" snippet: paste it into the report verbatim.
7. **Write the report** to your reports directory (e.g.
   `~/video-tooling-scout-reports/`) as `have-vs-need-YYYY-MM-DD.md` with
   the Output Contract below, and append genuinely new tools to
   `references/tooling-watchlist.md` (the keep-on-the-side list).

## Output Contract
Every run delivers:
- Gap alerts (from `p1-gaps.md` matches), first in the report and first in
  the operator's summary.
- Videos scanned (count, subreddits, date range) and videos deeply analyzed
  (title, channel, URL, duration).
- Tooling extracted per video, each with a source quote or frame note.
- Per-inventory have-vs-need tables (primary first): Tool/stage | Found in
  (video) | Status (HAVE/PARTIAL/NEED) | Pipeline evidence |
  Recommendation (adopt now / backlog / watchlist / skip + why).
- Watchlist trending snippet (from `bin/trend_watchlist.py`).
- Gap recommendations: the 3-5 highest-leverage NEEDs, each with what it
  replaces or unblocks in the pipeline and a concrete next step.
- Explicit non-goals: tools found but correctly skipped, with one-line
  reasons.

## Operating Rules
- No live browser anywhere in this loop. Reddit via Arctic Shift API
  (PullPush API as the comments fallback), videos via captions/metadata
  (plain HTTP + local tools).
- **Approval rule: scheduled runs are strict, interactive runs allow exceptions.**
  Scheduled/cron runs: never trigger approval requests. Captions and metadata
  only: never download video files, never download model files, never fetch
  from hosts that prompt for approval. If any command hits an approval gate,
  kill the process immediately and skip that item; never retry it. If the
  same host prompts more than 3 times in one run, stop hitting that host
  entirely for the rest of the run. Surface skipped items and the host in the
  report.
- **Interactive exception (chat runs only, never cron).** When the operator
  is present in chat, a high-relevance video with no captions may be
  downloaded for local transcription ONLY with their explicit per-video
  go-ahead in chat first (ask: "this one needs a download to transcribe,
  approve?"). Cap 3 downloads per run. The per-host 3-prompt kill guard still
  applies, so the worst case is a handful of taps, never a loop. If they say
  no or don't answer, fall back to metadata + description and move on.
- Comparison target defaults to all inventories with the primary first.
  When the operator names a single inventory, lead with that inventory's
  table but still run the others. Never reuse one inventory for a different
  pipeline; if an inventory is missing or stale, re-derive it from that
  pipeline's repo/audit first.
- A tool is HAVE only with pipeline evidence (file path, CI workflow, or
  audit citation). "Probably has it" is NEED until verified.
- Keep per-video cost sane: captions/metadata first, always. Cap deep
  analysis at 8 videos per run unless the operator asks for more.
- The watchlist (`tooling-watchlist.md`) is append-only institutional memory:
  never delete an entry, only annotate it (adopted, superseded, skipped,
  seen-again dates). `p1-gaps.md` is maintained the same way: annotate
  resolved/deprioritized gaps with a date, never delete rows.
- This skill never posts, comments, or votes. It only reads.
