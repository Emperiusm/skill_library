---
name: spa-materials-baker-lumen-texture-bake
description: "Bake active Lumen lighting and reflections into textures in Unreal Engine with SPA Materials Baker V3.1: capture the rendered scene appearance (Lumen, reflections, sky, post-process, Lightmass bakes, decals, mesh overlays) as textures, one texture per material with Combine Lighting, Draft then Standard quality, and GLB export for reuse outside Unreal. Trigger when a UE scene needs to look like Lumen on VR, mobile, or low-end hardware without running Lumen."
---

# SPA Materials Baker: Bake Lumen Lighting into Textures

## Purpose

This skill reconstructs the SPA Materials Baker V3.1 workflow from the author's
video, post, and comments, step by step, so another agent can follow the same
process. Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The core method is: bake the
look, not the light.

## Source

Creator: Ali Shantia. Video: "Bake Lumen Lighting into Textures in UE5 | SPA
Materials Baker V3.1", https://youtu.be/wXYWbYiXq8w (5:15, no captions;
downloaded and 12 frames reviewed; the frames carry burned-in subtitles).
Reddit post: https://www.reddit.com/r/unrealengine/comments/1xua15y/finally_you_can_bake_lumen_lighting_and_reflections_into/ (r/unrealengine
post 1xua15y, score 23, 14 comments). Fab listing:
https://fab.com/s/4baa5507c1e8. Documentation:
https://sepinood.github.io/SPAMaterialBake/. Sample GLB exported for the video:
https://drive.google.com/drive/folders/1dkkuBiZzNMit3YlDljYk1fntzh3v9MH4?usp=sharing.
2026-11-13 scout run, audit 1.

This is a distinct tool from the UE 5.8 video-in-materials skill
(`ue58-video-in-materials`): that one plays video inside materials; this one
bakes a whole lit scene into textures. Do not merge them.

## Tools used

**SPA Materials Baker V3.1** (Unreal Engine plugin, on Fab), **Unreal Engine**
Lumen, **Lightmass** (optional, for reading existing bakes).

## Phase 1: Set up the scene as usual

**Do**
1. Build the scene with normal Unreal lighting. The demo room uses point
   lights, rect lights, and a spot light, plus decals and an emissive mesh
   (a blue neon strip). The author's narration: "I've added decals. These
   project extra surface detail onto the meshes."
2. Keep the materials, decals, and mesh overlays you want flattened. The tool
   also bakes sky and post-process contributions and can read an existing
   Lightmass bake.

**Check**
- The live-lit scene reads correctly before any baking starts. In the video,
  the opening frame shows the live room next to the baked result; the two
  should read the same at a glance (warm wall light, blue neon spill, gate
  and fern shadows on the brick wall).

**Why**
The bake captures what the scene looks like, so the scene has to look right
first. A bake cannot fix a bad light.

## Phase 2: Switch the bake source to Batch Meshes

**Do**
1. Open the SPA Materials Baker panel (shown as "SPA Materials Baker V3.1" in
   the editor UI).
2. Under Mesh Settings, switch Bake Source to Batch Meshes. The author's
   narration: "Then under Mesh Settings I'm switching Bake Source to Batch
   Meshes."

**Check**
- The panel shows the batch list of selected meshes before baking.

**Why**
Batch mode bakes the whole room in one pass instead of one material at a time,
which is what makes the workflow a scene operation rather than a per-asset
chore.

## Phase 3: Combine Lighting into the albedo

**Do**
1. Enable Combine Lighting. The author's narration: "Combine Lighting puts the
   lighting into the albedo, so we get one texture per material."

**Check**
- One texture per material comes out, with the lighting already in it.

**Why**
One lit texture per material is the whole point of the tool: the material
becomes simple (no dynamic lights, no layered materials, no separate
projection effects), which is what VR, mobile, and low-end targets need.

## Phase 4: Bake at Draft, then re-bake at Standard

**Do**
1. Bake first at Draft quality.
2. Change the quality from Draft to Standard and bake again. The author's
   narration: "So I'm changing the quality from Draft to Standard, and baking
   again. It takes a bit longer, but the reflections come out cleaner."

**Check**
- Compare the Standard bake against the Draft bake; the reflections should
  read cleaner. The author shows the floor tiles and stair treads as the
  comparison surfaces.

**Why**
Draft is for iterating the setup; Standard is the deliverable. Paying the
longer bake once, at the end, is cheaper than re-baking Standard after every
settings change.

## Phase 5: Export and reuse

**Do**
1. Export the results. V3.1 adds GLB export for selected level meshes; the
   sample GLB for this video is on the author's Drive, and the modular assets
   in it use separate textures, each with a 1K output (author, in comments).
2. For settings questions, check the online documentation. The author's
   narration: "If you have any questions about the settings, check the online
   documentation. The link's in the description. And you can get the exported
   GLB file here."

**Check**
- The exported GLB opens outside Unreal with the baked look intact. The video
  closes on a Babylon.js viewer showing the baked room.

**Why**
The deliverable is a reusable texture-based asset, not a render. The GLB
export is what lets the baked look leave Unreal.

## The human method, distilled

1. Bake the look, not the light: the captured lighting is a snapshot, and the
   author is explicit that it "won't change with moving lights or viewpoints."
2. Verify baked against live, side by side, before exporting.
3. Draft first, Standard once, at the end.
4. Know what the bake is for: the author positions it for VR, mobile, and
   low-end projects, and warns it is "mainly designed to help optimize
   (material, light, decal, ...) workflows, not simply make files smaller."
   A commenter puts the use case plainly: "I could see it useful for low end
   or the Series S if you want the game to look at close to lumen as possible
   with it off."
5. A baked snapshot is a tradeoff, not a replacement: the author states this
   is "an optional workflow, not a replacement for using Lumen in real time."

## Failure modes

- **Moving lights or a moving camera after the bake.** The baked lighting is
  fixed. If the scene needs dynamic lights, do not bake it; keep Lumen live.
- **Wrong UV layout.** The author: the result "depends on the source materials,
  bake settings, and most importantly a suitable UV layout." Check the UVs
  before blaming the bake.
- **Baking at Standard too early.** Every settings change after a Standard bake
  costs a full slow bake. Iterate at Draft.

**Depth status:** FULL (video downloaded, 12 frames reviewed, frames carry
burned-in subtitles; full post text; 13 comments read; no captions exist for
this video).
