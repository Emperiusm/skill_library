---
name: infinity-castle-seeded-grammar
description: "Generate an infinite explorable structure from a seed in three.js: resolve every point in space by hashing coordinates plus seed (no stored state), organize generation with an architectural grammar (chapters to districts to plots to rooms), merge each cell to about 2 draw calls with vertex-baked AO, and synthesize the audio from the generation rate. Trigger when building infinite procedural architecture that must stay coherent and bounded in frame cost."
---

# Infinity Castle: Seeded Grammar Worlds

## Purpose

This skill reconstructs the Infinity Castle streaming-grammar workflow, step by step, so another agent can build infinite procedural architecture the same way. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: resolve every point in space by hashing coordinates + seed so there is no stored state; organize generation with an architectural grammar; merge each cell to ~2 draw calls with vertex-baked AO; synthesize the sound too.

## Source

- Post: "I made an infinite, self-assembling Demon Slayer–style castle in Three.js: no models, no textures, all procedural" by Thre4dripper — https://www.reddit.com/r/threejs/comments/1xms4uk/i_made_an_infinite_selfassembling_demon/ (r/threejs, score 22, 6 comments)
- Fly it: https://infinity-castle.ijlalahmad.dev/
- Code: https://github.com/Thre4dripper/Infinity-Castle-ThreeJs
- Evidence: full author writeup + 6 comments (2026-11-04 scout run). "Geometry skills" undisclosed.

## Tools used

three.js; hash-coordinate streaming; architectural grammar; vertex-baked ambient occlusion; runtime texture atlas; Karplus-Strong biwa synthesis. "No physics engine at all, pure threejs and geometry skills" (author; "geometry skills" is the author's term for LLM coding skills — u/Kole88 asked him to share them, no reply captured).

## Phase 1: Hash the world

**Do**
1. "Each point in space is resolved by hashing coordinates + seed, so there's no stored state and it can stream in any direction."

**Check**
- Flying in any direction (including back) reproduces the same geometry: determinism from the hash, not from saved chunks.

**Why**
No stored state means no save/load, no chunk borders, no memory growth. Infinity is an addressing scheme, not a storage problem.

## Phase 2: Grammar, not noise

**Do**
1. "A grammar of chapters → districts → building plots → rooms keeps it from turning into noise soup."
2. "Every building is complete from foundation to roof ridge."

**Check**
- Buildings read as complete structures (foundation to roof ridge), not noise fields: the grammar is the difference between procedural and random.

**Why**
Raw noise makes terrain; grammar makes architecture. The chapter/district/plot/room hierarchy is what keeps a Demon Slayer–style castle from becoming "noise soup."

## Phase 3: Move districts as rigid bodies

**Do**
1. "Districts move as rigid bodies, and collision is computed in each district's local frame."

**Check**
- "You can graze a rotating tower at 40 m/s" — collision stays correct while the district moves.

**Why**
Local-frame collision is what makes moving architecture flyable: the world moves, the math doesn't.

## Phase 4: Budget the frame

**Do**
1. "Each cell merges down to ~2 draw calls with vertex-baked AO."
2. "New cells are built first along your flight direction."

**Check**
- The draw-call budget is per cell (~2), not per building: merging is the mechanism, the number is the contract.
- Generation priority follows the camera: what you fly toward exists first.

**Why**
A fixed per-cell draw-call budget is what makes "infinite" renderable: the frame cost is bounded by the visible cells, not the world size.

## Phase 5: Paint and sound at runtime

**Do**
1. Generate everything at runtime from the seed: "beams, shoji panels, lanterns, even the painted byōbu screens (painted into a texture atlas at runtime)."
2. Synthesize the audio: "a Karplus-Strong biwa, plus construction sounds that follow how fast cells are being generated."

**Check**
- The title's "no models, no textures" = no authored assets; textures are generated into the atlas at runtime (inference, confirmed by the author's own "painted into a texture atlas at runtime").
- Construction audio tracks the generation rate: the soundscape is coupled to the streaming system.

**Why**
If the world is generated, its paint and its sound should be generated too: authored assets would break the seed-determinism contract.

## The human method, distilled

1. No stored state (hash everything; stream any direction).
2. Grammar before noise (complete buildings, not soup).
3. Budget the frame (~2 draw calls per cell; build along the flight direction).
4. Collision in the mover's frame (districts as rigid bodies).
5. Sound follows the system (construction audio tracks generation rate).

**Depth status:** PARTIAL (author writeup + 6 comments; no code parameters beyond "~2 draw calls" and "40 m/s"; the "geometry skills" undisclosed).
