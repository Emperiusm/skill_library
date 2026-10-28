---
name: ai-3d-pbr-materials-textures
description: "Author and verify PBR materials for AI assets: channel meanings and color spaces, material-first texture prompting, normal map generation versus checking, the two-light and moving-light tests, and the 2K-master rule. Trigger when texturing an AI asset with PBR maps."
---

# PBR Materials and Textures for AI Assets

## Purpose

This skill makes AI textures behave like materials instead of pictures:
separated channels, correct color spaces, and tests that catch baked
lighting before it ships. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: define the material first, generate to
it, and test it under lights that move.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/what-are-pbr-materials
- https://customuse.com/learn/ai-texture-generator-for-3d-assets
- https://customuse.com/learn/ai-normal-map-generator-for-3d-assets
- https://customuse.com/learn/what-is-a-normal-map

Evidence note: one member article's FAQ tail was unseen; all substantive
sections were read.

## Tools used

Tools used: AI texture generators, DCC tools (Blender, Substance) for
map authoring and testing, engines for in-context verification. The
tests below are tool-agnostic.

## Phase 1: Define the material before generating

**Do**
1. Name the material and its channels before generating anything:
   albedo (base color, no baked shadows), normal, roughness, metallic,
   and where applicable ambient occlusion.
2. Assign material regions to slots: metal, fabric, glass, and painted
   surfaces each get their own slot. A single fused painted map is not
   a material.
3. Prompt material-first: describe the material regions so they can
   become slots, not just the object's appearance.

**Check**
- Can you list the slots and what each one carries?
- Does the albedo contain shadows or highlights baked in? If yes, it
  is not an albedo yet.

**Why**
PBR is a contract between maps and lights. A baked shadow in the albedo
is a second, frozen light that fights every real light in the scene
forever.

## Phase 2: Generate at 2K master and pack ORM

**Do**
1. Generate and keep a 2K master for every map, then derive lower
   resolutions per platform budget (1024 standard, 512 background).
2. Pack occlusion, roughness, and metallic into one ORM texture:
   ambient occlusion in R, roughness in G, metallic in B.
3. Keep color spaces straight: color maps in sRGB, data maps (normal,
   roughness, metallic, ORM) linear. A data map flagged as color is a
   silent material failure.

**Check**
- Is there a 2K master to regenerate platform sizes from?
- Are data maps linear and color maps sRGB, without exception?

**Why**
The 2K-master rule exists because downscaling is free and upscaling is
fiction. Color-space errors do not look like errors in a viewer; they
look like wrong materials in the engine.

## Phase 3: Normal maps, generated or checked

**Do**
1. Distinguish the two jobs: generating a normal map (from high-poly
   bake or from a height source) versus checking a baked one.
2. When checking, verify the green channel convention for the target:
   OpenGL Y+ versus DirectX Y-. A flipped green channel inverts the
   lighting direction on the surface.
3. When generating from a height source, confirm the detail reads at
   the map's shipping resolution, not just at master resolution.

**Check**
- Does the surface light from the correct direction under a known
  light?
- Is the green channel convention recorded for this asset's target?

**Why**
Normal maps are the highest-leverage cheap detail in a game asset, and
the green-channel flip is the classic silent failure: the asset looks
fine until a light moves, and then it looks inside out.

## Phase 4: Test under lights that move

**Do**
1. Run the two-light test: light the asset from two opposed
   directions and confirm no baked highlight or shadow survives both.
2. Run the moving-light test: sweep a light across the asset and watch
   for highlights that stay glued to the texture instead of traveling
   with the light.
3. Test in the engine under the level's lighting, not the generator's
   preview lighting.

**Check**
- Do highlights travel with the light, or do they stay painted on?
- Does the asset read correctly under the scene's lighting, not just
  the preview's?

**Why**
A static preview cannot catch baked lighting; only a moving light can.
This is the test that separates a texture from a material, and it costs
minutes where a shipped failure costs days.

## The human method, distilled

1. Material first, generation second. Slots before pixels.
2. 2K master, derive down. Never upscale a shipped map.
3. Data maps linear, color maps sRGB. No exceptions.
4. Green channel convention is a per-target fact. Record it.
5. Moving light is the verdict. Static previews cannot catch baked
   light.

## Depth status

FULL (article text; substantive sections read, one FAQ tail unseen).
