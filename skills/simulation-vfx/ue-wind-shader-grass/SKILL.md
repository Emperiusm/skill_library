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
