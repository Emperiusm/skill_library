---
name: toon-2d-in-3d-dynamic-texture
description: "Render a classic DBZ cel look in 3D with a dynamic texture: fake the light direction with a target point (not an actual light), let it drive the drawn cel shapes on the texture, and verify with extreme-zoom closeup animation. Trigger when building a 2D-anime look in a 3D engine or writing toon-shading rules for an art bible."
---

# Dynamic-Target-Point Toon Texture (2D Anime Look in 3D)

## Purpose

This skill reconstructs the toon-rendering technique that _VirtualEntrance_
demonstrates in "Perfecting 2D in 3D" (r/3Dmodeling post 1x9dca0, score 504,
25 comments), step by step, so another agent can reproduce the same 2D anime
look in a 3D engine. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The technique's
core method is: fake the light direction with a target point and draw the
shapes on a dynamic texture; never rely on real lighting.

## Source

Creator: _VirtualEntrance_ (r/3Dmodeling post 1x9dca0; 25 comments).
Source: https://www.reddit.com/r/3Dmodeling/comments/1x9dca0/
Evidence: native Reddit clip + the author's own answers in the comments.
No tool name, no texture resolution, and no node/shader parameters were
disclosed. Corroborating commenter: Earth513 (Nomad Sculpt on iPad firsthand
use). Author's YouTube short demo referenced by Earth513:
https://youtube.com/shorts/Jn5ymzsYnGc.

**Tools used:** none named by the author; the technique is a dynamic texture
driven by a scene target point. Nomad Sculpt (iPad) corroborated by a
commenter as a working platform for the same style via paintwork.

**Depth status:** PARTIAL (mechanism from the author's own answers; no
parameters disclosed). The technique is reproducible at the recipe level.

## When to use this skill

- Building a 2D anime (cel-shaded, DBZ-style) look in a 3D engine.
- Writing toon-shading rules for an art bible (this is the first codified
  "toon law" entry the video-tooling-scout has surfaced for 2d3d's P1 gap).
- Deciding between renderer-driven lighting and texture-driven cel shading.

## Phase 1: Define the target look and the acceptance test

**Do**
1. Aim for the classic DBZ cel-animated style.
2. Set the acceptance test up front: the look must survive extreme zoom
   during closeup animations with no pixelation.

**Check**
- Quoted (author): "the zooming is just to show that there is no
  pixelation no matter how much you zoom in for closeup animations."
- Quoted (author, score 34): "And the classic dbz style is exactly what i'm
  trying to achive" and "it's a texture but dynamic".

**Why**
Pixelation breaks the 2D illusion instantly; if the look survives closeup
zoom, the technique works everywhere else. The dynamic texture is what makes
zoom-safety possible (static texture resolution would be the limit).

## Phase 2: Drive the cel shading with a target point, not a light

**Do**
1. Place a target point (not an actual light) in the scene.
2. Have the target point simulate the light direction.
3. Let the simulated direction affect the drawn shapes on the texture.
4. Keep every lit/drawn decision intentional: the author says "most things
   shown are intentional... it's dynamic at the same time."

**Check**
- Quoted (author, score 4): "there's a target point (not actual light) that
  simulates light direction which affects the drawn shapes."
- Verification method implied by the technique: move the target point and
  watch the drawn cel shapes move across the model. Static shapes mean the
  texture is not truly dynamic and the technique is broken.

**Why**
Separating the light-direction control from the real render lights keeps the
cel shading art-directable like a drawing. Real lights would add physically
correct gradients that fight the cel look; the target point is the
art-directable handle. (Inference, labeled: the author never states this
reasoning, but it follows from "not actual light".)
Question the genre convention first: a commenter asked "Inverted hull?
Grease pencil? Some other approach?" (thegenregeek); the author's answer
is neither, which rules out the two standard anime-shader recipes and makes
this a distinct third approach.

## Phase 3: Reproduce via paintwork in a sculpting app (alternative route)

**Do**
1. In Nomad Sculpt on iPad, build the style through careful paintwork; the
   style "is very forgiving of imperfections on the sculpt."
2. Do not start with the sculpt; start with the paint discipline.

**Check**
- Quoted (Earth513): "it's phenomenal in Nomad Sculpt as all it really
  involves is careful paintwork and it's very forgiving of imperfections on
  the sculpt." and "I haven't played with lighting in Nomad Sculpt to add
  to the effect as you have" (confirming the lighting component is still
  open in that app).

**Why**
The cel look is primarily a painting discipline, not a modeling one: paint
forgives modeling imperfections, so mesh perfection is the wrong place to
spend effort. This is an independent corroboration route (different app,
different author) that the style is paint-led.

## The human method, distilled

1. **Fake the light, draw the truth.** A target point simulates light
   direction; the texture carries the cel shapes. Never fight the renderer
   for a drawn look.
2. **Zoom is the acceptance test.** If the look survives extreme closeup
   animation without pixelation, the technique works.
3. **Paint forgives modeling.** The style is forgiving of sculpt
   imperfections; paint discipline matters more than mesh perfection.
4. **Rule out the standard recipes first.** The answer was neither inverted
   hull nor grease pencil; check the conventional approaches before
   building a custom one.

## Failure modes

- **Real lights fighting the cel look.** Physically correct gradients on
  top of drawn cel shapes produce a muddy hybrid; keep real lights away
  from the shaded surface or disable them entirely.
- **Static texture mistaken for dynamic.** If moving the target point does
  not move the cel shapes, the texture pipeline is not wired; re-check the
  target-point-to-texture drive.
- **Pixelation at zoom.** If closeup animation pixelates, the dynamic
  texture resolution (or its sampling) is the bottleneck, not the
  geometry.

## Watchlist / pipeline notes

- 2d3d: this technique is filed as the recommended first written entry for
  the P1 "Written art bible... toon law" gap (rec 2). No toon stage exists
  in any repo pipeline today (NEED).
- Nomad Sculpt evidence strengthens the 2026-10-12 "Nomad Sculpt live link
  to Blender" watchlist row (WATCH): a second, independent firsthand-use
  report of the app for this exact style.
- Watchlist row added 2026-10-20: "Dynamic-target-point toon texture (2D
  anime look in 3D)".
