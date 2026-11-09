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
