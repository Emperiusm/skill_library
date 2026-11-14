---
name: niagara-explosion-sprite-sheets-godot
description: "Make Godot explosions look like Unreal Niagara: build the explosion in UE Niagara, render it out to sprite sheets with depth and thermal data baked in, and import the sheets into Godot, where they play at zero frame cost. Trigger when a Godot game needs one hero explosion effect that the engine's built-in particles cannot reach."
---

# Niagara Explosions Rendered to Sprite Sheets for Godot

## Purpose

This skill reconstructs the Niagara-to-Godot explosion pipeline from the
author's post and comments, step by step, so another agent can follow the same
process. Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The core method is: use the
best tool for the effect, bake it, ship the bake.

## Source

Creator: Fonix_za (QuestIO Studio). Video: "I updated my explosions in my game
- CSAR: Behind Enemy Lines", https://www.youtube.com/watch?v=DtascqyUKqc (no
captions; the media download was blocked by a YouTube sign-in wall, so no
frames were reviewed). Reddit post:
https://www.reddit.com/r/godot/comments/1xuo3fk/i_used_unreal_engine_to_make_my_godot_game_look/
(r/godot post 1xuo3fk, score 104, 15 comments). 2026-11-13 scout run, audit 4.

This is a distinct workflow from the smoke-flipbook skill
(`smoke-flipbook-particles`): that one builds flipbooks inside the engine's own
particle tooling; this one renders Unreal Niagara out to sheets for a different
engine. Do not merge them.

## Tools used

**Unreal Engine Niagara**, **Godot**. Game: CSAR: Behind Enemy Lines.

## Phase 1: Build the explosion where explosions look good

**Do**
1. Build the explosion in Unreal Engine with Niagara, which the author says
   "can make convincing looking explosions." The author spent about 3 weeks
   iterating on explosion look in Godot before switching approach.
2. Take inspiration from a reference: the author "got inspiration from that
   new game Defilade thats making the rounds, saw those explosions in that
   game and i was like... I have to do something similar in mine."

**Check**
- The explosion reads as punchy and realistic in the rendered frames; the
  author judges it sells the game ("it will really help sell the game, its
  like a minor thing but also not").

**Why**
Godot's built-in particles were not reaching the look after 3 weeks. Switching
tools for one effect is cheaper than fighting the engine for another month.

## Phase 2: Render to sprite sheets, with depth and thermal data

**Do**
1. Render the Niagara explosions out to sprite sheets.
2. Bake in depth and thermal data as well as color, "to really sell the effect."

**Check**
- The sheets look right when played back as sprites in Godot; the depth and
  thermal channels make the fire read as volumetric rather than flat.

**Why**
A sprite sheet is a frozen render: it costs nothing at runtime. Depth and
thermal data are what keep a flat sheet from looking flat.

## Phase 3: Import into Godot and ship

**Do**
1. Import the sprite sheets into the Godot game.
2. Accept the tradeoff the author states: "The sprite sheets are pretty large
   but at least there is like no fps performance impact for such good looking
   effects (imo)."

**Check**
- Frame rate does not drop when explosions play; the sheets are large on disk
  but free in the frame budget.

**Why**
Disk is cheap and frames are not. Baking an expensive effect into a large,
cheap-to-play asset is the right trade for a 2D game.

## AAA studio practice

Baking a simulation out to a flipbook is the shipped-game path; heavyweight
caches are the cinematic path. CCP Games (EVE Online) generates explosions
in EmberGen and renders them out as animated texture atlases for the live
game: "In the development of these missile impact visuals we generated
explosions of different types and rendered them out as animated texture
atlases, sometimes bringing them into After Effects to make them tileable
(for applying to a sphere...) or to add some distortion." In the Viridian
expansion (June 2023), "somewhere between 60-80% of the textures were
created using Embergen." The deciding factor was authoring speed: "the
faster we can generate and author the resources to create the visual
effects, the better", with real-time authoring and curve-animated parameters
letting "a small team to deliver a good big mix of assets." CCP also shows
the data-size discipline AAA applies to baked sims: raw DDS volumes were
"300-400 megabytes", so they built in-house compression (re-digitizing,
run-length-encoding, zlib) for "around a 10x decrease in file size", and ship
half-resolution textures for low-quality settings. Source: JangaFX,
"Insight: CCP Case Study", https://jangafx.com/insights/ccp-case-study

The grid follows the frame, not a default square. Kirill Anchikov created
flame bursts in EmberGen and baked them into an 8x4 flipbook "since the
elongated flame shape allowed for a 1:2 frame aspect ratio", assembling them
in Niagara (GlueIT for sheet packing), with texture generation first and
blockout in the particle system second, timing tuned "almost like classical
2D animation", and color driven through the material rather than the particle
system. Source: 80 Level, "Creating a Flame Burst Effect With Unreal Engine
5", https://80.lv/articles/creating-a-flame-burst-effect-using-unreal-engine-5

Daryll Espanola (whose portfolio includes VFX for Lords of the Fallen) used
"8 x 8 flipbooks 'for game optimization and polished visuals' to export the
project to Unreal Engine", and advises against Alembic "unless it is a
cinematic" (VAT "works too but you have to deal with some artifacts"). The
rule is direct: flipbooks are the game path, heavyweight caches are the
cinematic path. Source: 80 Level, "Gunshot VFX Made with EmberGen &
LiquiGen", https://80.lv/articles/cool-gunshot-effects-created-with-embergen-liquigen

The industry-standard version of baking extra data into sheets renders
separate passes so lighting is not baked into color. SideFX Labs' Flipbook
Textures ROP renders "Final Color, Non-emissive Color, Depth,
Multi-directional Contribution (MDC)", where "MDC maps... are designed to
achieve full-dynamic realistic volumetric relighting in engine", and supports
"SideFX Labs' new motion vector encoding technique that offers close to
16-bit quality at half the memory." That is the direct precedent for this
skill's depth/thermal data: the production version renders depth plus
multi-directional lighting contribution as separate passes, plus motion
vectors for frame interpolation. Source: SideFX Labs, "Labs Flipbook
Textures", https://sidefxlabs.artstation.com/projects/o2AX8k

Epic's own guidance confirms the premise: "Most performant will be a
flipbook, which can be generated from the baker tab" (Niagara Baker); the
alternative is a simulation cache asset, sampled "at a low rate and then use
interpolation option, that way you don't have to save a lot of cache
frames", triggered at runtime with SetSimCache() on a Niagara component.
Source: Epic Developer Community Forums, Michael Galetzka,
https://forums.unrealengine.com/t/cached-baked-fluid-sim-as-in-game-triggered-fx/1304091

The engine side has to consume those passes. O3DE documents six-point
lighting for lit flipbook smoke/clouds: "approximates how each texture
should be lit from any given direction by using six tangent lightmaps that
represent the top, bottom, left, right, front, and back of a plume of smoke",
with a depth texture option and a depth pass shader. Source: O3DE,
"Custom Lighting Tutorial with Flipbook Animation",
https://version-2305--o3deorg.netlify.app/docs/learning-guide/tutorials/rendering/six-point-lighting-tutorial/

Two flags, stated plainly: no source documents a "thermal" pass by that
name (SideFX documents Depth and MDC; packing a thermal/heat channel like
the non-emissive color pass is this skill's own convention, not an AAA
practice), and no source documents a Godot shader consuming depth/MDC
passes, so any Godot shader code is skill-authored. "Zero frame cost" is
also the skill's own measured claim, not an AAA attribution; the sources
support flipbooks as the cheapest runtime path, not literally zero cost.

### Agent automation

- **Flipbook spec manifest and grid gate.** Before rendering, write a
  manifest (effect name, grid such as 8x8 or shape-matched 8x4, frame count,
  frame aspect ratio, source sim file) and check that the exported sheet's
  grid matches the manifest and every frame cell is non-empty. (Grounded in
  Anchikov's aspect-ratio-matched 8x4 and Espanola's 8x8-for-optimization
  rule; the manifest format is a skill-design choice.)
- **Multi-pass render checklist with per-pass validation.** Require the four
  passes SideFX Labs documents (Final Color, Non-emissive Color, Depth, MDC)
  or explicitly record which are omitted and why, and check that each pass
  file exists and matches the color sheet's grid and frame count. The
  receiving Godot shader must consume those passes; a color-only sheet does
  not use the depth/thermal data.
- **Bake-vs-simulate decision gate and size budget.** If the effect must
  trigger in gameplay, bake to flipbook (Niagara Baker or EmberGen export);
  reserve sim caches, Alembic, and VAT for cinematics only. Record sheet
  resolution and memory in the manifest and keep a half-resolution tier for
  low-quality settings. (Grounded in Espanola's "no Alembic unless
  cinematic", Epic's "most performant will be a flipbook", and CCP's 10x
  compression plus half-res tier.)

## The human method, distilled

1. When the engine fights you for 3 weeks, change the tool, not the goal.
2. Bake the expensive thing once; play the cheap thing forever.
3. Ship the bake and move on; the author may make a high-level tutorial video
   later ("if there is more interest ill try cobble something together"), but
   the pipeline already works.

## Failure modes

- **Flat-looking sheets.** If the explosion reads as a flat card, the depth and
  thermal channels are missing or too weak. They are what sell the volume.
- **Sheet size bloat.** The sheets are large by design. If disk size becomes
  the constraint, reduce the sheet resolution or frame count rather than
  dropping the depth and thermal data.
- **Purpose-built alternatives.** Commenters note EmberGen is "tailored
  specifically for this kind of thing" (huttyblue), and JangaFX Elemental Suite
  is "pretty banger" if there is budget (ArcticDev_). If the project needs many
  explosion variants, a dedicated tool beats a hand-rolled Niagara render.

**Depth status:** PARTIAL (full post text plus 15 comments; the YouTube video
itself could not be deepened: the media download was blocked by a YouTube
sign-in wall and the video has no captions, so no frames were reviewed and no
Niagara settings were recovered).
