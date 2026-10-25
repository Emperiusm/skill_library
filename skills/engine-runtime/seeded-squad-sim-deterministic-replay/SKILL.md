---
name: seeded-squad-sim-deterministic-replay
description: "Build a seeded, exactly-reproducible browser simulation: one seed determines terrain, weather, and forces; separate RNG streams per system; an event log with a hash plus replay checking proves determinism; per-soldier deterministic decisions from perception plus morale/cohesion values; squads reach platoon HQ through a radio operator. Trigger when building a seeded sim, a deterministic game, or a replay/debugging harness."
---

# Seeded Squad Sim: Deterministic Replay Checking

## Purpose

This audit reconstructs the exact workflow from EmeraldOnFire101's
seeded squad-combat simulation post and the comment thread, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The workflow's core method is: one seed determines everything,
and a hashed event log plus replay checking makes every run exactly
reproducible.

## Source

Creator: EmeraldOnFire101 (r/proceduralgeneration post 1x6tlyo, score 27,
9 comments).

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x6tlyo/seeded_squadcombat_simulation_in_the_browser/
(native Reddit video, 48 s; 2026-10-17 scout run). Playable demo linked in
the post: https://sim.shaykas.com/?seed=19

## Tools used

Tools used: browser-based sim (engine/framework undisclosed). No code, no
repo, no language, no RNG algorithm, no hash algorithm, no decision
thresholds disclosed. The architecture below is the author's stated design,
quoted verbatim where quoted; anything beyond the quotes is labeled
inference.

## Phase 1: Seed determines the battle

**Do**
1. Generate "each battle ... from a seed" (author's selftext, verbatim).
2. Pick one of four map types per seed: "a bocage hamlet, open ridge
   farmland, a highway junction or a market town, each with its own weather"
   (selftext).
3. Give "one in ten seeds ... a tank" (selftext).
4. Make "battles ... seed specific, so you can share a link to an exact
   fight" (selftext). The demo URL carries the seed as a query parameter
   (`?seed=19`).

**Check**
- The same seed URL reproduces the same fight. (Author's stated behavior;
  the 48-second clip shows one seed, not a proof.)
- The 1-in-10 tank rate is checkable only by sampling many seeds; the author
  states it, no sample was posted.

**Why**
- Seed-as-URL turns a battle into a shareable, debuggable artifact: a bug
  report is a link, not a description. It also makes the sim trivially
  demoable: one link, one exact fight.

## Phase 2: Separate RNG streams per system

**Do**
1. Use "separate RNG streams per system" (selftext).
2. Derive every system's randomness from its own stream, seeded from the
   master seed (inference: the author states the streams exist, not how
   they are derived).

**Check**
- (Inference) Change one system's randomness (e.g. weather rolls) and
  confirm no other system's rolls shift. Each stream must be independently
  reproducible from the master seed.
- Failure mode: a single shared RNG means tuning one system re-rolls the
  whole battle, and replay checking (Phase 3) cannot localize which system
  diverged.

**Why**
- Per-system streams isolate randomness: tuning one system cannot silently
  re-roll the world. Isolation is what makes replay checking tractable:
  a hash mismatch can be traced to one stream.

## Phase 3: Hashed event log + replay checking

**Do**
1. Keep "an event log with a hash" (selftext).
2. Run "replay checking, so any run can be reproduced exactly" (selftext).
3. Replay the same seed and compare the event-log hash (inference: the
   author states the log and the hash exist, not the comparison step).

**Check**
- Same seed, same hash: the run is deterministic.
- Hash mismatch on replay: nondeterminism crept in somewhere. (Inference)
  Bisect by per-system stream to find which system diverged.
- Failure mode: logging only some events (e.g. skipping weather rolls)
  lets nondeterminism hide below the hash. The log must cover every
  random draw and every decision (inference: follows from the author's
  "any run can be reproduced exactly").

**Why**
- The hash turns "is this deterministic?" from a belief into a checkable
  property: any divergence in any system changes the log hash. This is the
  pattern's core principle: determinism is a check, not a hope.

## Phase 4: Per-soldier deterministic decisions

**Do**
1. Give "soldiers each ... a deterministic decision algorithm that responds
   to their perception of their environment and personal values" (author's
   comment, verbatim).
2. Drive behavior from morale and cohesion: "a soldier with low morale who
   is pinned down might try to flee and need to be re-rallied by his squad
   leader. Soldiers with high morale and squad cohesion will execute
   tactical attacks like stacking up on a building's windows and throwing
   grenades through them" (author's comment).

**Check**
- Same perception + values produce the same decision on replay (follows
  from Phase 3). No decision tables, thresholds, or perception radii were
  disclosed, so the check is structural, not numeric.
- Failure mode (inference): if any decision reads wall-clock time, an
  unseeded random source, or floating-point state that differs across
  browsers, the replay hash will mismatch. Every decision input must come
  from the seeded streams or the event log.

**Why**
- Decisions from perception + values (not from fresh randomness) keep the
  sim deterministic while still producing readable tactical behavior:
  fleeing, rallying, stacking, grenading are all downstream of two numbers
  (morale, cohesion) plus what the soldier perceives.

## Phase 5: Radio operator to platoon HQ

**Do**
1. Give "each squad ... a radio operator via which they reach platoon HQ,
   which makes decisions on where to engage and if to provide fire support"
   (author's comment).

**Check**
- (Inference) Squad-level decisions and platoon-level decisions are
  separate layers: squads decide tactics, HQ decides engagement and fire
  support. A replay hash mismatch in HQ decisions points at the radio/HQ
  layer, not at individual soldiers.

**Why**
- The radio-operator link is the hierarchy: local perception stays local,
  and only the HQ layer spends shared resources (fire support). Hierarchy
  keeps the decision layers separately testable and separately replayable.

## Phase 6: The open question (decision model)

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
- (Inference) A learned decision model would break the determinism the
  whole design is built on (Phases 2-3) unless its outputs are also hashed
  and replay-checked, which is the cost the author is weighing. The
  principle: any new decision source must enter through the hashed log,
  or determinism is lost.

## The human method, distilled

1. **Seed everything, share by URL**: a battle is a link.
2. **Streams per system**: isolate randomness so tuning one system does not
   re-roll the world.
3. **Hash the log, replay the run**: determinism is a check, not a hope.
4. **Decisions from perception + values**: morale and cohesion are the two
   numbers that produce tactics.
5. **Hierarchy through radio**: squads fight, HQ spends fire support.
6. **New decision sources must enter through the log**: anything unhashed
   is nondeterminism waiting to happen.

**Depth status:** PARTIAL (full post text + all 9 comments with the complete
decision architecture quoted; no code, no RNG/hash details, no thresholds).

## AAA studio practice

Sources:
- Ensemble Studios, Age of Empires (GDC 2001, Bettner and Terrano, as summarized): multiplayer used deterministic lockstep, sharing only commands (not game state), with all clients simulating identically from a pre-agreed RNG seed; out-of-sync detection hashed relevant game data per turn and compared hashes across clients. https://samu.space/Age-of-Empires-and-networking/
- Wube Software, Factorio (official forums/wiki): multiplayer uses deterministic lockstep, sending only user inputs; every client must simulate every tick identically, and any slight difference is a desync, reported with a full state comparison (desync report) so the divergence can be bisected. https://wiki.factorio.com/index.php?title=Desynchronization&direction=prev&oldid=199235
- Wube Software, Factorio (developer guidance on desyncs): functions that are not safe for the lockstep simulation must be marked as such, and any data that is not part of the shared game state must never leak into simulation decisions. https://forums.factorio.com/viewtopic.php?p=399097

**Do**
1. Adopt the Age of Empires/Factorio hash cadence: hash the full simulation state (or the event log) every tick or every N ticks, not just at run end, and write the hash sequence to a file alongside the seed.
2. Automate replay checking as a command, not a manual re-run: `replay --seed <seed> --compare <hash-file>` must exit non-zero on the first tick whose hash diverges, printing the tick and the per-system stream that diverged.
3. Mark non-deterministic sources as forbidden in simulation code (wall clock, unseeded RNG, platform float behavior that differs across browsers) and add a lint or code-review checklist item for it, following the Factorio rule that unsafe functions must be marked.
4. Automate the per-system isolation test: for each system stream, re-roll only that stream and confirm no other system's log entries change; this is the executable version of the Phase 2 check.

**Check**
- Two runs of the same seed produce identical hash sequences, tick by tick.
- A deliberately injected nondeterministic read (for example, Date.now() in a decision) is caught at the first diverging tick, with the system named.
- The replay command runs headless with no rendering, so determinism checks are fast enough to run on every change.

**Why**
In production lockstep games, determinism is not a property you assert, it is a hash you compare every turn, with a report that localizes the divergence. This skill's hashed event log is the same mechanism; the AAA addition is the cadence (per tick), the automated compare command, and the forbidden-source marking.
