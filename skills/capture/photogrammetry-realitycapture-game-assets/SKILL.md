---
name: photogrammetry-realitycapture-game-assets
description: "Turn real-world objects into game assets with photogrammetry: shoot overlapping photos in manual mode, reconstruct in RealityCapture, understand the feature-point triangulation underneath, then clean up and bake color and normal maps for the game-ready version. Trigger when scanning real objects for games, film, or VR."
---

# Photogrammetry to Game Asset: RealityCapture Workflow

## Purpose

This skill captures real-world objects as game assets through
photogrammetry: consistent photography, reconstruction, and the
cleanup pass that makes the scan game-ready. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it),
and **Why** (the principle). The core method is: consistent photos
in, raw scan out, optimized asset with baked maps at the end.

## Source

Instagram, kennedy_artist ("The Graphics dude") (transcribed from
reel audio with faster-whisper tiny, 2026-11-02; captions unavailable
via API):

- https://www.instagram.com/reel/Dap90ZqMjNa/ — "How 3D Scanning works"

Evidence note: reel-length narration (about 3 minutes); machine
transcription, minor word errors possible. Tool names and the
workflow order are as spoken.

## Tools used

Tools used: any camera that takes consistent photos (phone, camera,
drone); RealityCapture (free, part of the Epic Games ecosystem;
"there are a lot of other free alternatives"); game engine of
choice. Load-bearing caveat from the narration: "Reflective and
plain-colored objects won't scan at all, because there would be no
detail on the surface for the computer to hang on to."

## Phase 1: Shoot for the solver, not for beauty

**Do**
1. Take many photos around the object, ensuring overlap between
   shots.
2. Shoot everything in manual mode: "that way we get consistent
   colors and brightness values across the images."

**Check**
- Is there overlap between every adjacent pair of photos?
- Are exposure, white balance, and focus locked (manual mode)?

**Why**
The reconstruction does not see the object; it sees detail points
tracked across images. Inconsistent exposure breaks the matching the
whole pipeline depends on. Manual mode is not about image quality,
it is about giving the solver consistent input.

## Phase 2: Reconstruct and understand what happened

**Do**
1. Feed the images into RealityCapture and "just click start and let
   it do its thing."
2. Know what it did: the software identifies detail points appearing
   across several images, tracks how they shift relative to one
   another, and uses triangulation to place them accurately in 3D
   space while also solving each camera's position (selecting a
   camera icon displays its corresponding image).
3. Every three points connect into triangles; millions of triangles
   make up the 3D object.

**Check**
- Do the solved camera positions make sense against where you
   stood?
- Is the raw mesh complete, or are there holes where the solver
   found no detail?

**Why**
Understanding the triangulation underneath tells you why scans fail:
no surface detail means no trackable points, which means no geometry.
Holes in the mesh are missing data, not bugs, and they trace back to
the shoot.

## Phase 3: Clean up and bake the game-ready asset

**Do**
1. Clean up the raw scan and create an optimized version of the
   asset: "that is what we use in game."
2. Transfer the color into an image texture and the surface detail
   into a normal map texture.
3. Judge the result against modeling: scanning captures "insane
   detail that you might not even think about," plus it preserves
   historical artifacts.

**Check**
- Is the optimized asset actually game-usable (polygon budget,
   clean topology)?
- Do the baked color and normal maps carry the detail the raw scan
   had?

**Why**
The raw scan is evidence, not an asset. The cleanup-and-bake pass is
where the scan becomes usable: detail moves into textures where it
is cheap, and geometry keeps only what the silhouette needs.

## The human method, distilled

1. Manual mode, overlapping shots; consistency over beauty.
2. RealityCapture (or equivalent) for the reconstruction; know the
   triangulation underneath.
3. Reflective and plain-colored objects will not scan; plan around
   it.
4. Clean up, optimize, bake color and normals; the raw scan is not
   the asset.
5. Scan when the detail exceeds what you would model by hand.

## Depth status

PARTIAL (transcribed reel audio, about 3 minutes; workflow order and
tool names as spoken; no frame-level verification).
