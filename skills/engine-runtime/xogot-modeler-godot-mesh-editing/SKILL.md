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

## AAA studio practice

In-editor modeling and blockout-first level design are AAA disciplines, not
just convenience features. Naughty Dog's Uncharted 2 postmortem (GDC 2010)
documents the block-mesh-first rule: "Levels were first designed using block
mesh, which let the team sketch out an experimental flow, and they simply
began building out the level with art, play testing, and iterating." The same
talk carries the caution: rushing from block mesh straight into art without a
reflection beat meant the team missed opportunities to create interesting
scenes and produced misleading, confusing design. Source: GameSpot report of
Richard Lemarchand's GDC 2010 talk,
https://www.gamespot.com/articles/naughty-dog-dissects-uncharted-2/1100-6253470/

Insomniac started Manhattan for Marvel's Spider-Man (9,800+ buildings, their
densest city to date) with early block-outs "based on more polygon like
structures as the building blocks", then ran a Houdini modularization pass
that cut per-building time from 30 minutes to 4 hours by hand to 5 to 15
minutes, freeing artists to dress and polish; a Polyline tool turned standard
building blocks into varied architecture, and the city was split into
districts with "beautiful corners" carrying each district's dressing. The
pattern is blockout primitives, then procedural/modular variation, then dress,
without rebuilding the layout. Insomniac's procedural systems were
"originally designed to support iterations and dependencies" and were used to
"author, modify and monitor much more content than planned", so the blockout
layer is treated as a monitored, re-generable system, not disposable scratch
geometry. Sources: VR Voice report of the GDC 2019 talk,
https://vrvoice.co/world-building-spider-mans-manhattan-with-substance/ ;
Game Developer summary of David Santiago's GDC 2019 talk,
https://www.gamedeveloper.com/programming/video-procedurally-creating-manhattan-for-i-marvel-s-spider-man-i-
(The per-building time figures come from a secondary report of the GDC panel,
not from Insomniac's own published text.)

Epic's UE5 Modeling Mode is the direct engine-side analogue to Xogot: a full
in-editor polygon-modeling toolkit (Shapes, PolyEdit, TriEdit, deform, UV
tools) built so artists stop round-tripping to a DCC. "How do you block out
your level, and sculpt some rocky terrain? ... These workflows typically
require you to jump out of Unreal Engine, go back to your DCC, make
adjustments, and reimport. That process could repeat numerous times with
multiple artists. UE5's modeling tools can help make those changes directly
in the editor, cutting out costly transfers." It also documents the hazard
that comes with in-editor editing: edits operate on the saved asset itself
and affect every instance ("your interactions are operating directly on the
saved version of the static MeshAsset and this will impact any instances of
that asset"), with an Accept/Cancel commit model and per-user subfolders plus
random-string suffixes so generated assets never collide or overwrite shared
data. Source: Epic Games, "Unreal Engine 5's modeling mode takes shape",
https://www.unrealengine.com/tech-blog/unreal-engine-5-s-modeling-mode-takes-shape

Ubisoft Massive built Snowdrop (The Division, The Settlers, South Park)
around a unified game and editor and fast iteration as a core principle:
"The game and the editor are unified, and everything in the engine runs in
real time, which means that the ongoing project is always playable", and
"for Snowdrop, it was important to prioritize iteration so we could start
and test the game quickly", explicitly contrasted with a prior engine that
took up to 45 minutes to compile. The Xogot parallel: the value of in-editor
modeling is not the modeling per se, it is that the level stays playable
while it is being shaped. Source: Ubisoft Massive, "The History of Snowdrop:
From R&D Concept to AAA Engine",
https://www.massive.se/blog/games-technology/snowdrop/the-history-of-snowdrop-from-rd-concept-to-aaa-engine/

No source documents a specific AAA studio using Xogot, Godot in-editor
modeling, or equivalent Godot tooling. All AAA evidence above is from
Unreal, Snowdrop, and proprietary engines with Houdini/Maya pipelines; the
transferable claim is the workflow discipline, not the tool. No source was
found documenting AAA use of in-editor collision generation as a distinct
practice, or AAA UV/material authoring inside the engine editor; do not
invent claims for those Xogot features.

### Agent automation

- **Blockout gate.** Before any material, UV, or detail work, playtest the
  level from the blockout with a character controller at real scale, and label
  each space by gameplay intent (combat, puzzle, safe, traversal). Record a
  `blockout_manifest` (scene metadata or a text file listing each blockout
  mesh, its gameplay intent, and its playtest status); every mesh must be
  marked playtested or explicitly untested before detailing begins.
  (Grounded in Naughty Dog's block-mesh-then-playtest loop.)
- **Proxy-swap promotion check.** Keep blockout meshes as named, separable
  assets (e.g. a `*_blockout` naming convention) so a finished mesh can
  replace a blockout mesh in place without touching transforms or collision.
  A scripted scan of the scene verifies every `*_blockout` mesh still has a
  matching collision shape and no blockout mesh carries final materials.
  (Labeled inference: an adaptation of Insomniac's blockout-to-modular
  pipeline, not a pattern any source documents for Godot.)
- **Shared-asset safety check.** Before accepting any in-editor mesh edit,
  verify whether the edited mesh resource is shared by other scenes or
  instances, and warn that the edit hits the saved asset and all its
  instances. Automatable as a GDScript/EditorScript scan listing scenes
  referencing the edited `.res`/mesh. (Grounded in Epic's explicit Modeling
  Mode warning; the Godot-side scan implementation is an inference.)

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
