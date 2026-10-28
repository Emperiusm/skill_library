---
name: ai-3d-engine-export
description: "Hand an AI asset to Unity, Unreal, or Blender without losing scale, materials, or pivots: shared export gates plus per-target settings tables and a fresh-scene re-import proof. Trigger when exporting an AI asset into an engine or DCC tool."
---

# Engine and DCC Export for AI Assets

## Purpose

This skill is one canonical export checklist with per-target sections,
not three separate checklists: the shared gates are identical across
Unity, Unreal, and Blender, and only the values differ. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The core method is: shared gates
first, per-target settings second, re-import proof always.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/export-ai-3d-assets-for-unity
- https://customuse.com/learn/export-ai-3d-assets-for-unreal-engine
- https://customuse.com/learn/how-to-export-ai-3d-assets-for-blender
- https://customuse.com/learn/ai-3d-to-blender-workflow

Evidence note: one member article's FAQ tail was unseen; all substantive
sections were read.

## Tools used

Tools used: Unity, Unreal Engine, Blender as destinations; DCC tools
for finishing. FBX is the default handoff for rigged and engine work;
GLB for PBR-first and web delivery; USD for studio assembly.

## Phase 1: Apply the shared gates, every target

**Do**
1. Set real-world scale before export. AI output scale is arbitrary
   until you set it.
2. Bake transforms and freeze them. Unbaked transforms are the most
   common source of import surprises.
3. Place the pivot deliberately (base for props that sit on floors,
   center for hanging or floating assets).
4. Verify material slots and texture paths survive: slots intact, maps
   connected, no absolute paths pointing at a generator's temp folder.
5. Re-import the exported file into a fresh scene and verify it there,
   not in the scene you exported from.

**Check**
- Scale, pivot, slots, and paths all survive a fresh-scene re-import?
- Would a teammate opening only the exported file get the right asset?

**Why**
These gates are target-independent: every engine and DCC tool punishes
the same five mistakes. Doing them once, identically, is what keeps
three export targets from drifting into three different checklists.

## Phase 2: Unity settings

**Do**
1. Export FBX and set the Unity scale factor to 0.01 for
   centimeter-sourced assets, so the asset lands at real-world size.
2. Run Extract Materials so Unity creates editable material assets
   instead of embedded read-only ones.
3. Assign URP Lit or HDRP Lit shaders to match the render pipeline;
   do not leave materials on a generic shader.
4. Validate in a Unity scene: 1:1 scale, two material slots intact
   where applicable, normals not inverted, no import warnings.

**Check**
- Scale 1:1, slots intact, normals correct, zero warnings?
- Are materials editable assets, not embedded?

**Why**
Unity's scale factor and material extraction are the two Unity-specific
traps: both fail silently, and both are trivial once they are on the
checklist.

## Phase 3: Unreal settings

**Do**
1. Work in centimeters: Unreal uses centimeters, so the asset imports
   at 100x the meter-scale value. Set Import Uniform Scale to 100
   where the source is in meters.
2. Bake Z-up orientation on export so the asset does not arrive lying
   down.
3. Pack occlusion, roughness, and metallic into one ORM texture
   (AO in R, roughness in G, metallic in B) for the Unreal material.
4. Enable Generate Lightmap UVs where baked lighting is needed.
5. Decide Nanite explicitly: record whether the asset uses Nanite or a
   manual LOD chain.
6. Follow the naming convention: SM_ for static meshes, SK_ for
   skeletal meshes, M_ for materials, T_ for textures.

**Check**
- Lands at the right size, upright, with ORM packed and lightmap UVs
  where required?
- Naming follows SM_, SK_, M_, T_ so the asset is findable later?

**Why**
Unreal's centimeter scale is the single most expensive silent failure
in this skill: a 100x asset looks correct in a thumbnail and absurd in
a level. Naming is not bureaucracy; it is how a level with hundreds of
assets stays searchable.

## Phase 4: Blender settings

**Do**
1. Apply transforms with Ctrl+A so scale, rotation, and location are
   baked into the mesh.
2. Recalculate normals with Shift+N and check the Face Orientation
   overlay: blue out, red in.
3. Wire materials through Principled BSDF nodes, with PBR maps in
   their correct sockets.
4. Run Pack Resources so textures travel inside the file.
5. Re-import into a fresh Blender scene and verify: the fresh-scene
   re-import loop is the Blender proof, not the working scene.

**Check**
- Face Orientation all blue outward? Transforms applied? Resources
  packed?
- Does the fresh scene show the same asset, or did something only
  exist in the working scene's dependencies?

**Why**
Blender's working scene hides missing dependencies: linked textures,
unapplied transforms, and flipped normals all look fine until the file
moves. The fresh-scene loop is what makes the export portable.

## The human method, distilled

1. Shared gates first, per-target settings second. Never maintain
   three separate checklists.
2. Scale is a setting, not a property of the mesh. Set it per target.
3. Materials must survive as editable assets with connected maps.
4. Fresh-scene re-import is the proof for every target. No exceptions.
5. Record Nanite and naming decisions; ambiguity is how assets rot.

## Depth status

FULL (article text; substantive sections read, one FAQ tail unseen).
