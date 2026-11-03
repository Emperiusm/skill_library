---
name: smoke-flipbook-particles
description: "Fake volumetric smoke in games with flipbook textures: simulate offline in Houdini, Maya, or Blender, render the first 64 frames into an 8x8 flipbook, and play it on camera-facing particle cards with a simple upward force. Trigger when adding smoke, fire, or explosions to a game."
---

# Game Smoke With Flipbooks: Offline Sim, Cheap Playback

## Purpose

This skill produces convincing game smoke without real-time fluid
simulation: bake a good sim once, then play it back on cheap
particles. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle).
The core method is: simulate offline, flipbook the frames, emit
cards.

## Source

Instagram, kennedy_artist ("The Graphics dude") (transcribed from
reel audio with faster-whisper tiny, 2026-11-02; captions unavailable
via API; a non-English intro segment untranscribed):

- https://www.instagram.com/reel/DaSfyiMsZo4/ — "How smoke works #unrealengine #animation #gamedev"

Evidence note: reel-length narration (about 3 minutes); machine
transcription, minor word errors possible. Simulation parameters
(voxel size, frame counts) are as spoken.

## Tools used

Tools used: offline fluid simulation (Maya, Houdini, or Blender);
game engine particle system with flipbook texture support. Load-
bearing caveat from the narration: Unreal Engine can render
high-quality volumetric smoke, "but they are quite expensive, so
they are not usable for video games; for animations, fair game."

## Phase 1: Simulate offline and mind the voxels

**Do**
1. Build the smoke simulation the traditional way in specialized
   software (Maya, Houdini, Blender), tuning fire/smoke transition
   and velocity.
2. Budget the detail honestly: "for me to get good detail, I have to
   reduce the size of each voxel, which would require more RAM. As
   the simulation runs, all this per-voxel data is cached in files
   for every frame. And these can get massive, several gigabytes for
   a simple smoke simulation."
3. Ensure the first 64 frames contain a good simulation; those are
   the frames you will bake.

**Check**
- Is the simulation good within its first 64 frames?
- Can your machine actually hold the voxel cache?

**Why**
This workflow is only viable for animations if you simulate at film
quality, but for games you simulate to bake: the sim exists to
produce 64 good frames, not to run in real time. "This would be good
for animations where one can sit and wait for frames to finish
rendering, even if they take several days. But for games where we
have to render at least 30 frames for every second, this is
completely unusable."

## Phase 2: Bake the flipbook

**Do**
1. Position a camera facing the simulation directly.
2. Render the first 64 frames into PNGs.
3. Arrange the PNGs into one massive PNG in an 8x8 grid: "we call
   this PNG a flipbook texture, and the reason for that is because
   it's like a flipbook that stores an animation that you can flip
   through."

**Check**
- 64 frames, 8x8 grid, camera dead-on facing the sim?
- Does the flipbook read as continuous motion when scrubbed?

**Why**
The flipbook is the compression step that makes the whole trick
work: 64 frames of fluid dynamics become one texture. The facing
camera matters because the cards will always face the viewer, so
bake the view you will actually see.

## Phase 3: Emit cheap cards in the engine

**Do**
1. In the game engine, create a simple particle system: "just a few
   particles, very simple, no fluid dynamics, no physics, just a few
   particles and an upward force."
2. Remember the particles are cards: "when you look at the
   particles, they look like spheres, but they are actually very
   small flat cards with round cutouts, and because they always face
   the camera, you can't tell that they're cards."
3. Connect the flipbook texture: "as a particle is born, it's going
   to play that flipbook animation across its lifetime." Increase
   particle count and size from there.

**Check**
- Do the cards stay camera-facing at all play angles?
- Does the flipbook play across each particle's lifetime without
   visible popping?

**Why**
The engine does almost no work: no fluid solver, just textured cards
with an upward force. "It's not necessarily volumetric, but it looks
like a volume, and that's good enough for games." The next time you
see a huge fire in a game, "it's just a bunch of PNGs floating by."

## AAA studio practice

**Winni Li via 80 Level, "VFX Production in Houdini & UE4."** The standard professional pipeline this skill mirrors: simulate in Houdini, then use Houdini's mosaic node to organize the rendered frames into one flipbook texture, typically 6x6 or 8x8. More frames look more consistent, but Unreal's import limit depends on image size, so grid size is a budget decision, not a free choice. The particle material is translucent with a particle color node feeding the texture, exactly the card setup in Phase 3 (https://80.lv/articles/006sdf-vfx-production-in-houdini-ue4).

**Gasper Znoj via 80 Level, "Creating a VFX Explosion in UE4" (VFX artist, EA's Plants vs. Zombies: Battle for Neighborville, Relic's Age of Empires IV).** For fake volumetric lighting on smoke, Znoj takes a dot product between a manually set light vector and the vertex normal direction, then pans a 1x512 gradient texture toward or away from the light; using the camera position (with an offset) as the light direction keeps the explosion looking the same from any angle. He notes the same trick already exists as drawn highlights and shadows on 2D animated flipbooks (https://80.lv/articles/creating-a-vfx-explosion-in-ue4). This upgrades Phases 2 and 3: the flipbook's baked lighting and the engine-side fake light must agree, or the cards will fight the scene lighting.

**GDC 2023 VFX Roundtable notes (realtimevfx.com).** The industry's own roundtable discussed using Stable Diffusion to "fill in frames of a flipbook" and generally clean up work artists already do, alongside Houdini workflows for packing data into UV channels (https://realtimevfx.com/t/gdc-2023-vfx-roundtable-discussion-notes/23367). This points at the automation ceiling for this technique: interpolation between baked frames is the natural agent task, scoped to real popping ranges rather than speculative generation.

**Agent-executable upgrades (from the above).**
1. Flipbook manifest JSON: {frame-count, grid (e.g. 8x8), frame-size px, total texture px, alpha-channel present, engine import limit pass or fail}. The agent runs a batch validation loop after every bake: frame count equals grid squared, no missing tiles, alpha channel exists, total texture within the engine's import budget. This automates Phase 2's Check.
2. Lighting consistency gate: log the baked light direction {x, y, z} and the engine-side fake light vector; the agent flags a mismatch before the effect ships, with Znoj's camera-offset convention recorded as the chosen standard so future effects inherit it.
3. Frame-interpolation queue: any flipbook where scrubbing shows visible popping is logged with the popping frame range as a candidate for AI frame fill (the GDC 2023 roundtable use case). The queue entry is scoped to the range, never a vague "improve this."

## The human method, distilled

1. Simulate offline for bake, not for playback; 64 good frames is
   the target.
2. Voxel size is the detail/RAM trade; cache sizes get massive.
3. Flipbook: facing camera, 64 PNGs, 8x8 grid, one texture.
4. Engine side: few particles, upward force, camera-facing cards,
   flipbook across lifetime.

## Depth status

PARTIAL (transcribed reel audio, about 3 minutes; workflow and
parameters as spoken; no frame-level verification).
