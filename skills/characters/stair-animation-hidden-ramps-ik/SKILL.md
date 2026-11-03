---
name: stair-animation-hidden-ramps-ik
description: "Ship believable stair climbing without dedicated stair animations: hide a ramp under the stairs as the character collider, place it to match the game's look, understand why capsule-vs-step causes jitter, and plant feet with an IK system. Trigger when characters need to climb stairs."
---

# Stair Climbing Without Stair Animations: Hidden Ramps and IK Feet

## Purpose

This skill explains the industry-standard stair trick (a hidden ramp
as the collider) and why it works, plus what proper stair animation
would actually require. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: ramp for the body, IK for the feet,
and honest accounting of what the shortcut costs.

## Source

Instagram, kennedy_artist ("The Graphics dude") (transcribed from
reel audio with faster-whisper tiny, 2026-11-02; captions unavailable
via API):

- https://www.instagram.com/reel/DeMm2ZGsrbk/ — "Does this game have bad stair animations?"

Evidence note: reel-length analysis (about 3 minutes) comparing two
shipped games' stair handling; machine transcription, minor word
errors possible. Game names as spoken.

## Tools used

Tools used: game engine character controller (capsule collider);
animation system with IK (inverse kinematics) foot planting.

## Phase 1: Hide a ramp under the stairs

**Do**
1. Do not use the stairs as the collider. Instead, play the walk
   animation and put a hidden ramp under the stairs as the
   character's collider.
2. Place the ramp deliberately: in the comparison, one game's ramp
   runs along the edges of the stairs so the character appears to
   walk above the stairs; the other game's ramp is recessed, so the
   character appears to walk through the stairs.

**Check**
- Does the character read as walking ON the stairs, not through
   them?
- Is the ramp invisible to the player?

**Why**
The ramp is the whole trick: the capsule slides up a ramp smoothly,
while stepping on actual stair colliders produces jitter. Ramp
placement is the difference between a convincing climb and a
character clipping through geometry.

## Phase 2: Understand the jitter you are avoiding

**Do**
1. Know why stairs-as-colliders fail: the player character is
   usually a capsule; moving forward pushes the capsule, and when it
   hits a step it is raised upward, which reads as jitter as the
   character progresses step by step, unlike the smooth slide up a
   ramp.
2. Know what the real fix would cost: dedicated stair-climbing
   animations, plus animators, environment artists, and engineers
   agreeing on a standard stair height for every stair in the game
   (the same pre-agreement already used for vault barriers).

**Check**
- If you see jitter on stairs, is the collider the stairs
   themselves?
- Before committing to real stair animations, is the stair-height
   standard agreed across disciplines?

**Why**
The ramp is a shortcut with a known price: it looks right but the
feet never truly climb. The honest alternative (dedicated animations
plus a cross-discipline stair standard) is expensive, which is why
the ramp persists. Choose knowingly.

## Phase 3: Plant the feet with IK

**Do**
1. Add an IK system that reads the ground orientation and aligns the
   foot to it, so feet appear planted on slanted ground.
2. Verify the knees accommodate: in the demo, the character's knees
   bend to accommodate the foot that is higher on the slope.

**Check**
- On slopes and stair edges, do the feet sit on the ground or float?
- Do the knees bend plausibly for the height difference?

**Why**
The ramp handles the body; IK handles the feet. Without IK, the
character slides up correctly but the feet hover or clip, which is
exactly the kind of small wrongness players notice. IK is what sells
the contact.

## The human method, distilled

1. Hidden ramp under the stairs, placed to match the visual.
2. Stairs as colliders cause capsule jitter; know why before
   "fixing" it.
3. Real stair animations need a cross-discipline stair-height
   standard first.
4. IK plants the feet; knees must accommodate the slope.

## Depth status

PARTIAL (transcribed reel audio, about 3 minutes; comparative
analysis of shipped games, not a build procedure).
