---
name: ascii-raymarched-world-grid
description: "Build a single-file raymarched web game world on a 2048x2048 one-byte-per-cell material grid: place settlements first, bake roads with a Dijkstra slope-cost path search, then render every feature as a dumb per-ray material lookup, no SDF. Trigger when building a cheap grid-baked game world or an ASCII/character-cell renderer."
---

# ASCII Raymarched World Grid (Baked Roads, Material Lookup)

## Purpose

This audit reconstructs the exact world-generation and rendering workflow from
OddSliceOfMarketing's "Made a game entirely with ASCII characters!" (Land of
Ascii) post and the author's own technical comment, step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The workflow's core method is: bake everything (roads, rivers, fields) into a
flat per-cell material array at world-gen time, then let the per-ray lookup be
a dumb material read.

## Source

Creator: OddSliceOfMarketing (r/proceduralgeneration post 1x8bji8, score 44,
50 comments).

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x8bji8/made_a_game_entirely_with_ascii_characters_would/
(native Reddit video; 2026-10-19 scout run). Playable:
https://oddslice.itch.io/land-of-ascii

Note: most of the thread debates AI authorship (the author admits LLM help
with posts/notes; code authorship is contested). The tooling signal below is
from the author's own technical comment; the authorship dispute is out of
scope.

## Tools used

Tools used: single HTML file (web/HTML5), custom raymarching/raycasting
renderer on a heightmap, glyph-based rendering (colored backing, ascii
lettering as textural glyph). Commenter confirmation (ouroborus777): "This is
'just' raytracing. Low res (ascii), textured (glyphs), heightmap."

## Phase 1: Fix the world grid and its byte budget

**Do**
1. Fix the world as a 2048 x 2048 grid of one-metre cells. (Author: "The whole
   world is 2048x2048 one-metre cells, so a byte per cell is cheap.")
2. Store per-cell material as ONE BYTE per cell: 2048 * 2048 = 4,194,304
   bytes, roughly 4 MB for the entire world.

**Check**
- Memory: confirm the grid stays near 4 MB. If a feature needs more than a
  material ID can express, the architecture — not the byte — is wrong.

**Why**
One byte per cell at this resolution is the entire budget argument: every
feature (road, river, lake shore, field) must be expressible as a material
ID. Nothing finer survives the grid anyway.

## Phase 2: Place settlements first, then bake roads

**Do**
1. Place villages and the fort FIRST, before any roads exist. (Author:
   "Villages and the fort are placed first.")
2. Run a Dijkstra-style path search with cost rising with slope, over the
   heightmap, between the placed settlements. (Author: "a path search
   (Dijkstra-style, cost rising with slope) finds the route between them over
   the heightmap".)
3. Paint the found path into the per-cell material array, a few metres wide.
   (Author: "that path is painted into a per-cell material array a few metres
   wide".)

**Check**
- Roads follow terrain logic (low slope) because the cost function says so,
  not because a designer drew them. Walk a road in-game: it should read as
  walked, not drawn.

**Why**
Settlements-first ordering is the design decision: the road network serves
the places, so generate places before paths. Slope-cost makes roads look
natural; painting them into the grid makes them permanent.

## Phase 3: Render by material lookup

**Do**
1. Raymarch/raycast the heightmap. The depth map is a side effect of ray
   casting, not a separate pass. (ouroborus777: "heightmap (the term is
   'depth map' in this context, and is a side effect of how ray casting
   works)".)
2. For each ray, read "this cell is road" exactly the same way the ray reads
   grass or stone: one material lookup. (Author: "At render time the ray just
   reads 'this cell is road' the same way it reads grass or stone; the glyph
   set and colour follow from that.")
3. No signed distance field, no per-ray test. (Author: "No signed distance
   field, and no per-ray test.")
4. Choose the glyph set and color from the material. Roads, rivers, lake
   shores and fields are all the same kind of thing to the renderer: a
   material lookup. (Author: "An SDF would make sense if the roads moved or
   needed sub-metre edges, but they don't, and the text grid hides anything
   finer than a cell.")

**Check**
- The text grid hides sub-cell detail: zoom in and confirm the cell size is
  the resolution floor. If you need finer than a cell, this architecture is
  wrong for you — use an SDF.

**Why**
Baking features into the grid at gen time makes the renderer trivial: every
feature is one indirection. The renderer's simplicity is bought with gen-time
commitment. The author states the limit explicitly instead of hiding it.

## Phase 4: Iterate toward a fixed look target

**Do**
1. Budget for iteration: this is the author's 3rd version attempt with 80
   commits to reach the current world. (Author: "This is the 3rd version of my
   attempts and it still has 80 commits until i get it to the world I like".)
2. Fix the look target early: MS-DOS games the author played as a kid, no
   combat by design. (Author: inspired by the MS DOS games played as a kid;
   "hence no combat".)

**Check**
- "I saw it as inspiration" — the look target is remembered pixelation, not
  photorealism. Judge each iteration against the memory, not against a modern
  renderer.

**Why**
A fixed look target (MS-DOS memory) bounds the iteration: 80 commits toward
a known aesthetic, not open exploration.

## The human method, distilled

1. One byte per cell is the budget: make every feature fit a material ID.
2. Places before paths: settlements first, Dijkstra-with-slope-cost second,
   painted into the grid.
3. Bake at gen time, read at render time: the renderer is a material lookup,
   nothing more.
4. Name the resolution limit honestly: the text grid hides sub-cell detail;
   if you need finer, use a different architecture (SDF).

## Depth status

FULL (author-disclosed grid size, byte budget, Dijkstra recipe, and no-SDF
rationale; all parameters quoted; no values invented).

## AAA studio practice (refinement 2026-10-24)

**Do**
1. Write the road cost function down before running Dijkstra, with slope as a first class term and a hard cutoff. The procedural road generation literature defines the global cost as a sum of weighted functions over terrain and trajectory characteristics, where the slope transfer function returns infinity above a threshold so paths cannot climb unrealistically steep slopes, and otherwise charges a function of slope controlled by a maximum cost. That is the formal version of this skill's slope cost. Source: https://www.academia.edu/79198548/Procedural_Generation_of_Roads
2. Keep the layer order the skill already states (locations, then paths, then terrain flattening) and make each layer a separate, re-runnable pass. The LayerProcGen contextual generation design does exactly this: a GeoGrid layer generates coarse height data and flattens around locations, a Cultivation layer runs pathfinding between connected locations with cost based on terrain heights, and a Landscape layer flattens terrain around both locations and paths. Source: https://runevision.github.io/LayerProcGen/md_ContextualGeneration.html
3. Automate the bake as a script, not a manual paint: input is the heightmap plus settlement coordinates, output is the material array plus a road mask. [inference: automation step derived from the two sources above]

**Check**
- Automated validation script [inference]: after the bake, assert (a) every settlement is connected by at least one road cell path, (b) no road cell sits on a slope above the cutoff, (c) total road cells and the 4 MB grid budget (2048 x 2048 x 1 byte) are logged, and (d) re-running the script with the same seed produces a byte identical material array. A road that disconnects a settlement or climbs the cutoff slope fails the bake, even if it looks fine.
- Render check: walk one road end to end in the raymarched view and confirm the glyph and color change only at material boundaries, never mid cell. Mid cell changes mean the renderer is doing per ray work the bake was supposed to remove.

**Why**
Baked world generation is only cheap if the bake is deterministic and testable. The AAA and academic pattern is the same: cost function on paper, layers in order, bake once, render by lookup, and a validation pass that proves the bake before anyone plays on it.
