---
name: fable-one-prompt-mech-rig
description: "Test what Fable 5.2 (High) can build in one shot: one written brief, one agent session, no sub-agents, no follow-up prompts, no manual fixes, and the output is a ~65k-triangle Three.js mech with a 52-joint hierarchical rig, analytic two-bone leg IK, fully procedural walk with 0 mm measured foot drift, combat mode, 5 camera systems, and procedural WebAudio. Includes what the model wrote itself (custom IK and camera code, no libraries) and the honest reading that it reinvented systems rather than sourcing battle-tested ones. Trigger when evaluating agentic 3D code generation, or when a prompt-generated rig is needed as a research route."
---

# Fable 5.2 One-Prompt Mech: Rig, IK, and Procedural Walk in One Session

## Purpose

This skill reconstructs the one-prompt mech workflow from the author's post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: write one brief, let one agent session build the whole mech, and measure the locomotion instead of trusting the demo.

## Source

Creator: koss-tech. Reddit post:
https://www.reddit.com/r/threejs/comments/1xthmu3/mech_test_in_threejs_built_with_fable_52_high/
(r/threejs post 1xthmu3, score 69, 23 comments) | 2026-11-12 scout run, audit 5. Live demo: https://mech-fable-5-2.kosslabs.workers.dev/

This is a distinct Fable 5.2 workflow from the 2026-11-10 steering post (Opus-class model driving Blender MCP plus Tripo): that one steers Blender; this one is a one-shot Three.js build with a generated rig. The code is NOT public for this post ("not public at the moment"), and the prompt was not shared, so this skill records the measured output, not a reproducible prompt.

## Tools used

**Fable 5.2 (High)**, **Three.js** (the only external 3D dependency); custom analytic two-bone IK; procedural **WebAudio**.

## Phase 1: Write one brief, run one session

**Do**
1. Write one brief and run one agent session in Fable 5.2 (High). No sub-agents, no follow-up prompts, no manual fixes, no cleanup. The author's words: "First run. One prompt, one pass."

**Check**
- The author, who says he has "worked in 3D for most of the last 20 years", deliberately did not touch anything after generation, "because the whole idea was to show the raw one-shot output." His experience, in his own account, would have gone into seeing "the things that are a bit off, the small issues and nuances" and fixing them afterwards.

**Why**
- The test is the one-shot output, not the polished result. Any manual fix would have hidden what the model can and cannot do alone.

## Phase 2: Read what the session produced

**Do**
1. Take the output as delivered: ~65k triangles in the mech, 52-joint hierarchical rig, 14 hydraulic pistons, fully procedural walk with no keyframes, analytic leg IK, crouch / stand / power-down / power-up sequences, combat mode with cannon, missiles, shield and target tracking, exploded view, X-ray and joint debug modes, 5 camera systems, day / night modes, full sci-fi HUD, procedural WebAudio for footsteps, servos, weapons and explosions. The whole scene is ~163k triangles.
2. Try the live demo the author posted: https://mech-fable-5-2.kosslabs.workers.dev/

**Check**
- Measured 0 mm foot drift while walking, turning and stopping. That number is the author's measurement, and it is the check that matters: a procedural walk that slides is a broken walk, however good it looks.
- The gait, foot placement, weight shift, heel-to-toe roll, braking and turning are all generated procedurally. "It doesn't just play a walk animation."

**Why**
- Foot drift is the falsifiable claim. Triangle counts and feature lists are marketing; a zero-drift measurement is a test result.

## Phase 3: Know what the model wrote itself

**Do**
1. Note what is custom project code and what is a library: the leg solver is custom (analytic two-bone IK using Three.js vectors/matrices/quaternions, plus custom terrain sampling, foot placement and heel/toe rollover logic). The camera system is custom too (orbit, follow, hero, cinematic and cockpit views, all implemented in the project code; no OrbitControls or other external camera library).
2. Note the dependency discipline: "Runtime-wise, Three.js is basically the only external 3D dependency. No external IK, physics, animation, rigging or model libraries."

**Check**
- Commenter FormerKarmaKing asked exactly the right question: did it write its own IK and camera systems, or source existing libraries? The author's answer (above) is that it reinvented them. That is less impressive than sourcing battle-tested libraries, and it is the honest reading: the model reinvented the systems rather than sourcing them.

**Why**
- Reinvented IK is a capability signal (it can derive the math) and a quality risk (unproven code). Both readings belong in the audit.

## The human method, distilled

1. One brief, one session, no fixes: measure the raw output.
2. "Being able to describe what you want is starting to matter more than knowing how to build it." (author)
3. Experience still matters after generation: "Someone who spent years in 3D still understands why something works, what looks wrong, what to ask for, and how to push a result further." (author)
4. Measure locomotion (foot drift), do not eyeball it.

**Depth status:** PARTIAL (full post text with exact counts and measurements + 22 comments including the author's IK/camera disclosure; code not public, prompt not shared, so the one-shot claim and the 0 mm measurement are the author's reports, not independently verified).

**Gap note:** this workflow is a meaning-match for the Aegis P1 rigging / skinning / animation-retarget gap (audit-verified absent): it demonstrates automated rig creation plus procedural locomotion. It is a research lead, not a drop-in stage: the rig lives in Three.js, not Blender/UE, and the code is not public. Compare against the Tripo P2.0 route in `aegis-pipeline/rigging-stage-design.md` and the GEM-X mocap-retarget lead from 2026-11-11.
