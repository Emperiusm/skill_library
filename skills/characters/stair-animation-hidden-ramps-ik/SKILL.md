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

## AAA studio practice

- **Ubisoft Montreal, GDC 2013 Animation Bootcamp (Jonathan Cooper,
  AC3).** A detailed procedural lean and foot-placement system for
  turning while running, created procedurally and then fine-tuned
  by comparing against real motion-capture data. Assassin's Creed
  games use IK for detailed hand and foot placement in climbing,
  plus a procedural layer for overall body movement on jumps and
  landings. Secondary motion is spring-based too: cloth simulation
  on the cape, spring physics on the equipment bits attached to the
  character. Source: Wolfire Games GDC13 Animation Bootcamp
  summary:
  https://www.wolfire.com/blog/2013/04/GDC13-Summary-Animation-Bootcamp-Part-4-6/
- **Ubisoft Montreal, GDC 2016, Simon Clavet, "Motion Matching and
  The Road to Next-Gen Animation" (For Honor).** Toe-locking at
  run-time to a ground socket matching the toe's position in the
  animation fixes foot-slide; foot IK is also implemented for
  slopes, pulling the hips down to connect to the lowest foot on
  slopes and stairs, with the hard rule that dropping the hips
  must never break the pose or hyper-extend the knees (animator
  silhouettes are preserved). Instead of timescaling animations
  more than 10% faster or 20% slower to adjust speed, designers
  slide the characters and let foot IK relieve the foot-sliding.
  Source: Game Anim writeup:
  https://www.gameanim.com/2016/05/03/motion-matching-ubisofts-honor/
- **Epic Games, Valley of the Ancient sample documentation.**
  "Flexible real-time animation using full-body Inverse Kinematics
  (IK) and motion warping to fit character motion with gameplay."
  The UE5 Motion Warping system adapts an animation's root motion
  to warp points in the environment, condensing the workload of
  environmental interactions like vaults. Source: Epic Developer
  Community documentation (mirrored):
  https://github.com/gcampton/claude-skill-unreal-engine-full/blob/HEAD/references/epic-official/valley-of-the-ancient-sample-game-for-unreal-engine_1805937c.md

**Agent-executable upgrades**

1. **Traversal manifest (`traversal.json`).** Every staircase and
   slope test case: step height and width (must match the
   cross-discipline stair standard), ramp placement (edge-running
   vs recessed), and collider type. An automated loop walks each
   case and records gates.
2. **Gates per case.** Capsule jitter check (vertical oscillation
   of the capsule root while climbing stays under threshold; if
   not, the collider is the stairs themselves). Foot contact check
   (feet sit on the ground, no floating or clipping). Knee check
   (bend accommodates the height difference without
   hyper-extension). Silhouette check (hip drops for slopes and
   stairs never break the authored pose, per Clavet's rule).
3. **Cross-discipline standard check.** Reject any new staircase
   whose step height deviates from the agreed standard before the
   real-stair-animation path is even considered.

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
