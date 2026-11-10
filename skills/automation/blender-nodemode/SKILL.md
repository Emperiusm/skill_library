---
name: blender-nodemode
description: "Do everything Blender does through a Houdini-style node graph with NodeMode: isotropic remesh, Still bake, cloth solving with explicit solver parameters, portal data routing, noise-driven surface deformation, and in-chain mesh repair. Trigger when a Blender workflow needs visible, editable, repeatable node parameters instead of a modifier stack."
---

# Blender NodeMode: Houdini-Style Node Graph Inside Blender

## Purpose

This skill reconstructs the workflow from Default Cube's "Introducing...
Blender NodeMode!" (YouTube, 2026-11-05), step by step, so another
agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The workflow's core method is: do everything Blender does
through a node graph, with named nodes and explicit parameters, the way
Houdini works.

## Source

Creator: Default Cube.

Source: https://www.youtube.com/watch?v=jEynICHP1gM | Uploaded
2026-11-05 | 766 s (12:46) | 60,356 views | Site:
https://www.blendernodemode.com (per the video description and the
end card frame) | 2026-11-09 scout run.
Evidence: 12 frames extracted from a downloaded copy of the video
(download 1 of 2 in this run's pre-approved allowance; no approval gate
fired), plus the video description. No captions exist in a retrievable
form: the subtitle fetch hit YouTube HTTP 429 and was not retried. No
transcript lines are quoted anywhere in this skill, because none were
retrieved.

## Tools used

Tools used: **Blender**, **NodeMode** (Houdini-style node graph inside
Blender).

## Phase 1: Remesh with the Isotropic Triangle node

**Do**
1. Feed the mesh into an "Isotropic Triangle R..." node (frame shows
   "Isotropic Triangle R", presumably Remesh).
2. Set Target E... 0.1 m, Iterations 7. Check Preserve Boundary,
   Preserve Sharp, Transfer Attributes. Set Sharp Angle 30 deg.

**Check**
- The frame shows the node wired between a geometry source and a Bake
  node; the parameter values are visible on the node itself. Read the
  actual parameters instead of relying on node names (the Cinematic
  Cavern rule: node labels drift, values are the truth).

**Why**
Isotropic remeshing gives even triangles before baking, so the bake
downstream does not inherit stretched source topology.

## Phase 2: Bake it still

**Do**
1. Feed the remeshed geometry into a "Bake" node.
2. Set Animation: Still.

**Check**
- The Bake node sits between the remesh node and the output wire; a
  Still bake means the result is a static mesh, not an animated cache.

**Why**
Baking freezes the procedural result into a mesh the rest of the graph
(and the exporter) can treat as finished geometry.

## Phase 3: Simulate cloth with explicit solver parameters

**Do**
1. Use a "Cloth Solver" node with Geometry in, Simulation out.
2. Set Substeps 4, Iterations 4, Delta Time 0.042.
3. Set Force to (0.000, 0.000, -9.810): gravity down Z at 9.81.
4. Under Collision, set Thickness 0.010, Friction 0.500, check Self
   Collision. Tearing is available as a collapsed section.
5. Feed the solver output into a "Simulation" node (Skip, Geometry) and
   route the result through a Portal Receive node where the graph needs
   it downstream.

**Check**
- The cloth frame shows the solver wired into the simulation node with
  a Portal node carrying geometry onward; the substeps and delta time
  are the stability budget (4 substeps at 0.042 s).
- A separate frame shows "Simulation Input" and "Simulation Output"
  nodes bracketing falling cubes above a ground plane: the simulation
  zone is explicit in the graph, not hidden in a modifier stack.

**Why**
Solver parameters are on the node, in the open: substeps, iterations,
gravity, thickness, and friction are all visible and editable in one
place, which is the whole point of doing simulation as nodes instead
of as a modifier.

## Phase 4: Move data without wires using Portals

**Do**
1. Create a "Portal" node set to Transmit with a name (the frame shows
   a Portal named "Portal").
2. Anywhere else in the graph, create a Portal node set to Receive with
   the same name; it receives the value, vector, or geometry.
3. The frame shows a Vector node (X 0.000, Y 0.000, Z 0.000) wired into
   a Transmit Portal, and a second Transmit Portal below it, with a
   Receive Portal on the right exposing Value, Vector, and Value
   sockets.

**Check**
- The receive side lists the same sockets the transmit side offers; a
  portal that receives nothing has no data to show.

**Why**
Portals are the node-graph answer to long wires: data moves by name
across the graph, the same role Set/Get nodes play in ComfyUI (see
`comfyui-readable-node`, where hidden wires are exactly what the
Readable Node skill removes). The difference is that NodeMode portals
are named and visible as nodes.

## Phase 5: Deform a surface with noise

**Do**
1. Take a "Bunny [CGM]" source (Geometry, UVMap out) into a "Surface
   Deformation" node (Geometry, Mesh, Pick, Pin Position, Extra).
2. Drive the deformation with a "Random Value" node (Boolean,
   Probability 0.010, ID, Seed 0) and an "Add" vector node fed by a
   "Position" node.
3. Feed a "Noise Texture" node into the Add: 3D, FBM, Normalize checked,
   Vector in, Scale 5.000, Detail 2.000, Roughness 0.500, Lacunarity
   2.000, Distortion 0.000.

**Check**
- The frame shows the full chain wired: Bunny to Surface Deformation,
  Random Value and Noise Texture feeding the Add feeding the
  deformation's Pin Position. Probability 0.010 means roughly 1 in 100
  points is picked; Seed 0 means the pick is reproducible.

**Why**
Surface deformation driven by noise plus a sparse random pick is how
you add organic variation to a mesh without sculpting it: the noise
decides where, the probability decides how much.

## Phase 6: Repair the mesh before it leaves

**Do**
1. Run the mesh through a "Mesh Repair" node: check Merge Duplicates,
   Remove Degenerates, Stitch Borders, Orient Faces, Transfer Attributes
   (all five checked in the frame).
2. A side panel on the same frame shows emit toggles: Emit Sharp,
   Emit UV, Emit Color, Emit Material (partially visible, prefixed
   "...mit").

**Check**
- Repair is a node in the chain, so it runs every time the graph
  re-evaluates; a repaired mesh cannot regress when an upstream
  parameter changes.

**Why**
Mesh repair as a graph node turns cleanup from a manual step into a
rule, the same principle as the Cinematic Cavern scripted-repairs
phase: fix the geometry first, as a repeatable operation.

## What the frames also show

- A cracked/broken skull render (frame 2): the destruction/fracture
  look NodeMode is used to produce.
- A sponsor segment (frames 6-8): the presenter unboxing and reclining
  in a LiberNovo chair, matching the affiliate link in the video
  description. No tooling content.
- End card (frame 11): "BlenderNodeMode.com".

## AAA studio practice

NodeMode is a one-person Blender addon, but the idea it implements,
do everything through a named, parameterized node graph, is exactly
how AAA open worlds get built. The differences are scale, handoffs,
and automation around the graph.

- **Ubisoft, Far Cry 5: the graph lives inside the editor, and it
  rebuilds nightly.** Technical artist Etienne Carrier's team built
  the Hope County tools in Houdini and ran them through Houdini
  Engine directly inside the Dunia editor, so game artists crafted the
  world with Houdini tools from the editor they already worked in.
  The same tools ran as nightly builds on build machines to fully
  refresh the world daily. The NodeMode parallel: the graph is not a
  side tool, it is the authoring surface, and a re-cook must be
  runnable without the artist present.
  (https://christianjmills.com/posts/procedural-tools-far-cry-5-notes/index.html)
- **Sequential tools with data handoffs, not one big graph.** Far Cry
  5's generation ran in a fixed order, freshwater, then cliffs, then
  biomes, and each tool exported data the next one read: the freshwater
  pass produced a water mask the biome tool consumed, and biome
  recipes reacted to water proximity, altitude, and cliff erosion
  lines. NodeMode's chain already runs in order (remesh, bake,
  simulate, deform, repair); the AAA discipline is to name each
  stage's output data and make the next stage fail loudly if its input
  is missing or stale, instead of silently cooking on old geometry.
  (https://christianjmills.com/posts/procedural-tools-far-cry-5-notes/index.html)
- **Ghost Recon Wildlands: rules beat hand-placement at scale.**
  Ubisoft generated the geography of a fictional Bolivia and
  populated it with vegetation and infrastructure from real data plus
  procedural rules, roughly 5x faster than hand-placing terrain
  content, with a comparatively small team. The node graph's job is
  the same in NodeMode: the artist defines rules (target edge length,
  noise scale, pick probability) and the graph fills the world.
  (https://www.bsm3d.com/articles/houdini-environments-production.html)
- **One asset definition, many outputs.** SideFX Labs ships tools
  (Auto UV, PolyReduce, LOD Generate) that let a technical artist
  build one HDA taking a high-poly asset and outputting several LODs
  plus an imposter sprite, ready to import, often wired into the
  build pipeline via PDG/Deadline. The NodeMode equivalent of the
  Bake node is that freeze step: one cooked result feeding every
  downstream consumer (export, LOD, collision), never a live graph
  evaluated differently per consumer.
  (https://www.bsm3d.com/articles/houdini-environments-production.html)
- **Portals are HDA inputs and outputs, done by name.** In Houdini
  production, a digital asset exposes named parameters and inputs;
  data moves between tools by name and by contract, not by tracing
  wires across a network. NodeMode portals do the same job inside one
  graph. The AAA rule that follows: every portal pair gets a written
  contract (name, data type, expected range), and an unmatched Receive
  is a build failure, not a silent empty socket.
  (Inference from the Far Cry 5 HDA practice above, labeled as such.)

### Agent-executable upgrades

1. **Graph contract file.** Before running the graph, write
   `graph-contract.json` next to the .blend: every node name, its
   parameters (e.g. Isotropic Triangle Remesh target 0.1 m, 7
   iterations, sharp angle 30 deg; Cloth Solver 4 substeps, 4
   iterations, delta 0.042, gravity -9.81 Z), and the expected output
   of each stage (mesh name, approximate vertex count). After each
   re-cook, diff the baked mesh against the contract; a parameter that
   drifted without an entry in the contract is a regression, not a
   tweak.
2. **Portal registry.** List every Transmit/Receive pair (name, data
   type, source node, consumer node) in the contract file. A Receive
   with no matching Transmit, or two Transmits sharing one name, fails
   the gate before the bake runs.
3. **Stage-order gate.** Enforce the Far Cry 5 order as a rule:
   remesh, then bake, then simulate, then deform, then repair. A graph
   that repairs before it deforms, or bakes before it remeshes, fails
   the gate; the stage outputs are named per stage
   (`<asset>_remeshed`, `<asset>_baked`, `<asset>_simulated`) so a
   stale stage is visible in the outliner.
4. **Re-cook hash log.** After every bake, export the baked mesh
   (glb or obj) and record its SHA-256 plus vertex count in
   `recook-log.jsonl` with the date. A re-cook that changes the hash
   without a contract change means an upstream parameter moved; find
   it before exporting. This is the small-scale version of Far Cry 5's
   nightly full-world rebuild: the world is re-derived from the rules
   every time, and the log proves it.

## The human method, distilled

1. **Nodes for everything.** Remesh, bake, cloth, deformation, and
   repair are all nodes with visible parameters, not modifier-stack
   entries.
2. **Read the parameter, not the label.** Target 0.1 m, 7 iterations,
   30 deg sharp angle, 4 substeps, 0.042 delta time: the values are the
   workflow.
3. **Name the data to move it.** Portals carry values by name across
   the graph instead of long wires.
4. **Repair is a step, not an afterthought.** The Mesh Repair node sits
   in the chain and runs on every evaluation.

**Depth status:** PARTIAL (12 frames from a downloaded copy with
verified node names and parameters; no captions, the subtitle fetch
failed with YouTube HTTP 429 and was not retried, and local
transcription is unavailable in the sandbox by design; no pricing
stated in the video or description).
