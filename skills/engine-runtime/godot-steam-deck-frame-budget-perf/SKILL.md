---
name: godot-steam-deck-frame-budget-perf
description: "Make a Godot game run smoothly on the Steam Deck the way Richard-Dev did for Wreck and Repeat: spend spare frame budget building the next procedural city in advance, rewrite the hottest loops in GDExtension C++, cap main-thread destruction at 3 ms per frame with worker threads, and measure every frame per system. Trigger when a Godot game stutters or loads slowly on low-power hardware."
---

# Godot Steam Deck Frame-Budget Performance

## Purpose

This audit reconstructs the exact workflow from Richard-Dev's post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The post's core method is: give every frame a millisecond budget, measure everything per frame, and spend spare budget on the expensive work.

## Source

Creator: Richard-Dev. Post: "Tips and Tricks on how I made my game run smoothly on the SteamDeck", https://www.reddit.com/r/godot/comments/1xy0xbh/tips_and_tricks_on_how_i_made_my_game_run/ (score 41, 9 comments). Game: Wreck and Repeat, https://store.steampowered.com/app/5519480/Wreck_and_Repeat/. Evidence: full post text and all 9 comments read firsthand. 2026-11-17 scout run.

## Tools used

Tools used: **Godot**, **GDExtension with C++**, worker threads, occlusion culling, batched shadows. No engine version stated in the post.

## Phase 1: Build the next city with spare frame budget

**Do**
1. Set a millisecond budget per frame for the target frame rate.
2. If a frame finishes under budget, spend the leftover on generating the next procedural cyberpunk city, a little at a time, in advance.
3. Target low-input screens (score screen, screen transitions) with a much larger per-frame budget, because the player tolerates stutters there.
4. Rewrite the most expensive loops in GDExtension C++. The author: "This took a long time but was extremely worth it, sometimes cutting the load time in half or more by itself."

**Check**
- Load times before: long loads, then 10-20 fps in-game on the Steam Deck. After: the game runs at the target frame rate (the author aims for 16 ms per frame on the main thread).
- If a screen still stutters, the budget on that screen is too small: raise it on low-input screens first.

**Why**
Generation is the first resource hog (a huge procedural city between runs). Spreading it across frames the player never notices turns a load-time problem into a budgeting problem, and the C++ rewrite attacks the loops that budgeting alone cannot fix.

## Phase 2: Cap main-thread destruction work per frame

**Do**
1. Give the main thread about 3 ms per frame for destruction math; anything above that spills over to the next frame.
2. Delegate the expensive parts to worker threads that never slow the game: collision calculation, and how much support a building has (whether it should crumble, topple, or stand still).
3. Cap physics per frame (the author: "starting to see a pattern here?").
4. Accept that threaded destruction is, in the author's word, "dangerous" and bug-prone, and stabilize it with measurement (Phase 4).

**Check**
- The game stays at the target frame rate while buildings are being destroyed; destruction that would blow the 3 ms budget visibly continues over following frames instead of hitching.

**Why**
Destruction is the second resource hog (everything destructible within the run). A hard per-frame cap plus offloading is the only way a bursty system like destruction coexists with a steady frame rate.

## Phase 3: Cut what is drawn

**Do**
1. Draw fewer things through batched shadows: 1,200 down to 400 at street level.
2. Use occlusion culling: do not render the back face of meshes (author's wording).
3. Put distant systems to sleep: the Ferris wheel sleeps when the player is far away.

**Check**
- Draw-call counts in the per-frame telemetry (Phase 4) drop; street-level scenes are the benchmark because that is where the 1,200-to-400 cut was measured.

**Why**
Rendering is the third cost center after generation and destruction. Batching and culling cut the work the GPU is asked to do at all, and sleeping distant systems is free performance with no visual cost at distance.

## Phase 4: Measure every frame, per system

**Do**
1. Record, every frame: wall time; main-thread time split into process and physics; GPU time (lagging a frame or two); render-thread time; draw calls; awake physics bodies; debris counts.
2. Tag each frame with the system that was working: destruction phases (mesh, crumble, blast, support), city-build pieces, explosions, topples, shader compiles, the crowd, cops, light updates.
3. Keep a per-system CPU split (CpuSplit): microseconds per frame for police, cop cars, crowd, HUD, light pool, juice effects, and the rest.
4. Aim for 16 ms per frame on the main thread and offload everything else to the other cores.

**Check**
- Any regression shows up as a named system in the per-frame record, not as a vague slowdown: the tag says whether it was destruction, city-build, shader compiles, or the crowd.

**Why**
The author frames it as a min-max offloading problem: you cannot budget what you do not measure, and per-system attribution is what turns "it runs like crap" into "the support calculation on worker threads is the bottleneck."

## The human method, distilled
1. "Give every frame a millisecond budget, and spend the spare on the expensive work." (post, Load times section.)
2. "Cap physics by frame... starting to see a pattern here?" (post: the pattern is that every system gets a budget.)
3. "I aim for 16ms per frame on the main thread and to offload everything else to the other cores." (author comment, quoted.)

## Failure modes
- Threaded destruction bugs: the author calls threads "dangerous" and says they lead to "a lot of bugs". Mitigation is the per-frame telemetry in Phase 4, which attributes every hitch to a named system.
- A commenter suggests multi-meshes for rendering speed; the author does not report using them, and the commenter notes they carry "a lot of programmatic overhead if you're not reusing assets like crazy". Treat multi-mesh as an untested suggestion, not part of this workflow.
- One commenter asked whether GDExtension C++ beat C# compiled to a native DLL; the author did not answer with a comparison. Do not claim C++ beats C# here; the claim is only that the C++ rewrite halved load times or better versus the author's own GDScript loops.

## AAA studio practice
Every shipped console game runs on a frame budget with per-system attribution: Unreal, Unity, and Godot all ship profilers that break frame time down by system for exactly this reason. The difference here is that the author built the attribution into the game (per-frame records with system tags) instead of relying on an external profiler, which makes the data available on the Steam Deck itself, where a desktop profiler is not attached.

### Agent automation upgrade (Do / Check / Why)
**Do**
- Add a CI gate that runs the game's heaviest scene headless, dumps the per-frame telemetry to JSON, and fails the build if main-thread time exceeds 16 ms on more than 1% of frames or if any single system's CPU split regresses more than 10% against the stored baseline.
**Check**
- The gate prints the top three regressing systems by name from the frame tags, so the failure points at the system, not at "performance".
**Why**
- The author's method only works if the telemetry is read after every change; a gate turns a habit into a contract.

**Depth status:** FULL (full post text + all 9 comments read firsthand; exact numbers: 10-20 fps before, 16 ms main-thread target, 3 ms destruction budget, load time halved or better by the C++ rewrite, batched shadows 1,200 to 400).
