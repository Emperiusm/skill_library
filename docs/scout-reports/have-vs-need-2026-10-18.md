# Video tooling scout: have-vs-need 2026-10-18

Run: daily-video-tooling-scout, 2026-10-18 08:18 ET. Depth mode: `pre-approved`
(max 2 media downloads). No live browser anywhere in this loop. Per the goal
workspace rule, this report lives in the goal's hidden_files/ (bookkeeping),
not in your_files/.

## Gap alerts (p1-gaps.md matches)

**None.** Neither video this run fills or touches a P1/P2 gap. Extracted tools
(Houdini + OctaneRender render showcase; Unity engine mention) match no gap
keyword or meaning in references/p1-gaps.md.

## Videos scanned

- Range: last 2 days (2026-10-16 to 2026-10-18).
- Subreddits queried: 18 (unity, unrealengine, godot, blender, houdini,
  substance3d, photogrammetry, gameassets, topology, aigamedev, comfyui,
  vibecoding, technicalart, proceduralgeneration, vfx, Simulated, 3Dmodeling,
  gamedev).
- **r/proceduralgeneration scan failed: Arctic Shift returned HTTP 429** for
  that sub. The other 17 subs returned normally. Arctic Shift 429 is a hard
  stop, so no Arctic Shift requests were made after the scan (fetch_comments.py
  was bypassed entirely).
- Video posts found: **2** (min_score 20). Both are native Reddit video
  (v.redd.it); neither has captions or a transcript.

## Comment coverage failure (all three sources)

Both posts are comment-light (1 and 2 comments) and comment retrieval failed
on every fallback this run: PullPush API HTTP 429 for both post IDs, old
Reddit JSON HTTP 403 (bot-wall, as documented in fetch_comments.py). No
post text or comment detail was obtainable for either video.

## Videos deeply analyzed

### 1. "Houdini with Octane.." (Roberty_85)

Source: https://www.reddit.com/r/Houdini/comments/1x7rvbs/houdini_with_octane/ |
clip https://v.redd.it/pwo48k7a8wvh1 | r/Houdini post 1x7rvbs (score 45)

Tools used: Houdini (SideFX, version undisclosed); OctaneRender GPU renderer
(OTOY; inferred from title "with Octane", meaning rendered with Octane for
Houdini rather than Karma/Mantra; the exact plugin version is not stated).

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. The video's core method is: a
Houdini scene rendered with Octane. The post is a showcase clip, not a
tutorial: no selftext, no comments, no node graph, no render settings, and no
tutorial narration are available.

### Phase 1: Scene setup (unobserved)

**Do**
1. (Unknown: not visible from the post.)

**Check**
- Not verifiable: post body is empty, no comments, no breakdown.

**Why**
- This phase is an inference placeholder. The title attests only that the
  finished frames were produced with Houdini and Octane.

### The human method, distilled

1. Not extractable: the showcase format gives no decisions, parameters, or
   quoted principles.

**Depth status:** DEPTH-LIMITED (native Reddit clip, no captions; empty
selftext; 1 comment, all comment APIs failed this run: Arctic Shift 429,
PullPush 429, old Reddit 403). The pre-approved depth-escalation allowance
(max 2 downloads) was not spent on this clip: it is a render showcase, not a
tutorial, so a download plus frame review could confirm the render engine look
and any visible scene content but could not supply a phased workflow with
Do/Check/Why, parameters, or quoted principles. FULL depth is unreachable
without the creator posting a breakdown.

### 2. "We're working on In Control: Rocketry, a rocket builder and
spaceflight sim with real orbital mechanics!" (InControlRocketry)

Source: https://www.reddit.com/r/unity/comments/1x7kqyk/were_working_on_in_control_rocketry_a_rocket/
| clip https://v.redd.it/gas3vb13vuvh1 | r/unity post 1x7kqyk (score 26)

Tools used: Unity (engine, from r/unity subreddit context only; version and
any plugins undisclosed). Post selftext describes a rocket builder and
spaceflight sim with real orbital mechanics, a Turing-complete wiring system
for control panels (sensors, inputs, outputs), in development since 2025.

This is a game announcement, not a tooling demo. No asset pipeline, DCC, or
plugin is named anywhere in the available post text; relevance 0.1.

**Depth status:** NO-TOOLING (no tooling signal beyond the Unity engine
mention; announcement format; 2 comments, comment APIs failed this run).

## Tooling extracted (with source)

- Houdini (SideFX): title "Houdini with Octane..", r/Houdini post 1x7rvbs,
  score 45.
- OctaneRender (OTOY GPU spectral renderer): title inference from the same
  post ("with Octane" = rendered with Octane for Houdini, per standard r/Houdini
  titling; exact meaning cannot be confirmed without the clip).
- Unity: subreddit context only, r/unity post 1x7kqyk (game announcement, no
  pipeline detail).

## Per-repo have-vs-need (Aegis primary)

| Tool/stage | Found in (video) | Aegis | 2d3d | Desktop City | Solarempire | Recommendation |
|---|---|---|---|---|---|---|
| Houdini (DCC/sim) | #1 | NEED | NEED | NEED | NEED | watchlist; no repo uses Houdini; existing Houdini watchlist rows already cover the patterns |
| OctaneRender (offline GPU spectral renderer) | #1 | NEED | NEED | NEED | NEED | watchlist; offline film/VFX renderer, no game-runtime attach point in any repo pipeline (inventories show in-engine/Blender/Godot render stages only) |
| Unity engine | #2 | n/a | n/a | n/a | n/a | skip; engine mention only, no pipeline information |

Repo evidence: none of the four inventories
(aegis-pipeline-inventory.md, 2d3d-pipeline-inventory.md,
desktop-city-pipeline-inventory.md, solarempire-pipeline-inventory.md) mention
Houdini or Octane. Aegis renders via multi-view render QA and the Sprite2D
render pipeline; Desktop City via headless Blender sprite renders; 2d3d via
the Godot renderer. All four therefore NEED these tools in the formal sense,
with the recommendation above.

## Watchlist trending

trend_watchlist.py --date 2026-10-18 was run against the skill's watchlist.
Its raw auto-match flagged 9 rows as "seen again 2026-10-18" by token overlap
on "Houdini" and "Unity". **All 9 annotations were false positives** (today's
posts carry no workflow content: one render-showcase title, one game
announcement) and were reverted in place, consistent with the 2026-10-17
false-positive note already in the watchlist.

```
## Watchlist trending (corrected)
- (none) No genuine reappearances this run. Raw script output of 9
  "seen again 2026-10-18" matches was token-overlap noise and was reverted.
```

## Gap recommendations

None this run: with no extractable workflow and no P1/P2 gap matches, there
are no adoption recommendations. OctaneRender joins the watchlist as a render
engine choice alternative to the existing Karma XPU rows, pending a future
post with actual render settings or comparisons.

## Explicit non-goals (found, correctly skipped)

- Unity engine (rocketry game announcement): no pipeline information; nothing
  to adopt.
- Houdini as a DCC for any repo: none of Ehsan's pipelines use Houdini; the
  existing Houdini pattern rows stay as watch items.

## New watchlist additions

- 2026-10-18 | OctaneRender for Houdini (OTOY GPU spectral renderer plugin for
  Houdini) | r/Houdini 'Houdini with Octane..' (Roberty_85) | WATCH |
  DEPTH-LIMITED audit (native Reddit clip, showcase only; title implies Octane
  render of Houdini scene; no node graph, parameters, or comments; comment
  APIs rate-limited this run); render-engine choice alternative to
  Karma/Mantra XPU on existing watchlist entries; no attach point in any repo
  pipeline today. (Appended to the skill's watchlist and synced to the
  skill_library mirror's references copy.)

## Depth-escalation usage

- Downloads attempted: 0 (allowance was 2, pre-approved by Ehsan 2026-09-27).
- Downloads succeeded: 0. Downloads skipped: 2 (both videos are native Reddit
  clips, not YouTube/Vimeo; neither has captions; neither is a tutorial, so
  the deepened pipeline could not reach FULL depth).
- Approval gates hit: 0 (no download was started; no gate encountered).

## skill_library staging (step 8)

- DEPTH-LIMITED / NO-TOOLING audits with no extractable workflow stay in this
  report only. No new, expanded, or variant skills staged this run.
- Full report copy staged at
  ~/workspace/video-tooling-scout-public/docs/scout-reports/have-vs-need-2026-10-18.md;
  docs/scout-reports/README.md index updated.
- Watchlist row synced into the mirror's
  video-tooling-scout/references/tooling-watchlist.md. No README skills-table
  changes needed.
- Note: the standing daily push pipeline (push_skill_library.py + the
  daily-skill-library-push cron) remains blocked on the github-write token
  scope (civic-ledger only; skill_library writes 403). Staged files accumulate
  locally until Ehsan widens the token.

## Run metadata

- Scan: exit 0, 2 videos, 1 sub (r/proceduralgeneration) failed with HTTP 429.
- Comment APIs: Arctic Shift 429 (hard stop observed), PullPush 429,
  old Reddit 403. fetch_comments.py not used (it would have re-hit Arctic
  Shift first).
- Watchlist script: 9 false-positive annotations reverted in place; no genuine
  trending additions.
