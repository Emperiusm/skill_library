---
name: character-animation-pipeline-rig-mocap
description: "Take a character from model to game-ready animation: build the joint-and-control rig with painted skin weights, break motion into interruptible layered clips, capture performance with a mocap suit or video, then clean up and exaggerate for fantasy. Trigger when producing character animation for games."
---

# Character Animation Pipeline: Rig, Clips, Capture, Exaggerate

## Purpose

This skill takes a character from finished model to game-ready
animation: rigging, clip architecture, motion capture, and the manual
pass that makes it sing. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: rig for control, clips for
responsiveness, capture for truth, exaggeration for character.

## Source

Instagram, kennedy_artist ("The Graphics dude") (transcribed from
reel audio with faster-whisper tiny, 2026-11-02; captions unavailable
via API; a Swahili segment mid-video untranscribed):

- https://www.instagram.com/reel/Dcv0LEPsyRq/ — "How we create animations for characters"
- https://www.instagram.com/reel/Dc3k_uYMwOa/ — "Why breakdown animations to short clips?"

Evidence note: two reel-length narrations (about 3 minutes each, a
two-part series); machine transcription, minor word errors possible.

## Tools used

Tools used: DCC rigging tools (joint chains, control rigs, weight
painting); animation state machine with clip interruption and
layering; motion-capture options: sensor suit (sensors on the body,
hub, data to PC over Wi-Fi), Hollywood computer-vision systems with
depth cameras, Unreal Engine video-based motion capture (any device).

## Phase 1: Rig the character for animators

**Do**
1. Build the animation rig: "a digital skeleton made up of joints
   and controls that allow an animator to move different body parts
   of a character."
2. Assign each joint its area of influence by painting weights
   ("painting these gradients"), since joints are rigid and the mesh
   is not.

**Check**
- Can the animator reach every needed body part through controls?
- Do the weight gradients deform smoothly, with no candy-wrapper
   collapsing at the joints?

**Why**
The rig is the contract between model and animator: joints move,
controls are the handles, weights decide what follows. Bad weights
surface as bad animation no matter how good the performance is.

## Phase 2: Break motion into clips for responsiveness and layering

**Do**
1. Break every action into its own animation clip instead of one
   long animation. A game ends up with thousands of animations
   because "every little movement is a separate animation."
2. Design for responsiveness: "we need to be able to cut that
   animation at that point and start playing the block animation,
   that way the game feels more responsive." Clips must be
   interruptible and swappable in real time based on player or NPC
   state.
3. Design for layering: "modular animations can be layered on top of
   each other based on different game states." Example: when a
   weapon is equipped, layer an idle animation over all locomotion,
   restricted to the weapon arm so it swings less, "creat[ing] this
   illusion of weight on that arm."

**Check**
- Can any clip be interrupted at any point by a higher-priority
   state?
- Do layered clips mask to the right body parts?

**Why**
Clip granularity is not complexity for its own sake; it is the
mechanism behind responsive controls and rich state blending. One
long animation can never be interrupted cleanly or layered
partially. The complexity is the price of a game that feels alive.

## Phase 3: Capture performance, starting with reference

**Do**
1. For hand animation, film yourself performing the action and use
   the video as reference: "animators usually film themselves
   performing the action." Remember that whole-body motion is
   involved even in "simple" moves (a wave moves the entire body).
2. For capture, pick the tier: a sensor suit (sensors across the
   body, hub, Wi-Fi to PC) for accessible capture; Hollywood
   computer-vision with depth cameras for maximum accuracy (at the
   cost of expensive cameras and studio space); Unreal's
   video-based capture from any device as the fast-moving middle
   ground.

**Check**
- Reference filmed before animating, not after?
- Does the capture tier match the project's fidelity needs and
   space budget?

**Why**
Reference is the cheapest quality multiplier in animation: the human
eye knows how bodies move, and filming removes guesswork. Capture
tier is a budget decision, but every tier still needs the next
phase.

## Phase 4: Clean up and exaggerate for the fantasy

**Do**
1. Take the capture data and "do a lot of manual cleanup."
2. Exaggerate the movements to fit the fantasy: "no one moves quite
   like the fantastic co-characters that we create; an actor or a
   stunt person cannot jump as high as Kratos." In some cases use
   the mocap only as a reference point and animate everything from
   scratch "making the characters more expressive."

**Check**
- Does the final motion read as the character, not as the actor in
   a suit?
- Is the exaggeration deliberate and consistent across the set?

**Why**
Raw mocap is realistic; game characters are not real. The manual
pass is where realistic motion becomes character motion. Skipping it
leaves performances that are accurate and lifeless; overdoing it
leaves cartoons. The animator's judgment is the step no pipeline
automates away.

## The human method, distilled

1. Rig: joints, controls, painted weights; no shortcuts at the
   joints.
2. Clips: interruptible for responsiveness, maskable for layering.
3. Reference first (film it), capture at the tier the budget
   allows.
4. Clean up, then exaggerate: mocap is the truth, character is the
   goal.

## Depth status

PARTIAL (transcribed reel audio, two reels about 3 minutes each;
pipeline stages and the clip rationale as spoken; no frame-level
verification).
