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

## AAA studio practice

AAA locomotion is measured against foot slide, not eyeballed, and the industry's two poles are the procedural route (derive the motion from a few poses plus IK) and the data route (search a mocap bucket for the best-matching clip). The mech sits on the procedural pole; the honest comparison is against both.

- **Wolfire Games, Overgrowth (GDC 2014 Animation Bootcamp).** David Rosen's talk shows how simple procedural techniques achieve interactive, fluid animation using very few keyframes, with examples from Overgrowth, Receiver, and Black Shades: interpolate bone transforms between sparse keyframes with spring-like easing instead of linear interpolation, and use simple trigonometry for IK rather than complex solvers.
  (https://www.gamedeveloper.com/design/video-an-indie-approach-to-procedural-animation)
  The direct parallel: the mech's analytic two-bone IK plus procedural gait is the same construction, and Rosen's rule (automate with math what an artist would tweak by hand) is the test the one-shot output passes or fails.
- **Naughty Dog, The Last of Us Part II (GDC 2021).** The motion-matching system replaces the state machine with a bucket of hundreds of mocap clips chopped into small pieces; at runtime the system finds the clip that matches the path the character is already taking and blends frame by frame, with as little blending as possible at every foot plant, applied to the player, NPCs, horses, and dogs.
  (https://www.naughtydog.com/blog/naughty_dog_at_gdc_2021)
  The direct parallel: motion matching is the data-driven answer to the same foot-plant problem, and its discipline (minimal blending at the plant, measured per plant) is the standard the mech's 0 mm drift claim should be judged against.
- **Foot-slide elimination (field practice).** The standard toolkit is velocity-based play-rate scaling, root motion, IK foot locking, distance matching, and stride warping. IK foot locking works by recording the exact world-space transform where the foot touched down (signaled by an animator-placed contact curve), pinning the foot bone there with a two-bone IK solver while the plant lasts, then blending out as the curve drops. Root motion is preferred for single-player precision; IK locking and stride warping are the standard for responsive or multiplayer titles.
  (https://salivity.github.io/game-development/article/preventing-foot-sliding-in-game-animation)
  The direct parallel: the mech's 0 mm drift is a foot-locking claim, and the field's measurement is world-space foot position during the plant phase, which is how an agent should verify it rather than trusting the demo.

**Agent automation**

1. **Locomotion acceptance log.** Keep `mech-locomotion.json` per build: for each gait (walk, turn, stop, crouch) record the maximum foot drift in millimetres measured from foot world positions during plant phases, plus the frame range of each plant. The 0 mm claim becomes a measured number per gait, not a single headline.
2. **Foot-slide measurement procedure.** During a walk, log each foot's world position at plant start and at lift-off; drift is the horizontal distance between them. Any gait whose max drift exceeds 5 mm is flagged for a gait fix before the demo is shown.
3. **Library-vs-custom decision record.** For each system the session wrote (IK solver, camera system, terrain sampling, foot placement), record whether it was custom code or a sourced library and one line on why. Reinvented systems are flagged as capability signal plus quality risk, the honest reading from Phase 3, and any system a battle-tested library exists for gets a "sourced alternative" note.
4. **One-shot test harness.** Re-run the same brief in a fresh session and diff the two outputs' measured numbers (triangle count, joint count, max foot drift). A one-shot claim is only meaningful with the variance across runs recorded.

**Depth status:** PARTIAL (full post text with exact counts and measurements + 22 comments including the author's IK/camera disclosure; code not public, prompt not shared, so the one-shot claim and the 0 mm measurement are the author's reports, not independently verified).

**Gap note:** this workflow is a meaning-match for the Aegis P1 rigging / skinning / animation-retarget gap (audit-verified absent): it demonstrates automated rig creation plus procedural locomotion. It is a research lead, not a drop-in stage: the rig lives in Three.js, not Blender/UE, and the code is not public. Compare against the Tripo P2.0 route in `aegis-pipeline/rigging-stage-design.md` and the GEM-X mocap-retarget lead from 2026-11-11.
