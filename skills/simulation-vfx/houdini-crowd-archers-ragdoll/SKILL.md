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

## AAA studio practice

This skill's exact mechanics are the production crowd mechanics. SideFX's crowd documentation describes sticky collisions as a first-class feature: arrows shot at agents stick instead of bouncing off, and the Crowd Trigger counts sticky collisions on an agent to trigger new behavior, with the documented example being agents that transition from walking to ragdoll after two sticky collisions. SideFX's crowds overview names the same state machine this skill uses: partial and full ragdoll states, where agents hand control to a rigid-body simulation for impacts, knockdowns, and death events, plus hero agents directed to stand out from the crowd. At blockbuster scale, the Battle of Winterfell in Game of Thrones (Rodeo FX) used Houdini crowd simulation for thousands of undead soldiers and human forces responding to shifting battle dynamics, running, falling, and fighting without per-soldier animation. The lesson that scales from that shot to this skill: the crowd solver owns behavior and transitions, the artist owns triggers and handoffs.

- Source: https://www.sidefx.com/docs/houdini/crowds/ragdoll.html (SideFX: sticky collisions, Crowd Trigger counting sticky collisions to change state, walking-to-ragdoll after two hits)
- Source: https://www.sidefx.com/products/houdini/characters/crowds/ (SideFX: partial/full ragdoll state transitions, hero agents)
- Source: https://studioimageworks.com/houdini-crowdsimulation-smarter-dynamic-crowd/ (Battle of Winterfell: Houdini crowd simulation for thousands of agents in shifting battle dynamics)

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Replace the Phase 2 hand-off description with the SideFX trigger pattern: configure sticky collisions on the arrow RBD and the agent states, and set the Crowd Trigger to count sticky collisions per agent (1 to 3 hits, per this skill) and transition the agent to the ragdoll state at the threshold. Log the hit count per agent that died, so the death rule is auditable.
2. Automate the Phase 1 prop-attachment check: before the full sim, run one archer agent through draw and release and verify the arrow rides the hand for the whole motion. A failed attachment stops the sim before any crowd compute is spent.
3. Automate the Phase 3 collapse test the same way: run one agent as a ragdoll on a collapsing floor section first, and verify it falls with the floor (no hovering) before the full crowd collapse runs.
4. Automate the Phase 4 render-iteration gate: render the behavior pass in Unreal first for turnaround, and promote to Karma only after the behavior (aim, stick, death, collapse) is signed off. Record which renderer produced each review pass, so a slow Karma render is never spent on an unapproved behavior.

**Check**
- The trigger counts sticky collisions per agent and transitions to ragdoll at the configured threshold; the hit log exists per dead agent.
- The single-agent draw/release check passes before the crowd sim starts.
- The single-agent collapse check passes before the full collapse runs.
- The Unreal behavior pass is signed off before any Karma hero render is queued.

**Why**
- The crowd solver's cost is in the full sim, so every check that can run on one agent must run on one agent. The trigger pattern also replaces the author's hand-tuned handoff with the documented mechanism, which means the next artist can reproduce the deaths instead of reverse-engineering them.

## The human method, distilled

1. **Fix the library animation first**: re-attach before you simulate.
2. **The handoff is the technique**: RBD arrow to crowd sim, cleanly.
3. **Render where you can iterate**: Karma quality vs Unreal speed,
   chosen for turnaround, not for looks alone.

**Depth status:** PARTIAL (post text + all 9 comments; no solver
parameters, agent setup, or render settings disclosed).
