---
name: runevision-voronoi-terrain-stack
description: "Drive large-scale procedural terrain with Voronoi macro-cells for level-design control over noise: LayerProcGen framework, fast erosion filter, GPU Instancer Pro instancing + occlusion culling, Microsplat, Amplify Impostors. 70-90 fps on M1 MacBook, zero baking. Trigger when procedural terrain needs designed macro-features (lakes, rivers, cliffs) instead of rolled noise."
---

# Voronoi Macro-Cell Terrain with a Runtime Instancing Stack

## Purpose

This audit reconstructs the architecture from runevision's post and their
answers across 26 comments, step by step, so another agent can follow the
same process. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The architecture's
core method is: give the *designer* control of macro-structure with Voronoi
cells, and leave micro-detail to noise.

Related: `raup-shell-morphospace` (morphospace-as-UI parametric design) and
`procedural-pixel-creature-generator` (procedural asset pipelines) are the
same problem class — parametric control over generative systems — applied
to shells and creatures instead of terrain.

## Source

Creator: runevision

Source: https://www.reddit.com/r/proceduralgeneration/comments/1wz2oe8/largescale_voronoiesque_cells_to_drive_my/
(native Reddit video; r/proceduralgeneration post 1wz2oe8, score 356, 26
comments) | 2026-10-08 scout run. Post selftext was truncated in the scan;
substance comes from the author's 26 comments, including tool names,
perf numbers, and links.

## Tools used

Tools used: author's **LayerProcGen framework**
(https://runevision.github.io/LayerProcGen/, open, includes a full terrain
demo scene), author's **fast erosion filter** (blog, 2026-03:
https://blog.runevision.com/2026/03/fast-and-gorgeous-erosion-filter.html),
**GPU Instancer Pro** (indirect GPU instancing + GPU occlusion culling),
**Microsplat Terrain**, **Amplify Impostors**, paid 3D models. Hardware:
**MacBook Pro M1 (32 GB), 1920x1080, 70-90 fps.**

## Phase 1: Replace pure noise with Voronoi macro-cells

**Do**
1. Layer Voronoi-esque cells over the base noise terrain.
2. Assign designed features per cell: lakes, rivers, giant walls, impassable
   steep cliff faces — *placed* strategically, not rolled from noise.

**Check**
- Walking across a cell boundary shows the designed feature, not a noise
  seam; each cell's feature reads from the intended viewing distance.

**Why**
"Down the line, this allows me all kinds of level design control not
possible with traditional noise functions" (post text). Macro-cells turn
terrain generation into a design language: noise supplies texture,
cells supply intent. This is the transferable idea — it applies to any
procedural layout problem (districts, biomes, sectors), not just heightmaps.

## Phase 2: Erode, then render without baking

**Do**
1. Run the fast erosion filter (blog link above) before mesh finalization.
2. Instance all vegetation through GPU Instancer Pro: indirect GPU
   instancing plus GPU occlusion culling.
3. Shade in real time with Microsplat Terrain; impostor distant trees with
   Amplify Impostors. **No lightmaps, no baking** — the author confirms:
   "Correct, there's no lightmaps or other baking involved."

**Check**
- 70-90 fps on the named hardware at 1920x1080 with the full forest scene.

**Why**
Zero baking keeps the iteration loop minutes-long: move a cell, re-erode,
walk the terrain immediately. Baking would turn every design change into
an offline job; real-time shading makes macro-cell layout a live design
activity.

## Phase 3: Scope the known defect honestly

**Do**
1. Accept terrain LOD pop-in at flight altitude as a known limitation.
2. Tree LODs already crossfade; for terrain, crossfading "would require
   changes both to the Microsplat shader, and a lot of infrastructure to
   send the right fading values to the right materials at the right times."

**Check**
- Pop-in is invisible at walking altitude; only noticeable when flying
  (the author's debug flight ability is not a normal game mechanic).

**Why**
The honest bound on the technique: design the game around pop-in at
altitude (flight is a debug ability), and scope the crossfade fix as
future shader + infrastructure work, not a launch blocker. Stating the
defect in public is what makes the perf numbers trustworthy.

## Phase 4: Ship the building blocks, keep the game

**Do**
1. Open-source the framework (LayerProcGen) and the erosion filter technique.
2. Keep the game's specific terrain proprietary: the full demo "depends on
   paid third party tools like GPU Instancer Pro, Microsplat Terrain,
   Amplify Impostors, and various paid 3D models" and "this terrain is made
   specifically for my own game."

**Check**
- Another developer can reproduce the *technique* from the open parts; they
  cannot reproduce the game's *terrain* without the paid stack.

**Why**
The technique is the product being shared; the content is the game's. This
is the reproducible-research model for procgen devlogs: open the method,
keep the art.

## The human method, distilled

1. **Designer controls macro, noise controls micro.** Voronoi cells place
   features; noise textures them. Never ask noise to do level design.
2. **Admit the defect in public and scope around it** (terrain LOD
   crossfade) instead of hiding it — the admission is what makes the
   70-90 fps claim credible.
3. **Quote the number that matters, on named hardware** (70-90 fps, M1,
   1080p), not the number that flatters.

## Failure modes

- Washed-out design: features feel random — check that macro-cells (not
  noise) own placement of every feature the player navigates by.
- Pop-in complaints: verify the viewing altitude where pop-in appears; if
  it's walking altitude, the LOD distances are wrong — the technique as
  documented only hides pop-in at ground level.
- Iteration too slow: check that no baking step crept into the pipeline;
  every design change must be walkable within minutes.

## Reproduction note

The full terrain in the video is not reproducible from open sources alone
(paid stack + game-specific content). The transferable artifacts are: the
LayerProcGen framework (open), the erosion filter (documented), and the
macro-cell design pattern (this skill).

## AAA studio practice

**Do**
1. Drive placement by designer rules in a graph editor, the way Guerrilla Games did on Horizon Zero Dawn: artists define procedural placement rules in a graph editor, and GPU algorithms create a dense world around the player on the fly, so painting in a tree line or redirecting a road is as easy as moving a mountain or changing a desert into a tropical swamp. Voronoi macro-cells are the same idea at the terrain layer: the cell is the rule's scope. Source: https://www.guerrilla-games.com/read/gpu-based-procedural-placement-in-horizon-zero-dawn
2. Link tools into an ecosystem, the way Ubisoft did on Far Cry 5: freshwater networks, cliffs, and vegetation were generated by linked Houdini tools, each feeding the next, with species growing only where conditions (humidity, sunlight, slope) allowed and competing for ground. A Voronoi cell should therefore carry its own growth conditions, not just its feature label. Source: https://blog.playstation.com/archive/2018/03/22/how-the-stunning-open-world-of-far-cry-5s-hope-county-montana-was-created
3. Use Voronoi diagrams as the macro structure, the way DwarfCorp does: lay out fault lines, compute a Voronoi diagram of the fault map (distance from every pixel to the nearest fault line), then distort with noise. That ordering, structure first, noise second, is the executable version of this skill's Phase 1 rule (cells own intent, noise owns texture). Source: https://www.gamedeveloper.com/programming/how-we-generate-terrain-in-dwarfcorp
4. Automate the macro-cell pipeline as agent-executable steps:
   - Script cell assignment: every cell gets a feature type plus its placement conditions in a data file (feature, minimum slope, water proximity, exclusion list); the generator reads that file, never a hand painted mask that is not versioned.
   - Script the iteration loop: move a cell, re-erode, rebuild, and measure frame time on the named hardware profile; fail the run if frame time regresses beyond the previous run's measurement, and log the cell that caused it.
   - Script the LOD check: capture screenshots at walking altitude and at flight altitude for the same camera path, and log pop-in events per altitude; the skill's Phase 3 bound (pop-in invisible at walking altitude, visible only when flying) becomes a counted metric instead of a claim.

**Check**
- Every navigable feature (lake, river, cliff, wall) traces back to a cell assignment in the data file. If a feature exists with no cell owning it, noise has taken over level design.
- A design change (move a cell) is walkable within minutes with no baking step, per the skill's Phase 2 rule; if a bake creeps in, the iteration loop is broken and the run fails.

**Why**
- Guerrilla, Ubisoft, and DwarfCorp all separate the same two jobs this skill separates: designer owned macro-structure (rules, cells, fault lines) and noise owned micro-detail. The automation above makes that separation auditable: cell ownership, frame time regression, and pop-in counts are all logged, so the 70-90 fps claim stays attached to a reproducible measurement.

**Depth status:** PARTIAL. Tool stack, technique, and perf numbers come from
the author's comments; the selftext body is truncated and the cell
generation code itself was not fetched (it lives in the linked framework).
No parameters were invented.
