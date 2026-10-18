---
name: "procedural_pixel_creature_generator"
description: "Generate pixel-art creatures in code (Godot 4.5 / C#): seed-driven bodies, limbs, faces, markings, rigs, and multi-directional animations, with frame counts derived by the rigging engine and export as transparent PNG sprite sheets plus a JSON manifest (directions, frames, pivots, timing). Trigger when building a procedural 2D creature pipeline, a sprite-sheet export contract, or seed-deterministic game art."
---

# Procedural Pixel Creature Generator

## Purpose

Reconstruct the exact workflow for generating animated pixel-art creatures
purely in code, so an agent can follow the same process on a new creature
pipeline. Everything is generated procedurally from seeds; no pre-rendered
assets, no manual keyframing, no manual frame counts. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The core method throughout: seeds are the source of truth,
parameters are derived from the rig, and exports ship as a machine-readable
contract (PNG sheets + JSON manifest).

**Source:** "Procedural Pixel Creatures: Generating bodies, rigs, and
animations from code (Godot / C#)" by idlerunner00.
https://www.reddit.com/r/proceduralgeneration/comments/1wvzchs/

**Tools used:** Godot 4.5 (.NET / C#); a custom pure-code generator +
animation framework; Claude Opus 5.5 and GPT Astra 6 (used by the author to
build the generator).

**Depth status:** FULL (post text + 13 comments, including author answers to
direct tooling questions; no media, none needed)

## When to use this skill

- Building a procedural 2D creature/enemy generator where seeds replace art files.
- Setting up a sprite-sheet export contract a game engine can import without
  human reconciliation (directions, frames, pivots, timing).
- Replacing hand-specified animation parameters with rig-derived values.

## Prerequisites

- Godot 4.5 with the .NET / C# toolchain.
- A deterministic seed pipeline (same seed -> same creature).
- No 3D tooling needed: this workflow is purely 2D end to end.

## Phase 1: Seed the creature

**Do**
1. Feed a seed into the generator. The generator produces body shapes, limbs,
   faces, and markings, all procedurally (author: "Everything is generated
   procedurally from seeds: body shapes, limbs, faces, markings, rigs, and
   multi-directional animations").
2. Use no pre-rendered assets. (Author's post is truncated at "no pre-render",
   inferred: no pre-rendered sprites anywhere in the pipeline.)

**Check**
- The same seed must regenerate the same creature. (Inference: determinism is
  the contract when seeds replace files.)

**Why**
Seeds are the source of truth. Art becomes a function call, not a file.

## Phase 2: Rig procedurally

**Do**
1. The rigging engine builds a rig for the generated body as one of the
   seed-generated outputs (bodies, limbs, rigs are all generated, not authored).
2. Stay purely 2D. When asked whether anatomy/animations are modeled in 3D
   before baking into 2D rasters, the author answered "its purely 2D".

**Check**
- Quadruped joints read correctly in the demo (commenter: "The joints on your
  quadrupeds remind me of Spore's morphs", a positive signal that joint
  placement is believable).

**Why**
A 3D-to-2D bake pass is a tool you do not need. Staying 2D end to end removes
an entire pipeline stage.

## Phase 3: Generate the animation set

**Do**
1. The animation framework produces multi-directional animations: idle, walk,
   run, and hit reactions.
2. Do NOT set frame counts manually. Author, quoted: "The frame count and
   animation loops are computed automatically by the procedural rigging engine
   based on the movement type rather than set manually."

**Check**
- Direction count and frame timing are consistent across the set (verified from
   the exported JSON manifest, Phase 4).

**Why**
Derive, don't specify. When the rig knows the movement type, the animation
parameters are a consequence, not an input.

## Phase 4: Export sprite sheets + JSON manifest

**Do**
1. Export transparent PNG sprite sheets.
2. Export a JSON metadata file with every sheet "containing all directions,
   frames, pivots, and timing details" (author, quoted).

**Check**
- The JSON manifest is complete per sheet: directions, frames, pivots, timing.
  This is the frame-manifest discipline a 2D asset import validation gate
  should check.

**Why**
The engine importer reads a contract, not the artist's memory. Exporting the
manifest with the art is what makes procedural art engine-consumable.

## The human method, distilled

1. **Seeds are the source of truth** ("Everything is generated procedurally
   from seeds").
2. **Derive, don't specify**: frame counts and loops come from the movement
   type, never from a hand-filled field.
3. **Export contracts, not files**: PNG sheets are inert without the JSON
   manifest; ship both, always.
4. **Delete the pipeline stage you don't need**: no 3D bake pass, no manual
   keyframing, no manual export config.
5. **Use AI as the build crew**: the author built the generator "heavily
   utilizing AI. Claude Opus 5.5 and GPT Astra 6 were used in this." (quoted)

## Failure modes

- Specifying animation parameters by hand: frame counts set manually drift
  from the rig; always let the rigging engine compute them from the movement type.
- Exporting sheets without the JSON manifest: the engine side must then guess
  pivots and timing; always export the manifest with the art.
- Adding a 3D modeling pass "for quality": the author's pure-2D pipeline has
  no such stage and produces believable quadruped joints; a bake pass adds
  tooling without evidence of payoff.
