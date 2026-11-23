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

## Expansion (2026-11-22): weapon overlays over shared locomotion

Source: Instagram, callme_dixon (Dixon), Heroika, Unreal Engine,
reel https://www.instagram.com/reel/DfnIl3MTsx7/ ("How I saved
making hundreds of animations in my game", 76.5 s, Nov 11 2026;
downloaded media, local faster-whisper tiny transcription, 12 frames
read firsthand; all 19 comments fetched). What follows separates
what the reel demonstrates from what the Godot transfer derives.
Nothing in this section was shown being built in an editor: the reel
shows runtime panels and results, not construction, and it ends
mid-sentence ("So here's how...") with no follow-through.

### What an overlay is, as demonstrated

An overlay is one static pose per weapon, applied on top of a shared
set of locomotion animations, instead of one full animation set per
weapon. Dixon's arithmetic: 18 weapons x 10 locomotion animations =
180 animations on his to-do list. With overlays, the 10 unarmed
locomotion animations are shared by every weapon (idle ready, idle
break/fidget, jog forward/back/left/right, jump start, jump fall,
jump recovery, slide), and each new weapon needs only one unique
static pose. Result claimed: 180 animations down to 18 poses.

Two pieces, taken by Dixon from the Advanced Locomotion System
(ALS) while rejecting the rest of ALS as overcomplicated for his
project:

1. **Overlay.** Selects which bones the static pose overwrites.
   The pose is stored per weapon in a data asset
   (`DA_Overlay_<Weapon>`), with per-bone-group weights from 0.00
   to 1.00 for Spine, Head, Arm Left, Arm Right, Pelvis, and Legs,
   under Override and Additive sections. The crossbow panel shows
   Additive expanded with all four upper-body groups at 0.00 and
   Off Hand Lock at 1.00; the katana panel shows Override expanded
   with all six groups at 1.00.
2. **Additive layer.** Controls how much of the original animation
   still plays through underneath the pose. Additive at 0.00 means
   the base animation is fully visible under the pose's bone
   selection; Override at 1.00 means the pose replaces the base on
   those bones.

Two further rules, as shown:

- **Idle exception.** While the character is not moving, the pose
  may override the full body, giving each weapon a unique idle
  pose (the katana panel's all-groups-at-1.00 Override).
- **Off Hand Lock.** For two-handed weapons, the creator picks the
  lead hand and the other hand follows (shown at 1.00 in both
  panels). The transcript word for this was flagged as a probable
  tiny-model mishearing; the frames confirm "Off Hand Lock" and
  the two-handed reading.

Trade-off, admitted on camera: every weapon ends up with the same
style of movement, since the locomotion underneath is shared. Time
saving claimed: 30 minutes to 1 hour to polish each animation, so
"more than 100 hours saved in total." That is the creator's
estimate, not a measurement (162 avoided animations x 0.5 to 1 hour
= 81 to 162 hours, so the claim sits inside his own estimate
range). The reel does not cover attack or combat animations (only
locomotion and idle), foot IK, weapon attachment, blending times,
or transitions. How the static poses were made is not shown, and
the polish tool name in the transcript is unconfirmed (a probable
mishearing, not visible in any frame); do not cite a tool for it.

This section extends Phase 2's layering idea with a concrete
accounting: Phase 2 says layer an idle over locomotion restricted
to the weapon arm; the overlay pattern generalizes that to a
per-weapon pose asset with per-bone Override/Additive weights over
a shared locomotion set. It does not replace Phase 3: the reel
shows no capture, no Blender, and no retargeting. Where a pose
needs to come from a performance, the sibling skill
`characters/self-recorded-mocap-blender-retarget` covers capture
and retarget; the pose itself can be a single held frame of a
captured clip.

### The correction: ALS is not required

The reel frames the pattern as "a well-known trick from ALS," but
the comment thread corrects that framing, and the correction is
verified verbatim in the raw comment JSON (19 of 19 comments
fetched). Do not present ALS as a requirement, and do not
attribute the ALS warning to Dixon: it comes from an unnamed viewer
(author_id 17841421480782610; Dixon's verified author_id in the
same account's threads is 17841472214163695).

- Echo Alan Wise (viewer): "the overlay is just an enum. Additive
  animations are part of unreal and can be set up on your own. You
  don't need ALS"
- Topher Birth (viewer): "You don't need ALS for this."
- Unnamed viewer: "ALS is a very complicated Blueprint. It might
  look fun and convenient to use right now, but it will become a
  nightmare when you start adding more features and integrating
  other systems. You will end up dealing with tons of errors. Why
  waste time figuring out someone else's complicated Blueprint and
  fixing issues when you can easily create your own custom BP or
  Character Blueprint and modify it however you want?"
- Same unnamed viewer, in short form: "why using ALS for this you
  can use a simple locomotion add poses for weapons"

The takeaway: build the overlay/additive mechanism in your own
character setup. Adopting the full ALS Blueprint for this one
pattern is the maintenance burden the thread warns against.

A further viewer suggestion addresses the sameness trade-off
directly. Alex Bloor (viewer; no creator reply in the fetched
comments, so this is a suggestion, not an endorsed technique):
"Can you add a third layer animation where the bones are moving up
down or side to side? Then do the same thing but only have small
adjustments for each animation to remove that sameness feel to the
animation? So an axe for example would have an up down animation
layer on the hand to pull down the whole arm with the movement to
give it more weight than the bow." Treat it as a lead: a third,
small per-weapon motion layer for weight variation, to be tested
rather than assumed.

### Godot transfer (derived, not demonstrated)

The reel is Unreal-only. The following is this skill's derivation
of the same pattern in Godot 4 `AnimationTree` blend trees,
grounded in the blend-tree node and filter behavior described in
Godot community writeups; it has not been run hands-on, and the
node names below are the derived mapping, not the creator's setup.

**Do**
1. Keep one shared locomotion graph as the base: a blend space or
   state machine over the 10 locomotion clips (idle, fidget, jog
   directions, jump phases, slide), driven by speed and direction.
2. Author one static pose per weapon as a single-keyframe
   animation (or one held frame taken from a captured clip), and
   one per-weapon data resource holding: the pose reference, the
   per-bone-group Override/Additive weights (spine, head, arms,
   pelvis, legs, 0.0 to 1.0), the idle full-body override flag,
   and the off-hand-lock setting for two-handed weapons.
3. Layer the pose over the base with a blend node carrying a bone
   filter (mask): the filter admits only the bone groups the
   overlay owns, so the legs keep the locomotion while the arms
   and spine take the weapon pose. Use an additive blend node for
   the Additive case (the pose authored as a delta from the base
   pose) and an override blend for the full-replacement case.
   Drive the blend amount from the per-weapon weights.
4. Idle rule: when speed is effectively zero and the weapon's
   idle-override flag is set, raise the blend to full and remove
   the bone filter so the pose overrides the whole body, giving
   the unique idle pose.
5. Off-hand rule: for two-handed weapons, lock the off hand to
   follow the lead hand's grip point (a two-bone IK or a
   hand-to-weapon attachment constraint), driven by the
   per-weapon lock setting, rather than animating the off hand
   separately.
6. Optional third layer (from the viewer suggestion above): a
   small per-weapon cyclic motion clip (bob, pull-down) blended
   additively at low weight on the weapon arm only, to break the
   shared-movement sameness. Test it per weapon; do not assume it
   reads as weight.

**Check**
- Does swapping weapons change only the pose layer, with zero
  changes to the locomotion graph?
- With the filter on, do the legs keep the base locomotion
  exactly while the arms take the pose?
- At idle, does the full-body override produce the distinct idle
  pose without snapping, and does it release cleanly on the first
  movement input?
- Does the off hand stay on the grip through the whole jog cycle
  for two-handed weapons?
- Is the sameness trade-off acceptable for the roster, or does a
  weapon need its own locomotion variant after all?

**Why**
The overlay pattern is Phase 2's layering pushed to its
accounting conclusion: locomotion is the shared truth, and
everything weapon-specific is one pose plus weights. The cost is
uniform movement character across weapons; the saving is the
combinatorial explosion it avoids (weapons x locomotion). The
filter is the load-bearing piece: without per-bone masking, an
overlay either fights the legs or replaces them, and the walk
breaks.

**Limits and failure modes**
- Shared movement style is inherent: if two weapons must feel
  different in motion, not just in pose, they need separate
  locomotion variants or the third motion layer above.
- Additive clips must be authored as deltas from the base pose;
  an absolute clip blended additively double-applies the base
  and distorts the pose.
- Assign the spine and pelvis to one layer only. A bone owned by
  two layers twists unnaturally; decide per weapon whether the
  pelvis belongs to locomotion or to the pose.
- Blend-tree bone masks are authored in the graph editor, not
  changed freely at runtime; per-weapon variation lives in the
  weights and pose references, not in mask edits.
- The reel shows no transition handling: add explicit blend-in
  and blend-out times on weapon swap, or the pose pops.

## AAA studio practice

- **Ubisoft Montreal, GDC 2016, Simon Clavet, "Motion Matching and
  The Road to Next-Gen Animation" (For Honor).** The industry
  replacement for hand-managed state machines: a "ridiculously
  brute-force" selection that, every few frames, jumps to the
  mocap segment best matching the character's current situation
  and the desired destination. Trajectory comes from code (a
  simulated point, essentially a spring-damper on the desired
  velocity); animation is "a cosmetic detail on top." The goal is
  predictability, not responsiveness. At the time, 4-5 Ubisoft
  projects were using motion matching. Source: Game Anim writeup:
  https://www.gameanim.com/2016/05/03/motion-matching-ubisofts-honor/
- **Ubisoft Montreal mocap pipeline practice (same talk).** Shoots
  are planned with "dance cards": required action coverage (walks,
  runs, starts, stops, turns, plants) captured in long takes with
  buffer motion before and after each move. Animators do NOT chop
  clips or author cycles (called out as the biggest time-sink of
  traditional pipelines); they do an initial tweak, import, and
  mark events at the exact significant moment (e.g. sword
  contact), and all pose-matching metadata is precomputed offline
  for runtime speed. Pose matching uses about 10 factors: match
  only a few bones, local velocity, feet positions and
  velocities. A realism-vs-comfort slider lets animators and
  designers balance fidelity against immediacy, and aggressive LOD
  keeps it efficient with 100+ characters on screen.
- **Sony Santa Monica, GDC 2019, Bruno Velazquez (God of War
  2018).** A full studio-level rework of the animation approach
  for Kratos, covering the "clean up and exaggerate for the
  fantasy" end of this pipeline: realistic capture as the starting
  point, character-specific exaggeration as the goal. Source: Game
  Developer (GDC Vault video):
  https://www.gamedeveloper.com/art/video-animating-i-god-of-war-i-

**Agent-executable upgrades**

1. **Mocap dance-card manifest (`dance-card.json`).** Required
   action coverage per character (walks, runs, repositions,
   starts, stops, turns, plants, strafe patterns), each with
   buffer-motion requirements. An automated coverage check rejects
   a shoot day whose take library leaves a dance-card action
   uncovered.
2. **Event-markup gate.** Every clip must carry its gameplay
   events (stance changes, hit moments) at the significant frame,
   not clip boundaries; untagged clips fail the gate. All
   pose-matching metadata (pose, velocity, feet
   positions/velocities) is precomputed offline by a batch script,
   never at runtime.
3. **Responsiveness/interruption test.** Automated loop asserting
   every clip can be interrupted at any point by a
   higher-priority state and that masked layers apply to the right
   body parts (upper-body masks with weapon-arm swing reduction,
   per this skill's Phase 2).
4. **LOD/cost check.** Character-count stress test: animation
   update cost stays within budget at the game's target on-screen
   character count, with the LOD policy recorded per character
   tier.

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
verification. Expanded 2026-11-22 with the weapon-overlay pattern
from the Dixon reel, 12 frames read firsthand; overlay construction
and the Godot transfer are labeled as demonstrated vs derived in
that section, and the reel shows no editor setup).
