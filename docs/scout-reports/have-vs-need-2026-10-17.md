# Video tooling scout: have-vs-need 2026-10-17

Run: daily cron `daily-video-tooling-scout`, Sat 2026-10-17 08:18 EDT.
Depth mode: `pre-approved` (max 2 media downloads/run, enabled by Ehsan 2026-09-27).
Depth escalation used: **0 attempted / 0 succeeded / 0 skipped** (see Depth note).
Scan: `/usr/bin/python3 bin/scan_videos.py 2` over 18 subreddits, Oct 15-17 2026.
**Result: scan succeeded, 6 video posts** (no warnings, no per-sub errors).

Report: `hidden_files/have-vs-need-2026-10-17.md` (goal workspace; the body's
`~/workspace/your_files/video-tooling-scout/` path is stale per goal rules).

## Depth note

Only 6 posts in the 2-day window, and 2 of them (FLUX 3 Image Klein, no-symmetry
cube sculpt) are the same posts audited 2026-10-16, re-scanned because the
windows overlap. They were NOT re-audited: the cube post's comments are
unchanged (same 3 comments re-fetched), and the FLUX comments re-check failed
with Arctic Shift HTTP 422 (transient API error, not an approval gate; not
retried in a loop). Yesterday's audits stand for both.

Of the 4 new posts, 3 are native Reddit clips (tooling signal in post text +
comments, fully retrieved via `bin/fetch_comments.py`, Arctic Shift, no
failures) and 1 is a YouTube video (Barcelona). For Barcelona,
`yt_summarize.py --no-transcribe --no-frames` returned metadata + description
with transcript source `none`: **no captions exist** for it. No media download
was attempted: the video is a 109-second product flythrough with no narration
or visible UI, so frames would show showcase footage only, not a workflow.
The pre-approved allowance (2) went unused. No approval gates were hit
anywhere in this run.

## Gap alerts

**No P1/P2 gap was filled today.** Explicit checks against `references/p1-gaps.md`
(keyword AND meaning):

- The Barcelona pack's "120 FPS at FULL HD" is a vendor perf claim for a
  finished district, not per-asset performance budgets (no tri counts, texel
  densities, or draw-call budgets disclosed): it does NOT fill Aegis's P1
  per-asset perf-budget gap.
- The scan's `rig` hit on the Barcelona post is a substring artifact: it
  matches the first three letters of "right" in "recorded right on location".
  No rigging, skinning, or retargeting is disclosed anywhere: it does NOT
  fill Aegis's P1 rigging / skinning / animation-retarget gap.
- The Barcelona pack discloses no mesh compression, virtual-texture output,
  or mesh-refinement deviation metrics: it does NOT fill Aegis's P1
  mesh-compression or mesh-refinement gaps.
- The squad-combat sim's deterministic replay checking is a reproducibility
  technique, not a validation gate: it fills neither Aegis's P1 automated
  engine import validation gate nor 2d3d's P1 asset import validation gate
  (no naming/dims/pivot/manifest checks of any kind).
- The squad sim discloses no written acceptance spec for generated assets,
  no MCP-driven DCC loop, no art bible, no shader skyline fill, and no
  Godot import validation. The VFX showreel and desk-process clips disclose
  no tools at all.

## Videos scanned

6 video posts across 18 subreddits (Oct 15-17, 2026). Ranked by the scan's
tooling-relevance x engagement score; the 4 new ones were deeply analyzed.
The 2 repeats were not re-audited (see Depth note).

## Audits

### 1. "80 km on foot to capture Barcelona in Unreal Engine? We tried!" (stXbr / Scans Factory)

Source: https://www.youtube.com/watch?v=nP9vhZnNsd8 | YouTube, 109 s, 3,910 views | r/unrealengine post 1x6w4z3 (score 32, 1 comment)
Channel: Scans Factory. Video title on YouTube: "Barcelona - Plaça Reial - Unreal Engine 5 | 4K Flythrough".

Tools used: **Unreal Engine 5**, **RealityScan** (hashtag `#realityscan`),
**Lumen** (hashtag `#lumen`), **FAB** (pack sold at fab.com/s/eba8d877568d),
**Blueprints**, VFX/Audio. No versions, no capture settings, no cleanup or
modular-kit rules disclosed.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: capture a real district on foot, sell it as a
modular UE5 asset pack with three lighting scenarios.

### Phase 1: On-foot capture

**Do**
1. Walk "80 km on foot to capture Barcelona's unique vibe" (description).
2. Capture "Plaça Reial surrounded by narrow streets, architecture, local
   spots, and landmarks" (post selftext).
3. Record "props, foliage, sounds ... right on location" (selftext).

**Check**
- Coverage claimed: "Over 20,000 m² of a captured district, featuring Gothic
  Quarter architecture, Catalan streets, landmarks, props, and foliage"
  (description). No capture pattern (overlap, photo count, walking grid) was
  disclosed, so this is the vendor's stated coverage, not a verified recipe.

**Why**
- (Inference) On-foot capture of a real district trades studio control for
  authentic architecture, props, and sound; the 80 km figure is the vendor's
  evidence for coverage, not a method.

### Phase 2: Package as a modular city-building kit

**Do**
1. Ship "over 1,400 assets in total for modular city building"
   (description).
2. Include "VFX/Audio/Blueprints & detailed technical documentation"
   (description).

**Check**
- Asset count (1,400+) and the documentation claim are vendor figures; no
  module list, naming convention, or kit rules were disclosed.

**Why**
- A modular kit (rather than one baked district) is what makes the capture
  reusable: buyers rearrange the same assets into new streets.

### Phase 3: Three dynamic lighting scenarios

**Do**
1. Ship "3 Dynamic Lighting Scenarios - Day, Sunset, and Overcast/Rain"
   (description; selftext repeats "3 dynamic lighting scenarios (Day, Sunset,
   and Overcast/Rain)").

**Check**
- The flythrough demonstrates all three scenarios. No Lumen settings,
  light rigs, or weather-system parameters were disclosed.

**Why**
- (Inference) One captured district, three lighting moods: lighting is the
  cheap multiplier on capture work, since geometry is captured once.

### Phase 4: Performance claim

**Do**
1. Claim: "Achieve 120 FPS at FULL HD on high scalability settings"
   (description).

**Check**
- No hardware, no per-asset budgets, no profiling method disclosed. This is
  a vendor claim, unverified, and not a recipe.

**Why**
- (Inference) The FPS claim is the pack's performance story; without
  hardware or budgets it cannot be reproduced or checked.

### The human method, distilled
1. **Capture real, package modular**: the district is the raw material, the
   1,400-asset kit is the product.
2. **Lighting multiplies capture**: three scenarios from one geometry set.
3. **Sell the numbers**: 80 km, 1,400 assets, 20,000 m², 120 FPS are the
   pack's evidence, all vendor-stated.

**Depth status:** PARTIAL (full metadata + description with exact figures;
no captions exist; no capture workflow, no settings, no code). A media
download would add flythrough footage only, not a workflow. Distinct from the
2026-09-27 photogrammetry rows (frame extractor, SAM cleanup, Planer, Cave
Expedition): this is a commercial capture-to-FAB-pack pipeline, not a tool
or a recipe, so it is watchlisted, not skill-staged (fails the compression
test: another agent could not execute a capture from this evidence).

### 2. "Seeded squad-combat simulation in the browser: terrain, weather, forces and unit-level decision making" (EmeraldOnFire101)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x6tlyo/seeded_squadcombat_simulation_in_the_browser/ | native Reddit clip, 48 s | r/proceduralgeneration post 1x6tlyo (score 27, 9 comments)
Playable at https://sim.shaykas.com/?seed=19 (link in selftext; not fetched, out of read-only scan scope).

Tools used: browser-based sim (engine/framework undisclosed). No code, no repo,
no language disclosed.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: one seed determines everything, and a hashed event
log plus replay checking makes every run exactly reproducible.

### Phase 1: Seed determines the battle

**Do**
1. Generate "each battle ... from a seed" (selftext).
2. Pick one of four map types per seed: "a bocage hamlet, open ridge farmland,
   a highway junction or a market town, each with its own weather" (selftext).
3. Give "one in ten seeds ... a tank" (selftext).
4. Make "battles ... seed specific, so you can share a link to an exact fight"
   (selftext).

**Check**
- Same seed URL reproduces the same fight. (Author's stated behavior; the
  clip is 48 s of one seed, not a proof.)

**Why**
- Seed-as-URL turns a battle into a shareable, debuggable artifact: a bug
  report is a link, not a description.

### Phase 2: Separate RNG streams per system

**Do**
1. Use "separate RNG streams per system" (selftext).

**Check**
- (Inference) A change to one system's randomness (e.g. weather rolls) does
  not shift every other system's rolls; each stream is independently
  reproducible.

**Why**
- Per-system streams isolate randomness: tuning one system cannot silently
  re-roll the whole battle, which is what makes replay checking tractable.

### Phase 3: Hashed event log + replay checking

**Do**
1. Keep "an event log with a hash" (selftext).
2. Run "replay checking, so any run can be reproduced exactly" (selftext).

**Check**
- Replay the same seed and compare the event-log hash: a mismatch means
  nondeterminism crept in somewhere. (Author's stated mechanism; hash
  algorithm and log format undisclosed.)

**Why**
- The hash turns "is this deterministic?" from a belief into a checkable
  property: any divergence in any system changes the log hash.

### Phase 4: Per-soldier deterministic decisions

**Do**
1. Give "soldiers each ... a deterministic decision algorithm that responds
   to their perception of their environment and personal values" (author's
   comment, verbatim).
2. Morale/cohesion drive behavior: "a soldier with low morale who is pinned
   down might try to flee and need to be re-rallied by his squad leader.
   Soldiers with high morale and squad cohesion will execute tactical
   attacks like stacking up on a building's windows and throwing grenades
   through them" (author's comment).

**Check**
- Same perception + values produce the same decision on replay (follows from
  Phase 3). No decision tables, thresholds, or perception radii disclosed.

**Why**
- Decisions from perception + values (not from randomness) keep the sim
  deterministic while still producing readable tactical behavior: fleeing,
  rallying, stacking, grenading are all downstream of two numbers.

### Phase 5: Radio operator to platoon HQ

**Do**
1. Give "each squad ... a radio operator via which they reach platoon HQ,
   which makes decisions on where to engage and if to provide fire support"
   (author's comment).

**Check**
- (Inference) Squad-level decisions and platoon-level decisions are separate
  layers: squads decide tactics, HQ decides engagement and fire support.

**Why**
- The radio-operator link is the hierarchy: local perception stays local,
  and only the HQ layer spends shared resources (fire support).

### Phase 6: The open question (decision model)

**Do**
1. Commenter ericpruitt proposed "a decision model ... make decisions for
   the commands and maybe the individual soldiers."
2. Author: "I've been meaning to test out a decision model with it. I think
   it could certainly be fun, but my only worry is it would be too
   computationally intensive for a [browser]" (comment truncated in
   retrieval at "for a"; the sentence is cut off in the source).

**Check**
- Unresolved in-thread: no decision-model test was posted, no compute
  measurement exists.

**Why**
- (Inference) A learned decision model would break the determinism the whole
  design is built on (Phases 2-3) unless its outputs are also hashed and
  replay-checked, which is the cost the author is weighing.

### The human method, distilled
1. **Seed everything, share by URL**: a battle is a link.
2. **Streams per system**: isolate randomness so tuning one system does not
   re-roll the world.
3. **Hash the log, replay the run**: determinism is a check, not a hope.
4. **Decisions from perception + values**: morale and cohesion are the two
   numbers that produce tactics.
5. **Hierarchy through radio**: squads fight, HQ spends fire support.

**Depth status:** PARTIAL (full post text + all 9 comments with the complete
decision architecture quoted; no code, no RNG/hash details, no thresholds).
Staged as a new skill (see Staged skills): the architecture is executable as
a design pattern, and no existing skill covers seeded determinism with
hashed replay checking. (The 2026-09-27 "Deterministic-vs-learned bot eval
harness" row is an eval harness for bots, a different tool.)

### 3. "VFX Showreel 2026 | Igor Sandimirov" (R3animatr)

Source: https://www.reddit.com/r/Houdini/comments/1x6onxo/vfx_showreel_2026_igor_sandimirov/ | native Reddit clip, 27 s preview | r/Houdini post 1x6onxo (score 231, 10 comments)
Full reel: https://youtu.be/ifS32_6vaJU (linked in selftext; not fetched: it is a linked video, not the post itself).

Tools used: undisclosed. Posted in r/Houdini, which suggests Houdini, but no
tool, version, or technique is named anywhere in post text or comments.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
No phases are recoverable: the clip is a 27-second preview montage and the
comments are reactions plus one piece of presentation advice.

### The human method, distilled
1. None extractable. (Commenter advice, attributed: for a professional
   showreel, avoid "a song thats so intense and has explicit language";
   "let the work speak for itself with something instrumental and maybe do
   some sound design. Would love to hear the liquid of the lego terminator
   or the ignition of the fire on the Futur logo!" — msvart, score 1.
   Commenters also praised "the last one especially. Cool abstract fire.
   Almost looks like an abstract underwater fire." — MindofStormz, score 7.)

**Depth status:** DEPTH-LIMITED (showcase only; tools undisclosed; no
workflow). A media download would add montage footage only.

### 4. "The process of creating a desk!" (6Pseudo6)

Source: https://www.reddit.com/r/3Dmodeling/comments/1x6zrb2/the_process_of_creating_a_desk/ | native Reddit clip, 11 s | r/3Dmodeling post 1x6zrb2 (score 65, 3 comments)

Tools used: undisclosed. Selftext is empty. No software, render settings, or
technique named anywhere in post or comments.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
No phases are recoverable: the title promises a process, the 11-second clip
and the thread deliver none.

### The human method, distilled
1. None extractable. (Comments: "modern art" — South_Composer_8666; "Now
   draw the rest of the owl." with the draw-the-owl meme link —
   Tall_Addendum_368; AutoModerator's process-details boilerplate.)

**Depth status:** DEPTH-LIMITED (showcase only; tool undisclosed; empty
selftext). A media download would add 11 seconds of footage, not a workflow.

## Per-repo have-vs-need

Tool/stage keys: A = Barcelona photogrammetry-to-UE5 FAB pack (RealityScan +
Lumen); B = Seeded deterministic sim (per-system RNG streams, hashed event
log, replay checking, morale/value soldier decisions); C = VFX showreel
2026; D = Desk-process clip.

### Aegis (primary)

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| A photogrammetry -> UE5 pack | #1 Barcelona | NEED | Foundry is TRELLIS-2 generation; no photogrammetry capture stage, no RealityScan route, no FAB-pack workflow | watchlist (alternative intake route, vendor product not a recipe) |
| A 120 FPS claim | #1 Barcelona | NEED | No per-asset perf budgets; a vendor FPS claim is not a budget | skip (unverified claim, no method) |
| B seeded determinism + hashed replay | #2 squad sim | PARTIAL | Deterministic Rust zone sim exists (Q16.16 fixed-point, SoA store), but no per-system RNG streams, no hashed event log, no replay-checking harness | backlog (cheap determinism harness: streams + hash + replay check) |
| B morale/value soldier decisions | #2 squad sim | NEED | No NPC decision layer in sim (gameplay modules are stubs) | watchlist (pattern for a future ai/NPC module) |
| C VFX showreel | #3 showreel | NEED | No VFX stage; tools undisclosed | skip |
| D desk process | #4 desk | NEED | No modeling stage; tool undisclosed | skip |

### 2d3d

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| A photogrammetry -> UE5 pack | #1 Barcelona | PARTIAL | Reference-driven art pipeline exists (Depth Anything 3 + SAM 2 reconstruction, plate extraction); no RealityScan route, no UE5 | watchlist (capture-pattern evidence for the reference pipeline) |
| B seeded determinism + hashed replay | #2 squad sim | PARTIAL | Golden-path bot plays the level per commit; seeded generators exist (`pipeline/proc`, seeded); no per-system RNG streams, no hashed event log, no replay checking | backlog (replay-check the golden-path bot via a hashed event log) |
| B morale/value soldier decisions | #2 squad sim | NEED | No NPC decision layer | skip (no NPC sim in scope) |
| C VFX showreel | #3 showreel | NEED | No VFX stage; tools undisclosed | skip |
| D desk process | #4 desk | NEED | No modeling stage; tool undisclosed | skip |

### Desktop City

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| A photogrammetry -> UE5 pack | #1 Barcelona | PARTIAL | Reference extraction exists (`tools/extract_reference_world.py`, `gen_town_reference.py`); headless Blender sprite path exists; no photogrammetry capture, no UE5 | watchlist (real-district capture as reference input is the closest fit) |
| B seeded determinism + hashed replay | #2 squad sim | PARTIAL | Procedural generators (`tools/procedural_art.py`, `city_*`) are seeded in spirit; no per-system RNG streams, no hashed event log, no replay checking | watchlist (pattern: streams + hash would make city-gen diffs debuggable) |
| B morale/value soldier decisions | #2 squad sim | NEED | No NPC decision layer (residents are simulated, not decision-driven) | skip |
| C VFX showreel | #3 showreel | NEED | No VFX stage; tools undisclosed | skip |
| D desk process | #4 desk | NEED | No modeling stage; tool undisclosed | skip |

### Solarempire

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| A photogrammetry -> UE5 pack | #1 Barcelona | NEED | Pipeline is Meshy-GLB-in, Blender stages; no photogrammetry capture, no UE5 | skip (wrong engine, vendor product) |
| B seeded determinism + hashed replay | #2 squad sim | PARTIAL | Pipeline stages are deterministic in practice (audit + optimization reports with measured figures); no hashed event log or replay checking | watchlist (hash the stage outputs to catch nondeterminism) |
| B morale/value soldier decisions | #2 squad sim | NEED | No NPC decision layer | skip |
| C VFX showreel | #3 showreel | NEED | No VFX stage; tools undisclosed | skip |
| D desk process | #4 desk | NEED | No modeling stage; tool undisclosed | skip |

## Watchlist trending

Verbatim output from `bin/trend_watchlist.py` (2 auto-matches), with
false-positive correction: the script matches on token overlap, and BOTH of
its hits are NOT genuine reappearances. Zero genuine reappearances today.

- Flux klein 9B/4B distilled variants + CCTech/Flux Klein ComfyUI node pack
  (first seen 2026-10-05, status WATCH; seen again 2026-10-16, 2026-10-17)
  **TRENDING** — FALSE: the 2026-10-17 auto-match was the same 2026-10-16
  FLUX 3 post re-scanned in the overlapping window, not a new mention.
- FLUX 3 Image Klein (5.6B, Black Forest Labs, native ComfyUI) (first seen
  2026-10-16, status WATCH; seen again 2026-10-17) — FALSE: same post
  re-scanned, already audited 2026-10-16; comments re-check failed (Arctic
  Shift HTTP 422). Both rows annotated in place in
  `references/tooling-watchlist.md` to say so.

New watchlist additions this run (2):

- Scans Factory Barcelona photogrammetry-to-UE5 pack (RealityScan + Lumen, FAB)
- Seeded deterministic browser sim (per-system RNG streams, hashed event log, replay checking)

## Gap recommendations

1. **Hashed event log + replay checking (Aegis zone sim, backlog).** The
   strongest transferable technique today: per-system RNG streams plus a
   hashed event log turns "is this deterministic?" into a checkable
   property. Aegis already has a deterministic Rust sim; what it lacks is
   the harness that proves it. Next step: log zone-sim events with a hash
   per run and replay-check in CI; a hash mismatch on replay is the
   nondeterminism alarm.
2. **Same harness for 2d3d's golden-path bot (2d3d, backlog).** The bot
   already plays the whole level per commit; hashing its event log would
   turn that run into a replay check that catches nondeterminism in
   generators and physics. Next step: add an event log + hash to the bot's
   output and fail the gate on hash drift for a fixed seed.
3. **Barcelona capture-to-pack as intake-route evidence (Aegis intake,
   watchlist).** Not adoptable as a recipe (vendor product, no workflow),
   but it is the clearest recent datapoint that photogrammetry capture +
   modular kit + documentation is a sellable pipeline shape. Next step: none
   until a capture workflow (settings, overlap, cleanup) is actually
   disclosed; keep on watchlist.
4. **Morale/value decision pattern (Aegis ai service, watchlist).** Two
   numbers (morale, cohesion) producing readable tactics is the cheapest
   NPC-decision sketch seen in the scout. Next step: none until gameplay
   modules exist (all 3 are stubs); park the pattern.

## Explicit non-goals

- Barcelona 120 FPS claim (#1): vendor claim, no hardware or method —
  correctly skipped as evidence; the pack itself is watchlisted, not adopted.
- VFX showreel (#3): montage with no disclosed tools — correctly skipped;
  the full YouTube reel was not fetched (linked video, not the post itself).
- Desk-process clip (#4): 11 seconds, empty selftext, tool undisclosed —
  correctly skipped.
- FLUX 3 / no-symmetry repeats: same posts as 2026-10-16, not re-audited —
  correctly skipped as duplicates; FLUX comments re-check failed on a
  transient Arctic Shift 422, not an approval gate.
- Decision-model (LLM) proposal in the squad-sim thread: commenter's idea,
  author's unresolved compute worry, no test posted — noted, not treated as
  a tooling finding.

## Staged skills (ready-to-publish, not yet uploaded)

Per the standing rule (Ehsan 2026-09-28), staged locally in
`~/workspace/video-tooling-scout-public/`; browser upload happens when Ehsan
is present with a signed-in session, never unattended:

- NEW skill `skills/seeded-squad-sim-deterministic-replay/` — seeded
  deterministic sim with per-system RNG streams, hashed event log, replay
  checking, morale/value soldier decisions, radio-to-HQ hierarchy (audit #2).
  Dedup: no existing skill covers seeded determinism with hashed replay
  checking (the 2026-09-27 deterministic-vs-learned row is a bot-eval
  harness, a different tool).
- Full report copy: `docs/scout-reports/have-vs-need-2026-10-17.md`.
- Watchlist rows synced into the repo mirror's
  `video-tooling-scout/references/tooling-watchlist.md`; README skills-table
  rows added.

Audits #1, #3, #4 stay in this report only: #1 (Barcelona) is a PARTIAL
vendor-product announcement with no executable capture workflow (fails the
compression test), and #3/#4 are DEPTH-LIMITED with no extractable workflow.
