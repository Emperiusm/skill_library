---
name: mass-entity-niagara-crowd
description: "Render massive UE crowds without per-agent actors: simulate in custom C++ MassEntity processors, stream transform arrays into Niagara GPU particles, animate with VATs. Trigger when building RTS/battle crowds, swarm renders, or agent visualizations in Unreal."
---

# MassEntity to Niagara Crowd Rendering (Mass Battle recipe)

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle). The core method is:
separate brains from bodies. Simulate everything on the CPU in custom MassEntity
processors (AI, movement, collision), stream agent transforms as data arrays into
Niagara, and let Niagara spawn, move, and render GPU particles while Vertex Animation
Textures pick the animation per agent state.

## Source

Creator: LeroyWorks (Reddit: JollyGarden5354)

Source: https://www.youtube.com/watch?v=eUOZfDG9VA4 (401 s) | r/unrealengine post
1wta7oe (score 81, 28 comments) | "This is what happens when you optimize Unreal Engine
to the limit"

Caution: the video is the creator's own product demo. **Mass Battle** is a crowd
framework listed on Fab (fab.com/listings/191850b4-44d3-4455-aa76-874bc0196a10). The
thread techniques are the creator's stated method and are reproduced here as stated;
performance figures are vendor claims and are marked as such.

## Tools used

Unreal Engine, MassEntity framework (custom C++ processors), Niagara GPU particles,
Vertex Animation Textures (VATs), custom hash grid + spatial queries, RVO2 /
force-based avoidance, hybrid pathfinding (cell grid + multi-layer navmesh; flow field
for crowds, A* for individuals), deterministic lockstep replication (Fix64 math lib)

## Phase 1: Build the agent brain in MassEntity (custom C++ processors)

**Do**
1. Use no actors or characters. Agents are MassEntity entities only: "They are mass
   entities, visualized via niagara gpu paticles" (creator, spelling as posted).
2. Write custom MassEntity processors in C++ for movement, collision, and AI: "The
   movement and collision is handled by custom written mass entity processors"; "The ai
   logic is coded in a mass processor in c++."
3. Build your own spatial queries: a custom hash grid plus spatial query, with custom
   avoidance on top.
4. Resolve collisions as a cheap final pass, not the main event: "a simple custom
   single iteration capsule vs capsule PBD collison resolving with the neighbors as
   well. The result proves worthy. The additional cost is negligable."
5. Pathfinding, hybrid: cell grid and nav mesh (multi-layer); flow field for the crowd,
   A* for individuals.
6. Movement: RVO2 or force-based avoidance plus traffic rules; support flying, falling,
   and uneven surfaces; align to ground normal; pitch/bank with velocity; group masks.
7. Tasks as async building blocks: GenerateFormation, AgentsMoveTo, AgentsChaseAttack,
   with "smart bubble packing" for clean formation transforms.

**Check**
- Agents avoid each other and resolve overlaps without popping or exploding.
- Profile the PBD pass to confirm the "negligable" cost claim in your own scene; the
  spread between scenes is where optimization lives.
- The governing principle, quoted from a practitioner in the thread: "doing avoidance
  is vastly cheaper than doing actual Collison if you can avoid it. Collision is very
  expensive. We basically used no collision at all and set up our own spatial partition
  graph for doing things like sphere or box queries when we needed to check for things
  hitting the entities."

**Why**
Avoidance first, collision last. Full collision for tens of thousands of agents is the
bottleneck; a spatial-partition graph plus avoidance handles the common case, and one
PBD iteration cleans up the rest. Query spatially, never pairwise.

## Phase 2: Decouple sim from rendering with transform arrays

**Do**
1. "I passed the transform data of agents to niagara in the form of arrays." Copy
   agent transforms into Niagara data arrays each frame.
2. Keep the simulation fully CPU-driven: "gameplay and simulation stay in lock-step, no
   GPU readback, no sync headaches, every frame inspectable in the editor, at GPU-grade
   performance."

**Check**
- The array count matches the live agent count every frame. Stale entries are the
  classic desync bug: a dead agent rendered at its last position.

**Why**
Sim on CPU, render on GPU, never read back. The CPU side stays deterministic and
inspectable; the GPU side gets dense parallel rendering. The bridge between them is
data, not objects.

## Phase 3: Render with Niagara GPU particles + VATs

**Do**
1. "I then use the data in niagara to spawn, move and render the particles." One
   Niagara system consumes the transform arrays and renders the whole crowd.
2. Bake animations into Vertex Animation Textures: "The VAT can jump between different
   frame ranges based on character state like walking, standing, firing, etc." Each
   particle looks up its animation frame from the texture according to its agent state.

**Check**
- Every particle shows the right animation for its agent state, with no pops on state
  change. Compare a close-up against a skeletal-mesh reference.

**Why**
VATs remove per-agent skeletal cost on the GPU. Visual variety comes from data-driven
texture lookups, not from thousands of skinned meshes. (Same family as UE 5.8's own
crowd approach: metahumans fading to Niagara + VATs.)

## Phase 4: Budget the hardware honestly

**Do**
1. Record the author's numbers: 9800X3D + 5070 Ti at 4K, with explicit tradeoffs: "to
   render a more detailed textured scene, i'll have to lower the resolution. If the
   scene also consumes cpu (say it contains some cpu particle emitters) then i have to
   lower agent count."
2. Treat the vendor claim separately: 100,000 agents at 60fps during combat (product
   listing, unverified).

**Check**
- Stress with CPU particle emitters present and with a detailed textured scene; drop
   agent count until frame time holds. Reproduce the 100k/60fps figure before quoting
   it.

**Why**
Headline numbers are scenario numbers: "high end hardware will hide many many
problems, believe me." Publish the hardware and the tradeoffs alongside the numbers.

## Phase 5: Replicate with deterministic lockstep

**Do**
1. Replicate via deterministic lockstep backed by a Fix64 math lib: "easily replicate
   10K+ agents via deterministic lockstep." Fixed-point math is what keeps
   "deterministic" true across machines.
2. Size the network from the community estimate: "max 50 Packets per Player per second.
   So for 1000 Players its only 50k Packets per second. If all is Optimized properly
   the average packet size is around 200bytes. So the needed bandwith would only be
   around 10Mb/s or 80mbit." For tick-rate context: Eve's 1 fps server tick is why it
   cannot do WASD control; an RTS-grade experience wants tick >= 16, MMO-grade ~30.

**Check**
- Verify lockstep determinism across clients before scaling player counts; redo the
  packet math for your own agent and player counts.

**Why**
Lockstep turns N-agent replication into a determinism problem instead of a bandwidth
problem.

## The human method, distilled

1. **Not actors or characters.** Scale comes from refusing per-agent actors: agents are
   mass entities, their visuals are GPU particles.
2. **Avoidance is vastly cheaper than collision.** Avoid with a spatial-partition graph;
   resolve the leftovers with one PBD iteration.
3. **Sim on CPU, render on GPU, never read back.** Determinism and inspectability on one
   side, parallel rendering on the other, arrays as the bridge.
4. **Quote the tradeoffs.** Resolution, agent count, and CPU emitters are one budget;
   publish the hardware alongside the numbers.
5. **Lockstep makes 10k+ replication tractable.** Fixed-point math keeps it true across
   machines.

## Depth status

FULL (reconstructed from the creator's own comments + the Fab product description; the
video file itself was not retrievable: captions unavailable, download blocked by
YouTube's 429/bot challenge. Vendor performance claims marked unverified; inferences
labeled.)

## AAA studio practice (refinement 2026-10-24)

**Do**
1. Start from Epic's own crowd reference, not from a blank Mass project. The Matrix Awakens (Epic, Unreal Engine 5) ran a simulated city with 35,000 walking pedestrians that keep functioning procedurally as the camera moves, plus a freeway chase, as a demonstration that a whole city can be simulation driven rather than hand animated. Source: https://toptech.news/epic-games-shows-off-unreal-engine-5-with-stunning-simulated-city-in-the-matrix-awakens-demo/
2. Use the City Sample as the working template: thousands of MetaHuman agents driven by AI systems, with procedural Houdini city generation and World Partition managing the vast environment, and Chaos physics simulating vehicles, clothing, and destruction in engine. That is the production shape of this skill's Phase 1 to 3: Mass entities for brains, procedural city for context, GPU particles or VATs for bodies at distance, hero skeletal meshes only near camera. Source: http://www.cgw.com/Press-Center/In-Focus/2021/The-Matrix-Awaits-in-The-Matrix-Awakens-An-Unrea.aspx
3. Automate the sim to render bridge as a per frame data contract [inference]: a processor that writes transform arrays plus a per agent state id, and a Niagara system that reads exactly that contract. Add a frame validator that asserts array count equals live agent count and that every state id maps to a VAT frame range; stale or unmapped entries fail the frame in the editor instead of rendering a frozen agent.

**Check**
- Distance LOD gate: at far distance, agents must render as Niagara particles with VATs; at near distance, compare one agent against a skeletal mesh reference for animation correctness, per the original skill's Phase 3 check. If far agents are skeletal meshes, the crowd budget is broken even if frame rate currently holds.
- Reproduce the vendor numbers before quoting them: run the scene on stated hardware, with CPU particle emitters present and a detailed textured scene, and log agent count at a locked frame time. The original skill already warns that 100,000 agents at 60fps is a vendor claim; Epic's 35,000 pedestrian city is the independently reported reference point, not a replacement claim for this framework.

**Why**
Epic's crowd work proves the architecture (data oriented entities, procedural city, GPU bodies) at city scale, and it proves the discipline that matters: near camera heroes, far camera particles, simulation always CPU inspectable, rendering always GPU parallel. The skill's Mass to Niagara bridge is that discipline applied to battle crowds.
