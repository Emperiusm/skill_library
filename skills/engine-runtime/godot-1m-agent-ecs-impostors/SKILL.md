---
name: godot-1m-agent-ecs-impostors
description: "Simulate 1,000,000 agents in Godot 4.6 C# at 300-450 FPS: structure-of-arrays data with batch passes (no formal ECS framework), fully rigged/skinned rendering only for the nearest few thousand, GPU impostors for the rest. Trigger when a crowd, battle, or swarm scene must scale with camera distance, not with total count."
---

# Godot 1M Agents: ECS-Style Data-Oriented Crowds with GPU Impostors

## Purpose

This skill reconstructs the 1M-soldiers battle-simulation workflow, step by step, so another agent can build a large-agent scene the same way. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: simulate everyone, render only what is near, and let cost scale with camera distance, not with army size.

## Source

- Post: "1M Soldiers in Godot 4 C# at 300–450 FPS — ECS-Style Data-Oriented Design" — https://www.reddit.com/r/godot/comments/1xh7eiw/ (score 38, 3 comments)
- Evidence: full post text, 2026-10-28 scout run. No code was published in the post; this skill encodes the design, not a code listing.

## Tools used

Godot 4.6 (.NET / C#), Forward+ renderer, Mixamo (soldier model/animation), GPU impostors (distant soldiers). Test PC: Core i5-12600K, RTX 4070 Ti, 32 GB DDR5, NVMe SSD. Settings: 1920×1080, 60 Hz monitor, VSync off (uncapped), running inside the editor with JIT.

## Phase 1: Store soldiers as arrays, not objects

**Do**
1. Give each soldier an index into structure-of-arrays data: position, yaw, HP, animation time, team, state, and so on.
2. Run logic as batch passes over that data. This is NOT a formal ECS framework: "no entities, components, queries or system scheduler". It is ECS-style separation of data and behavior plus data-oriented design taken "to the extreme".
3. Simulate all 1,000,000 agents at once: AI, movement, collisions, combat, respawn; two armies chasing, fighting, dying, and respawning.

**Check**
- The simulation count is 1,000,000 agents, not 1,000,000 rendered characters. Any claim otherwise misreads the source.

**Why**
Batch passes over flat arrays are cache-friendly and branch-light; per-soldier objects with per-frame virtual calls are what would make 1M agents impossible. The author separates the two halves of ECS/DOD and takes only the data-oriented half to the extreme.

## Phase 2: Render near soldiers fully, distant soldiers as impostors

**Do**
1. Fully rig and skin only the nearest few thousand soldiers at any moment (Mixamo model/animation).
2. Draw the rest as GPU impostors.
3. Let scaling follow the camera: "Cost depends on how many soldiers are near the camera, not on the total."

**Check**
- FPS is reported across all modes, graphics levels, and camera positions in the video; headline numbers are 300–450 FPS overall, dropping to ~180 at Ultra, because "GPU load grows mainly with graphics level (Ultra costs the most)" while "scaling with soldier count is mostly CPU-side (simulation, pose, culling)".

**Why**
Rendering cost must scale with what the camera sees, or the army size is capped by the GPU. Simulation cost scales with army size and stays on the CPU, where batch passes carry it.

## Phase 3: Report the measurement honestly, including what was not tested

**Do**
1. Measure inside the editor with JIT, VSync off, and say so: "FPS shows performance headroom rather than what the monitor displays."
2. State the untested configurations plainly: "Not yet tested: a release export (no editor, no debug engine) and NativeAOT. I expect release to be faster, but I haven't measured it yet."

**Check**
- Any reuse of the 300–450 FPS figure must carry the editor/JIT caveat and the untested-release caveat with it.

**Why**
A benchmark without its conditions is a marketing number. The author's own caveats are what make the number usable: headroom in-editor, release expected faster but unmeasured.

## AAA studio practice

- **Run two crowd systems, not one: a cheap systemic crowd plus full AI that dips in and out.** Ubisoft's Assassin's Creed Unity had a dedicated crowd-realisation team and two cooperating systems: a "bolt crowd" simulating how people move inside a crowd (flock-like, systematic), with individual complex AI dipping in and out of it, becoming part of the bolt crowd when they move away and full AI again when they step out. Crowds reached 5,000 AI in some missions and 10,000 for the beheading of the King. Applied here: the 1M-agent simulation is the bolt-crowd layer; the near field that gets full rigs is the dipping-in layer, and the boundary between them is a designed system, not an accident of distance.
  Source: https://www.techradar.com/news/gaming/inside-assassin-s-creed-unity-ubisoft-s-leap-of-faith-1268435/2
- **Simulate the whole city, not a bubble around the player.** Epic's The Matrix Awakens Mass AI system simulated 35,000 pedestrians and about 17,000-20,000 traffic vehicles across the city, with the developers stressing it was not a frustum bubble: they kept track of everything, with optimizations, but did not exclude agents by view frustum. The Godot skill's "simulate everyone, render only what is near" is the same contract at 1M scale, and the Matrix numbers are the proof that the contract holds in a shipped tech demo.
  Source: https://gamingbolt.com/the-matrix-awakens-demo-features-35000-metahuman-pedestrians-billions-of-polygons-for-7000-buildings
- **Bake distant animation into textures, and bake it at 16-bit.** A production GPU-driven crowd framework described on 80 Level bakes each animation state (idle, clap, yell, stand) as a separate vertex-animation-texture (VAT) bake with constant topology, using 16-bit floating point raster depth because 8-bit textures lack the precision to store world-space position offsets without visible vertex jitter, especially close to the camera. That is the production form of this skill's GPU impostors: the impostor is not a flat billboard by default, it is a baked animation texture with a precision floor.
  Source: https://80.lv/articles/6-000-agents-on-one-game-thread-novel-high-performance-framework-for-gpu-driven-crowd-systems

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Log a per-frame distance-band budget: agents simulated, agents fully rigged/skinned, agents drawn as impostors, and the camera distance at which the near/impostor boundary falls, sampled at three camera positions (close, mid, far) per test run.
2. Add an impostor-pop check: fly the same camera path twice, once with the boundary at its shipping distance and once with the boundary halved, and diff the frames at the transition distance; visible popping at the boundary is a defect, not a tradeoff to accept silently.
3. Add a release-export gate before any FPS figure is quoted: re-measure the same scene in a release export (no editor, no debug engine), since the author's own caveat is that release is untested and only expected to be faster; the editor/JIT figure and the release figure are reported as two separate numbers, never merged.

**Check**
- A crowd scene is shippable only when the distance-band budget shows render cost flat as total agent count grows at a fixed camera position, and the pop check passes at the shipping boundary.
- Any FPS figure quoted without its build type (editor/JIT or release export) is incomplete and must not be reused.

**Why**
The skill's headline (1M agents, 300-450 FPS) is only usable if its two halves are measured separately: simulation cost that scales with army size, and render cost that scales with camera distance. The band budget proves the second half, and the release gate closes the author's own open caveat.

## The human method, distilled

1. Simulate everyone, render only the near field; never let render cost scale with total count.
2. Take the data-oriented half of ECS (flat arrays, batch passes) and skip the framework ceremony when it adds nothing.
3. Report the rig actually measured on, and name what has not been measured yet.

## Depth status

FULL — full post text with hardware, settings, and caveats. Comments add nothing beyond praise, so no comment technique is claimed. No code was published, so this skill is a design recipe, not a copy-paste implementation.
