---
name: unity-dots-fake-ragdoll-crowds
description: "Render 10,000-character crowds in Unity with fake ragdolls: premade ragdoll animation clips plus deterministic launch instead of physics, baked vertex animations, sub-1000-triangle meshes, no armatures, 3 LOD levels. Includes the no-full-ECS alternative (arrays plus Burst/Jobs plus TransformAccessArray into pooled GameObjects). Trigger when a crowd or swarm must scale past a few thousand agents."
---

# Unity DOTS Fake-Ragdoll Crowds (10k Skeletons)

## Purpose

This skill reconstructs the exact technique GrumpyBullGames demonstrates for
10,000 skeletons with fake ragdolls in Unity DOTS, plus the alternative
stack commenter ledniv proposes for teams that do not want full ECS, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The workflow's core method is: never simulate what you can
bake — a premade animation plus a deterministic launch reads as a ragdoll at
crowd scale.

Related skill: `mass-entity-niagara-crowd` (UE MassEntity + Niagara GPU
particles for 100k agents) is the same problem class in a different engine;
this skill is the Unity DOTS + CPU-baked variant.

## Source

Creator: GrumpyBullGames.
Post: https://www.reddit.com/r/unity/comments/1xbqaw6/10000_skeletons_with_fake_ragdolls_in_unity_dots/
(r/unity post 1xbqaw6, score 36, 13 comments; native Reddit clip) |
2026-10-23 scout run. Evidence: the creator's own answers in the comments
(no narration or captions exist on the clip).

**Tools used:** Unity DOTS/ECS, premade animation clips, baked vertex
animations, LOD groups. Alternative stack (commenter ledniv): plain arrays,
Burst/Jobs, TransformAccessArray, pooled GameObjects.

**Depth status:** PARTIAL (comments only; the clip itself was not
downloadable this run — v.redd.it timed out behind an approval gate — and
carries no narration).

## When to use this skill

- Hundreds to tens of thousands of characters must animate and die on
  screen at 60+ fps.
- Real ragdoll physics is unaffordable at the target agent count.
- You want the cheaper alternative first and full ECS only if profiling
  demands it.

## Prerequisites

- Unity with the DOTS/Entities stack (or, for the alternative, Burst + Jobs
  + GameObjects).
- A humanoid animation clip that reads as a ragdoll collapse (the "fake").

## Phase 1: Build the fake ragdoll

**Do**
1. Author (or capture) ONE premade animation clip of a body going ragdoll:
   collapse, tumble, land.
2. At kill time, play the clip with a random starting rotation and launch
   the agent into the air on a deterministic trajectory ("Premade animation,
   some random rotation, deterministic launch into air" — GrumpyBullGames).
3. No physics bodies, no joint solvers, no per-agent collision ("Real
   ragdoll would probably not perform well in such numbers").

**Check**
- At crowd distance the launch + tumble reads as physical; no two agents
  share the exact silhouette because rotation is randomized per agent.
- Deterministic launch means the trajectory is reproducible and cheap —
  no solver state per agent.

**Why**
Ragdoll *simulation* answers "where does the body go"; at 10k agents the
audience only asks "did it fall convincingly". A baked clip plus ballistic
launch answers the second question at a fraction of the cost.

## Phase 2: Strip the per-agent cost to the bone

**Do**
1. Keep triangle count under 1000 per skeleton ("could go lower perhaps,
   but good enough so far").
2. Bake the animations to vertex animation — **no armature, no skinning**
   at runtime.
3. Author 3 LOD levels and switch on distance.

**Check**
- Profile: the vertex shader, not the CPU, is now the binding cost.
- Silhouette holds at each LOD switch; LOD popping is the defect to watch.

**Why**
Skinning and armatures are per-bone CPU/GPU costs multiplied by 10,000.
Baked vertex animation moves the cost to a texture fetch; LODs cut the
vertex load where the audience cannot see the difference. (Concrete
per-asset budget: <1000 tris, 3 LODs, zero bones — compare against your own
P1 perf-budget rows.)

## Phase 3: Drive the crowd (two stacks)

**Do — Stack A (creator's): full DOTS/ECS**
1. Entities carry the baked-animation state; systems update 10k agents in
   parallel jobs.

**Do — Stack B (commenter ledniv's, no full ECS)**
1. Keep simulation data in plain arrays; process all agents in tight loops.
2. Add Burst/Jobs only if profiling says the loops are the bottleneck.
3. Push the resulting positions/rotations back with `TransformAccessArray`
   into **pooled** GameObjects, in parallel.
4. Treat the baked-animation/fake-ragdoll side as a separate
   rendering/animation optimization from the simulation side.

**Check**
- Stack B "gives you most of the Data-Oriented Design benefit without
  restructuring the whole game around Entities, Components and Systems"
  (ledniv). If arrays + Jobs + TransformAccessArray eventually bottleneck,
  ECS remains "another optimization step rather than the starting
  architecture".

**Why**
ECS is an optimization, not a prerequisite. The scaling wins come from data
layout (arrays, tight loops) and from deleting work (no physics, baked
anims); the entity framework is the last 10%, adopted only when the profiler
proves the need.

## Phase 4: Related cheap-crowd patterns (from the same thread)

**Do**
1. Model agents as pure data containers with a single director object
   (commenter PoopsMcScoots' FPS-flea pattern).
2. Remove physics; express jumps as animation curves, not forces.
3. Lock hit colliders to a coarse grid ("grid locked cubes") instead of
   per-agent colliders.

**Check**
- PoopsMcScoots reports choking at ~5k with this pattern — it is the
  starting point the DOTS recipe improves on, not the ceiling.

**Why**
Every deleted subsystem (physics, per-agent colliders, skinned bones) is
headroom for more agents. Delete in order of cost until the profiler is
quiet.

## The human method, distilled

1. **Fake the physics, keep the read.** Premade clip + random rotation +
   deterministic launch.
2. **Bake what repeats.** Vertex animations, no armatures — 10,000 agents
   share the cost model.
3. **Budget per asset, in numbers.** Under 1000 tris, 3 LODs. A budget is a
   number, not an aspiration.
4. **Optimize the data layout before the architecture.** Arrays + tight
   loops + Burst/Jobs + TransformAccessArray first; ECS when profiling
   demands it.
5. **Delete subsystems before scaling them.** No physics, grid-locked
   colliders, one director — the cheapest agent is the one the engine barely
   knows about.

## Failure modes

- **LOD popping:** the 3-level chain needs distance tuning per camera; the
  defect shows at mid-range first.
- **Identical silhouettes:** randomize rotation AND clip phase per agent, or
  the crowd reads as synchronized.
- **ECS-first rewrite:** adopting Entities before profiling the array
  version spends the rewrite budget on the smallest win (per ledniv's
  argument).
- **Unverified scaling claims:** a commenter claims "hundreds of thousands
  at hundreds of fps" without DOTS or GameObjects — presented without
  evidence; treat as a lead to verify, not a result.

## Open questions (from the thread, unresolved)

- mechatui: how far has DOTS animation tooling come — "I was missing stuff
  that you needed for animation" three years ago; no authoritative answer in
  the thread.

## AAA studio practice

Sources:
- Ubisoft Montreal, Assassin's Creed Unity (GDC Vault talk, Massive Crowd: AI Recycling): with a limit of 40 real AIs and 120 high-resolution models, the team pooled and recycled NPCs between low-resolution and high-resolution representations without the player noticing, reaching 10,000 crowd NPCs on screen at once with a simplistic AI brain for the masses. https://www.gdcvault.com/play/1022411/Massive-Crowd-on-Assassin-s
- Epic Games, Unreal Engine MassEntity (Matrix Awakens demo, 2021): Mass is an ECS framework built for large-scale crowd simulation, representing each character as a lightweight entity id over data fragments so thousands can be processed in parallel with a cache-friendly layout, with expensive visuals layered only near the camera. https://irendering.net/unreal-engine-5-5-how-ai-breathes-life-into-thousands-of-digital-characters/
- Epic Games City Sample / TerraCrowds (Unreal crowd plugin reporting): 100,000 agents simulated and visualized in real time by adapting rendering detail to camera distance, from skeletal animation down to vertex-based and simplified models. https://ucrowds.com/blog/2025-09-17-introducing-terracrowds-for-unreal-engine/

**Do**
1. Add the Assassin's Creed Unity pooling rule to Phase 3: budget real AI separately from rendered bodies (Unity's 40 real AIs vs 10,000 on screen is the precedent). Agent-executable step: count active AI brains, active high-resolution models, and total rendered agents in the profiler, and log all three; a crowd that needs one brain per body has not applied the lesson.
2. Automate the LOD and silhouette checks: script a camera dolly from far to near across the crowd, capture frames at each LOD switch distance, and diff silhouettes; popping or synchronized silhouettes fail the run (this automates the existing Phase 2 check).
3. Automate the per-agent budget gate: script an asset audit that fails the build if any crowd mesh exceeds 1000 triangles, lacks 3 LOD levels, or carries a runtime armature, instead of checking meshes by hand.
4. Apply the MassEntity separation explicitly: simulation data in arrays (Stack B) must be a separate system from the baked-animation rendering system, so either side can be profiled and swapped without touching the other.

**Check**
- AI brain count, high-resolution model count, and total agent count are three separate logged numbers.
- Camera dolly frames show no LOD popping and no synchronized silhouettes.
- The asset audit passes before any crowd scene is accepted.

**Why**
Every production crowd system at this scale is the same three moves: pool and recycle bodies, LOD the brain as well as the mesh, and bake what repeats. The Unity DOTS recipe in this skill already does the baking; the AAA addition is the separate AI budget and the automated asset gate.
