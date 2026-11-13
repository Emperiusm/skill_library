---
name: xogot-modeler-godot-mesh-editing
description: "Build and edit 3D meshes directly inside the Godot editor with Xogot Modeler (first public beta, Godot Asset Store): block out levels with basic shapes, edit vertices, edges, and faces, extrude and bevel, draw curved shapes, apply materials, adjust UVs, and generate collision shapes, all output as standard Godot meshes and nodes with no proprietary format. Trigger when level blockout or simple assets need to happen in-editor instead of round-tripping to Blender."
---

# Xogot Modeler: Build and Edit 3D Meshes Directly in Godot

## Purpose

This skill reconstructs the Xogot Modeler workflow from the author's post, step
by step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The core method is: model inside the editor, ship standard
meshes.

## Source

Creator: XogotApp (Miguel). Reddit post:
https://www.reddit.com/r/godot/comments/1xuenon/build_and_edit_3d_meshes_directly_in_godot_with/
(r/godot post 1xuenon, score 25, 2 comments). Godot Asset Store:
https://store.godotengine.org/asset/xogot/modeler/. Blog post with background
and demonstrations: https://blog.xogot.com/xogot-modeler-for-godot/. Earlier
preview: https://www.reddit.com/r/godot/comments/1wz5py3/modeler_prototype_levels_and_assets_from_the/.
2026-11-13 scout run, audit 2.

This is a distinct tool from the Godot runtime procedural-creature skill
(`godot-runtime-procedural-creatures`): that one generates creatures at
runtime; this one is an editor modeler for hand-built levels and assets. Do not
merge them.

## Tools used

**Xogot Modeler** (first public beta, Godot Asset Store), **SwiftGodot** (the
desktop port layer; Xogot itself is written in Swift).

## Phase 1: Block out with basic shapes

**Do**
1. Start with basic shapes to block out a level or environment, or to create a
   simple 3D asset, without leaving the Godot editor.

**Check**
- The blockout reads as the intended space before any detail work starts.

**Why**
The tool exists because the authors "really missed having something like
Blender available" on Xogot for iPad; the blockout stage is the part of
Blender they needed first.

## Phase 2: Edit the geometry directly

**Do**
1. Edit vertices, edges, and faces.
2. Extrude and bevel geometry.
3. Draw curved shapes.

**Check**
- The edited mesh holds its intended silhouette from the editor views.

**Why**
Direct mesh editing, rather than assembling primitives, is what separates a
modeler from a level blockout kit.

## Phase 3: Finish the asset in-editor

**Do**
1. Apply materials and adjust UVs.
2. Generate collision shapes.

**Check**
- The asset renders with its materials and collides as expected in a test
  scene.

**Why**
Materials, UVs, and collision are the minimum for an asset to be usable in a
game; without them the modeler would only produce grey boxes.

## Phase 4: Ship standard Godot meshes

**Do**
1. Export nothing special: everything Modeler creates uses standard Godot
   meshes and nodes. The author: "There's no proprietary mesh format or custom
   runtime required, and your scenes work just fine without the addon installed.
   You only need the Modeler to continue editing the geometry with its
   specialized tools."

**Check**
- Disable or remove the addon and confirm the scene still loads and renders.

**Why**
Compatibility is the design constraint the authors call out explicitly: the
tool must never hold a project hostage. That is also why it ports cleanly to
desktop Godot (Xogot is written in Swift; the desktop port uses SwiftGodot).

## The human method, distilled

1. Bring the missing tool to where the work happens, instead of round-tripping
   to another application.
2. Make compatibility a feature: standard meshes out, no lock-in.
3. Ship a beta and ask what is missing ("let us know what works, what doesn't,
   and what you'd like to see us add next").

## Failure modes

- **Expecting a Blender replacement.** This is a first public beta for levels,
  blockout, and simple assets. Complex sculpting and hard-surface modeling
  still belong in Blender.
- **Assuming the addon must stay installed.** It must not: if a scene breaks
  without the addon, that is a bug in the compatibility promise, not a
  workflow requirement.

**Depth status:** PARTIAL (full post text; the 2 comments could not be
retrieved: Arctic Shift returned HTTP 422, old Reddit JSON returned 403, and
the PullPush API returned 403; the linked blog post and demonstration video
were not retrieved, no live browser in this loop).
