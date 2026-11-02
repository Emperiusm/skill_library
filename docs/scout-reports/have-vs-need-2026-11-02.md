# Video tooling scout — have-vs-need, 2026-11-02

Run mode: `pre-approved` depth escalation (max 2 media downloads; Ehsan 2026-09-27).
Scans: Reddit (23 subreddits, last 2 days, Arctic Shift API) + YouTube channel
feeds (11 channels, last 2 days). Report date: 2026-11-02.

## Gap alerts

1. **P2 agentic-DCC gap — live evidence.** Magic Studios (Boundless Games,
   r/aigamedev "Free editable sprites and video generation on your own GPU")
   is an *agent-first* asset tool: it ships an MCP server and an API
   "exposed for your local coding agents (Claude Code, Codex, etc.)" so
   agents can drive sprite/video generation reliably. This is the P2 gap
   "MCP-driven DCC loop (agents drive Blender/UE, iterate visually)"
   matched by meaning: a shipped product betting that the agent, not the
   human, is the primary operator of the asset tool. Concrete next step:
   review its MCP/API surface and diff against the existing
   `agentic-blender-asset-pipeline` skill; consider the MCP-for-agents
   pattern for Aegis foundry intake.
2. **P1 perf-budget gap (Aegis) — field evidence, not a fill.** The
   three.js after-dinner prototype (technomeg) ships with a <2 ms/tick
   budget at 400 enemies and golden-test digests (5 seeded scenarios x 600
   steps hashed; refactors must match bit-for-bit). This is exactly the
   discipline the Aegis P1 gap asks for, practiced in the wild. The
   golden-test digest workflow is directly adoptable for Aegis's
   deterministic Rust zone sim (which already has Q16.16 fixed-point).

No tool today fills the Aegis P1 rigging/retarget gap. Magic Studios
*plans* "to include our 3D modeling, rigging, and animation studio" —
future plans only, watch-only.

## Videos scanned

- Reddit: 39 video posts across 23 subreddits (2026-10-31 → 2026-11-02),
  ranked by tooling-relevance x engagement; top 8 tooling-relevant
  candidates deep-analyzed.
- YouTube: 11 channels re-scanned (RyanKingArt, DefaultCube, Ducky3D,
  JoshGambrell, MaxHayArt, BlenderSecrets, GDQuest, KaizenTutorials,
  Brackeys, Entagma, OlivioSarikas); 2 videos in window, 1 in scope.
- Infra note: the channel scan initially failed on all 11 channels with
  SSL CERTIFICATE_VERIFY_FAILED — the sandbox egress proxy CA had rotated
  again and the video-summarizer venv's certifi bundle carried the stale
  CA. Refreshed the appended CA from
  /usr/local/share/ca-certificates/hatch-egress-ca.crt and re-ran; scan
  then succeeded. (Standing AGENTS.md lesson applied.)

## Videos deeply analyzed

| # | Video | Creator | Source | Depth |
|---|-------|---------|--------|-------|
| 1 | "Years of work on one shared procedural voxel world. The engine works. I haven't found the game yet." | rbsolu (INFINITRA) | r/proceduralgeneration post 1xl12dk + 38 comments (post text, 6.3k chars) | PARTIAL (architecture-rich devlog; promised dev video not yet published; author's technical replies were mod-removed) |
| 2 | "How I made my boss turn into silk and tie his ghosts together in Godot 4" | StillEnvironmental64 (game: THE INK TOWER) | r/godot post 1xl7xvc + 31 comments (post text + author's technique replies) | FULL |
| 3 | "We released an UE5 plugin to render Stable 3D Pixel Art (No severe pixel jitter)" | Nuphar_Studio | r/GraphicsProgramming post 1xl3ppu (post text; 0 comments) | FULL (technique) |
| 4 | "Free editable sprites and video generation on your own GPU" (Magic Studios) | ilganeli / Boundless Games | r/aigamedev post 1xll10e + 14 comments | PARTIAL (announcement; no internals) |
| 5 | "Had this game in my mind since i was a kid, built a quick prototype with three.js after dinner." | technomeg | r/threejs post 1xkmn2m + 33 comments | FULL (technique) |
| 6 | "Procedural Marble Sculpt Material (Blender Tutorial)" | Ryan King Art | YouTube (2026-11-01, 1012 s; metadata + description) | DEPTH-LIMITED (YouTube 429 on captions; no node names/parameters) |
| 7 | "How to Use Cel Studio: Anime Cel Shaders in Godot 4 (Quick Start)" | Iconoclaststudios | YouTube (metadata only) + r/godot post | DEPTH-LIMITED (YouTube 429 on captions) |
| 8 | "Houdini Tutorial \| Creating Knitted Fabric in Houdini \| 1. Intro" | DTMGFX | YouTube (99 s; auto-captions retrieved) + r/Houdini post | DEPTH-LIMITED (intro episode only; series not yet published) |

---

## 1. "Years of work on one shared procedural voxel world" (rbsolu / INFINITRA)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xl12dk/ (v.redd.it/nvt806qwnzyh1) | r/proceduralgeneration post 1xl12dk (score 229)

Tools used: C# / Unity (IL2CPP client, .NET server), custom voxel engine (closed source; GitHub richardbogad/INFINITRA reserved for first release), infinitra.xyz (server at www.infinitra.xyz — note: bare domain misconfigured per commenter).

This audit reconstructs the world-generation architecture described in the post, so another agent can apply the same deterministic-world design rules. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: *one shared procedural world defined by a replaceable processing graph, computed identically on every machine from definition + position alone.*

### Phase 1: One replaceable world definition

**Do**
1. Define the entire world as a processing graph of ~2,300 steps: terrain, caves, cities, roads, interiors, object placement with pattern matching.
2. Serve the definition from the server; clients reload it in seconds with no new client build. The same engine runs different worlds.

**Check**
- Swap the definition on the server; every client sees the new world without updating.

**Why**
- Decoupling definition from build turns world iteration into data iteration (author: "The server can replace it all for everyone with no new client build").

### Phase 2: Order-independent point evaluation

**Do**
1. Compute every point from the definition and its position only. A point may query the definition at any other position, but nothing depends on what was generated before or in what order.
2. Store nothing for places nobody changed; items override local geometry to modify the world.
3. Calculate positions and geometry in doubles on both client (IL2CPP) and server (.NET); use 64-bit cell keys. Coordinate space reaches ~1 light year. (Author notes a light year of terrain is not realistic and plans to replace endless terrain.)

**Check**
- Recompute any region in a different order or on a different machine; results must be identical. The server spot-checks a random share of collected items by recomputing them.

**Why**
- Order-independence is what makes server-side verification possible: the server trusts nothing the client computed, it re-derives it (author: "That's the design, and it lets the server spot-check a random share of collected items by recomputing them").

### Phase 3: Geometry networks on bounded windows

**Do**
1. For features needing more than one point, read the land at fixed points in a bounded window anchored to the world, not the player. Every machine needing a road link computes the same window and route.
2. Lava rivers: flow routing on a 25 m lattice; each point drains to its steepest lower neighbour; pits become lakes or get cut through.
3. Roads: route search with bridges, viaducts, tunnels. Hiking trails: route search following contours, switchback climbs, tunneling through ridges only as last resort. Parcels: farm fields and building plots with tracks/streets graded into the ground.

**Check**
- Two machines independently compute the same road link through the same window; routes must match exactly.

**Why**
- Anchoring to the world (not the player) keeps network features deterministic across machines.

### Phase 4: Voxel LOD that preserves detail

**Do**
1. Use 16^3 cells per block at every LOD; 1 m cells at finest; distant blocks cover more ground with the same cell count.
2. Store signed-distance values so coarse grids preserve detail far away; allow sub-metre modifications (thin walls, fences).
3. Never average finer cells into coarse ones; let the distance field decide where to look closer.
4. Anchor objects to the world and place them in a fixed order; a coarse block shows the first ones, so a far object has the same kind, position, rotation, size as on arrival — approaching only adds objects.
5. Natural ground: marching cubes. Buildings/glass: greedy-merged boxes. Where block sizes meet, the finer block conforms to the coarser.

**Check**
- Fly toward a distant structure: it must not pop, change kind, or move — only gain detail (author: "Coming closer only adds objects").

**Why**
- LOD without popping requires the coarse representation to be a strict subset-preview of the fine one, not an average.

### The human method, distilled
1. "The engine is far ahead of the game" — the author is explicit that the unsolved part is gameplay using the strengths (huge shared world, dynamic changes everyone sees); "a simple shooter would use none of that."
2. Invest in verification-by-recomputation rather than trust: deterministic evaluation exists so the server can audit the client.
3. Ship the world as data: ~119k lines engine+server code, 89k lines tests (commenter-noted ratio), but the world itself is a replaceable definition.

**Depth status:** PARTIAL — architecture fully described in the author's post, but the promised development video ("how it's built") is not yet published, and the author's technical comment replies were removed by moderators, so no code-level parameters exist. A media download would add nothing (the Reddit video is a fly-through trailer); the FULL version waits on the dev video.

---

## 2. "How I made my boss turn into silk and tie his ghosts together in Godot 4" (StillEnvironmental64 / THE INK TOWER)

Source: https://www.reddit.com/r/godot/comments/1xl7xvc/ (v.redd.it/bkx0rx8v41zh1) | r/godot post 1xl7xvc (score 559) | game: THE INK TOWER (Steam app 5295020, itch nathannhu/the-ink-tower)

Tools used: Godot 4, 2D vector shapes, custom pixelation shader. Earlier breakdowns in the series: ground slam (r/godot/comments/1x8i8fc), lava (r/godot/comments/1xei4ae).

This audit reconstructs the exact VFX workflow from the author's post and comment replies, so another agent can follow the same process. Every phase has three parts: **Do**, **Check**, **Why**. The video's core method is: *smooth 2D vector shapes with tonal variation, pixelated by a custom shader, animated as dots moving along lines.*

### Phase 1: Find the motion reference in film

**Do**
1. Start from a film reference, not a tool: the author began from the cloth-trails VFX of the monks (tengu) in the movie *47 Ronin*.
2. Prototype the motion crudely first: a spinning cross that leaves a trail, then a cloth dragged behind the character.

**Check**
- The crude prototype should read as "cloth-like motion" before any styling is applied.

**Why**
- Motion first, look second: the author iterated motion ("it started from the cloth trails visual effect... First i tried a spinning cross that leaves a trail, then a cloth dragged behind him") before committing to the pixel look.

### Phase 2: Build the look — vector shapes + pixelation shader

**Do**
1. Draw the effect as smooth vector shapes with different tones to mimic a 3D look (tonal variation fakes volume).
2. Put a custom shader on top that pixelates the whole thing. The game is 2D with a pixel renderer ("Its smooth vector shapes with different tones to mimic the 3d look, and i put a custom shader on top to make it look pixelated"; "Yeah, its 2d with a pixel renderer").

**Check**
- Zoom in: edges should snap to a pixel grid while the underlying shapes stay smooth and re-poseable.

**Why**
- Vector-then-pixelate separates the two hard problems: fluid motion (vectors are cheap to animate) and retro look (the shader imposes the grid). Commenter Vathrik: "Programmatic pixel art is an interesting artistic challenge as you want to add fluidity but not too much shimmer or detail causing visual noise. You nailed the sweet spot."

### Phase 3: Animate silk as dots along lines

**Do**
1. Animate the silk as dots moving along lines ("most of it is moving dots along lines").
2. Render the back half of each strand fainter so the silk reads as round ("the rest is making the back half fainter so it looks round").

**Check**
- Freeze a frame: strands should read as tubes, not ribbons — the faint back half is what sells volume.

**Why**
- A line with a brightness gradient across its width is the cheapest possible tube; dots along the line give flowing motion without simulating cloth.

### Phase 4: Iterate the ghost-cut moment by rejection

**Do**
1. For the money shot (ghosts cutting the silk), try versions and reject by look: the author tried 4 (a piece falling off, a whip, a loose end with rags, a fire running along it) — "none of them looked right, one was like confetti."
2. Ship the version that reads: the coil around a ghost comes off when it attacks, and the loose silk pulls over to the next ghost.
3. Cut scope that delays the move's start: the boss originally dove in and hit at every stop, but the author removed it so "the move start[s] right away."

**Check**
- Each rejected version should fail for a named visual reason (confetti = wrong motion language for silk).

**Why**
- Trial and error with explicit rejection ("it was mostly trial and error") beats planning when the goal is a *feel*; responsiveness (move starts right away) outranks spectacle (extra dive hits).

### The human method, distilled
1. "Because i dont use AI assets?" — hand-made, in response to a commenter suspecting AI from the step-by-step panels.
2. Steal motion from film, not from other games (47 Ronin cloth trails).
3. Reject by look, with the failure named ("one was like confetti").
4. Responsiveness over spectacle: cut the dive so the move starts immediately.

**Depth status:** FULL — technique fully specified by the author in post + comments (motion method, look stack, iteration history). No invented parameters.

---

## 3. "We released an UE5 plugin to render Stable 3D Pixel Art" (Nuphar_Studio)

Source: https://www.reddit.com/r/GraphicsProgramming/comments/1xl3ppu/ (v.redd.it/96c8ea8760zh1) | Fab listing 3a9f54a9-6514-4de7-a212-1955f903061f | tech demo: averdrian0.itch.io/true-pixel-art-3d-tech-demo

Tools used: Unreal Engine 5 (5.6–5.8 per docs site), custom post-process plugin (Fab), itch.io tech demo. Inspired by Project Shadowglass trailers and "the recent 3D pixel art discoveries of Dylan Ebert and Lunar Blank". 3 months of work. Music: "space cadet" by congusbongus.

This audit reconstructs the rendering technique from the author's explainer, so another agent can implement the same stabilization. The video's core method is: *pixelate through slowly-refreshed cubemaps, and hide the staleness with disocclusion.*

### Phase 1: Kill rotation jitter with cubemaps

**Do**
1. Render the game through a post-process that pixelates via cubemaps. Sampling the pixel grid from a cubemap removes the pixel jitter caused by camera rotation.

**Check**
- Rotate the camera in place (first person): pixels should stay locked, no shimmer.

**Why**
- Rotation jitter comes from re-rasterizing the pixel grid every frame; a cubemap lookup decouples the pixel grid from the camera orientation.

### Phase 2: Hide translation staleness with disocclusion

**Do**
1. Recapture the cubemaps at a slow rate (~every 0.25 s) instead of every frame.
2. Apply the disocclusion technique discovered by Lunar Blank / Dylan Ebert to keep the render fluid despite the slow capture rate.

**Check**
- Strafe sideways: motion should look fluid, not steppy at 4 Hz.

**Why**
- Slow capture is what buys the stable pixel look; disocclusion (reprojecting newly-visible pixels) is what buys back fluidity — the two techniques cover each other's weakness.

### Phase 3: Layer by distance with different far-field raymarching

**Do**
1. Layer the render by distance; use a different raymarching method for far/background elements.
2. This solves the disocclusion technique's non-pixel-art edges at distance ("solve the non pixel art edges issue of the disoclusion technique").

**Check**
- Look at the horizon: distant edges should pixelate consistently with the foreground, not go smooth.

**Why**
- Disocclusion breaks down where depth complexity is low and distances are large; a separate far-field path keeps the pixel contract everywhere.

### Phase 4: Dynamic elements via custom depth + stencil, plus "3D billboards"

**Do**
1. Render dynamic elements through a custom depth pass with stencil.
2. Use the author's "3D billboard" technique for applicable elements (details beyond the brief explainer: "(this is a brief explanation, there is a lot more going on)").

**Check**
- Moving characters should pixelate identically to static geometry.

**Why**
- The cubemap path is inherently static-scene-friendly; dynamics need their own pass or they smear.

### The human method, distilled
1. Build on public discoveries, credit them: the plugin started from Project Shadowglass trailers + Ebert/Blank's disocclusion work.
2. Ship the technique as a product: Fab listing + playable tech demo, not just a video.
3. Name the exact capture rate (0.25 s) — the one number that makes the tradeoff concrete.

**Depth status:** FULL (technique) — the author published the method; per-element parameters beyond the explainer are not public. No invented values.

---

## 4. "Free editable sprites and video generation on your own GPU" — Magic Studios (ilganeli / Boundless Games)

Source: https://www.reddit.com/r/aigamedev/comments/1xll10e/ (v.redd.it/0eue5ok7x3zh1) | magicstudios.ai | contact admin@magicstudios.ai

Tools used: ComfyUI + MiniMax H3 packaged as a local app; runs on the user's own NVIDIA GPU (tested 16/24 GB VRAM) or the user's own Higgsfield key (Higgsfield bills; the app adds nothing). MCP server + API for local coding agents (Claude Code, Codex). Signup free (Google or email). App itself planned to be open-sourced.

What it does (author's list): multi-directional sprite animation from an initial 2D image (edit + export); short movies from images + a script, shot by shot; camera flights between location images; screenplay and audio editing/refinement.

Key quotes:
- "This is an agent-first tool, built to give coding agents more reliable results when driving asset generation."
- "The core approach is simple. The video models handle the hard work of interpolation and visual consistency during the motion. This is animation from video not building a 2d/3d model and figuring out rigging."
- "We provide and MCP and an API, exposed for your local coding agents (Claude Code, Codex, etc.)"
- Sweet spot: "480/720 at 32fps to be a pretty good feeling combo"; 1080p "would not be a problem"; 12 GB cards untested but being looked into; Intel/AMD "not tested... I'll take a pass at generalizing."
- Commenter alternative (UnfortunateHurricane): "It is nothing more than a comfyui wrapper using Minimax H3... my fully open source spin on that without anything leaving your PC: https://github.com/fmmix/sprite_h3"

**Depth status:** PARTIAL — product announcement with architecture (packaged ComfyUI+H3, MCP/API, agent-first design) but no internals, no workflow an agent could execute. No skill staged beyond the pattern (see automation/magic-studios-agent-first-sprite-video).

---

## 5. "Had this game in my mind since i was a kid" — three.js after-dinner prototype (technomeg)

Source: https://www.reddit.com/r/threejs/comments/1xkmn2m/ (v.redd.it/7y8kkhlakvyh1) | playable: operationelsewhere.com | Boxhead-style co-op arena shooter, Three.js + TypeScript + Vite. All code "vibed with Opus 5.5 as lead/reviewer, with Grok on the sim gameplay and cameras."

This audit reconstructs the exact engineering workflow from the author's post, so another agent can follow the same process. Every phase has three parts: **Do**, **Check**, **Why**. The video's core method is: *headless deterministic sim over typed arrays, rendered by interpolation, with crowds faked cheaply and correctness locked by hashed golden tests.*

### Phase 1: Split sim from render

**Do**
1. Run the game sim headless at a fixed 60 Hz step (120 Hz optional) over plain typed arrays (SoA). No Three.js inside the sim.
2. Have the renderer read the buffers and interpolate between previous and current step, so motion stays smooth on 120 Hz displays.
3. Step projectiles *back* along their flight instead of extrapolating forward. (Measured failure: "Extrapolating drew rockets up to ~33 cm inside the wall they were about to hit.")

**Check**
- Rockets must never render inside walls; 120 Hz displays must show smooth motion from a 60 Hz sim.

**Why**
- The sim stays deterministic and testable; the renderer owns smoothness. Backstepping projectiles trades one frame of latency for zero tunneling artifacts.

### Phase 2: Render the horde in 7 draw calls

**Do**
1. Build each enemy from 7 InstancedMeshes (head, eyes, torso, 2 legs, 2 arms) — 7 draw calls no matter the enemy count.
2. Compose matrices by hand straight into the instance arrays; no Object3D per enemy.

**Check**
- Draw calls stay at 7 from 10 to 400+ enemies.

**Why**
- Per-enemy scene-graph nodes are the classic three.js perf cliff; instancing with hand-composed matrices removes it.

### Phase 3: Fake the crowd with flow field + spatial hash

**Do**
1. Flow field toward the players + spatial hash for separation + a relaxation pass so bodies don't overlap.
2. Give each enemy its own slot on a ring around its target, so they surround the player instead of forming a conga line.

**Check**
- Enemies should encircle, not queue.

**Why**
- Ring slots turn "N seekers, 1 target" from a traffic jam into an encirclement with O(1)-ish per-enemy cost.

### Phase 4: Budget the tick, lock correctness with golden tests

**Do**
1. Measure: sim step 0.23 ms at 400 enemies; keep a <2 ms per-tick budget at 400. (Next target: move the ~180 KB/frame CPU instance upload to the GPU.)
2. Before refactoring the sim, record 5 seeded scenarios x 600 steps hashed into digests; every refactor since must match bit for bit.

**Check**
- Any sim refactor that changes a digest is a behavior change, not a refactor — reject it.

**Why**
- "We live in an incredible time" (author, on AI-assisted coding): when the code is vibed, hashed golden tests are what keep refactors honest. The author is explicit the whole thing was AI-written with Opus 5.5 as lead/reviewer.

### The human method, distilled
1. "because I had plenty usage left. Codex was gone and claude was like 20% left" — model choice was opportunistic, not principled; Opus 5.5 led, Grok did sim/cameras.
2. The game setup comes from "my childhood daydream boardgame" — the design predates the tooling.
3. Perf feedback requested with GPU/browser specified — measurement is part of the dev loop.

**Depth status:** FULL — concrete architecture, numbers, and the golden-test discipline, all from the author.

---

## 6. "Procedural Marble Sculpt Material (Blender Tutorial)" (Ryan King Art)

Source: https://www.youtube.com/watch?v=kRiI5zZjlbo | 1012 s (16:52) | uploaded 2026-11-01. Description timestamps: Intro 0:00, Scene Setup 2:46, Procedural Setup 4:27, Node Group 9:56. Project files on Gumroad/Patreon; companion sculpting tutorial https://youtu.be/-CUyPta7-IU.

**Depth status:** DEPTH-LIMITED — YouTube rate-limited caption downloads (HTTP 429, treated as hard stop for that scope this run), so no node names, parameters, or values are available. Metadata confirms it is a procedural shader-node marble material with a node-group organization step. A media download (pre-approved allowance) was not attempted: the 429 was on YouTube's own subtitle endpoint and a media fetch would ride the same throttled path. No skill staged.

## 7. "How to Use Cel Studio: Anime Cel Shaders in Godot 4 (Quick Start)" (Iconoclaststudios)

Source: https://youtu.be/zWKW3E9YfBM | r/godot post 1xlcsky by Sad_Library123 ("Custom Anime Cel Shaders live in the Godot Engine", score 26).

Tools used: Cel Studio — a Godot 4 add-on for anime cel shading (quick-start video).

**Depth status:** DEPTH-LIMITED — same YouTube 429 on captions; only the title/add-on identity is established. Relevance: 2d3d's inventory cites a toon-ramp law in its (missing) art bible but has no cel-shader add-on; this is a watchlist candidate for that slot. No skill staged (no extractable workflow).

## 8. "Houdini Tutorial | Creating Knitted Fabric in Houdini | 1. Intro" (DTMGFX)

Source: https://www.youtube.com/watch?v=kETBv7j3POs | 99 s | r/Houdini post 1xlj506 by Wide-Power4327 ("Houdini Tutorial | Creating Knitted Fabric in Houdini | 1. Intro", score 31). Auto-captions retrieved.

Announced plan (from captions): (1) study real knitted-fabric construction, (2) build base geometry with trigonometry (sine/cosine functions), (3) animate via a cloth simulation solver, (4) use "the volume solver" for the simulation, (5) detail pass: stray fibers, individual fiber thickening, render prep, (6) assemble in Solaris (materials, lights, cameras), render with Karma.

**Depth status:** DEPTH-LIMITED — this is the series intro; the actual tutorial episodes are not published yet. Pairs with the 2026-10-23 watchlist row "Houdini fabric/knitted-asset HDA" (different item, same topic). No skill staged.

---

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Deterministic evaluation enabling server spot-checking (recompute-to-verify) | #1 INFINITRA | PARTIAL | Aegis has deterministic Rust zone sim w/ Q16.16 fixed-point (`crates/zone`), but no recompute-to-audit-client pattern | backlog: adopt the spot-check-by-recomputation idea for anti-cheat/audit |
| Per-tick perf budgets + hashed golden tests | #5 three.js prototype | NEED | No per-asset performance budgets (P1 gap, verified absent) | **adopt now (practice): golden-test digest workflow (5 seeded scenarios x 600 steps hashed) fits the existing deterministic sim** |
| MCP/API for coding agents driving asset generation | #4 Magic Studios | NEED | No MCP-driven DCC loop (P2 gap) | watchlist: review MCP surface vs `agentic-blender-asset-pipeline` skill |
| Stable 3D→pixel-art rendering (cubemap + disocclusion) | #3 UE5 plugin | NEED | No pixel-art render stage; foundry is TRELLIS→UE, no pixel path | skip for Aegis (UE client is the separate Aetheria repo; pixel-art not its style) |
| Vector-shape VFX + pixelation shader | #2 silk VFX (Godot) | NEED | No 2D/VFX pixel pipeline in foundry | skip for Aegis (not its art direction) |
| Procedural marble shader material | #6 RyanKingArt | NEED | No material-authoring stage (PBR import policy also absent) | watchlist (materials bucket) |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Vector shapes + custom pixelation shader for VFX | #2 silk VFX | PARTIAL | HAVE `pipeline/pixelize` (asset pixelation) but no runtime vector-shape VFX method | **backlog: the dots-along-lines + back-half-fainting technique is directly reusable for 2d3d's 2D/3D hybrid VFX** |
| Stable 3D→pixel-art rendering (cubemap + disocclusion) | #3 UE5 plugin | NEED | No 3D→pixel render path; 2d3d renders 2D with 3D camera rotation | watchlist: disocclusion idea transfers if 2d3d ever pixelates 3D views |
| Anime cel-shader add-on (Godot 4) | #7 Cel Studio | NEED | Toon-ramp law cited for the (missing) art bible; no cel-shader add-on | watchlist: candidate for the toon-look slot |
| Deterministic world definition as replaceable data | #1 INFINITRA | NEED | 2d3d has seeded procgen (`pipeline/proc`) but no server-replaceable world definition | skip (2d3d is single-player; no server) |
| Golden-test digest workflow | #5 three.js prototype | PARTIAL | HAVE golden-path bot (61.8 s, 0 falls) + 198 QA gates | backlog: hash-based digests would harden the existing golden-path bot |
| Agent-driven asset generation via MCP | #4 Magic Studios | NEED | No MCP-driven DCC loop | watchlist |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Geometry networks (route search on lattice, graded parcels) | #1 INFINITRA | NEED | HAVE `tools/procedural_art.py`, `tools/city_*` families, but no route-search street/parcel networks described | **backlog: lava-river flow routing + road route-search is a pattern candidate for street/parcel generation** |
| Deterministic recomputation | #1 INFINITED | NEED | Seeded procgen probes exist (`tools/procgen_*`) | watchlist |
| Headless-sprite / asset-diet discipline | #5 three.js (7 draw calls, instancing) | NEED | HAVE sprite contract + decoded-memory bounds (PRD 17.2) | HAVE-adjacent: the 7-draw-call discipline evidences the existing standard; no action |
| Shader-driven skyline fill | — | NEED | P1 gap, still absent | unchanged; INFINITRA's distance-layered far-field rendering (#3's cousin idea) is a watchlist angle for far-city rendering |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Deterministic topology via recomputation | #1 INFINITRA | PARTIAL | HAVE "Deterministic topology via VDBs + math" | HAVE: INFINITRA's order-independence rule is the same principle, already practiced |
| Per-class export profiles / budgets | #5 three.js tick budgets | NEED | P1 gap: Godot import gate + re-measured export budgets still open | backlog: the <2 ms/tick + digest discipline is evidence for the budget culture the gap asks for |
| Pixel-art / cel rendering | #3, #7 | NEED | No pixel/cel path; concept-PNG-as-authority pipeline | skip (not its art direction) |
| MCP-driven DCC | #4 Magic Studios | NEED | Blender pipeline stages are scripted, not agent-driven | watchlist |

## Watchlist trending (corrected)

The auto-matcher ran with token-overlap and produced 21 false-positive
"seen again" annotations (e.g. matching "Scalable Vector Shapes 2D" on the
word "vector" in the silk-VFX tool string); all 21 were reverted in
`references/tooling-watchlist.md`. The one genuine reappearance:

- **material-painter** (free open-source Substance Painter alternative,
  Admirable-Struggle78) — first seen 2026-11-01, seen again 2026-11-02
  (r/3Dmodeling repost, score 309, 71 comments; already audited 2026-11-01,
  skill staged then).
- "Four generated worlds on a cube-sphere" (chronicleofgods, audited
  2026-11-01) also re-surfaced in this window's scan; no new information.

9 new rows appended to `references/tooling-watchlist.md` (INFINITRA,
silk-VFX, UE5 pixel-art plugin, Magic Studios, sprite_h3, three.js
sim/render split, Cel Studio, marble material, knitted-fabric intro).

## Gap recommendations (highest leverage)

1. **Golden-test digests for Aegis's deterministic sim (adopt now).** The
   three.js prototype's "5 seeded scenarios x 600 steps hashed, refactors
   must match bit-for-bit" is a concrete, cheap practice that fits Aegis's
   existing Q16.16 fixed-point zone sim. Next step: prototype a digest
   harness over `crates/zone` scenarios.
2. **Magic Studios MCP pattern vs the P2 agentic-DCC gap (evaluate).**
   Review the MCP/API surface at magicstudios.ai; diff against the
   `agentic-blender-asset-pipeline` skill. If the MCP contract is clean,
   it becomes the reference design for agent-driven Aegis foundry intake.
3. **Silk-VFX vector method for 2d3d (backlog).** Dots-along-lines with
   back-half fainting + a pixelation shader is a runtime VFX technique
   2d3d's pixel pipeline doesn't have. Cheap to prototype in Godot.
4. **INFINITRA geometry networks for Desktop City streets (backlog).**
   Flow-routing on a lattice + route-searched roads with bridges/viaducts
   is a stronger street/parcel model than the current city_* families.
5. **UE5 cubemap+disocclusion pixel rendering (watchlist).** Engine-specific
   today, but the disocclusion-for-slow-capture idea is the transferable
   core if any repo ever pixelates 3D views.

## Explicit non-goals

- "New MiniMax H3 Singularity V2" (r/comfyui, cgpixel23): H3 workflows
  already covered 3x in the watchlist; no new workflow detail. Skipped.
- "My Cartoon Furniture Ultimate Pack Finally Come With Godot Support!"
  (r/godot, Solegame_10): asset-pack announcement, no workflow. Skipped.
- "I finally reached the launch stage..." (r/godot, Bridgelands):
  launch news, no tooling. Skipped.
- "my buddy's 1-bit ruins had a giant skull in them, so i put it on mocap"
  (r/proceduralgeneration gif): fun, no tooling detail. Skipped.
- "Nodevember 1 - Origami" (r/blender, Molto-Accelerando): 361-char post,
  0 comments. One nugget: author claims no mesh-bisect node exists in
  Geometry Nodes (unverified). Too thin to audit.
- "Which Voice Typing app is Worth your money?" (Olivio Sarikas):
  not game-pipeline relevant. Skipped.
- material-painter and cube-sphere posts: already audited 2026-11-01;
  counted as reappearances above.

## Depth-escalation usage

- Mode: `pre-approved`, allowance 2. **Downloads attempted: 0,
  succeeded: 0, skipped: 0.** Captions/metadata came first per the hard
  rule; both YouTube caption fetches that mattered (cel-shaders, marble)
  hit YouTube HTTP 429 and were treated as a hard stop for that scope —
  the audits were marked DEPTH-LIMITED instead. The knitted-fabric
  captions downloaded cleanly before the throttle began.
- skill_library artifacts staged: 5 new skills (see below), full report
  copy under `docs/scout-reports/have-vs-need-2026-11-02.md`.

## skill_library staging

- `skills/procgen-worlds/infinitra-deterministic-voxel-world/`
- `skills/simulation-vfx/godot-silk-vfx-vector-pixelation/`
- `skills/engine-runtime/ue5-stable-3d-pixel-art-rendering/`
- `skills/engine-runtime/threejs-sim-render-split-horde/`
- `skills/automation/magic-studios-agent-first-sprite-video/`
- Watchlist rows synced to the repo mirror
  `video-tooling-scout/references/tooling-watchlist.md`; skill counts and
  grouped tables in `skills/README.md` + root README updated.
