---
name: infinitra-deterministic-voxel-world
description: "Design a deterministic shared procedural voxel world: replaceable processing-graph definition, order-independent point evaluation, geometry networks, SDF-preserving LOD. Trigger when building server-authoritative procedural worlds."
---

# I'm building a deterministic shared voxel world

## Purpose

This skill reconstructs the exact world-generation architecture described by the INFINITRA developer (rbsolu), step by step, so another agent can apply the same deterministic-world design rules. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: *one shared procedural world defined by a replaceable processing graph, computed identically on every machine from definition + position alone.*

## Source

Creator: rbsolu (INFINITRA; C# / Unity since 2017)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xl12dk/ | r/proceduralgeneration post 1xl12dk (score 229, 2026-11-01) | video: fly-through trailer (v.redd.it/nvt806qwnzyh1)

Expanded 2026-11-06 with the author's second, fuller writeup: https://www.reddit.com/r/unity/comments/1xnvj49/years_of_work_on_one_shared_procedural_voxel_world/ | r/unity post 1xnvj49 (score 26, 11 comments, all retrieved) | trailer https://youtu.be/_q_Wmsdp2ng, long flight https://youtu.be/LjluoZq5hhY, site https://www.infinitra.xyz, dev pictures https://www.infinitra.xyz/docs/dev/PROGRESS.html. The expansion adds the gameplay/item systems with exact numbers, the pop-in defect and its root cause, and the download status.

Depth: PARTIAL — architecture fully described in the author's posts; the promised "how it's built" dev video is not yet published and no code-level parameters exist.

## Tools used

C# / Unity; IL2CPP on the client, .NET on the server; custom closed-source voxel engine (GitHub richardbogad/INFINITRA reserved for first release); server at infinitra.xyz. Scale: ~119k lines engine + server code, 89k lines tests. Runs on a 5-year-old laptop at lowest detail. Desktop and PC VR share the same world. Download not out yet (waiting for its code-signing certificate to be approved); it will be a free Windows download, whole world locally with no account, online features (saved locations, items, avatar, other players) behind the account.

## Phase 1: Define the world as one replaceable processing graph

**Do**
1. Define the entire world as a processing graph of ~2,300 steps: terrain, caves, cities, roads, interiors, and object placement with pattern matching.
2. Serve the definition from the server. Clients reload the new definition in seconds with no new client build.
3. Keep the engine world-agnostic: the same engine binary runs different worlds.

**Check**
- Swap the definition server-side; every client sees the new world without updating.

**Why**
- Decoupling definition from build turns world iteration into data iteration (author: "The server can replace it all for everyone with no new client build").

## Phase 2: Make point evaluation order-independent

**Do**
1. Compute every point from the definition and its position only. A point may query the definition at any other position, but nothing may depend on what was generated before or in what order.
2. Store nothing for places nobody changed. Let items override local geometry — that is how the world gets modified.
3. Calculate positions and geometry in doubles on both client and server; use 64-bit cell keys. [inference]: the IL2CPP-vs-.NET split means you must pin down floating-point behavior — the author states "both calculate positions and geometry in doubles" as the mechanism that makes cross-runtime results match.

**Check**
- Recompute any region in a different order, or on a different machine: results must be identical. The server spot-checks a random share of collected items by recomputing them (author: "That's the design, and it lets the server spot-check a random share of collected items by recomputing them").

**Why**
- Order-independence is what makes server-side verification possible: the server trusts nothing the client computed, it re-derives it. This is the anti-cheat/audit primitive.

## Phase 3: Build geometry networks on world-anchored windows

**Do**
1. For features needing more than one point (rivers, roads, trails, parcels), read the land at fixed points in a bounded window **anchored to the world, not the player**. Every machine that needs a road link computes the same window and route.
2. Lava rivers: flow routing on a 25 m lattice — each point drains to its steepest lower neighbour; pits become lakes or get cut through.
3. Roads: route search with bridges, viaducts, tunnels. Hiking trails: route search that follows contours, climbs in switchbacks, and tunnels through a ridge only as a last resort. Parcels: farm fields and building plots with tracks and streets graded into the ground.

**Check**
- Two machines independently compute the same road link through the same window; the routes must match exactly.

**Why**
- Anchoring to the world (not the player) keeps network features deterministic across machines; bounded windows keep the computation finite.

## Phase 4: Use SDF-preserving voxel LOD

**Do**
1. Use 16^3 cells per block at every LOD; 1 m cells at the finest; distant blocks cover more ground with the same cell count.
2. Store signed-distance values so coarse grids preserve detail far away. Allow sub-metre modifications (thin walls, fences).
3. Never average finer cells into coarse ones — let the distance field decide where to look closer.
4. Anchor objects to the world and place them in a fixed order; a coarse block shows the first ones. A far object keeps the same kind, position, rotation, and size as when you arrive — approaching only adds objects.
5. Natural ground: marching cubes. Buildings and glass: greedy-merged boxes. Where block sizes meet, make the finer block conform to the coarser one.

**Check**
- Fly toward a distant structure: it must not pop, change kind, or move — only gain detail (author: "Coming closer only adds objects").

**Why**
- LOD without popping requires the coarse representation to be a strict subset-preview of the fine one, not an average. SDFs carry the detail the coarse grid cannot.

## Phase 5: Build gameplay on the shared world (2026-11-06 post)

**Do**
1. Explore as a walker or a drone; neither flies without a JetPack. The drone has twice the battery and half the gravity, and survives harder falls.
2. Drain battery by distance and mass: about 33 km on a full walker charge, 25 km on a drone's. An empty battery means quarter speed and slowly lost health. Falls and lava cost health. When you die, what you carried drops where you fell.
3. Add shared items, all visible to everyone: JetPack (one minute of flight, also saves you mid-fall); First Aid (restores 25 health); Energy Pack (restores 25 kWh of battery); Gps & Compass (shows position and bearing until switched off); Location Saver (saves position to a slot, teleport back later); Carver Sphere (the only item that changes the world so far: cuts a 10 m wide hole for about a minute, for everyone; if you're still inside when it closes, you die).
4. Respawn collected items after 30 to 60 seconds. Start all new online players in the same 500 m square. No chat yet.
5. Add procedural music and reverb measured from the space around you.

**Check**
- Every item action must be visible to every player, not just the actor; the Carver Sphere hole must appear for everyone and kill anyone still inside when it closes.

**Why**
- The engine's strength is a huge shared world with dynamic changes everyone sees; the gameplay has to use that strength, which is why the author rejects a simple shooter ("A simple shooter would use none of that"). The Carver Sphere is the proof-of-concept: one item, one shared world change, everyone affected.

## Phase 6: Handle the known defect — pop-in (2026-11-06 post + comments)

**Do**
1. Expect object pop-in: the author states the root cause plainly (comment): "the object density needs to be reduced over larger distances. This causes objects to appear as you move closer to them."
2. In real time, fade objects in more gradually; the time-lapse videos make the pop-in much more noticeable.
3. A time-lapse-adjusted crossover effect exists, but the same adjustment has not been implemented for the fade-in yet.

**Check**
- Watch a real-time (non-time-lapse) fly-through: the fade-in should be gradual, not a hard appear. A commenter flagged the pop-in at the very start of the video as "super bad" — treat that as the acceptance test.

**Why**
- The defect is a density-over-distance rule, not a rendering bug: far blocks show fewer objects by design (Phase 4), so the transition has to be a fade, and the fade has to be tuned separately for real-time and time-lapse viewing.

## AAA studio practice

- **Hello Games (No Man's Sky) — GDC 2017, Innes McKendrick.** McKendrick's GDC talk breaks down the continuous world-generation pipeline: voxel-based world generation, then polygonization and texturing, then population and simulation, all generated continuously in real time as the player moves from space down to the surface. Source: https://www.gamedeveloper.com/programming/video-how-continuous-world-generation-works-in-i-no-man-s-sky-i-
- **Hello Games — deterministic universe from one seed.** No Man's Sky computes nearly everything through deterministic algorithms from a single 64-bit seed: a star's position seeds its planetary system, each planet's position seeds its features, and so on down the hierarchy. Very little is stored on servers; every machine derives the same elements by recomputing them when the player is near, which is why two players visiting the same location see the same world. This is the shipped-AAA version of "computed identically on every machine from definition + position alone." Source: https://alchetron.com/Development-of-No-Man%27s-Sky

Agent-executable upgrades this research unlocks:

1. **parity-harness.json** — a manifest of (seed, region, expected-digest) entries. A CI job recomputes each region on a different runtime/architecture and fails on any digest mismatch, turning "recompute any region on a different machine" from a manual check into an automated gate. The server's random spot-check of collected items becomes a configured sampling rate in the same manifest.
2. **Float-behavior audit** — the IL2CPP-vs-.NET split is the same hazard that forced Rocket League-era determinism patches between processor types. Pin the audit to the manifest: declare the precision envelope (doubles, 64-bit cell keys) and add a cross-runtime digest entry so drift is caught by the harness, not by players.

## The human method, distilled

1. "The engine is far ahead of the game" — the author is explicit that the unsolved part is gameplay that uses the strengths (one huge shared world, dynamic changes everyone sees); "a simple shooter would use none of that." Build the tech for the game it enables, and admit when the game is not found yet.
2. Invest in verification-by-recomputation rather than trust: determinism exists so the server can audit the client.
3. Ship the world as data: the world is a replaceable definition, the engine is a fixed evaluator.
4. [inference] Test volume follows from determinism: 89k lines of tests against 119k lines of engine code is affordable because every test is a recomputation check.

## Failure modes

- **Author's own caveat:** "A light year of terrain isn't realistic, so I plan to replace the endless terrain with something else." Do not copy the 1-light-year coordinate space as a feature; the author considers it a placeholder.
- **Moderated-away detail (2026-11-01 post):** the author's technical comment replies were removed by moderators; treat any parameter not in the post text as unknown.
- **Pop-in is a known, unfixed defect (2026-11-06 post):** the fade-in adjustment for real-time viewing is not implemented; time-lapse videos exaggerate it. Do not present the fly-throughs as the real-time experience.

**Depth status:** PARTIAL (post-text architecture + gameplay systems with exact numbers; dev video pending; no code-level parameters)
