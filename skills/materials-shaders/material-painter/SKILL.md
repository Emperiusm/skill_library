---
name: material-painter
description: "Paint PBR materials in material-painter, the free open-source Substance Painter alternative: node-graph material design, WGSL custom shader nodes, GPU baking with caching, engine export presets. Trigger when a Substance-free texturing workflow is needed."
---

# material-painter: Free Open-Source Substance Painter Alternative

## Purpose

This skill reconstructs the tool's design from the author's published comments,
step by step, so another agent can evaluate and use it. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The tool's core method is: author materials in a built-in
node graph, extend with WGSL shader nodes, bake on the GPU with caching,
export through engine presets — no proprietary formats anywhere.

## Source

Creator: Admirable-Struggle78 (alla2001 on GitHub).
Reddit post: https://www.reddit.com/r/3Dmodeling/comments/1xkrhq4/i_built_a_free_opensource_alternative_to/
(r/3Dmodeling post 1xkrhq4, score 190, 36 comments) | 2026-11-01 scout run,
audit 1. Repo: https://github.com/alla2001/material-painter

## Tools used

**material-painter** (alla2001/material-painter, free, open source).
Builds: Windows, Linux, Mac (one app for Apple Silicon and Intel; not
notarized yet — first launch: right-click the app and choose Open). The author
wrote it with Claude's assistance: "Claude is not a person, so yeah it's only
me, and I did contribute by debugging and testing so I did help in the
creation process."

## Phase 1: Design the material in the node graph

**Do**
1. Build the material in material-painter's built-in node graph — material
   design happens inside the tool, no external graph editor needed.
2. For custom behavior, write shader nodes directly in **WGSL**.

**Check**
- The graph evaluates live in the viewport; iterate until the material reads
  correctly.

**Why**
- The node graph is the author's named differentiator against ArmorPaint
  ("more mature and battle-tested"): design inside the tool, and WGSL keeps
  custom nodes portable to WebGPU-class targets.

## Phase 2: Bake on the GPU with caching

**Do**
1. Bake textures with the GPU baker.
2. Re-bake incrementally after edits — caching makes unchanged regions
   return near-instantly.

**Check**
- After an edit, re-bake: cached regions should resolve immediately; only
  changed regions recompute.

**Why**
- GPU baking with caching is the second named differentiator. The texture
  bake-test loop is the bottleneck in hand painting; the loop has to be
  cheap or the tool is unusable.

## Phase 3: Export to engine presets

**Do**
1. Export with the built-in presets for **Unreal, Unity, Godot, and Blender**.
2. Verify the exported maps against the target engine's material inputs
   (albedo / normal / roughness / metalness / AO per the preset).
3. If the source material is a Substance file: stop. **`.sbsar`/`.spp` are
   proprietary and cannot be loaded.** Import textures instead.

**Check**
- The exported texture set matches the target engine's expected channels;
  nothing silently dropped.

**Why**
- The author considered importing Substance materials and rejected it on
  copyright grounds ("that seems to be against copyright rules"), so the
  growth strategy is the community making and sharing materials, and the
  interoperability story is export presets instead of format conversion.

## The human method, distilled

1. **Ship the tool, grow the asset commons**: the value of a painting tool is
   its materials library — make the community the library (Discord for bug
   reports, releases on GitHub).
2. **Route around proprietary formats** with export presets instead of
   fighting import.
3. **An AI-assisted solo dev can ship a DCC tool**: prompt, debug, test,
   ship. (The thread's own proof: the author built this with Claude.)

## Failure modes

- **Substance lock-in doesn't transfer**: any pipeline relying on `.sbsar`
  procedural graphs has no path into material-painter; plan texture imports
  or rebuilds.
- **Un-notarized Mac build**: first launch requires right-click > Open; this
  is a distribution friction, not a bug.
- **Community-content bet**: the author's strategy assumes a material-sharing
  community forms; today the library is thin (commenter Rikarin's objection:
  "no one will start using it because there's no community/assets available").

**Depth status:** FULL (author's comments carry the feature set, the WGSL /
GPU-bake differentiators, the ArmorPaint comparison, the copyright position,
and the Mac build notes).
