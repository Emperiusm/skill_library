---
name: procedural-race-circuits-racing-line-first
description: "Generate procedural race circuits racing-line-first: measure 173 real circuits (corner radii and angles, straights, length, compactness), sample corners and straights from those distributions, solve each sequence so the lap closes (reject or repair failures), score up to 24 candidates per seed against their grade's statistics and keep the best, design the pit lane with the lap, compute a minimum-curvature racing line coloured by the speed profile, and grow surroundings last. Trigger when generated circuits must read as real circuits of a stated grade instead of random closed loops."
---

# Procedural Race Circuits: Racing Line First

## Purpose

This skill generates race circuits that read as real circuits, by measuring real ones first and growing the world around the racing line last. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: measure, solve closed, score candidates, line first, world last.

## Source

- Post: "Procedural race circuits: the racing line, then the world grown around it" by Staz-GameDev — https://www.reddit.com/r/proceduralgeneration/comments/1y5b6hn/ (score 37, 6 comments; comments were not fetched in this run, so no commenter corrections are included). Evidence: the author's full post text (797 characters, all five steps with exact numbers). v2 of a generator first posted a few months earlier. Scout audit 2026-11-26, audit 7, FULL.

## Tools used

The author's own procedural track generator, v2. No engine, language, or tool named; no code or file disclosed. All numbers below are the author's.

## Phase 1: Measure real circuits and sample from their distributions

**Do**
1. "I measured 173 real circuits (corner radii and angles, straights, length, compactness) and the generator samples corners and straights from those distributions."

**Check**
- Sampled corners and straights come from measured distributions, not invented ranges. The count (173) and the measured quantities are the evidence; no per-circuit data is disclosed.

**Why**
Real circuits are the spec: sampling from measured distributions keeps generated circuits plausible in the same dimensions real ones vary (radii, angles, straights, length, compactness).

## Phase 2: Solve the lap closed, reject or repair failures, score up to 24 candidates

**Do**
1. "The sequence is solved so the lap closes, then rejected or repaired if it fails."
2. "Up to 24 candidates per seed are scored against the statistics of their grade, and the best one wins."

**Check**
- The lap must close; the solve is a constraint, not a preference. Failed sequences are rejected or repaired, never shipped. The winner is the best-scoring of up to 24 candidates against its grade's statistics, not the first that closes.

**Why**
Closure is a hard requirement for a circuit; scoring against grade statistics keeps a club circuit from being judged as a Grand Prix circuit. Generating candidates and picking the best is cheaper than perfecting one candidate.

## Phase 3: Design the pit lane with the lap

**Do**
1. "The pit lane is designed with the lap." No pit-lane parameters are disclosed.

**Check**
- [Inference: the pit lane must join and leave the lap without breaking closure.] No pit-lane check is stated.

**Why**
[Inference: designing the pit lane alongside the lap, rather than bolting it on after, keeps the lap and pit geometry consistent.] Labelled as inference: the post states the timing ("with the lap"), not the reason.

## Phase 4: Compute the racing line and colour it from the speed profile

**Do**
1. "The racing line is a minimum-curvature path, and the colours come from the speed profile computed on the circuit."

**Check**
- The line is the minimum-curvature path through the solved circuit, and the colours follow the computed speed profile. No curvature or speed numbers are disclosed.

**Why**
The racing line is the point of the generator: the circuit exists to be raced, so the line is computed, not drawn, and the speed profile is the visible proof that the line is drivable.

## Phase 5: Grow the surroundings last

**Do**
1. "The surroundings come last: run-off, barriers, service roads, grandstands, car parks, fields."

**Check**
- Surroundings follow the finished circuit and racing line instead of constraining them. The listed elements are the complete stated set; no counts or placement rules are disclosed.

**Why**
Order is the method: line first, world second. Surroundings that come first would dictate the circuit; surroundings that come last fill in around a circuit that already works.

## AAA studio practice

- **The racing line is a minimum-curvature path plus a speed profile, solved iteratively, and validated against a professional driver's line.** Stanford's sequential two-step algorithm (Kapania, Subosits, and Gerdes) divides trajectory generation into a forward-backward integration that determines the minimum-time longitudinal speed profile under tire friction constraints, and a convex optimization that updates the path by minimizing curvature while staying within track boundaries. Repeated until predicted lap time stops improving, it converged in four to five iterations at about 30 seconds per iteration over the full 4.5 km Thunderhill Raceway course, and the resulting lap time and racing line were comparable to a nonlinear gradient-descent solution and to a trajectory recorded from a professional racecar driver. That is the research form of this skill's Phase 4: minimum-curvature line first, speed profile computed on the circuit second, and the colouring is the visible proof the line is drivable. No iteration count, timing, or curvature value from this paper may be copied into this generator's settings. Source: https://ar5iv.labs.arxiv.org/html/1902.00606
- **Real circuits are the spec, and the spec is measured to millimetres before any generation or authoring starts.** iRacing recreates tracks from three-dimensional laser scans accurate to within 2 mm, so a bump or crack in the real pavement is present in the virtual track, and rescans a track after repaving (Daytona, 2010). Turn 10's *Forza Motorsport 5* process is the same discipline at studio scale: laser-scanning the circuit surface, surrounding buildings, and vegetation, with the digital model rendered in sub-centimeter accuracy, tens of thousands of photographs and 360-degree video as reference, and about 1.4 billion data points per track, after which an outline is mapped and tested and added to the daily build. The lesson for this generator is the order in Phase 1: measure 173 real circuits first, and keep the measured quantities (corner radii and angles, straights, length, compactness) as the distributions that are sampled, never replaced by invented ranges. Sources: https://www.iracing.com/in-good-company/ and https://www.iracing.com/track-technology/ and https://www.autoblog.com/news/forza-motorsport-5-behind-the-scenes-exclusive
- **Player-facing track creation in AAA is built on the studio's own internal tools, with rules, and a drivability check before sharing.** Playground Games' EventLab in *Forza Horizon 5* is based on the studio's own internal design tools, altered for players, built on a rules-based system, and the route creator requires the creator to drive the route and verify the race can be completed before sharing it. That is the production form of this skill's Phases 2 and 5: candidates are generated and scored, the winner must close and be drivable, and surroundings are dressing added only after the circuit and line work. Source: https://gamerant.com/forza-horizon-5-events-lab-features/

**Agent automation**

Write `circuit-manifest.json` beside every generated circuit, with exactly these fields: measured-circuit count (173), distributions sampled, candidates generated per seed (up to 24), grade, closure result per candidate (closed, rejected, or repaired), winner score against its grade's statistics, pit-lane join result, racing-line method, and surroundings list. Fail the run if the winner's score or candidate count is empty: the winner must be the best-scoring of the candidates generated, not the first that closed. Then run these gates in order: (1) closure gate, every candidate is logged as closed, rejected, or repaired, and no failed sequence ships, mirroring Phase 2; (2) grade gate, the winner's score is recorded against its own grade's statistics, so a club circuit is never judged as a Grand Prix circuit; (3) pit-lane gate, the pit lane must join and leave the lap without breaking closure, and the result is recorded [inference: this join check is agent design, built from the skill's own "designed with the lap" statement, since no pit-lane check is stated]; (4) order gate, the speed profile and racing line must be computed and recorded before any surroundings are grown, enforcing line-first, world-last. No engine, language, code, curvature number, or speed number may be entered into the manifest, because none was disclosed.

## The human method, distilled

1. **Measure before you generate:** 173 real circuits define the distributions.
2. **Generate candidates, pick the best:** up to 24 per seed, scored against grade statistics.
3. **Line first, world last:** the racing line is computed on the solved lap; surroundings are dressing.

## Depth status

FULL from the author's full post text. No engine, language, code, or timings were disclosed, and none are invented here. Comments were not fetched for this post; if they add parameters, fold them in.
