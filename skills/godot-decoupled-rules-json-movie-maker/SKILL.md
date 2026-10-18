---
name: "godot_decoupled_rules_json_movie_maker"
description: "Build a Godot game with engine-decoupled rules: game logic in a plain library with no Godot dependency, each rule a small class behind a name-to-builder dictionary, content as JSON rule lists, 3D-to-pixel-art via a small viewport plus pixelation shader, and trailers as scripted runs re-shot with Godot Movie Maker mode after every change. Trigger when structuring a Godot game's rules, content data, or trailer pipeline."
---

# Godot: Engine-Decoupled Rules + JSON Content + Movie Maker Re-Shoots

## Purpose

This audit reconstructs the exact workflow from CursedCreatives' Burgero post
and the comment thread, step by step, so another agent can follow the same
process. Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The workflow's core method is:
decouple the rules from the engine, describe content as data, re-shoot the
trailer from the same scripted run after every change.

## Source

Creator: CursedCreatives (r/godot post 1x6u64w, score 24, 4 comments).

Source: https://www.reddit.com/r/godot/comments/1x6u64w/in_my_burger_roguelike_layers_boost_the_ones_they/
(native Reddit video; 2026-10-16 scout run). Game: Burgero, a roguelike where
you stack burgers for customers.

## Tools used

Tools used: **Godot 4 + C#**, **Blender** (primitive models), pixelation shader
(engine undisclosed), **Godot Movie Maker mode**. No versions, no shader
parameters, no Movie Maker settings disclosed.

## Phase 1: Engine-decoupled rules library

**Do**
1. Put the game rules in "a plain C# library with no Godot dependency"
   (author's selftext, verbatim). The Godot project consumes the library, not
   the reverse.
2. Model each rule as "a small class" (author's comment, verbatim).
3. Keep "a dictionary [that] maps the rule's name to a function that builds it
   from its parameters" (author's comment, verbatim).

**Check**
- The rules library compiles and runs with no Godot reference. A new rule is
  a new small class plus one dictionary entry.
- (Inference: the author states the separation; no build proof was posted.)

**Why**
- Rules as data + builders means new content needs no new code paths, only
  new JSON (Phase 2). Engine independence means the rules are testable and
  portable outside the engine.

## Phase 2: Content as JSON rule lists

**Do**
1. Describe each ingredient as JSON "with a list of rules and their numbers"
   (author's comment, verbatim).
2. Encode adjacency boosts in the rules: "many ingredients boost the layers
   they touch (cheese right on a patty, onion next to one)" (selftext).
3. Score each layer with Flavor and Mult. Add the wobble mechanic: "Taller
   burgers score more but get wobbly, and a Shaky burger can collapse when you
   serve it" (selftext).

**Check**
- A new ingredient works by adding JSON only; the score/wobble behavior
  follows from its rule list. No rule-class change is needed for new content.

**Why**
- Content-as-data keeps the design surface in JSON where it is cheap to
  iterate; the class-per-rule structure keeps each rule's logic isolated.
  Adjacency rules make ordering matter more than inventory: "the order
  matters more than what you have" (selftext).

## Phase 3: Pixel-art look from 3D

**Do**
1. Model ingredients as "primitive models made in Blender" (author's comment).
2. Render "the 3D scene ... to a small viewport for the pixel-art look"
   (selftext).
3. Apply "a pixelation shader ... to make them look more stylish" (author's
   comment).

**Check**
- The viewport render reads as pixel art, not as low-res 3D. No shader
  parameters were posted, so this check is the author's stated outcome, not
  a verified recipe — expect to tune the viewport size and shader yourself.

**Why**
- Small-viewport rendering + pixelation gets pixel-art readability out of 3D
  models without hand-drawing sprites. Primitive Blender models are enough
  because the pixelation hides low-poly simplicity.

## Phase 4: Scripted re-shoot trailer

**Do**
1. Record the clip as "a scripted run recorded with Godot's Movie Maker mode"
   (selftext).
2. After every change, "re-shoot it" from the same scripted run (selftext).

**Check**
- The trailer after a change shows the same run with the new behavior; drift
  between trailer and build is zero by construction.

**Why**
- A scripted run is a reproducible trailer: marketing footage stays in sync
  with the game for free. No hand re-recording, no stale footage.

## The human method, distilled

1. **Decouple rules from the engine** so content iteration never touches
   engine code.
2. **Content is JSON; logic is small classes** behind a name-to-builder
   dictionary.
3. **Re-shoot, don't re-record**: the trailer is a deterministic artifact of
   the scripted run.
4. **Order is a mechanic**: when rules boost neighbors, arrangement beats
   inventory — design content so the JSON rule lists create that depth.

## Failure modes

- **No parameters posted.** The pixelation shader, the Movie Maker settings,
  and the wobble/collapse thresholds are all undisclosed. This skill is an
  architecture recipe, not a settings sheet — the numbers are yours to tune.
- **The pattern transfers across languages.** The author used C#; the
  structure (dependency-free rules module + JSON content + scripted re-shoot)
  applies equally to GDScript or Python. Do not treat C# as a requirement.

**Depth status:** PARTIAL (full post text + all comments with quoted
architecture; no code, no shader parameters, no Movie Maker settings).
