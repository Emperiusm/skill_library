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

## The human method, distilled

1. Simulate everyone, render only the near field; never let render cost scale with total count.
2. Take the data-oriented half of ECS (flat arrays, batch passes) and skip the framework ceremony when it adds nothing.
3. Report the rig actually measured on, and name what has not been measured yet.

## Depth status

FULL — full post text with hardware, settings, and caveats. Comments add nothing beyond praise, so no comment technique is claimed. No code was published, so this skill is a design recipe, not a copy-paste implementation.
