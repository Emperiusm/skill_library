---
name: unreal-jiggle-physics-spring
description: "Add jiggle physics to character joints in Unreal with Animation Blueprint spring controllers: identify the joints, add a spring controller per joint, tune stiffness and damping, and budget the CPU cost honestly. Trigger when adding secondary motion to characters in Unreal."
---

# Jiggle Physics in Unreal: Spring Controllers on Joints

## Purpose

This skill adds spring-driven secondary motion ("jiggle physics") to
character joints using Unreal's Animation Blueprint spring
controllers. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle).
The core method is: joints first, one spring controller per joint,
tune the spring, then pay the CPU bill with open eyes.

## Source

Instagram, kennedy_artist ("The Graphics dude") (transcribed from
reel audio with faster-whisper tiny, 2026-11-02; captions unavailable
via API):

- https://www.instagram.com/reel/DfFPh00MYIE/ — "In the pursuit of realistic characters, we have to obsess over every tiny detail."

Evidence note: reel-length narration (about 3 minutes); machine
transcription, minor word errors possible. Node names and the
stiffness/damping semantics are as spoken.

## Tools used

Tools used: Unreal Engine Animation Blueprints (visual node scripting;
the spring controller node). Context from the narration: Blueprints
connect to other Blueprints, and components can be reused and shared.

## Phase 1: Identify the joints that should jiggle

**Do**
1. Remember how flesh moves: "the most common way of moving flesh in
   a character is by using joints, which are literally markers in 3D
   space that we assign an area of influence, and that's what
   animation runs on."
2. Identify or create the joints controlling the body parts that
   should jiggle.

**Check**
- Is each jiggling body part driven by a declared joint?
- Are you jiggling parts where the motion will actually be seen?

**Why**
Jiggle is applied to joints, not to meshes. If no joint owns a body
part, there is nothing for the spring to drive. Choosing the joints
first keeps the effect deliberate instead of sprayed.

## Phase 2: Add spring controllers in the Animation Blueprint

**Do**
1. Connect an Animation Blueprint to the character's Blueprint so
   you can modify any animation the character plays.
2. In the Animation Blueprint, add the spring controller node: "a
   node that adds spring behaviour to any joint that we declare."
3. Select the joints the spring applies to. For several joints, copy
   the node and change the joints per copy.

**Check**
- Does every target joint have its own spring controller?
- Is the controller wired into the animation graph (input node
   through the manipulation nodes to the controllers)?

**Why**
One controller per joint (or per joint set) keeps the tuning
independent: a belly spring and a chest spring want different
stiffness. Copying the node per joint is the intended pattern, not a
hack.

## Phase 3: Tune stiffness and damping, then budget the CPU

**Do**
1. Tune the two settings: "stiffness is stiffness, and damping is
   how quickly the spring controller loses or absorbs the initial
   energy."
2. Face the cost honestly: "there's a CPU cost to calculating that
   spring, and for the most part, the visual impact isn't worth that
   cost. Unless, of course, this is very important for the game."

**Check**
- Does the motion settle naturally (damping), without endless
   oscillation or a dead stop?
- Have you counted the springs per character against the frame
   budget?

**Why**
Jiggle physics is easy to add and expensive to keep: the reason only
high-budget games use it broadly is the CPU cost per spring, not the
difficulty. The decision is economic (is this motion worth its
springs?) rather than technical.

## The human method, distilled

1. Joints own flesh; declare the joints before the springs.
2. One spring controller per joint set, copied not shared.
3. Stiffness sets the spring, damping settles it.
4. Budget springs like any other per-frame cost; most games should
   use few.

## Depth status

PARTIAL (transcribed reel audio, about 3 minutes; node names and
settings as spoken; no frame-level verification of the graph).
