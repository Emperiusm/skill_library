---
name: godot-500-rigidbody-octree-two-viewport
description: "Run a 500-ship RigidBody3D fleet battle in Godot 4.7: keep real rigid bodies moved with apply_force/apply_torque, replace a 30ms+ GDScript neighbour search with an engine-level octree, drive ships with shoot/evade timers and predictive targeting (target_pos + target_vel * dist/projectile_speed), scale particle effects slightly with distance in a shader, and composite two viewports with +25 degrees FOV on the background pass. Trigger when a Godot battle's script-side neighbour search is the bottleneck, or when one camera cannot serve both battle readability and a vast background."
---

# 500 RigidBody3Ds in Godot: Engine Octree + Two Viewports

## Purpose

This skill keeps 500 real rigid bodies fighting without letting the neighbour search or the camera eat the frame. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: real bodies, engine-side spatial search, timer-driven behaviour, and two viewports with different FOVs.

## Source

- Post: "Testing a 500 RigidBody3Ds spaceship battle" by OMUTV — https://www.reddit.com/r/godot/comments/1y59r3w/ (score 124, 37 comments; 25 retrieved). Evidence: the author's full post text plus the author's own comment answers on the octree, the 30ms figure, the targeting formula, the timers, the raycasts, the shader trick, and the two viewports. Captured running in the editor with OBS. Scout audit 2026-11-26, audit 2, FULL.

## Tools used

Godot 4.7 "with a few engine tweaks"; GDScript; a C++ engine addition (spatial partitioning/search, "just an octree"); OBS for capture. No add-ons or asset packs named. No post-fix frame-time number, battle-camera FOV value, or engine-tweak code was disclosed; none is invented here.

## Phase 1: Give every ship a real rigid body

**Do**
1. Build each ship as a RigidBody3D in Godot 4.7.
2. Move ships with `apply_force` and `apply_torque`, so they have mass and inertia.
3. Let ships collide and bounce off each other; projectile impacts push ships around "in realistic-ish ways".

**Check**
- Ships collide and bounce instead of passing through each other. The author defends the choice on exactly this ground: "They do collide and bounce off of each other."

**Why**
The battle is an autobattler whose feel comes from physical shoving. A kinematic fake would need a separate collision story; the cost of real bodies is paid once, in the neighbour search (Phase 2).

## Phase 2: Move the neighbour search into the engine

**Do**
1. First try GDScript spatial search for "find the closest enemies". Measure it: "it was 30ms+ per frame just searching for 500 ships."
2. Add "some basic spatial partitioning and searching to the engine" instead. The structure, confirmed by the author when asked: "Yes just an octree!"

**Check**
- Frame time must drop from the 30ms+ GDScript search. No post-fix number is stated; the posted video of 500 ships moving and shooting is the evidence offered. Do not quote a post-fix frame time.

**Why**
"I probably could have improved the gdscript quite a bit more but I wanted to try adding a feature to the engine." When script is the bottleneck and the search is a data structure, the fix belongs in the engine, not in a cleverer script. Measure the script bottleneck first (Phase 1's 30ms+ figure is the trigger); do not jump to an engine change on suspicion.

## Phase 3: Drive the battle with shoot/evade timers and predictive targeting

**Do**
1. Give each ship a timer: "shoot for some time and then evade for some time, so they never seem to get into a deadlock. Ships also change their state if they are too close or too far (and some other rules)."
2. Aim with predictive targeting: `target_pos + target_vel * (dist_to_target / projectile_speed)`. The author notes: "They miss a lot at slow speeds but these projectiles are fast enough that it's not a big deal."
3. Avoid collisions with "a few raycasts! It's not perfect (they still bump into each other) but hopefully good enough for an autobattler!"

**Check**
- No deadlock: ships never circle each other forever. The timers plus proximity state changes are the deadlock fix.
- Misses are acceptable at slow speeds; judge the battle as a whole, not per-shot accuracy.

**Why**
An autobattler needs behaviour that never stalls and aiming that is good enough at combat speeds. Exact targeting and perfect avoidance are not the goal; a battle that keeps moving is.

## Phase 4: Scale effects with distance, in the shader

**Do**
1. "For effects I actually use a bit of a shader trick to scale up some particle effects *slightly* when they are far away from the camera, like muzzle flares and sparks." (author's comment, emphasis as written).

**Check**
- Distant muzzle flares and sparks stay visible without near effects looking oversized. "Slightly" is the author's own limit; no scale factor is stated, and none is invented.

**Why**
At fleet scale, physically correct effect sizes vanish with distance. A small distance-based upscale keeps combat readable.

## Phase 5: Render the battle and the background as two viewports, composited

**Do**
1. Keep the battle world "totally separate from the backgrounds, the planets, the asteroids, and stars, etc."
2. "I actually render two separate viewports and composite them together. This also lets me add +25 degrees to the camera FOV when rendering the background so it seems 'bigger' and it lets me keep my battle camera at a low FOV so all important objects appear similar in size."

**Check**
- Background objects read as vast while battle ships keep consistent apparent size. The +25-degree background FOV is the exact number; the battle camera's FOV value is not stated and is not invented.

**Why**
One camera cannot serve both jobs: a wide FOV makes the background feel big and the ships inconsistent; a low FOV keeps ships comparable but flattens the background. Two viewports let each FOV do one job.

## AAA studio practice

- **The neighbour search belongs in native engine code, measured first, and the broadphase is the part that must scale.** Guerrilla switched *Horizon Forbidden West* from a commercial physics engine to Jolt Physics, an engine architected specifically to solve streaming and multithreaded-update bottlenecks, and reports saving memory and executable size while doubling simulation frequency using less CPU time. The Jolt GDC 2022 talk is specifically about a lock-free broadphase and a lock-free simulation-island building algorithm: the broadphase is the query layer that decides which bodies may interact, and it must be safe to query while bodies move. That is the production form of this skill's Phase 2: a 30ms+ GDScript search is the measured trigger, and the fix is an engine-level spatial structure, not a cleverer script. The octree is this author's structure, not Jolt's, so do not present the octree as Jolt's structure; the shared principle is a native spatial index queried before any per-pair work. Source: https://www.guerrilla-games.com/read/architecting-jolt-physics-for-horizon-forbidden-west
- **Hundreds of real agents, thousands of cheap ones: tier the population instead of simulating every body at full cost.** Ubisoft's GDC 2015 talk on *Assassin's Creed Unity*, "Massive Crowd on Assassin's Creed Unity: AI Recycling", describes a pooling system swapping low-resolution NPCs to high-resolution NPCs without the player noticing, working within 40 real AIs and 120 high-resolution models to present 10,000 crowd NPCs on screen at once. The lesson for a 500-ship battle is to record which tier each ship is in (full rigid body with behaviour, or cheap pooled stand-in) and to promote only ships near the action, rather than paying full behaviour and search cost for all 500 at all times. The author's timer-driven behaviour (Phase 3) is the cheap tier's control loop: simple state changes, not full AI per ship. Sources: https://www.gamedeveloper.com/programming/get-coding-advice-from-insomniac-riot-and-ubisoft-at-gdc-2015 and https://www.gamedeveloper.com/programming/video-behind-the-massive-crowds-of-i-assassin-s-creed-unity-i-
- **Massive crowds in production are data-oriented, with baked animation for the far tier.** Epic's Mass framework is an archetype-based ECS created by Epic's AI team to facilitate massive crowd and traffic simulations, designed for and featured in *The Matrix Awakens* demo (2021). In the City Sample crowd work built on it, distant crowd members are instanced static meshes with baked bone animation managed through the Mass subsystem, while near characters use fuller representation. The lesson is the same tier split as above, stated as an architecture rule: the search, the behaviour, and the animation representation all change with distance, and the far tier never pays the near tier's cost. Source: https://vrealmatic.com/unreal-engine/mass
- **A background that must read as vast gets its own rendering treatment, decoupled from the gameplay pass.** Epic's Sky Atmosphere work decouples atmosphere rendering from final screen resolution with low-resolution lookup tables that maintain high-frequency features, making the technique scalable from mobile to high-end PCs by tweaking LUT resolution and ray-marching sample count. That decoupling is the production analogue of this skill's Phase 5, not the +25-degree value itself: the background pass is allowed different parameters (here, a wider FOV) because it answers a different question (vastness) than the battle pass (consistent ship size). No AAA source was found prescribing +25 degrees for a background viewport, and that number stays the author's, not a studio standard. Source: https://blog.selfshadow.com/publications/s2020-shading-course/hillaire/s2020_pbs_hillaire_slides.pdf

**Agent automation**

Write `fleet-perf-manifest.json` beside every battle run, with exactly these fields: ship count, GDScript neighbour-search time in ms before the engine change, engine octree query time in ms after it, battle-camera FOV, background-camera FOV (which must equal battle FOV plus 25, recorded, not assumed), and the longest observed deadlock stall. Fail the run if the post-fix query time is empty: no post-fix frame-time number was disclosed, and none may be invented or copied from another project. Then run these gates in order: (1) measure-first gate, the GDScript search must be timed on the 500-ship scene before any engine change is attempted, and the 30ms+ figure is re-measured, not quoted from memory; (2) octree-correctness gate, on a small test scene the octree's nearest-enemy answer must match a brute-force search for every ship, or the mismatch is logged before the battle runs [inference: this comparison harness is agent design, built from the skill's own "find the closest enemies" definition]; (3) deadlock gate, run the battle until every ship has changed state at least once and record any ship that never changes state; (4) composite gate, capture one frame from each viewport separately and one composited frame, and record that background objects read as vast while ships keep consistent apparent size. No engine-tweak code, battle-camera FOV value, or post-fix frame time from outside this skill may be entered into the manifest.

## The human method, distilled

1. **Measure the script bottleneck before rewriting it:** 30ms+ per frame in GDScript search is the stated reason for the engine change.
2. **Fix stalls with timers and state changes, not smarter AI:** shoot/evade timers plus proximity rules are the deadlock answer.
3. **Cheat scale where the camera is the problem:** distance-scaled effects and a +25-degree background viewport, both admitted as tricks, both in service of readability.

## Depth status

FULL from the author's full post text plus 25 retrieved comments. No video transcript or frame review exists for a native Reddit video; no engine-tweak code, battle-camera FOV, or post-fix frame time was disclosed, and none is invented here.
