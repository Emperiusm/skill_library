---
name: godot-runtime-procedural-creatures
description: "Generate creatures at runtime in Godot 4 with GDScript: build the skeleton and a single skin mesh from the creature design, animate with IK foot planting and body lean, drive behaviour with a daily schedule. No pre-made skeletal meshes. Trigger when a game needs evolving creatures, runtime-generated characters, or a procedural rig instead of a baked one."
---

# Runtime Procedural Creatures in Godot 4 (GDScript Rig + Skin)

## Purpose

This skill reconstructs the exact workflow from Ouvolk's Primordium devlog
(Spore-inspired evolution and tribe game, Godot 4), step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The workflow's core method is: the creature design generates the rig, the
skin, and the parts at runtime; nothing is pre-made.

Variant note: this is the same problem class as
`procedural-pixel-creature-generator` (Godot 4.5 / C#, seed to rig to sprite
sheets + JSON manifest) but a different workflow — 3D runtime rig and skin in
GDScript for a living game, not 2D sprite-sheet export. The watchlist also
tracks the Godot 4.5 .NET procedural creature pipeline (2026-10-04 row);
Primordium is the GDScript runtime variant of the same idea.

## Source

Creator: Ouvolk (Primordium).

Source: https://www.reddit.com/r/godot/comments/1xqph5m/working_on_a_sporeinspired_evolution_and_tribe/
(r/godot post 1xqph5m, score 32, 16 comments) | 2026-11-08 scout run.
Demo: https://akinjigames.itch.io/primordium. Kickstarter pre-launch page
linked in the post. Evidence: full author post text + 16 comments; no
transcript exists for the native Reddit clip. The comments are mostly an
AI-use debate, not workflow detail; the workflow evidence is the author's
post text.

## Tools used

Tools used: **Godot 4**, **GDScript** (runtime generation). No pre-made
skeletal meshes; no external DCC in the creature pipeline as described.

## Phase 1: Define the creature as a design

**Do**
1. Define the creature as a design (body plan + part list), not as a mesh.
2. Parts named by the author: curved Bezier horns, tapered ears, bi-lobed
   tail clubs, wings you can glide with, shader eyes with blinking eyelids.

**Check**
- The design, not a sculpt, is the input: "All the creatures are generated
  in GDScript at runtime, with no pre-made skeletal meshes."

**Why**
- A design-driven creature can evolve: the game is Spore-inspired evolution,
  so the creature must change shape as it evolves. Pre-made meshes cannot do
  that.

## Phase 2: Build the rig and skin at runtime

**Do**
1. In GDScript, build the skeleton from the creature's design.
2. Build a single skin mesh from the same design, over that skeleton.

**Check**
- One skin mesh per creature, generated, not imported. The author states the
  skeleton and "a single skin mesh are built from the creature's design."

**Why**
- Rig and skin from one design cannot disagree about proportions: the same
  numbers drive both. (Inference, labeled: the author does not state this
  principle; it is the reason the architecture works.)

## Phase 3: Animate with IK and lean

**Do**
1. Foot planting via IK: feet stay planted while the body moves.
2. Lean the body into turns.

**Check**
- Feet do not slide or float during walks and turns in the clip; the body
  banks into the turn.

**Why**
- IK planting plus lean is what makes a generated skeleton read as alive
  instead of procedural: the feet obey the ground and the body obeys
  momentum. (Inference, labeled.)

## Phase 4: Drive behaviour with a daily schedule

**Do**
1. Give herds a daily schedule: sleeping in nests at night, stretching at
   dawn, resting at midday.
2. In the tribe stage, let tribe members gather, hunt, defend, and play
   instruments.

**Check**
- The same creatures behave differently by time of day in the clip (nest
  sleeping at night, stretching at dawn).

**Why**
- Schedule-driven behaviour makes the ecosystem visible without scripting
  every creature: time of day is the director.

## The human method, distilled

1. **Design is the asset.** The creature design generates rig, skin, and
   parts; nothing is pre-made.
2. **One design, one rig, one skin.** A single source of truth for
   proportions.
3. **Ground the feet, lean the body.** IK planting and turn lean carry the
   believability.
4. **Schedule, don't script.** Daily routines produce living-ecosystem
   behaviour from a clock.

## Failure modes

- **Comments warn the game reads as a Spore copy without its own mechanics.**
  Multiple commenters: the footage does not yet show what is new versus the
  original Spore. A runtime-rig game still needs a unique mechanic to be a
  game, not a tech demo.
- **No code, parameters, or performance figures were disclosed.** The author
  offered to answer questions about mesh generation, IK walking, and AI;
  treat the phase parameters above as architecture, not copy-paste code.

**Depth status:** PARTIAL (full author post text + 16 comments with exact
technique inventory; no code, no numeric parameters, no performance figures
disclosed; author offered Q&A).
