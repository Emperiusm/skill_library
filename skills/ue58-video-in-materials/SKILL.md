---
name: "ue58_video_in_materials"
description: "Route real video into Unreal materials: Media Framework pipeline, procedural scanlines, CRT glass, mosaic UV math, SubUV flipbooks, yaw-only billboards, light-function projectors. Trigger when putting video on screens or in materials in UE."
---

# Unreal 5.8: Video in Materials (Materials Masterclass Ch8)

## Purpose

This audit reconstructs the exact techniques from the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: route real video into the material system, then use math-driven UV work for effects that are cheaper and more controllable than texture assets.

## Source

Creator: Enrique Ventura

Source: https://www.youtube.com/watch?v=vp2tBQiLuM4 | 49:32 | r/unrealengine post 1wqu5r7 (score 26) | 888 views | 2026-09-28 scout run

## Tools used

Tools used: Unreal Engine 5.8; Media Framework (Media Player, File Media Source, Media Texture); Material Editor; Blueprint; Volumetric Fog.

## Phase 1: Pipe an MP4 into a material via the Media Framework

**Do**
1. Drag an MP4 directly onto a mesh; UE auto-creates a **File Media Source** asset, a **Media Player**, and a **Media Texture**.
2. Open the Media Player; set the playlist to **Loop** for permanent playback.
3. Inspect the Media Texture: it starts as a microscopic **2x2** blank texture and "dynamically resize[s] to match the video perfectly" once data arrives. Set filter to **Nearest** and set the clear color (what it returns when video stops).
4. Create a material, set shading model **Unlit**, add a **Texture Sample Parameter** named e.g. "media texture", assign the live asset, plug RGB into **Emissive Color**.

**Check**
- Pause the Media Player mid-frame, reopen the Media Texture: "it has updated to capture that exact pause frame and the resolution has dynamically snapped to match the video file."

**Why**
- A TV "emits its own light", so emissive-only unlit output is physically right and cheapest.

## Phase 2: Retro scanlines, fully procedural

**Do**
1. TextureCoordinate to ComponentMask (isolate green channel to vertical gradient).
2. Multiply by a scalar parameter **Scan Line Count** = 100 (use right-click "promote to parameter" on the pin, auto-creates the parameter).
3. Feed through a **Sign** node to 100 alternating black/white lines; run through a **Lerp** with alpha = **Scan Line Brightness** = 0.75 (B fixed at 1.0) so lines don't delete the video.
4. Multiply the mask by the video output to Emissive.

**Check**
- Two exposed controls: how many lines, how dark they get.

**Why**
- Procedural scanlines cost a handful of ALU ops and are resolution-independent, no texture asset needed.

## Phase 3: CRT glass via Clear Coat

**Do**
1. Change shading model from Unlit to **Clear Coat**; keep video in Emissive, **Roughness = 1** (matte video), **Clear Coat Roughness = 0**.

**Check**
- The screen now reflects the scene on top of the video.

**Why**
- An old CRT is "a glowing layer... behind a layer of glass"; clear coat approximates it in one shading model.

## Phase 4: Mosaic video wall with UV math

**Do**
1. Add scalar parameters **Columns**, **Rows**, **Index**.
2. Columns/Rows to Make Vector 2; TexCoord divided by vector (UVs shrink to 1 tile).
3. X offset: **FMod(Index, Columns)**; Y offset: **Floor(Index / Columns)**; AppendVector to offset vector; divide by the same scale vector; **Add** to scaled UVs, into the texture UV input.
4. Make it universal: put the grid math behind a **Static Switch Parameter** named "mosaic" (false branch = plain TexCoord) so one material serves single TVs and walls; the 3x3 demo wall used material instances with indices 0-8.

**Check**
- Index 0..3 on a 2x2 grid shows each tile in turn; index 4 wraps to the first tile.

**Why**
- One material, one texture, N screens: the instancing story replaces N materials.

## Phase 5: Sprite-sheet flipbook via SubUV Function

**Do**
1. New material: Unlit + **Masked** blend mode ("going to save on performance versus translucent") for pixel art.
2. Use the **SubUV Function** (double-click reveals it implements the Phase-4 math): Texture Object input = **Sprite Sheet** texture object (reference only, "we cannot get colors or values from here"); Sub Images = Vector Parameter **XY Size** (e.g. 8, 1); Frame = Time x **Frames Per Second** (8) to **Floor**.
3. RGB to Emissive, Alpha to Opacity Mask; optional **Emissive Boost** parameter (5-10).

**Check**
- Material previews one frame at a time, advancing 8 frames per second.

**Why**
- The frame-count parameter, not a fixed texture size, makes the function reusable; Floor guarantees integer frames ("never... frame 1.3 or 7.2").

## Phase 6: Camera-facing sprites in Blueprint

**Do**
1. Blueprint with static-mesh base, warm-orange **Point Light** (casts real shadows), and a plane with the flipbook material.
2. Event graph, once per tick: **Find Look At Rotation** from the flame's world location to the camera (via **Get Player Camera Manager** to **Get Camera Location**); split the result, keep **Yaw only** (+90 degree correction for the author's mesh), and re-use the flame's current roll/pitch (**Get World Rotation**) for X/Y.

**Check**
- Play: flames face the camera; jumping shows the limitation, flames don't tilt, "one of the problems of" billboard sprites.

**Why**
- Full billboard breaks verticality; yaw-only keeps the flame grounded in the scene.

## Phase 7: Auto-play video + spatial audio via Blueprint

**Do**
1. Level Blueprint: two **Media Player object reference** variables with defaults set to the two players; both **Play on Open**; **Open Source** on each.
2. Speaker Blueprint: a cube mesh + **Media Sound** component whose Media Player source is set; override attenuation, enable the first three types: volume attenuation, binaural (left/right) panning, air absorption; inner radius 400.

**Check**
- Walk toward/away: volume, pan, and high-frequency absorption change with distance.

**Why**
- Author's principle: sound should live at points in the world ("a Dolby Atmos setup" of speaker blueprints), not inside the media player, editor playback sound and in-game sound are different paths.

## Phase 8: Real movie projector via Light Function materials

**Do**
1. Create material, set **Material Domain** from Surface to **Light Function** (only Emissive Color stays active).
2. Scale/offset the media texture to fit the spotlight cone: TexCoord x scale to 1-X ("inverse scale" so 1 = texture size), subtract half the scale factor (centers it).
3. Kill edge-stretch pixels with two **Step** masks: one on min(U,V) vs 0, one on max(U,V) vs 1; multiply to clean square inside the cone.
4. Assign to a **Spotlight**; add **Volumetric (Exponential Height) Fog** so the beam becomes visible light shafts that wrap around characters stepping into the beam.
5. Troubleshooting console settings: Project Settings, search "atlas", set **Light Function Atlas Format** to **8 bit RGB** (default 8 bit grayscale); console: `r.LightFunctionAtlas.Resolution` (default 256/512 to 1024/4K), and `r.VolumetricFog.GridPixelSize` (default 8 to 4; 2 or even 1 in extreme cases).

**Check**
- Character steps into the beam and casts dynamic shadows on the screen while the movie wraps around their back.

**Why**
- "It's actually the physics of the light projecting the image", interactivity (occlusion) comes free with real projection. Author's memory warning: raising both atlas resolution and fog resolution "can make your scenes really blow up in memory consumption."

## The human method, distilled

1. Rebuild the primitive yourself first (mosaic UV math), then adopt the built-in node (Flipbook/SubUV), "know exactly how that math works under the hood".
2. Expose everything as parameters (promote-to-parameter), never hardcode.
3. One material + instances over N bespoke materials.

## Depth status

FULL (complete captions, 1013 segments, + 14 reviewed frames).
