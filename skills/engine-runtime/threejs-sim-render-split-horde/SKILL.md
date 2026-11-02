---
name: threejs-sim-render-split-horde
description: "Ship a three.js action prototype fast: headless fixed-step sim over typed arrays, renderer interpolation, 7-draw-call instanced hordes, flow-field crowds, hashed golden tests. Trigger when building browser action games or AI-vibed prototypes."
---

# I'm shipping a three.js action prototype with a headless sim

## Purpose

This skill reconstructs the exact engineering workflow technomeg described for a Boxhead-style co-op arena shooter prototype (Three.js + TypeScript + Vite), step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: *headless deterministic sim over typed arrays, rendered by interpolation, with crowds faked cheaply and correctness locked by hashed golden tests.*

## Source

Creator: technomeg

Source: https://www.reddit.com/r/threejs/comments/1xkmn2m/ (2026-10-31) | video: v.redd.it/7y8kkhlakvyh1 | playable: https://operationelsewhere.com/?src=reddit-threejs

Depth: FULL — concrete architecture, measured numbers, and the golden-test discipline, all from the author.

## Tools used

Three.js, TypeScript, Vite. All code "vibed with Opus 5.5 as lead/reviewer, with Grok on the sim gameplay and cameras" (author: "because I had plenty usage left. Codex was gone and claude was like 20% left" — model choice was opportunistic). Measured: sim step 0.23 ms at 400 enemies; <2 ms per-tick budget at 400; ~180 KB/frame CPU instance upload.

## Phase 1: Split the sim from the renderer

**Do**
1. Run the game sim headless at a fixed 60 Hz step (120 Hz optional) over plain typed arrays in struct-of-arrays layout. No Three.js inside the sim.
2. Have the renderer read the buffers and interpolate between the previous and current step, so motion stays smooth on 120 Hz displays.
3. Step projectiles **back** along their flight instead of extrapolating forward.

**Check**
- Rockets never render inside walls (the author's measured failure: "Extrapolating drew rockets up to ~33 cm inside the wall they were about to hit").
- A 120 Hz display shows smooth motion from the 60 Hz sim.

**Why**
- The sim stays deterministic and unit-testable; the renderer owns smoothness. Backstepping projectiles trades one frame of latency for zero tunneling artifacts — the wall-penetration bug is the evidence that extrapolation was the wrong default.

## Phase 2: Render the horde in a constant 7 draw calls

**Do**
1. Build each enemy from 7 InstancedMeshes: head, eyes, torso, 2 legs, 2 arms — 7 draw calls no matter how many enemies exist.
2. Compose matrices by hand straight into the instance arrays. No Object3D per enemy.

**Check**
- Draw calls stay at 7 from 10 enemies to 400+.

**Why**
- Per-enemy scene-graph nodes are the classic three.js perf cliff; instancing with hand-composed matrices removes it. Body-part instancing (rather than one merged mesh) keeps per-part animation cheap.

## Phase 3: Fake the crowd with flow field + spatial hash + ring slots

**Do**
1. Steer with a flow field toward the players.
2. Separate with a spatial hash, then run a relaxation pass so bodies don't overlap.
3. Give each enemy its own slot on a ring around its target, so they surround the player instead of forming a conga line.

**Check**
- Enemies encircle the player; they never queue up in a line behind each other.

**Why**
- Ring slots turn "N seekers, 1 target" from a traffic jam into an encirclement at roughly O(1) cost per enemy; the relaxation pass is what prevents body overlap without a physics engine.

## Phase 4: Budget the tick and lock correctness with golden tests

**Do**
1. Measure and hold a budget: sim step 0.23 ms at 400 enemies; the test suite enforces a <2 ms per-tick budget at 400. Next target the author names: move the ~180 KB/frame CPU instance upload to the GPU.
2. Before refactoring the sim, record 5 seeded scenarios x 600 steps hashed into digests. Every refactor since must match bit for bit.

**Check**
- Any sim refactor that changes a digest is a behavior change, not a refactor — reject it.

**Why**
- When the code is AI-written ("We live in an incredible time"), hashed golden tests are what keep refactors honest. The digest is cheaper than re-validating gameplay by hand after every model-assisted change.

## The human method, distilled

1. "because I had plenty usage left. Codex was gone and claude was like 20% left" — pick the model you have budget for; put the strongest (Opus 5.5) as lead/reviewer and the other (Grok) on the sim and cameras.
2. The design predates the tooling: "The game setup is actually based on my childhood daydream boardgame."
3. Ask for perf feedback with GPU/browser specified — measurement is part of the dev loop, and the playable link (operationelsewhere.com) makes it testable.

## Failure modes

- **Rockets inside walls:** forward extrapolation under a fixed-step sim — fixed by backstepping projectiles.
- **Conga-line enemies:** pure seek steering without ring slots — fixed by per-enemy ring slots around the target.
- **Refactor regressions in vibed code:** fixed by hashed golden digests before refactoring, not after.

**Depth status:** FULL (author-specified architecture and numbers; no invented values)
