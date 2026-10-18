# Have-vs-need: 2026-10-06

Daily video-tooling-scout run. Scan window: last 2 days (2026-10-04 to 2026-10-06).
Depth mode: `pre-approved` (max 2 media downloads, Ehsan 2026-09-27).

## Gap alerts

**None.** Extracted tools (EmberGen, Blender, After Effects, DaVinci Resolve)
match no P1/P2 gap in `references/p1-gaps.md` by keyword or meaning. EmberGen
is a real-time smoke simulation tool; the P1 gaps cover rigging/retargeting,
per-asset perf budgets, engine import validation, mesh compression, mesh
refinement with deviation metrics, AI-vendor acceptance specs, MCP-driven DCC,
production conversion, art bibles, shader skyline fill, and Godot import gates.
Nothing extracted this run fills or addresses any of them. The second post's
tool (Desmond, molecular dynamics) is a scientific simulation tool, not a game
pipeline, and was excluded from the diff entirely.

## Scan summary

- Subreddits queried: unity, unrealengine, godot, blender, houdini, substance3d,
  photogrammetry, gameassets, topology, aigamedev, comfyui, vibecoding,
  technicalart, proceduralgeneration, vfx, Simulated, 3Dmodeling, gamedev.
- Coverage gaps: `blender`, `vibecoding`, and `3Dmodeling` returned HTTP 422
  from Arctic Shift this run; their video posts were not scanned.
- Video posts returned: 2 (r/vfx x1, r/Simulated x1).
- Deep analysis cap: 8. Deeply analyzed: 2.

| # | Title | Creator | Source | Depth |
|---|-------|---------|--------|-------|
| 1 | "Trickle Down" - Music Video VFX Breakdown (Blender, After Effects, and Resolve - no AI) | carmo97 | https://v.redd.it/n2crnx72phth1 (r/vfx post 1wxm3m4, score 50, 5 comments) | DEPTH-LIMITED |
| 2 | I ran a 100-nanosecond molecular dynamics simulation of Ozempic bound to its receptor | arrestenbias | https://v.redd.it/xwqhr5wuwgth1 (r/Simulated post 1wxi8e6, score 40, 2 comments) | NO-TOOLING |

## 1. "Trickle Down" - Music Video VFX Breakdown (carmo97)

Source: https://v.redd.it/n2crnx72phth1 | r/vfx post 1wxm3m4 (score 50, 5 comments) | native clip (VFX breakdown reel)

Tools used: Blender, After Effects, DaVinci Resolve, EmberGen.

This audit reconstructs the workflow from the author's post text, the only
retrievable evidence. The core method is: build fully-CG scenes in Blender,
simulate smoke in EmberGen, and composite real footage with CG in After
Effects, finishing in DaVinci Resolve.

### Phase 1: Build CG scenes in Blender

**Do**
1. Produce scenes that are fully CG in Blender ("many of the scenes being
   fully CG", author's post).
2. Produce the remainder as real footage to be mixed with CG.

**Check**
- The breakdown reel compares final frames against their component passes;
  the reel itself is the verification that a given shot is CG, real footage,
  or a mix.

**Why**
Blender is the 3D scene builder; real footage grounds the shots that are not
fully CG.

### Phase 2: Simulate smoke in EmberGen

**Do**
1. Simulate the smoke elements in EmberGen (author: "Smoke sim done with
   Embergen :)").

**Check**
- EmberGen's real-time preview shows the sim before export; final check is the
  smoke composited over the shot in the breakdown reel.

**Why**
EmberGen gives interactive iteration speed on volumetrics that a CPU fluid sim
in Blender cannot.

### Phase 3: Composite in After Effects

**Do**
1. Combine real footage with Blender CG in After Effects ("combines real
   footage with Blender composited in After Effects", author's post).

**Check**
- The breakdown reel's before/after splits are the human's proof the composite
  holds: edges, motion, and integration of CG over live footage.

**Why**
AE is the compositing stage: it is where footage and render passes meet.

### Phase 4: Finish in DaVinci Resolve

**Do**
1. Finish/grade the composited edit in Resolve (named as the final tool in
   the author's pipeline).

**Check**
- (Inference, labeled) The 2+ year schedule ("2+ years in the making") implies
  the grade was iterated alongside the comps; the music video "The River, the
  Shore" (full video linked in the post) is the final check.

**Why**
Resolve is the finishing stage after compositing.

### The human method, distilled

1. "No AI" as a deliberate constraint: the title states the pipeline
   explicitly excludes AI tooling; every effect is simulated or rendered.
2. Mix real footage and full CG per shot rather than committing the whole
   video to one medium.
3. Iterate on a long schedule (2+ years); the breakdown reel doubles as the
   verification artifact (before/after splits).

**Depth status:** DEPTH-LIMITED. Native Reddit clip: no captions exist and the
post's 5 comments could not be retrieved (Arctic Shift HTTP 422, PullPush
returned zero, old.reddit/www.reddit.com JSON endpoints returned blocked
HTML). Evidence is the author's post text only: tools are named, one
principle is quoted ("Smoke sim done with Embergen :)"), but no parameters,
versions, render settings, or sim values appear. A media download (enabled
under this run's pre-approved allowance) would show the breakdown reel's
before/after splits and might reveal which scenes are CG vs comped, but it
would not yield executable workflow parameters: the reel narrates nothing.

## 2. "100-nanosecond molecular dynamics simulation of Ozempic" (arrestenbias)

Source: https://v.redd.it/xwqhr5wuwgth1
| r/Simulated post 1wxi8e6 (score 40, 2 comments) | native clip

Tools named: Desmond (Schrödinger molecular dynamics engine; author's comment
answering "what did you use?"). A commenter asked "Is that some GROMACS?",
which the author did not confirm; GROMACS is not used per the author's answer.

What the post states: the author, a computational drug discovery researcher,
ran a 100-nanosecond MD simulation of semaglutide (Ozempic's active
ingredient) bound to the GLP-1 receptor, modeling how the drug interacts with
the receptor.

**Depth status:** NO-TOOLING. This is a scientific visualization of a
pharmaceutical molecular-dynamics simulation. No engine, DCC, or game-asset
pipeline tool is involved. The scanner's "unity" tooling hit was a false
positive from the post text. Excluded from the diff and the watchlist.

---

## Per-repo have-vs-need

Repo evidence below is by keyword search of each inventory this run
(`embergen|after effects|resolve|davinci` all absent in all four inventories).

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Real-time smoke simulation (EmberGen) | #1 | NEED | Not in aegis-pipeline-inventory.md | Watchlist (already listed 2026-10-04, cinematics bucket; reappeared today) |
| Blender + After Effects + Resolve VFX finishing pipeline | #1 | NEED | No post-production finishing stage in inventory | Watchlist: new row added this run; post-production bucket only |
| Molecular dynamics sim (Desmond) | #2 | - | Out of scope | Skip: scientific sim, not game tooling |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Real-time smoke simulation (EmberGen) | #1 | NEED | Not in 2d3d-pipeline-inventory.md | Skip: 2D pixel-art pipeline, no volumetric sim fit |
| Blender + After Effects + Resolve VFX finishing pipeline | #1 | NEED | No finishing stage in inventory | Skip: no cinematics pipeline in 2d3d |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Real-time smoke simulation (EmberGen) | #1 | NEED | Not in desktop-city-pipeline-inventory.md | Watchlist: possible cozy-city atmospherics reference, cinematics bucket only |
| Blender + After Effects + Resolve VFX finishing pipeline | #1 | NEED | No finishing stage in inventory | Watchlist |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Real-time smoke simulation (EmberGen) | #1 | NEED | Not in solarempire-pipeline-inventory.md | Watchlist: nebula/exhaust VFX reference for space cinematics |
| Blender + After Effects + Resolve VFX finishing pipeline | #1 | NEED | No finishing stage in inventory | Watchlist: trailer finishing pattern |

## Gap recommendations (highest-leverage NEEDs)

None this run. Both extracted pipeline patterns (a real-time smoke sim and a
post-production finishing stack) are watchlist-grade, not gap-fillers: no P1/P2
gap was matched, and neither pattern unblocks anything in the four repo
pipelines. The standing highest-leverage items remain the 2026-10-05 set
(OmniChar acceptance-spec template for Aegis P1; Marigold V2 eval for 2d3d;
Flux klein on watchlist; YEDP notes for the rig gap; Hillaire LUT atmosphere).

## Watchlist trending

## Watchlist trending
- EmberGen real-time volumetric cloud/lightning with author-shared project file (first seen 2026-10-04, status WATCH; seen again 2026-10-06)
- MCP servers driving Blender/Unreal (agentic DCC) (first seen 2026-09-27, status BACKLOGGED; seen again 2026-09-28, 2026-10-05, 2026-10-06) **TRENDING**
- Squishy Volumes (free Blender MPM soft-body, fracture upcoming) (first seen 2026-09-27, status WATCH; seen again 2026-10-05, 2026-10-06) **TRENDING**
- Procedural ribbon cables (Blender GeoNodes) (first seen 2026-09-27, status WATCH; seen again 2026-10-05, 2026-10-06) **TRENDING**
- Light Wrangler Blender add-on (gobo lighting rigs) (first seen 2026-09-27, status WATCH; seen again 2026-10-05, 2026-10-06) **TRENDING**
- Codex CLI driving Blender via MCP (mannequin-guided camera motion) (first seen 2026-09-28, status WATCH; seen again 2026-10-05, 2026-10-06) **TRENDING**
- GPT Astra (mesh split, UV fix, CC0 texture replacement; Blender MCP looping) (first seen 2026-09-28, status WATCH; seen again 2026-10-05, 2026-10-06) **TRENDING**
- HBLink (Blender<->Houdini live-link + cache bridge, Gumroad, by Itz_Keay) (first seen 2026-09-28, status BACKLOGGED; seen again 2026-10-05, 2026-10-06) **TRENDING**
- Raup shell morphospace (flare/verm/spire parametric 3D generation; snug-fit rule verm=1/flare; Blender geo nodes + TouchDesigner; Blender/TouchDesigner files on Patreon) (first seen 2026-09-27, status WATCH; seen again 2026-10-05, 2026-10-06) **TRENDING**

Analyst note: all rows after EmberGen matched on the generic "Blender" token
only (audit #1 names Blender among four tools) and are weak signals for this
run, not genuine reappearances. The one strong reappearance is **EmberGen**
("Smoke sim done with Embergen :)", author of the r/vfx post), its second
sighting since 2026-10-04.

## New watchlist additions (2026-10-06)

Appended to `references/tooling-watchlist.md` (append-only) and synced to the
public mirror:

| Date seen | Tool / stage | Seen in | Status | Note |
|-----------|--------------|---------|--------|------|
| 2026-10-06 | Blender + After Effects + DaVinci Resolve VFX finishing pipeline | r/vfx "Trickle Down" music video breakdown (carmo97) | WATCH | Smoke sim done with Embergen (already watchlisted 2026-10-04); full video mixes real footage with fully-CG Blender scenes, composited in AE/Resolve, 2+ years in the making; post-production bucket only; DEPTH-LIMITED audit (post-text evidence only) |

## Depth-escalation usage

- Mode: `pre-approved`, allowance 2 media downloads.
- Downloads attempted: 0. Downloads succeeded: 0. Skipped on approval gate: 0.
- Neither video is YouTube/Vimeo: both are native Reddit clips. The skill's
  deepened pipeline (download + frames, captions as text fallback) targets
  YouTube/Vimeo; for native clips the tooling signal lives in post text and
  comments per the skill. The sandbox skill path contains no download script
  for v.redd.it, and per standing rules media-host requests that fire
  approval cards are killed immediately, so no download was attempted. For
  audit #1 a download would have shown the breakdown reel only; it would not
  have yielded executable workflow parameters (no captions exist for native
  clips; the reel narrates nothing).

## Non-goals (found but correctly skipped)

- Desmond / GROMACS (audit #2): scientific molecular-dynamics tools for drug
  discovery; no game-asset pipeline relevance. Not watchlisted.
- The r/vfx post's full music video ("The River, the Shore") and the
  breakdown clip itself: not downloaded (see Depth-escalation usage).
- r/blender, r/vibecoding, r/3Dmodeling: Arctic Shift returned HTTP 422 this
  run; their video posts went unscanned.

## Publishing

Staged in `~/workspace/video-tooling-scout-public/` as ready-to-publish
(browser upload when Ehsan is present; never unattended):
- 0 new skills: audit #1 is DEPTH-LIMITED (stays in this report only per the
  standing rule), audit #2 is NO-TOOLING.
- Full report: `docs/scout-reports/have-vs-need-2026-10-06.md` (+ README index
  row).
- Watchlist mirror synced: `video-tooling-scout/references/tooling-watchlist.md`.
- No README skills-table rows (no new skills).
