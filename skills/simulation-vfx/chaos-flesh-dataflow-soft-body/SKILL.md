---
name: chaos-flesh-dataflow-soft-body
description: "Build a UE 5.8 Chaos Flesh soft-body asset with DataFlow: mesh prep rules, Static-to-Tet-Mesh template, tet density tuning, the missing Set-Flesh-Default-Properties fix, and deformable solver wiring. Trigger when adding squishy/rubbery physics to an Unreal scene."
---

# Chaos Flesh Soft-Body Basics via DataFlow | UE 5.8

## Purpose

This skill reconstructs the exact workflow shown in the tutorial, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: convert a static mesh into a tetrahedral volume with a DataFlow graph, bind the volume to the surface, and let the deformable solver deform the volume so the surface follows.

## Source

- Video: "Unreal Engine 5.8 Chaos Flesh and Soft Body Physics: Part 1 - The Basics | Beginners Tutorial" by Crawford Terrace Studios — https://www.youtube.com/watch?v=pFiwaoqHjWw (13:13)
- Project files: https://ko-fi.com/s/73d35cabcd
- Epic docs: https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh
- Evidence: full captions (287 lines) + 12 video frames reviewed, 2026-10-21 scout run

## Tools used

Unreal Engine 5.8, Chaos Flesh plugin (experimental), DataFlow graph ("Static to Tet Mesh" template), Deformable Solver actor. Creator's rig: i9-13900KF, 32 GB RAM, RTX 4070 12 GB.

## Phase 1: Prepare the mesh

**Do**
1. Use a closed mesh with no overlapping geometry (same rule as Chaos Destruction meshes).
2. Avoid thin geometry and long stretched vertices in the mesh.
3. Keep the mesh resolution under 30,000 triangles — "high-density meshes may not simulate very well."
4. Author at roughly 1 m scale: "size matters right now... the simulation seems to do best with meshes around 1 m in size. As you get smaller or larger than that, you'll start running into issues."

**Check**
- Inspect the mesh for open edges and overlaps in the DCC before import.
- Triangle count below 30k; overall size near 1 m.

**Why**
The deformable solver tessellates a tetrahedral volume inside the mesh; thin, stretched, or oversized geometry makes the solver unstable. Chaos Flesh is experimental: "expect limitations and issues, and save your work often." Chaos Flesh supports Nanite static and skeletal meshes.

## Phase 2: Set up the project and plugin

**Do**
1. Create a new project: Film/Video section → Blank template. The blank template's floor actor is monitored for collisions by the deformable solver by default.
2. Edit → Plugins → search "flesh" → enable Chaos Flesh → Restart Now.

**Check**
- After restart, the Flesh Asset type exists under Content Drawer → Physics.

**Why**
The blank template gives you a floor the solver already collides with, so the first simulation works without collision configuration.

## Phase 3: Create the flesh asset and assign a template

**Do**
1. Content Drawer → right-click → Physics → Flesh Asset. Rename it (the tutorial used `FA_gummybear`).
2. Assign the **"Static to Tet Mesh"** DataFlow template (for static-mesh-based assets).
3. Ignore the "static mesh to tet" template — per the tutorial it is "an exact copy of the skeletal to tet mesh template... just ignore this one for now."

**Check**
- The Flesh Asset editor opens with a blueprint-like DataFlow graph and viewport windows above it.

**Why**
UE 5.8's templates are the fast path: "starting with the 5.8 release and the addition of the new data flow templates, creating your Chaos Flesh assets are now easier than ever." The three system components are the flesh asset (geometry data), the DataFlow graph (procedural build), and the deformable solver (runs the simulation).

## Phase 4: Walk the DataFlow graph

**Do**
1. **Static Mesh node:** in Node Details, pick the source static mesh. Open the Construction viewport tab; if it is dark, click the preview-scene icon and select Gray Ambient.
2. **Static Mesh to Collection node:** extracts the geometry information into a collection.
3. **Create Tetrahedron node:** the solver does NOT operate on the static mesh. It builds a tetrahedral mesh volume filling the static mesh and binds that tetrahedral geometry to the surface; the surface follows the tets.
   - Set density via **Num Cells** in Node Details. Default is 10; the tutorial bumped it to 30 to recover the gummy bear's facial detail.
   - Cost rule: "assign only the minimum number of cells you absolutely need" — more tetrahedra = more simulation load.
   - Alternative method: set **Method** to **Tet Wild** — "better at preserving high detail and thin features of your mesh, but at a higher simulation cost." Reprocessing takes a few seconds.
4. **Set Flesh Default Properties node:** the 5.8 templates are missing this node — add it manually (right-click → search "set flesh default properties") and wire it after Create Tetrahedron. Without it, the solver assumes the asset has no density and "basically ignores gravity and any deformations."
5. **Density value:** default 1.0. The tutorial lowered it to 0.01: "A higher density value means gravity has a stronger effect on your mesh and your mesh tends to crumble under its own weight." At 1.0 the bear "deforms into a melting mess"; at 0.01 it gets "that gummy bear wiggle and jiggle."
6. **Flesh Asset Terminal node:** the process/output node. Save.

**Check**
- Construction viewport: detail appears/disappears as Num Cells changes (30 recovered the face; Tet Wild recovered thin detail).
- Simulation viewport: play shows the melt at density 1.0 vs. the jiggle at 0.01.

**Why**
Tet density is the resolution of the simulation, decoupled from the render mesh: tune the cheapest volume that preserves the silhouette, then set density so gravity reads correctly instead of crumbling the mesh.

## Phase 5: Wire the solver in the scene

**Do**
1. Drag the flesh asset into the scene (its material will be missing at first — fixed in step 4).
2. Add → Deformable Solver actor into the scene.
3. Select the flesh asset → Details → **Primary Solver** dropdown → select the deformable solver.
4. Solver-sharing rule: if multiple flesh assets interact with each other, have them share the same solver; if they won't interact, give each its own solver. "This is not a hard fast rule, just a recommended suggestion."
5. If the mesh rockets off into the sky on play, it is intersecting the floor: Scene Preview → Transform → set Location Z to 50, then re-run.
6. Material fix: select the flesh asset → Details → search "override mat" → Override Material → + → pick the source material.

**Check**
- Outliner shows the flesh asset and the deformable solver; Primary Solver is set.
- Play: the asset jiggles with its material applied.

**Why**
The flesh asset is inert until a solver runs it, and the material lives on the source asset rather than the sim volume, so it must be re-applied as an override.

## Chaos Flesh vs. Chaos Destruction (differences stated in the tutorial)

- Flesh assets (soft-body actors) do not work with Field Systems and cannot be fractured.
- Collisions do not work by default as with Chaos Destruction: you must specify which actors the deformable solver monitors (the blank-template floor is monitored by default).
- The workflow overlaps with Chaos Destruction's but is a different pipeline (DataFlow-based rather than fracture-based).

## The human method, distilled

1. Minimum cells that preserve detail; Tet Wild only when thin features matter.
2. Add Set Flesh Default Properties manually — the template is broken without it.
3. Start density low (0.01 worked for a 1 m gummy bear); 1.0 crumbles.
4. One solver per interacting group; save often (experimental).
5. If the mesh rockets, it is intersecting the floor — raise Z.

## AAA studio practice

**Do**
1. Follow the production split Epic documents for Chaos Flesh: simulate low-resolution geometry at runtime and cache high-resolution cinematic-quality results offline, rather than asking the runtime solver to carry hero detail. The tutorial workflow in this skill (tune Num Cells to the minimum that preserves the silhouette) is the asset-authoring side of that same split.
2. Automate the density and cell-count sweep: build a DataFlow test asset at 1 m scale, sweep Num Cells (for example 10, 20, 30) and density (for example 1.0, 0.1, 0.01), and record a short playblast per combination with its parameters burned into the frame. Pick the cheapest combination that holds the silhouette, and store that pair as the asset default. This replaces hand-tweaking with a reviewable matrix, the same discipline as the TOPs wedge in the net-break skill.
3. Plan for the shipped-game muscle path, not only the toy path: in the State of Unreal 2025 The Witcher 4 tech demo, Epic and CD Projekt Red showed the Chaos Flesh Solver physically simulating muscle movement under skin on Kelpie the horse, running on a base PlayStation 5, and Epic's 5.6 learning material then taught the same workflow as a Chaos Flesh muscle simulation based on a Witcher character asset. For character work, prefer the skeletal-mesh muscle route (offline sim baked or ML deformer) over a free-standing soft-body prop asset, and keep the free-standing route for props like the tutorial gummy bear.

**Check**
- The sweep playblasts exist with parameters visible, and the chosen Num Cells and density are the cheapest passing pair, not the highest.
- For character assets, the flesh asset is driven by skeletal animation, and its solver budget is measured on the target console or minimum-spec PC, not only in the editor.

**Why**
Epic's own framing is that Chaos Flesh's main focus is muscle deformation during skeletal animation. A prop demo proves the solver runs; a muscle asset proves it ships. [inference] The sweep step is the automation bridge between the two: it makes the tutorial's hand-found values (30 cells, 0.01 density) reproducible for any new mesh.

Sources:
- https://hothardware.com/news/witcher-4-unreal-engine-5-6-demo
- https://forums.unrealengine.com/t/community-tutorial-chaos-flesh/1134001
- https://www.unrealengine.com/learning/julys-free-learning-content-non-human-digital-characters-motion-capture-and-more

## Depth status

FULL — 287 caption lines and 12 video frames reviewed; description metadata (project files, docs links, creator rig) captured. Project files linked but not downloaded.
