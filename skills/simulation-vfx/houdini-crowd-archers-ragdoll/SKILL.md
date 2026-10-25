---
name: houdini-crowd-archers-ragdoll
description: "Stage a Houdini crowd battle: archers aiming at live targets, Mixamo animations fixed by re-attaching the arrow to the hand, a clean RBD arrow handoff into the crowd sim, arrows that stick, death after 1 to 3 hits, a floor collapsing into the abyss with ragdolls, and a Karma-to-Unreal render switch chosen for iteration speed. Trigger when a crowd shot needs physical hits and a collapsing floor, or when library animation props land in the wrong place."
---

# Houdini Crowd Battle: Archers, Sticky Arrows, Ragdolls, Collapsing Floor

## Purpose

This skill reconstructs the crowd-battle technique from the author's
post and comments, step by step, so another agent can follow the same
process. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The video's
core method is: aim archers at live crowd targets, make every hit
physical, and let the floor take the dead down with it.

## Source

Creator: andrey_krylevskiy. Reddit post:
https://www.reddit.com/r/Houdini/comments/1xde3q4/100_crowd_agents_vs_archers_sticky_arrows/
(r/Houdini post 1xde3q4, score 105, 9 comments) | 2026-10-25 scout run,
audit 2.

## Tools used

**Houdini** (crowd sim), **Mixamo** animations, **Unreal Engine 5**
(this version's render), **Karma** (the first version's render). No
crowd solver, agent count tuning, or render settings are disclosed;
none are claimed here.

## Phase 1: Aim archers at live targets

**Do**
1. Run the crowd sim in Houdini with archers aiming at live targets
   (not pre-baked paths).
2. Fix the Mixamo problem first: Mixamo animations came with the arrow
   in the wrong place, so re-attach the arrow to the hand.

**Check**
- The arrow must ride the hand through the draw and release; a
  mis-placed arrow breaks the shot before any arrow flies.

**Why**
- Library animation is a starting pose, not a finished prop rig: the
  attachment is the author's actual work in this phase.

## Phase 2: Make hits physical (sticky arrows, 1-3 hit deaths)

**Do**
1. Hand the RBD arrow cleanly off to the crowd sim at release.
2. Arrows that hit actually stick in the target.
3. Death after 1 to 3 hits (not a fixed hit count).

**Check**
- A stuck arrow must stay with the agent's motion after impact; a
  death must read as caused by the hits, not by a timer.

**Why**
- The author names the handoff as the hard part ("I had to re-attach
  it to the hand, and then hand off the RBD arrow cleanly to the crowd
  sim"). The handoff, not the arrow model, is the technique.

## Phase 3: Collapse the floor with the ragdolls

**Do**
1. Collapse the floor into the abyss, with ragdolls going down with it.

**Check**
- Ragdolls must fall with the collapsing floor, not hover where the
  floor was.

**Why**
- The collapse is the payoff for the crowd sim: the same agents that
  fought are the debris.

## Phase 4: Render where the iteration is cheap

**Do**
1. First version: render in Karma. This version: render in Unreal.
2. Accept the tradeoff the author states: Unreal lighting "isn't quite
   as good, but I got tired of waiting for renders."

**Check**
- The author is explicit that this is a time tradeoff, not a quality
  claim for Unreal.

**Why**
- Render time is a creative constraint: a crowd shot that cannot be
  iterated is a crowd shot that cannot be finished. The author on
  learning it: "The docs alone weren't enough for me - most of what I
  know came from Crowds for Feature Film courses, plus a lot of trial
  and error and forum digging." A commenter agrees there is still no
  proper crowd course, calling crowds "arguably one of the most useful
  things in Houdini for film/tv."

## The human method, distilled

1. **Fix the library animation first**: re-attach before you simulate.
2. **The handoff is the technique**: RBD arrow to crowd sim, cleanly.
3. **Render where you can iterate**: Karma quality vs Unreal speed,
   chosen for turnaround, not for looks alone.

**Depth status:** PARTIAL (post text + all 9 comments; no solver
parameters, agent setup, or render settings disclosed).
