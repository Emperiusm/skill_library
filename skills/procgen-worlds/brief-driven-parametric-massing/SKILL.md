---
name: brief-driven-parametric-massing
description: "Turn a written housing brief into a parametric greybox district in Godot 4: six sliders hold the brief, street lines split the site into blocks, courtyard rings subdivide into plots with L-shaped corners kept whole, a log-distance noise proxy flips loud plots to offices, a sun-angle cap limits south wings, and a live home count tunes the massing against the brief. Rebuilt from a narrated Grasshopper reel as a Godot construction with SurfaceTool extrusion and MultiMesh windows. Trigger when a district needs massing variants from a brief before any hand authoring."
---

# Brief-driven parametric massing

## Purpose

This skill reconstructs the brief-to-massing workflow end to end, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: encode the brief as a small set of named parameters, let street lines and analytic drivers (a noise proxy, a sun cap) decide the district's shape, and tune the parameters against a live unit count until the massing meets the brief. The output is a greybox district, not a finished town: footprints, heights, typologies, and counts, ready for a human to judge and then author by hand.

## Source

Creator: Abhinav Bhardwaj (abhinavbwj, architect / urban and computational designer). Instagram reel: https://www.instagram.com/reel/DgAvHDzosRz/ (posted Nov 21, 2026, 93 seconds, narrated end to end, 0 comments). Caption: "Parameter typologies as per brief in Grasshopper!" Full local transcription (faster-whisper tiny, corrected against on-screen subtitles), 12 frames read firsthand, work dir `~/workspace/custom-skills/local-video-summarizer/work/ahbinavs-DgAvHDzosRz/`.

What the reel shows, attributed as the creator's narrated claims (not verified measurements): a housing brief for Sloterdijk 1, an office park on the A10 in Amsterdam, asking for 1,000 homes, offices only where the motorway is too loud, and courtyards that keep the March sun. Six sliders hold the brief. The definition yields 1,166 homes, tuned to 1,314. 13 of 57 buildings become offices above a 70 dB proxy threshold. No Grasshopper or Rhino version is shown. The reel has no comments, so there is no comment-thread evidence for this skill.

## Gaps in the source, labeled

These are unknown from the reel and must not be presented as the creator's values:

- Two of the six sliders are unnamed in narration and on screen. Only street ring, building width, sun share, and base floors are named.
- The exact logarithm formula and distance units behind the decibel proxy are unstated. A "Log" component with a base-10 panel is visible in one frame; no formula is given.
- The sun-share percentage and the March sun angle value are unstated.
- The facade-grid component sequence is partly unclear (garbled narration, partly legible frames: Edges, Join, Flatten, EvalSrf at UV 0.5,0.5, an A/B component with a 3.6 panel).
- The home-count formula (homes per floor, per building) is unstated, and which slider move produces the 1,166 to 1,314 lift is unconfirmed.
- The 70 dB figure is a distance proxy rule, not a measured acoustic result. The reel does not say so explicitly; this skill does.

Everything in the phases below that fills these gaps is this skill's own construction, derived from Godot documentation, and is labeled as such wherever it appears.

## Tools used

Godot 4.x (C# or GDScript; C# names are given alongside GDScript where they differ). Geometry2D (polygon offset, clip, triangulate, point-in-polygon), SurfaceTool or ArrayMesh (extrusion), MultiMeshInstance3D (windows, trees), RandomNumberGenerator with a recorded seed, a DirectionalLight3D as the sun reference. No Rhino or Grasshopper is needed for the Godot construction.

## Phase 1: Write the brief as parameters, before any geometry

**Do**
1. Write a brief manifest, `brief-manifest.json`, before building anything. One entry per parameter: name, unit, allowed range, default, and what it drives. The four named from the reel: street ring (the street network that splits the site), building width (the ring depth, 14 m in the reel), sun share (the fraction of each courtyard that must stay sunlit), base floors (the starting floor count). Add two reserved slots, named `unknown_slider_a` and `unknown_slider_b`, with a comment that their identities are unknown from the source; fill them only with values the project itself decides (for example, courtyard depth and random-variation strength), never by guessing the creator's.
2. Declare the count formula in the manifest, because the reel does not give one. This skill's own formula: homes = sum over residential buildings of (floors x units per floor), with units per floor declared per building type (for example, 2 for a perimeter plot, 4 for a corner L-shape). Label it as this skill's declaration, not the creator's.
3. Declare the driver thresholds in the manifest: the noise-proxy threshold (70 in the reel, units: proxy decibels), the sun date and latitude the cap uses (March, equinox sun angle, declared latitude), and the set-back scale (0.8 in the reel).
4. Expose every manifest entry as an editor slider on the generator node (a `@tool` script or exported properties in C#), so dragging a slider regenerates the district in the editor. The sliders are the brief; there is no second, hidden copy of the numbers in code.

**Check**
- The manifest lists every number the generator uses, with units. A parameter with no unit is a bug: "14" means nothing until it says metres.
- Changing one slider and regenerating changes exactly the thing that slider names. If two outputs move, a rule is reading the wrong parameter.
- The two reserved slots are present and marked unknown. If they are silently filled with invented creator values, the manifest is lying about its source.

**Why**
- The reel's whole point is that the brief lives in six sliders and everything else is a consequence. If the numbers hide in code, the workflow collapses back into hand modeling with extra steps. The manifest is also what makes variant comparison possible: a variant is a manifest plus a count, nothing more.

## Phase 2: Split the site into blocks with the street lines

**Do**
1. Draw the site boundary as one closed polygon in plan (PackedVector2Array, metres, X east, Y south to match the map plane; Godot's 2D Y axis points down, so keep one consistent mapping to 3D X/Z and document it in the manifest).
2. Draw each existing street as a centreline polyline. Widen each centreline into a street polygon with `Geometry2D.offset_polyline` (GDScript) / `Geometry2D.OffsetPolyline` (C#), using half the street width as the delta. This is the Godot equivalent of the reel's "Line SDL carries the two existing streets through the site".
3. Subtract the street polygons from the site polygon with `Geometry2D.clip_polygons` / `ClipPolygons`, taking the difference pieces as blocks. In the reel this step (Surface Split) makes six blocks from two streets; the block count here is whatever the site and streets produce, and it is reported, not assumed.
4. Discard slivers: drop any block whose area is below a manifest minimum (this skill's default: 200 sq m, labeled as its own). A sliver block will produce a degenerate ring in Phase 3.

**Check**
- Block count is printed after the split. Six is the reel's number for its site, not a target.
- The blocks tile the site exactly: sum of block areas plus street areas equals the site area within rounding. A gap means a street polygon missed the boundary; an overlap means a street was subtracted twice.
- No block is a sliver. If one survives the area filter, the street buffer is too wide for that gap.

**Why**
- Streets are the only fixed input; everything else is derived. Splitting first means every later rule operates per block, and a changed street layout re-masses the whole district instead of requiring a rebuild.

## Phase 3: Rings, subdivision, and corners kept whole

**Do**
1. For each block, build the courtyard ring: shrink the block polygon inward by the building width with `Geometry2D.offset_polygon` / `OffsetPolygon` using a negative delta (14 m in the reel). The ring is the band between the original polygon (outer wall) and the shrunk polygon (courtyard edge). Keep both polygons: the outer polygon is the building footprint band, the inner polygon is the courtyard.
2. Subdivide the ring into plots by walking each outer edge and cutting at the building-width interval (the reel's Divide Distance step). Each cut produces one plot polygon. Record plot count per block.
3. Detect corners and keep them whole. A corner is a block vertex whose interior angle is close to 90 degrees (this skill's test: within 25 degrees of square, labeled as its own). Where two adjacent plots share a corner vertex, merge them into one L-shaped plot instead of cutting through the corner. This is the Godot equivalent of the reel's Discontinuity step, which "keeps the corners whole as L shapes".
4. Handle the offset call's return type honestly: `offset_polygon` returns an array of polygons, because shrinking can split a polygon or produce holes. Take the results explicitly (index [0] for the main result, and handle any extra polygons as separate courtyards or errors). Never assign the array directly to a single polygon variable: in GDScript that cast silently yields a single (0, 0) point, a documented forum gotcha, and the ring vanishes without an error.

**Check**
- Plot count per block is printed, with corner plots flagged. The reel's total is 57 buildings across six blocks; the count here is whatever the site produces.
- Every corner plot is one L-shaped polygon, not two rectangles meeting at a point. Render the plots in distinct colors and look: a split corner shows as a seam through the corner.
- No ring is empty: if the negative offset exceeds a block's narrowest dimension, `offset_polygon` returns an empty array. That block is too small for the building width; shrink the width or drop the block, and log which happened.

**Why**
- The ring is the perimeter-block typology: buildings face the street, courtyards stay open inside. Cutting corners through would break the typology the brief asks for, and L-shaped corner buildings are where the extra floors and extra homes come from in Phase 5.

## Phase 4: Analytic drivers, noise proxy and sun cap

**Do**
1. Noise proxy (typology switch). For each plot, measure the distance from the plot centroid to the noise source polyline (the motorway in the reel, the A10). Convert distance to a proxy level with this skill's own formula, labeled as a derivation, not the creator's: `proxy = reference_level - 20 * log10(distance / reference_distance)`, with reference level and reference distance declared in the manifest (this skill's defaults: 70 at 10 m, labeled as its own). If the proxy exceeds the threshold (70 in the reel), the plot becomes an office; otherwise it stays residential. The logarithm is base 10, matching the visible Log component, but the formula, the reference values, and the 20 factor are this skill's construction.
2. Sun cap (height limit). Declare the sun date, latitude, and the sun-share fraction in the manifest. Compute the sun elevation angle for that date and latitude (this skill's approximation: use the equinox noon elevation, 90 minus latitude, and document the simplification). For each south-facing wing, cap its height so its shadow length, `height / tan(elevation)`, stays within the sun-share fraction of the courtyard depth. This is the Godot form of the reel's "March-sun cap on south wings": a geometric approximation, not a radiation simulation, and it must be labeled as one.
3. Apply the drivers in a fixed order: typology first (noise proxy), then height rules (Phase 5), then the sun cap as a clamp on the result. A cap applied before the height rules would be overwritten by them.

**Check**
- The office/residential split is logged per plot with its proxy value and distance. In the reel 13 of 57 flip to offices; the split here follows the site's own distances.
- A test plot placed at the reference distance reads exactly the reference level. If it does not, the formula is misapplied.
- The sun cap binds on at least one south wing in a test run (force a tall south wing and confirm the cap cuts it). A cap that never binds is either misconfigured or the sun angle is wrong.
- No proxy value is ever reported as a measured decibel level. The manifest calls the field `noise_proxy`, never `noise_db_measured`.

**Why**
- Drivers are what make this parametric massing instead of random boxes. The noise proxy turns a site analysis into a typology decision, and the sun cap turns a daylight requirement into a height rule. Both are approximations with declared inputs; pretending either is a measurement would launder a guess into a fact.

## Phase 5: Extrude, plinth, body, set-back top, and height rules

**Do**
1. Extrude each plot polygon upward with SurfaceTool (GDScript: `begin(Mesh.PRIMITIVE_TRIANGLES)`, `add_vertex`, `generate_normals()`, `commit()`; C#: same calls in PascalCase, `Begin`, `AddVertex`, `GenerateNormals`, `Commit`) or an ArrayMesh built from vertex arrays (`add_surface_from_arrays`). Build the extrusion as three stacked parts, matching the reel: a plinth (ground floor, this skill's default 1 floor, labeled as its own), a body (the remaining floors), and a set-back top (the top 1 to 2 floors scaled by the set-back factor, 0.8 in the reel, about the footprint centroid). Triangulate each horizontal cap with `Geometry2D.triangulate_polygon` / `TriangulatePolygon`, which returns counter-clockwise triangles; flip winding for the bottom cap so its normal points down (Godot uses clockwise winding for front faces, per the SurfaceTool docs).
2. Apply the height rules in this order: start from base floors; quiet plots (proxy below threshold) gain floors (this skill's default: +2, labeled as its own; the reel says "quiet buildings gain floors" without a number); corner L-shaped plots gain two extra floors (the reel's number, attributed); then apply seeded random variation of plus or minus 1 floor (RandomNumberGenerator with the manifest seed; the reel's "random breaks up the rest"). Then clamp with the sun cap from Phase 4.
3. Assign material by typology: residential plots get a per-building brick variation (one hue shift per building from the seeded random stream, matching the reel's "every home building gets its own brick"); office plots stay grey (the reel's rule, attributed). Use per-instance or per-surface colors, not one material per building, so the building count does not become a material count.
4. Keep the extrusion deterministic: same manifest plus same seed regenerates the identical mesh. Hash the vertex array after generation and record it in the variant log.

**Check**
- Floor counts print per building with the rule that produced each (base, quiet bonus, corner bonus, random, sun clamp). A building whose count cannot be explained by the rules is a bug.
- The set-back top is visibly inset on all sides, not just shifted. A shifted top means the scale was applied about the origin instead of the centroid.
- Two runs with the same manifest and seed produce identical vertex hashes. If they differ, the random stream is unseeded or a dictionary iteration order leaked in.
- Winding is correct: no inside-out buildings. Viewed from outside, every face is lit; a dark or missing face is a flipped cap.

**Why**
- The three-part stack is what makes the massing read as buildings instead of extruded footprints: the plinth meets the street, the body carries the floors, the set-back top breaks the skyline. The height rules are where the brief's trade-offs live (quiet gets height, corners get height, sun takes it away), so they must be explainable per building.

## Phase 6: Facades, windows, landscape, and the live count

**Do**
1. Build the facade bay grid per building: divide each outer facade edge into bays of the manifest bay width (this skill's default: 3.6 m, labeled as its own; the reel's grid step is partly unclear). The reel's facade-grid sequence is not recoverable, so this grid construction is this skill's own, labeled as such.
2. Find the street side with the reel's Point In Curve idea, rebuilt in Godot: test each facade midpoint with `Geometry2D.is_point_in_polygon` / `IsPointInPolygon` against the street-buffer polygons from Phase 2. Facades facing the street take shopfronts on the plinth; facades facing the courtyard take balconies. Record the test result per facade; do not assume the outer ring always faces the street (corner plots have two street faces).
3. Place windows with one MultiMeshInstance3D per window type: set `transform_format` to TRANSFORM_3D, set `instance_count` before setting transforms (the MultiMesh docs require format first, then count), then `set_instance_transform` / `SetInstanceTransform` per bay per floor. This is the Godot form of the reel's Box Morph windows in every bay. One window mesh instanced thousands of times is one draw call; one MeshInstance3D per window is not.
4. Plant the courtyards and streets with a second MultiMesh (trees), scattered with the seeded random stream inside the courtyard polygons and along street edges, matching the reel's Populate Geometry step. Keep trees out of the building footprints by testing each candidate point against the plot polygons.
5. Compute the live count from the manifest formula (Phase 1) and display it next to the brief target in the editor and in the variant log: homes generated, brief target, difference, and the slider values that produced it. Tune one slider at a time until the count meets the brief, recording each variant. The reel's final move (1,166 to 1,314) is unattributed to a specific slider; do not copy it as a recipe.

**Check**
- Window count equals bays times floors times buildings, and every window sits on a facade (sample 10 windows: each lies on its building's outer wall, none floats in the courtyard).
- Shopfronts appear only on street-facing plinths, balconies only on courtyard-facing facades. A swapped assignment means the point-in-polygon test used the wrong polygon set.
- The count moves when a slider moves, and moves in the expected direction (more base floors raises the count; a higher sun share lowers it). A count that does not move is disconnected from the generator.
- Variant log holds at least three variants (initial, one overshoot, one tuned). A single variant is a guess, not a comparison.

**Why**
- Windows and trees are what make the greybox readable as a district at the fixed camera distance; without them the massing is abstract blocks and the count is the only thing to judge. The count is the reel's actual deliverable: the definition is tuned until the number answers the brief, and the tuning history is the evidence the answer was reached deliberately.

## Godot-native generation vs a Blender Geometry Nodes bridge

**Recommendation: generate natively in Godot.** The greybox is throwaway massing whose value is live re-tuning: drag a slider, watch the count and the skyline move, record the variant. A `@tool` generator script in Godot keeps the parameters live in the editor, the seed deterministic, and the variant log next to the scene. No export step, no frozen parameters, no second tool to keep in sync.

Use the Blender Geometry Nodes bridge only if the team already authors procedural work in Blender and wants the node graph as the authoring surface. The costs, verified from Blender 5.2 export references: glTF carries no Geometry Nodes; the recipe must be baked before export, either by applying the modifier or by exporting with `export_apply=True` (which applies modifiers, and without it geometry-node objects export empty), and instances must be realized first or they are dropped. Parameters freeze at export, so every re-tune is a round trip back through Blender. The bridge is one-way: the .blend keeps the recipe, the .glb keeps the realized geometry, and the two drift apart the moment a slider moves. For a greybox pass whose whole point is re-tuning, that drift is the failure mode. If the bridge is used anyway, keep the .blend as the source of truth, export with Apply Modifiers on, realize instances as the last node, and re-export on every parameter change; never hand-edit the exported mesh.

Sources: Blender 5.2 glTF export operator notes, https://github.com/aerolab/silicon-baires/blob/HEAD/.claude/skills/blender/references/api-5.2.md ; Geometry Nodes export limitations, https://github.com/roble3/cc-blender-skill/blob/HEAD/knowledge/04-geometry-nodes/00-overview.md ; Blender to glTF exporter settings, https://www.zachsimms.com/3d/export/web-threejs/

## The human method, distilled

1. **The brief is the model.** Sliders first, geometry second. If a number is not a slider, it is not part of the brief.
2. **One definition, many variants.** Change the site, the streets, or the sliders; the same rules re-mass the district. A new district is a new variant, not a new model.
3. **Drivers decide, taste judges.** The noise proxy and the sun cap make typology and height decisions the human does not have to remake per building; the human judges the resulting district and tunes the drivers.
4. **Corners are special, on purpose.** Keep them whole, give them the bonus floors, and check them first: they carry the district's identity and its count.
5. **The count is the deliverable.** A massing pass ends with a number against the brief and a tuning history, not with a pretty render.
6. **Approximations wear labels.** A proxy is called a proxy, a cap is called an approximation, and neither is ever reported as a measurement.

## Failure modes

- **A slider without a unit.** "14" with no unit, range, or default is not a parameter; it is a magic number with a handle. Every manifest entry carries a unit.
- **Offset returning an empty array.** A negative offset larger than a block's narrowest dimension returns nothing. The block is too small for the building width; log it and shrink the width or drop the block, never silently skip the ring.
- **Offset returning multiple polygons.** Shrinking can split a polygon. Taking only the first result drops courtyards. Handle the full array, and never cast the array to a single polygon (the silent (0, 0) result).
- **Corners cut through.** Without the corner-merge step, L-shaped corner plots become two rectangles and the corner bonus applies twice or not at all. Check corners in the colored plot view.
- **Proxy reported as measurement.** The log-distance value is a stand-in for a noise model that was never run. Any report, caption, or variant note that calls it measured decibels is wrong.
- **Sun cap with the wrong season.** An equinox angle used for a solstice requirement, or a latitude left at default, caps the wrong wings. The manifest declares date and latitude; the cap check forces a tall south wing through the clamp.
- **Unseeded variation.** Random floor variation without a recorded seed makes two runs differ and variants uncomparable. The seed lives in the manifest and the vertex hash proves determinism.
- **Two sliders moved at once.** The count moved, but nobody knows which slider moved it. Tune one slider per variant and log each.
- **Street side swapped.** Shopfronts on the courtyard side mean the point-in-polygon test ran against the wrong polygon set. Check with debug colors before placing windows.
- **Window instance explosion.** Bays times floors times buildings grows fast; a 57-building district at fine bay widths can pass 10,000 instances. Budget the bay width against the instance count, and remember one MultiMesh is one draw call only if the instances share one mesh.
- **Bridge export without Apply Modifiers.** Geometry-node objects export empty unless modifiers are applied at export. Realize instances first, or the export silently drops them.

## AAA studio practice

- **Parish and Muller, "Procedural Modeling of Cities", SIGGRAPH 2001.** The ancestor of this entire workflow: image maps (land-water, population density) drive an L-system street network, the land is divided into lots, and buildings are generated per lot with a texture-element system. The reel's version is the same shape with the maps replaced by sliders and two analytic drivers. The paper's warning still applies: with only a few building types, a generated city reads as repetition; the reel answers it with per-building variation rules (quiet bonus, corner bonus, random, per-building brick). Source (paper PDF, read firsthand): https://cgl.ethz.ch/Downloads/Publications/Papers/2001/p_Par01.pdf?ref=gorillasun.de ; abstract: https://cgl.ethz.ch/Downloads/Publications/Papers/2001/p_Par01.abstract
- **Muller, Wonka, Haegler, Ulmer, and Van Gool, "Procedural Modeling of Buildings", ACM Transactions on Graphics, 2006.** CGA shape: a shape grammar whose split rules evolve a mass model into detailed facades, integrated into the CityEngine framework, demonstrated by rebuilding Pompeii. The reel's plinth/body/set-back stack and bay-window grid are a hand-run version of a CGA split sequence: mass, split into parts, split parts into facades, facades into bays. The paper's lesson for this skill: write the split rules once (Phase 5 and 6), and let the parameters, not the modeler, produce the variety. Source (SIGGRAPH bibliography entry, read firsthand): http://gbib.siggraph.org/index.php?detail=Mueller:2006:PMO
- **Watson, Muller, Wonka, and colleagues, "Procedural Urban Modeling in Practice", IEEE Computer Graphics and Applications, 2008.** The practice tutorial for the same toolset, including Electronic Arts' use of procedural urban modeling in games and the cautionary detail that Parish and Muller's New York model used only six building types. The practice that transfers: keep the type count small, push variety into parameters and rules, and review the result as a district, not building by building. Source (tutorial PDF, read firsthand): http://peterwonka.net/Publications/pdfs/2008.CGA.Watson.ProceduralModelingTutorial.pdf

## Agent automation

- **Brief manifest gate.** The generator refuses to run without `brief-manifest.json`, and fails if any parameter lacks a unit, a range, or a default, or if the count formula is missing. A manifest with a reserved unknown slider still runs; a manifest that invents creator values for it fails review.
- **Determinism gate.** Regenerate twice from the same manifest and seed; fail if the vertex-array hashes differ. The seed is part of the manifest, not a runtime accident.
- **Count gate.** After generation, compare the computed home count against the brief target and fail the variant if it falls outside the manifest tolerance (this skill's default: within 10 percent, labeled as its own). Log the count, the target, and the slider values for every variant.
- **Driver audit.** Log every plot's typology decision with its proxy value and distance, and every sun-cap clamp with the pre-clamp and post-clamp heights. A plot with no logged decision is a fail; the drivers must be auditable, not just visible.
- **Polygon validity gate.** Fail if any offset returns an empty array without a logged disposition, if any ring polygon fails triangulation (empty index array), or if any window instance lands outside its building's footprint. These are the three silent-failure points in the pipeline.
- **Variant diff.** Record each variant as manifest plus count plus one fixed-camera screenshot. A variant without a screenshot cannot be judged; a variant without a manifest cannot be reproduced.

## Valkyrie note

Pellune's town is authored, not procedural, and this skill never replaces the authored map. Its fit is the greybox pass before authoring: generate massing variants for the Pellune district from a brief (street ring from the authored streets, building width from the town's plot sizes, sun share from the fixed iso camera's light direction), compare their counts and skylines, pick the variant that answers the brief, then hand-author the final town from it. The noise proxy and sun cap are massing-decision approximations, not simulation truth, and they must not leak into the sim as data. Where it does not fit: anything that needs final art (facades, materials, interiors), anything on the authored terrain masks (the scatter system owns those), and any district where the plot layout itself is a designed feature rather than a brief outcome.

**Depth status:** PARTIAL (reel read firsthand with full transcript and frames; Godot construction derived from class documentation read firsthand and labeled as this skill's own where it fills source gaps; the Godot path has not been run hands-on in this session; the creator's counts are narrated claims, not verified measurements; two slider identities, the logarithm formula, and the home-count formula remain unknown).
