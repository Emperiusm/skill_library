---
name: godot-48-trail3d-fogvolume-dust
description: "Exercise Godot 4.8 RC1's new Trail3D node and FogVolume volumetric fog in one training-ground scene: align the sword trail to the swing plane with mesh_alignment Local on a blade pivot, build break dust as real volumetric fog with a short custom shader at volume_size 160 and volume_depth 128, temporal reprojection 0.6, and anisotropy 0.6, and fix dark dust locally with warm emission on the sun-facing side instead of changing the global fog. Trigger when a Godot 4.8 scene needs a weapon trail or a lit, shadow-catching dust burst."
---

# Godot 4.8 Trail3D Sword Trail and FogVolume Dust Burst (RC1)

## Purpose

This skill reconstructs the exact workflow OkGarage1715 shows for exploring Godot 4.8 RC1 in a training-ground scene: a sword trail from the new Trail3D node, and break dust built from real volumetric fog. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: exercise each new feature in one scene, and when a feature fights the scene, fix it locally at the effect instead of changing the global setup.

## Source

Creator: OkGarage1715. Post: "Godot 4.8 is cooking..." — https://www.reddit.com/r/godot/comments/1y78ocx/godot_48_is_cooking/ (score 381, 14 comments, all retrieved). Video: https://v.redd.it/irhrlq8cz84i1. Scout audit 2026-11-28, audit 3, PARTIAL. Godot 4.8 is an RC1 in this post, not a release; do not treat these nodes as shipped.

## Tools used

Godot 4.8 RC1, Trail3D node (new in 4.8), FogVolume plus a custom fog shader, RigidBody3D, screen-space contact shadows (new in 4.8) and multi-bounce AO, Quaternius Universal Base Characters plus Universal Animation Library, free asset packs from Sketchfab, textures from Poly Haven and ambientCG. No shader source or license statement for the Quaternius assets is given in the retrieved text. The Trail3D width value is unknown: the retrieved comment text is truncated at 800 characters and the value is not guessed here.

## Phase 1: Build the training ground on 4.8 RC1

**Do**
1. "Grabbed 4.8 RC1 and put together a little training ground." (post text, verbatim).
2. Populate it with: a sword-trail test, a breakable dummy, grass, flowers, and rocks from free Sketchfab packs, textures from Poly Haven and ambientCG, and a Quaternius character with Quaternius animations.

**Check**
- Each new feature is visible in one clip: trail, fog dust, break, contact shadows, AO. The clip is the test scene, not a game level.

**Why**
A training ground isolates each feature so its failure is attributable. The author states this is exploration outside his game, which is why no game context is claimed here.

## Phase 2: Set up the sword trail with Trail3D

**Do**
1. Use the new Trail3D node for the sword trail.
2. Set `mesh_alignment` to Local instead of the default Billboard, "so the ribbon stays in the swing plane" (OkGarage1715, comment, verbatim reason).
3. Parent the trail to a pivot in the middle of the blade, rotated so the width runs along the blade. The numeric width is unknown (see Tools used).

**Check**
- The ribbon stays in the swing plane during the swing instead of billboarding toward the camera. The author reports Trail3D was "mostly fine out of the box, just a few tweaks" (comment, verbatim).

**Why**
A trail that billboards reads as a camera-facing card; a trail aligned to the swing plane reads as the blade's path. The alignment setting, not a shader, is the fix.

## Phase 3: Make the break dust from real volumetric fog

**Do**
1. On every bounce of the breaking dummy, emit a dust burst.
2. Build the dust as real volumetric fog: FogVolume plus a custom fog shader, "so it gets lit by the sun and catches the tree shadows" (post text, verbatim).
3. Write the fog shader short: "a fog shader is pretty short, you basically just set DENSITY and ALBEDO" (OkGarage1715, comment, verbatim). No shader source is given.
4. Use approximately 16 animated puffs for the dust (comment, "~16 animated puffs").
5. Raise the volumetric fog resolution in the project settings: `volume_size` 160, `volume_depth` 128, because "the default was too blurry for a small burst" (comment, verbatim). Lower temporal reprojection to 0.6 "so a short burst doesn't smear" (comment, verbatim).
6. Set the scene fog to scatter forward with anisotropy 0.6, with the sun behind the camera.

**Check**
- The dust is lit by the sun and catches tree shadows in the clip; a commenter singled out exactly that. The burst reads at small scale instead of blurring out.

**Why**
Real fog volumes inherit the scene's lighting and shadows; a sprite burst would have to fake both. Resolution and reprojection are the two settings that decide whether a short, small burst survives or smears.

## Phase 4: Fix the dark dust locally with emission

**Do**
1. Diagnose: with forward scattering (anisotropy 0.6) and the sun behind the camera, "the dust came out dark brown at first" (comment, verbatim).
2. Do not touch the global fog. Instead, "I added a warm EMISSION on the sun-facing side of each puff" (comment, verbatim), and: "I made the side facing the sun brighter and added a bit of emission" (comment, verbatim). The author also notes "godot's fog doesn't shadow itself, so the dust looked flat and kinda dark at first" (comment, verbatim).

**Check**
- The sun-facing side reads warm and bright; the burst no longer reads dark brown. The global fog is unchanged, so the rest of the scene is unaffected.

**Why**
Faking the missing self-shadowing with local emission on the lit side fixes only the broken effect. Changing the global fog to rescue one burst would re-light the whole scene. Inference, labeled: the "fix locally, not globally" reading is the auditor's summary of the author's stated choice.

## Phase 5: Break the dummy with RigidBody3D, add contact shadows and AO

**Do**
1. "The break is just RigidBody3D physics, with a dust burst on every bounce" (post text, verbatim).
2. Turn on screen-space contact shadows (new in 4.8) and multi-bounce AO.

**Check**
- The dummy breaks and bounces under physics; contact shadows ground the pieces. No settings for either feature are stated.

**Why**
Physics plus a burst per bounce is the whole break effect: no scripted break animation is claimed. The new 4.8 features are exercised as on/off capabilities here, not tuned.

## Failure modes

- Leaving Trail3D on the default Billboard alignment, so the ribbon billboards toward the camera instead of staying in the swing plane.
- Accepting the default volumetric fog resolution, so a small burst blurs out.
- Fixing dark dust by changing the global fog, re-lighting the whole scene to rescue one effect.
- Treating RC1 nodes as shipped; re-verify at 4.8 release.

## The human method, distilled

1. "Honestly the shader code was the easy part... what took time was getting it to look right" (OkGarage1715, comment, verbatim). Budget the look, not the code.
2. When the global setup fights one effect, fix the effect locally (emission on the puff) and leave the global setup alone.
3. Report the exact settings that made the difference (volume size/depth, reprojection, anisotropy), not only the feature names.

**Depth status:** PARTIAL. Fog settings, the Trail3D alignment fix, the emission workaround, and the asset sources are stated by the author in post and comments. The Trail3D width value is lost to comment truncation, no shader source is given, and no settings are stated for contact shadows or multi-bounce AO. What would reach FULL: the untruncated Trail3D comment and the fog shader source.
