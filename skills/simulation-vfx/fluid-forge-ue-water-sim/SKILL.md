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

**Depth status:** PARTIAL (downloaded trailer + 12 frames reviewed + full post text + 9 comments; no captions exist for the trailer; no tutorial content in the video itself; no benchmarks published).
