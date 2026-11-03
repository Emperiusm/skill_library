---
name: ue-wind-shader-grass
description: "Animate grass with wind in a material shader: rotate cards with RotateAboutAxis driven by a time-fed sine wave, offset each card's phase randomly, mask rotation to the grass tips with a height gradient, and drive direction with a painted world-space flow map. Trigger when adding wind to foliage in Unreal."
---

# Wind Shader for Grass: RotateAboutAxis, Sine, Flow Map

## Purpose

This skill animates grass with wind entirely in the material shader:
no skeletal animation, no CPU per-blade work, just math on the cards.
Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The core method is:
there is no wind, only the animated effects of wind.

## Source

Instagram, kennedy_artist ("The Graphics dude") (transcribed from
reel audio with faster-whisper tiny, 2026-11-02; captions unavailable
via API):

- https://www.instagram.com/reel/DVqJk6eDGgq/ — "We have Wind"

Evidence note: reel-length narration (about 3 minutes) over the
material graph; node names, value ranges, and the math chain are as
spoken, unusually specific for a reel. Machine transcription, minor
word errors possible. This video is the follow-up to the grass-cards
video (ue-grass-cards-lod skill): "On the next video we will be
applying some wind algorithm onto this grass."

## Tools used

Tools used: Unreal Engine material editor (RotateAboutAxis node,
sine, Time node, parameters); a black-and-white flow texture painted
along the landscape.

## Phase 1: Rotate cards about a declared axis

**Do**
1. Start from the principle: "the way wind works in video games is
   that there is actually no wind. What we do is animate the effects
   of wind on the different elements of our environment, trees,
   grass, and stuff like that, and then we play the appropriate
   sound, and it's usually very convincing."
2. Use the RotateAboutAxis node: "as the name suggests, it rotates
   things around an axis that we declare." The axis is a vector
   (direction with magnitude); 1,0,0 selects the X axis.
3. Feed the rotation angle a 0-to-1 value where 1 equals 360
   degrees. Verify with a debug value first: changing it from 0
   should visibly rotate the card along the axis.

**Check**
- Does the debug value rotate the card around the intended axis?
- Is the angle normalized 0 to 1?

**Why**
RotateAboutAxis is the entire wind mechanism: everything else is
just deciding what value to feed the angle. Verifying the rotation
with a debug value first separates "the rotation works" from "the
wind looks right."

## Phase 2: Drive the angle with an offset sine wave

**Do**
1. Build the oscillation: take the Time node ("this node just tracks
   time"), multiply it by a controllable parameter, and feed it into
   a sine. The result goes up and down; remap it into the 0-to-1
   range the angle expects.
2. Desynchronize the cards: "this part gives us a random value for
   each card. So remember our grass is made up of several cards. To
   avoid the scenario where they are all animating at the same time,
   we need to offset time, and that's what we are adding to the time
   to offset each card's time."
3. Multiply by an intensity parameter "so that we can control how
   strong that movement is." Set the pivot point and choose world
   vs local space for the rotation.

**Check**
- Are the cards out of phase with each other, or marching in
   lockstep?
- Does the intensity parameter give art-directable control?

**Why**
A single global sine is a metronome, not wind. The per-card random
offset is what breaks synchronization and sells natural motion; the
intensity parameter is what lets a designer tune it without touching
the math.

## Phase 3: Mask to the tips and add direction

**Do**
1. Fix the planted look: "this part of the math calculates a
   gradient along the height of the grass. We multiply that gradient
   with our rotation, so that just switches off the rotations at the
   base of the grass and it keeps the tips rotating. That way the
   grass appears planted."
2. Add direction with a flow map: "take a black-and-white texture
   and just draw that texture along our landscape. So remember,
   black is 0 and white is 1. So if we multiply that texture with
   our wind rotation, as the texture drags along the world, it's
   going to switch on and off the rotations as it moves."
3. Multiply in the attenuation and verify: "even without the sound
   it looks very convincing, and you can get the sense that there is
   wind blowing in the landscape."

**Check**
- Base of the grass: planted (no rotation)? Tips: moving?
- Does the wind have a visible direction of travel across the
   landscape?
- Does it read as wind with the sound off?

**Why**
The height gradient is what separates grass from a waving flag: real
grass is rooted. The flow map is what separates wind from vibration:
real wind travels. The sound-off test is the honest one, because
sound covers a multitude of shader sins.

## AAA studio practice

**Sucker Punch, GDC 2021: wind in Ghost of Tsushima (Bill Rockenbeck).** The studio's wind prioritizes volume over accuracy: "we're not doing any real modeling of fluid dynamics." The main wind vector keeps a constant direction while time-varying Perlin noise modulates the magnitude, which is what makes gusts visibly travel across large grass fields. Local swirl comes from "vorticles," invisible wind-generating particles that grass and other particles sample, plus local disturbance inputs such as character footfall. For the Guiding Wind feature they use a single vector from the hero toward the goal (https://www.gamedeveloper.com/design/using-vorticles-to-simulate-wind-in-i-ghost-of-tsushima-i-). This is the AAA version of the skill's "there is no wind": one authored global vector plus traveling noise plus local disturbances, with particles and sound selling the rest. It also shows the skill's flow map as the entry-level version of a real shipped idea: painted direction with traveling intensity.

**Sucker Punch, GDC talk "Procedural Grass in Ghost of Tsushima" (Eric Woley).** The studio generates per-blade grass data with a compute shader, models blade shape with cubic Bezier curves, drives a global wind system that is sampled on both CPU and GPU, applies the wind as rotation on the vertices, and layers an LOD system blending high to low detail for the performance win (talk listing: https://www.classcentral.com/course/youtube-procedural-grass-in-ghost-of-tsushima-165645). The RotateAboutAxis material approach in this skill is the same principle at grass-card scale; the compute-shader route is the documented escalation path when card counts grow beyond what instanced cards can carry.

**Epic Games, Pivot Painter 2.0 (official tool overview via 80 Level; SideFX Houdini HDA docs).** Epic's Pivot Painter stores each sub-object's pivot and rotation information in the model's data (UV channels or textures), which the shader references so every blade of grass rotates and bends around its own root, with branch-leaf hierarchies inheriting parent motion. Pivot Painter 2.0 raised the object limit from 3,000 to 30,000 sub-models specifically to represent complex foliage (https://80.lv/articles/working-with-pivot-painter-2-0-in-unreal ; https://www.sidefx.com/tutorials/game-tools-pivot-painter/). This is the industrial answer to Phase 2's desync problem: bake per-blade pivots once, compute motion per vertex in the shader, and get unique animation per blade without a single extra draw call.

**Agent-executable upgrades (from the above).**
1. Wind parameter manifest JSON: {global-vector, gust-noise scale and frequency, per-card phase source (random hash vs baked pivots), intensity min/max, tip-mask gradient, flow-map path}. Every exposed material parameter gets a default, a range, and an art-directable label, so a designer or agent tunes without touching the math, matching Phase 2's Why.
2. Traveling-gust gate: sample the wind field at 3 world positions 10 m apart over 5 seconds and require the gust peak to arrive at each in order (the Sucker Punch traveling-gust behavior). A single global sine fails this; Perlin noise or a scrolling flow map passes. An agent can run this check in-engine or in a test harness before approving the wind setup.
3. Sound-off visual regression: render the fixed-camera test scene with and without wind applied, then diff against a golden reference screenshot. The skill's "must read as wind with the sound off" becomes a pixel-diff gate with a documented threshold, re-run whenever the material graph changes.

## The human method, distilled

1. There is no wind; animate its effects and add sound.
2. RotateAboutAxis on a declared axis, angle 0 to 1.
3. Time times parameter into sine; random per-card phase offset;
   intensity parameter for control.
4. Height gradient keeps the base planted; flow map gives direction.
5. It must read as wind with the sound off.

## Depth status

PARTIAL (transcribed reel audio, about 3 minutes; node names, value
ranges, and the math chain as spoken with unusual specificity; no
frame-level verification of the graph).
