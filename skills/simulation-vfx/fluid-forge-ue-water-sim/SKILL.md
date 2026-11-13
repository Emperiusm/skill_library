---
name: fluid-forge-ue-water-sim
description: "Add real-time water to Unreal Engine with Fluid Forge 1.0 (FAB): a pouring/running water sim in a bounded area plus an 'infinite' mode that follows the player with preplaced rivers, lakes, puddles, and sea, an ocean for coastlines, liquid metal and slime examples, and a voxel visualization layer. Setup is two Blueprints and Play, after enabling Generate Mesh Distance Fields and Niagara Static Mesh DI Allow Distance Fields. Includes the author's positioning against Fluid Flux and Fluid Ninja and the missing-benchmark caveat. Trigger when a game or cinematic needs real-time water in UE and the frame-time cost is still unproven."
---

# Fluid Forge: Real-Time Water Simulation in Unreal Engine

## Purpose

This skill reconstructs the Fluid Forge setup workflow from the author's post, comments, and the downloaded launch trailer's frames, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: drop in two Blueprints, press Play, and let the water simulate around the player.

## Source

Creator: Atomic_Lighthouse. Reddit post:
https://www.reddit.com/r/unrealengine/comments/1xtkm7d/fluid_forge_is_finally_on_fab/
(r/unrealengine post 1xtkm7d, score 25, 9 comments) | YouTube launch trailer:
https://youtu.be/T8kk4FXooGw (60 s, 289 views, no captions; downloaded and 12 frames reviewed) | 2026-11-12 scout run, audit 6. FAB listing:
https://www.fab.com/listings/76bc0615-6364-4cec-834b-cde1ec80696f
Basic setup tutorial: https://youtu.be/esu04sWptIE

This is a distinct tool from the Tideglass web fluid sim skill (`tideglass-fluid-sim`): Fluid Forge is an Unreal Engine plugin for games and cinematics, not a browser app. Do not merge them.

## Tools used

**Fluid Forge 1.0** (Unreal Engine plugin, on FAB), **Unreal Engine Blueprints**; requires **Generate Mesh Distance Fields** (Engine - Rendering - Software Ray Tracing) and **Niagara Static Mesh DI - Allow Distance Fields** (Plugins - Niagara).

## Phase 1: Enable the required project settings

**Do**
1. In your project, activate: Engine - Rendering - Software Ray Tracing - Generate Mesh Distance Fields.
2. Activate: Plugins - Niagara - Static Mesh DI - Allow Distance Fields.
3. The author notes this information was left out of the published FAB listing and will be updated soon; without these settings the plugin will not work as shown.

**Check**
- If the sim does not appear, check these two settings first. They are the documented prerequisite, not a troubleshooting guess.

**Why**
- Distance fields are how the sim knows where the solid world is. No fields, no collision, no water.

## Phase 2: Drop in the sim and press Play

**Do**
1. Drop in a couple of Blueprints and press Play; the author states "you can get the main sim running by just dropping in a couple of blueprints and pressing Play."
2. Choose the sim mode: a bounded simulation area for pouring/running water, or the "infinite" mode, in which the simulation follows the player and the developer preplaces water in the world (rivers, lakes, puddles, the sea). The size of the simulation is user-definable.
3. Add the ocean for coastlines, with waves interacting with the shore. The author is explicit that the ocean "has not been the main focus of the plugin" and is "definitely something that I will improve for future versions, with the goal of having a hyper realistic ocean."

**Check**
- Frames reviewed from the downloaded trailer: a waterfall/river running between rocks; an editor view showing the bounded sim area as a blue water region with white voxel-like particles and a transform gizmo; an ocean surface with sun reflection. The demo map is "made for ease of use and clarity, not beauty" (author).
- The trailer is a showcase, not a tutorial; the setup steps above come from the post text, not from the video.

**Why**
- The infinite mode is the design decision that matters: instead of simulating the whole world, simulate only the water near the player. That is what makes a fluid sim affordable in a game.

## Phase 3: Tune and extend

**Do**
1. Move emitters around, turn water on and off, flood a section (author, in comments: "Yes. You can move emitters around, turn on/off water, flood a section and such.").
2. Use the liquid metal and slime examples for non-water fluids.
3. Add the voxel visualization layer for local water effects in voxel worlds; it is "very easy to add" but "not currently compatible with the infinite sim area."
4. For indoor simulations: the sim uses a heightmap, but you can exclude meshes, use RVTs, or set the height of the simulation below the roof (author, in comments).

**Check**
- Commenters asked for the comparison that matters: benchmarks against Fluid Flux and Fluid Ninja (resource requirements, effect on frame time) and a fair one-to-one demo (same map, same mountain, same floating object). The author has not published benchmarks; the comparison is open. The author's own positioning: "function wise Forge does mostly the same stuff [as Flux], but with a different look (and much simpler setup as far as I can tell)", plus the moving player-following simulation "like in Crimson Desert".
- The basic setup tutorial is at youtube.com/watch?v=esu04sWptIE; more tutorials were promised "in the following days."

**Why**
- A fluid sim is bought on frame time, not on looks. Until the Flux/Ninja benchmark exists, the honest recommendation is "simpler setup, unproven cost."

## The human method, distilled

1. Make the first run two Blueprints and Play; tuning comes after the sim exists.
2. Simulate only the water near the player; preplace the rest.
3. Ship the ocean as a secondary feature and say so, rather than overselling it.

## AAA studio practice

Fluid Forge's architecture is the shipped-title architecture: a 2D shallow-water grid projected on a heightfield, simulated only where the player is, with the frame-time cost as the buying criterion.

- **Fluid Flux in Senua's Saga: Hellblade II.** Fluid Flux is a real-time shallow-water simulation for UE5 whose simulation is calculated on a 2D grid projected on the captured ground heightfield, with fixed axis-aligned simulation areas (multiple sims for separate areas, at a cost), a cheap ripple solver that moves with the character, advected foam and caustics, and a Niagara fluid async readback system for sampling height and flow in Blueprints. Its project list includes Senua's Saga: Hellblade II.
  (https://forums.unrealengine.com/t/imaginaryblend-fluid-flux/2420009)
  The direct parallel: Fluid Forge's heightmap-based sim with a player-following infinite mode is the same architecture with the fixed areas replaced by a moving one, and the same tradeoff (area size vs GPU cost) governs both.
- **Crimson Desert (Pearl Abyss, 2026).** Former Rockstar artist David O'Reilly, who worked on Red Dead Redemption 2's water physics, called Crimson Desert's water a step above RDR2's fluid mechanics, describing it as effectively a live particle simulation in creeks and rivers, while noting minor inconsistencies he attributed to a bug or an optimization choice.
  (https://www.notebookcheck.net/Former-Rockstar-Games-artist-Crimson-Desert-s-water-physics-better-than-Red-Redemption-2-s.1257889.0.html)
  The direct parallel: the player-following sim is the same idea at a different scale, and O'Reilly's "bug or optimization choice" caveat is the standard the benchmark must meet: report the cost with the artifact attached.

**Agent automation**

1. **Benchmark manifest.** Keep `fluid-forge-benchmark.json` per test: map, sim resolution, sim area size, frame time with the sim off, frame time with the sim on, and object count in the sim. A check asserts every number is measured on the same map; a frame-time claim from a different map is not a comparison.
2. **One-to-one comparison protocol.** Build the commenters' fair demo as a scripted procedure: the same map, the same mountain, the same floating object, run once in Fluid Forge and once in Fluid Flux (and Fluid Ninja if available), recording the same manifest fields for each. The comparison is only valid when the map and object are identical.
3. **Sim-area budget table.** Record the resolution-to-cost table (e.g. 512x512 vs 1024x1024 grid) with measured frame times, so the "user-definable size" choice is a budget decision, not a guess.
4. **Settings preflight check.** Before the first Play, assert both required project settings are enabled (Generate Mesh Distance Fields; Niagara Static Mesh DI Allow Distance Fields) and log them in the manifest. If the sim does not appear, the preflight log is the first thing checked, not the Blueprints.

**Depth status:** PARTIAL (downloaded trailer + 12 frames reviewed + full post text + 9 comments; no captions exist for the trailer; no tutorial content in the video itself; no benchmarks published).
