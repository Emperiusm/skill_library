---
name: walkability-density-remap
description: "Test a station-area density claim with walked distance, not a crow-flies circle: pull a walkable street network from OpenStreetMap, route every plot to the station, remap walk distance to density steps, and extrude a stepped, colour-graded massing model in Godot 4, with street-graph centrality as an optional second lens. Trigger when a district plan, town layout, or game map needs density that follows the walk."
---

# Walkability Density Remap

## Purpose

This skill reconstructs the exact workflow Abhinav Bhardwaj demonstrates for
Saint-Denis Pleyel, step by step, so another agent can follow the same
workflow in Godot 4. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle). The core
method is: never trust the circle. A planner draws an 800 m circle around a
station and assumes everything inside it is an 800 m walk. The reel tests
that claim by routing every plot to the station on real streets, and the
circle loses: 438 plots inside the circle are over 800 m on foot. Density
then follows the walked distance, not the circle, through a remap: 6 at the
station, falling to 1 at 1,000 m, extruded 5 m per step.

The transferable core is the remap (an analysis value drives height and
colour), not the Urbano Router, which does not transfer. The Router is
replaced here by an offline Python pre-process (OSMnx plus NetworkX) that
computes walk distances and writes one analysis JSON, and by an optional
Godot AStar2D rebuild for interactive use. The Godot side builds checkable
analysis lenses over a map; it does not generate final geometry on its own.

## Source

Creator: Abhinav Bhardwaj (@abhinavbwj, architect / urban and computational
designer). Reel: "Density that follows the walk", Saint-Denis Pleyel,
https://www.instagram.com/reel/DgA92iHRU1Z/ (Nov 21, 2026, 59 s, narrated,
interface shown throughout, 2 comments). Summary read firsthand with the
full transcript and 12 frames. All hard numbers below (438 plots, 390 m
crow-flies versus 1,700 m walk, 1.7 million sq m) are the creator's narrated
claims, not independently verified, and the reel shows no on-screen table
to check them against. The 6-to-1 remap endpoints and the 5 m step are his
narrated values; the remap curve shape, the Router settings, the setback
value, and the 1.7 million sq m computation are not shown or stated, and
are labeled as gaps wherever this skill has to choose them.

The centrality lens comes from the same creator's earlier reel,
https://www.instagram.com/reel/DTG9bAyCA4c/ (Jan 4, 2026, 51 s, music-only,
code on screen throughout): a NetworkX snippet computing betweenness,
closeness, and degree centrality on one street graph, with the footer
mappings betweenness to transit corridors, closeness to emergency access,
and degree to retail hubs. That reel shows no street data source, runs the
snippet unweighted on an abstract graph of about 15 nodes, and its top-node
values are illegible at source resolution. Centrality appears in this
skill only as an optional second lens, computed offline on the real graph
with length weighting, never as the core.

## Tools used

Python 3 with OSMnx and NetworkX (GeoPandas and Shapely arrive with OSMnx),
Godot 4 (GDScript; AStar2D for the optional interactive rebuild), and a
text editor for the analysis JSON. No Rhino, no Grasshopper, no Urbano.
OSMnx downloads the street network from OpenStreetMap and models it as a
NetworkX graph; the pre-process below is the replacement for every Urbano
component in the reel.

## Phase 1: Site inputs (real data, metric coordinates, buffer)

**Do**
1. Pick the anchor point (the station, square, or market) as latitude and
   longitude, and a study radius in metres (the reel uses 800 m). Download
   the street network with OSMnx `graph_from_point` and
   `network_type="walk"`, with a download radius of study radius plus a
   buffer of at least 200 m. The buffer is this skill's rule, not the
   creator's: streets severed at the extract edge become dead ends, and a
   plot near the edge then routes the long way around a gap that does not
   exist.
2. Project the graph to a metric coordinate system with OSMnx
   `project_graph` before doing any distance work. Record the resulting
   CRS string in the manifest. This is the Godot-side equivalent of the
   reel's WGS84 to UTM step; the reel's exact projection is not stated.
3. Keep only the largest strongly connected component for routing, and
   record how many nodes were dropped. In the walk network this is
   normally nearly everything, because walking has no one-way
   restrictions; in a drive network it is not.
4. Bring the plots in as one GeoJSON FeatureCollection of polygons in the
   same projected coordinates. If the plots arrive as latitude and
   longitude, project them with the same CRS before anything else. Apply
   the exclusion rule as data, not by hand: a named exclusion list (the
   reel drops railyard plots through a pattern step whose component is
   not legible) or an exclusion polygon in the same GeoJSON. Record
   which plots were excluded and why.

**Check**
- The manifest records: anchor lat/lon, study radius, buffer,
  `network_type`, OSM extract date, CRS string, node and edge counts
  before and after the component cut, and the exclusion list.
- A plot of the graph shows streets reaching the anchor from every
  direction with no severed stubs at the study boundary. Stubs at the
  outer buffer edge are expected; stubs inside the study radius are a
  download error.
- Every kept plot polygon is closed, has nonzero area, and lies inside
  the study radius plus buffer.

**Why**
Routing on the wrong network is the silent killer of this whole
workflow. The walk network is a different network from the drive
network, not a filter over it: it includes footpaths, alleys, steps,
and pedestrianised streets, and it has no one-way restrictions. A
pedestrian test run on a drive graph misses exactly the shortcuts the
test exists to find. And distances computed on latitude and longitude
degrees are not metres; every distance in this skill is computed after
projection, or it is wrong by a factor that changes with latitude.

## Phase 2: Walk every plot to the anchor (offline pre-process)

**Do**
1. Snap each plot centroid to its nearest graph node with OSMnx
   `nearest_nodes`, and record the snap distance in metres for every
   plot. Snap the anchor the same way.
2. Route with NetworkX `shortest_path_length` from each snapped plot
   node to the anchor node with `weight="length"`. Never omit the
   weight: without it, the shortest path minimises the number of edges
   (fewest junctions), which has no relation to walked metres.
3. Write one analysis JSON. Plots that cannot route (no path in the
   kept component) get `walk_m: null`, never zero. The schema is:

```json
{
  "crs": "EPSG:32631",
  "anchor": {"lon": 2.378, "lat": 48.918, "node": 123456789},
  "radius_m": 800,
  "plots": [
    {"id": "plot_001", "polygon": [[x, y], [x, y]],
     "centroid": [x, y], "walk_m": 642.0, "snap_m": 12.0,
     "area_m2": 1250.0}
  ],
  "nodes": [[x, y]],
  "edges": [[0, 1]]
}
```

The `nodes` and `edges` arrays are the projected street graph in the
same coordinates, included so the Godot side can draw the street
network and optionally rebuild the AStar2D graph without re-running
Python. Node indices in `edges` refer to positions in `nodes`.
4. Run the circle-lie check in the pre-process and print it: count
   plots whose crow-flies distance to the anchor is at most the study
   radius while `walk_m` is over the study radius. This reproduces the
   reel's 438-plot finding as a check on the method, not as a number to
   copy: the count for a new site will differ, and a count of zero is a
   valid result that means the circle happens to be honest there.

**Check**
- The snap audit passes: mean snap under 25 m, max snap under 50 m
  (this skill's defaults). Any plot snapping further is listed for
  human review, because a long snap usually means the plot centroid
  sits across a barrier (river, rail line, wall) from the nearest
  street, and its routed distance is fiction.
- No plot has `walk_m` of exactly 0 unless its centroid is on the
  anchor node. Zero-filled unroutable plots are the most common
  silent corruption in this workflow.
- Spot-check three plots by hand: one near the anchor, one mid-range,
  one far. Read their `walk_m` values and confirm the ordering is
  sane (nearer on the network reads shorter, even when crow-flies
  order disagrees).

**Why**
The reel's Router does its work offline, before any massing exists,
and this phase keeps that separation. Routing is analysis, and
analysis belongs in the pre-process where the graph tooling lives,
not inside the game engine. Godot never downloads OSM data and never
guesses a projection; it consumes the checked JSON. The snap audit
exists because nearest-node snapping is the one place where a
correct graph still produces a wrong answer quietly.

## Phase 3: Remap walk distance to density steps

**Do**
1. Choose the remap endpoints and record them in a remap ledger: input
   range in walked metres, output range in density steps, step height
   in metres, and setback in metres. The worked example uses the
   reel's values: input 0 to 1,000 m, output 6 to 1, the step 5 m, so
   a plot at the anchor extrudes 30 m and a plot at or beyond 1,000 m
   extrudes 5 m. These endpoints are the creator's values for his
   site; for a new site they are starting points to tune, not truths.
2. Remap with clamping, in the pre-process or in Godot, identically:
   clamp the walked distance into the input range first, then apply
   the linear remap, then quantise down to whole steps with floor.
   The linear curve and the floor quantisation are this skill's
   defaults, chosen because they reproduce the reel's stepped
   massing; the reel's actual curve shape is unknown, so never claim
   it matches. In GDScript the call is `remap(value, istart, istop,
   ostart, ostop)` from `@GlobalScope`, and `remap` extrapolates
   outside its input range, which is why the clamp comes first.
3. Store the resulting integer step count per plot in the analysis
   JSON as `density`. Keep the float remap value alongside it as
   `density_float` so the quantisation is auditable.
4. Compute the total floor area as this skill's derived metric: the
   sum over plots of `area_m2` times `density`. Label it derived:
   the reel's 1.7 million sq m figure is a narrated claim whose
   computation is unstated, and this formula is the skill's
   reconstruction of it, not the creator's stated method.

**Check**
- Boundary values: walk 0 m gives the maximum steps, walk at or
  beyond the input maximum gives the minimum steps, and no plot
  produces zero or negative steps.
- The worked example reproduces by hand: 0 m to 6 steps (30 m), 500 m
  to 3.5 floored to 3 steps (15 m), 1,000 m or more to 1 step (5 m).
- The remap ledger and the JSON agree: re-running the remap from the
  ledger over the stored `walk_m` values reproduces every stored
  `density` exactly.

**Why**
The remap is the whole argument of the reel in one function: an
analysis value decides height. Everything else in this skill is
plumbing that keeps that function honest. Clamping before remapping
is the difference between a lens and a lie: without it, a plot at
1,500 m extrapolates below the minimum step and either vanishes or
inverts. Quantising to whole steps is what makes the output read as
the reel's stepped massing instead of a smooth height field; if a
smooth field is wanted, skip the floor and say so in the ledger.

## Phase 4: Build the lenses in Godot (plots, setback, extrusion, colour)

**Do**
1. Load the analysis JSON with `JSON.parse_string` (the static Godot 4
   form; it returns null on failure) or the instance `JSON.parse` form
   when error reporting matters. Convert every id and index with
   `int()`: JSON has one number type, and Godot parses all JSON
   numbers as float, so an id read as `123.0` will miss a dictionary
   key of `123`.
2. For each plot, apply the setback first: `Geometry2D.offset_polygon`
   with a negative delta (the delta is the setback in metres, this
   skill's parameter; the reel's setback value is unstated). The call
   returns an array of polygons; use the first result, and if it is
   empty (the polygon was too small for the setback), keep the
   original polygon and flag the plot.
3. Triangulate the set-back polygon with
   `Geometry2D.triangulate_polygon`, then build a prism with
   `SurfaceTool`: bottom ring at height 0, top ring at
   `density * step_height`, side quads between corresponding ring
   vertices, and the triangulated cap on top. Use clockwise winding
   for front faces, and call `generate_normals` after the vertices
   are in. Skip the bottom cap: nobody sees it, and it doubles the
   triangle count of the base for nothing.
4. Colour by value: set one vertex colour per vertex from the plot's
   density step through a fixed gradient (this skill's default: deep
   red at maximum steps fading through orange to pale grey at minimum,
   matching the reel's render), and use a `StandardMaterial3D` with
   `vertex_color_use_as_albedo` enabled and roughness 1.0. One
   material serves every plot; the colour lives in the vertices.
5. Draw the street network as a separate, toggleable layer from the
   `nodes` and `edges` arrays (thin line meshes or an
   `ImmediateMesh`), in a neutral dark colour, so the lens can be
   read against the streets that produced it. Draw the study circle
   as a ring at the study radius for the same reason: the circle is
   the claim being tested, and it must stay visible next to the
   answer.

**Check**
- Every plot with a non-null `walk_m` has exactly one prism; every
  null plot is drawn flat at a distinct hatch or grey and listed in
  the missing-data report, never extruded to a guessed height.
- From the fixed iso camera (or the default view): the red core sits
  at the anchor, colour fades outward along streets rather than in
  a perfect circle, and the fade follows street detours visibly
  (a plot across a rail line reads paler than its crow-flies
  neighbour).
- Toggle the street layer off and on: the colour pattern must still
  be legible on its own, because the lens, not the street drawing,
  carries the finding.

**Why**
The setback matters more than it looks: without it, neighbouring
prisms share edges and the massing reads as one fused slab; with it,
each plot reads as a separate block and the density steps are
countable. Vertex colours instead of per-plot materials keep the
whole lens to one draw call per layer, which is what makes it cheap
enough to leave on while designing. And the circle stays drawn
because a test whose null hypothesis is invisible is not a test.

## Phase 5: Read the test (claim, test, number)

**Do**
1. State the claim before reading the result, in the reel's argument
   shape: "everything inside the 800 m circle is an 800 m walk, so
   density should follow the circle." Then state the test (the
   routed distances) and the number (the circle-lie count and the
   total floor area from Phase 3).
2. Present the lens in the fixed-viewpoint morph the page uses: same
   camera, flat plots, then stepped prisms, then colour, then the
   street layer. Each stage must add exactly one thing, so the
   viewer can see what each stage contributes.
3. Write the one-paragraph finding in the remap ledger: the claim,
   the count, the worst case (crow-flies versus walked metres for
   the single worst plot), and what changes in the plan because of
   it (which plots drop a density step, which gain one, relative to
   the circle scheme).

**Check**
- The finding names its own limits: OSM data date, network type,
  and the fact that walked distance is not walked time (no speeds,
  no crossings, no slopes in this workflow).
- The worst-case plot is shown, not just counted: its route is
  drawn, so a sceptical reader can see the detour instead of
  trusting the number.
- Nothing in the finding uses the reel's numbers (438, 1,700 m,
  1.7M sq m) as evidence about the new site. Those numbers belong
  to Saint-Denis Pleyel; the new site's numbers are the ones in
  the JSON.

**Why**
"Claim, test, number" is the argument structure that makes this
reel persuasive, and it is also the structure that keeps the skill
honest. A lens that only ever confirms the plan is decoration. The
circle-lie count is designed to be able to embarrass the plan; if
it comes back zero, the plan survives the test and the lens has
still done its job.

## Phase 6 (optional): Centrality lens on the same graph

**Do**
1. In the same Python pre-process, on the same projected, largest
   component graph, compute the three NetworkX measures with
   length weighting: `nx.betweenness_centrality(G, weight="length")`,
   `nx.closeness_centrality(G, distance="length")`, and
   `nx.degree_centrality(G)`. The reel's snippet passes no weight
   at all and runs on a toy graph; this skill requires the weight,
   because an unweighted centrality on a street graph counts
   junctions, not streets.
2. Normalise each measure to 0..1 across the kept nodes and store
   the three per-node score dicts in the analysis JSON under
   `lenses`. Keep them as node scores, not plot scores.
3. In Godot, colour the street layer by the selected measure
   (betweenness: transit corridors; closeness: emergency access;
   degree: retail hubs, the reel's footer mappings), one measure
   at a time, cycling views so the same graph can be compared
   measure by measure. To attach a score to a plot for labelling,
   use this skill's rule: the plot takes the maximum score among
   the street nodes within its snap distance, and the rule is
   recorded in the ledger.
4. Never mix the lenses in one colour scale. Walkability colours
   plots by walked metres; centrality colours streets by graph
   position. Two different quantities on one gradient is the
   fastest way to produce a beautiful, unreadable map.

**Check**
- Each measure's top node is sane: betweenness peaks on a bridge
  or through-route, closeness peaks near the network centre,
  degree peaks at a multi-way junction. If all three peak on the
  same node, the graph is probably too small or too regular to
  learn from, and the lens should say so.
- The centrality JSON and the walkability JSON come from the same
  graph object in the same run. Rebuilding one without the other
  invalidates the comparison.

**Why**
Centrality answers a different question from walkability: not "how
far is this plot from the anchor" but "which streets does the
network itself make important." The reel's value is that it shows
all three measures on one graph with one code block, so their
differences are visible instead of asserted. The weight
requirement is the difference between that demonstration and a
usable lens: on real streets, a 500 m arterial and a 5 m alley
are not interchangeable edges.

## The human method, distilled

1. **Test the circle, do not assume it.** Crow-flies distance is a
   claim about the street network, and the network gets a vote.
2. **Route on the network for the mode in question.** Walk tests run
   on the walk network; drive networks miss the shortcuts that
   decide the answer.
3. **Project before measuring.** Degrees are not metres. Every
   distance in the workflow is computed after projection.
4. **The remap is the argument.** One function turns an analysis
   value into height and colour. Keep it clamped, quantised, and
   written down.
5. **Missing data stays missing.** An unroutable plot is drawn flat
   and listed, never filled with a plausible number.
6. **One lens, one quantity.** Walkability and centrality never share
   a colour scale.
7. **Fix data as data.** A wrong plot, a missing street, or a bad
   exclusion is corrected in the GeoJSON or the graph inputs and
   the analysis is re-run, never patched in the mesh.

## Failure modes

- **Drive network for a walk test:** the graph is missing footpaths,
  alleys, and steps, so walked distances inflate and the circle
  looks worse than it is. Fix: `network_type="walk"`, recorded in
  the manifest.
- **Severed boundary edges:** no buffer around the study radius, so
  streets leaving and re-entering the extract become dead ends and
  edge plots route absurdly. Fix: download radius plus buffer,
  analyse only inside the study radius.
- **Unweighted routing:** `shortest_path_length` without
  `weight="length"` minimises hop count. A route with two long
  arterials beats a route with ten short alleys. Fix: always pass
  the weight, and assert it in the pre-process.
- **Degrees treated as metres:** routing or remapping on EPSG:4326
  coordinates. Fix: `project_graph` first, and refuse to run if the
  CRS is geographic.
- **Silent zero-fill:** unroutable plots written as 0 m, which
  remap to maximum density at the far edge of the map. Fix: null,
  flat, listed.
- **Unclamped remap:** values beyond the input range extrapolate
  below the minimum step. Fix: clamp before `remap`, in that order.
- **Snap fiction:** a plot centroid across a barrier snaps to a
  street it cannot reach, and its distance looks fine. Fix: the
  snap audit with a max threshold and human review of outliers.
- **Inverted prisms:** wrong winding order in the SurfaceTool build
  makes prisms read as holes from above. Fix: clockwise front
  faces, and check from the working camera before adding colour.
- **JSON float ids:** ids and indices arrive as floats and miss
  dictionary keys. Fix: `int()` on read, everywhere.
- **Mixed lens scales:** walkability and centrality on one
  gradient. Fix: separate layers, separate scales, one measure
  visible at a time.
- **Borrowed numbers:** the reel's 438, 1,700 m, or 1.7M sq m
  quoted as evidence about a different site. Fix: the finding
  uses only the numbers in the run's own JSON.

## AAA studio practice

- **Space Syntax: the street configuration itself generates movement
  (Hillier and Hanson, UCL Bartlett, late 1970s).** Space syntax
  breaks a street system into a network of choices and scores it
  with integration (how many street-to-street transitions it takes
  to reach every other street), choice (how often a street lies on
  shortest paths, read as flow), and depth distance (metric distance
  from each segment to all others). The founding claim is "natural
  movement": the configuration of the network generates patterns of
  pedestrian movement before any land use is considered, and
  integration in particular is argued to predict how busy a street
  will be. This skill's two lenses are the same split the theory
  makes: the walkability remap is the metric, depth-distance side,
  and the centrality lens is the topological, choice side. Keep
  them separate for the same reason the theory keeps integration
  and depth distance separate: they answer different questions.
  (Space syntax summary, https://en.wikipedia.org/wiki/Space_syntax ;
  the theory's argument in full, https://humansandnature.org/bringing-people-together-or-keeping-them-apart/ )
- **The honest limit, from the critique, is the boundary problem
  (Ratti, MIT, 2004).** Ratti shows space syntax results are
  sensitive to boundary conditions, discard metric information in
  the topological representation, and can produce conflicting
  outcomes from one configuration. That critique is why this skill
  downloads a buffer, keeps the metric walk distances as the core
  lens, and treats centrality as the optional, explicitly
  topological second lens. A centrality score computed on a
  clipped graph is a statement about the clip as much as about the
  streets. (Ratti, "Urban texture and space syntax",
  https://senseable.mit.edu/papers/pdf/20040901_Ratti_SpaceSyntax_EnvironmentPlanning.pdf )
- **The tooling is the published tooling (Boeing, OSMnx).** Geoff
  Boeing's OSMnx work models street networks from OpenStreetMap
  for urban research at scale: 27,000 US street networks in the
  2018 study, and over 160 million nodes and 320 million edges
  across 8,914 urban areas in the 2021 global study, with a
  reproducible computational workflow and open indicator
  repositories. The pre-process in this skill uses the same
  package, the same projection discipline, and the same
  largest-component hygiene as that published workflow, at
  neighbourhood scale. The scale differs; the discipline does not.
  (Boeing 2018, https://arxiv.org/html/1705.02198v4 ; Boeing 2021,
  https://escholarship.org/content/qt5db3f718/qt5db3f718.pdf?v=lg )

## Agent automation

- Write a `site-manifest.json` per run: anchor lat/lon, study
  radius, buffer, network type, OSM extract date, CRS string,
  node and edge counts before and after the component cut,
  exclusion list, and the remap ledger (endpoints, curve,
  step height, setback). The run is not reproducible without it.
- Gate on the snap audit: fail the run if any plot snaps further
  than the max threshold (50 m default) without a recorded human
  review, and fail if any plot has a null walk distance that is
  not in the missing-data report.
- Gate on remap determinism: re-running the remap from the ledger
  over the stored walk distances must reproduce every stored
  density exactly. A mismatch is a ledger error, not a rounding
  difference.
- Gate on the circle-lie count: the check must run and print on
  every run, including when it returns zero. A skipped check is
  recorded as a skipped check, not as a pass.
- Log a per-run input hash (OSM extract date plus GeoJSON hash
  plus manifest hash) so a regenerated analysis JSON is provably
  identical when its inputs have not changed. A changed output
  without a changed input is a pre-process regression.
- Keep the centrality lens behind its own flag in the manifest
  (`lenses: ["walkability"]` by default). Adding `"centrality"`
  must re-run the pre-process on the same graph object, not bolt
  scores from a different extract onto the walkability JSON.

## Valkyrie note

Pellune's map is authored, not procedural, and that is exactly why
this skill fits as lenses, not as a generator. The walkability lens
answers which plots a citizen can actually reach on foot from the
town square or the market, given the authored street graph: a plot
that looks central on the map but sits across the ravine road
reads pale, and that is a design finding, not a rendering bug. The
centrality lens answers which streets the network makes important
before shops and stalls are placed. The sun-hours analysis from the
same creator's Barcelona reel is the natural third lens, same
contract, and it belongs in a follow-up skill, not crammed into
this one. No lens overwrites authored layout: a lens that disagrees
with the authored plan produces a finding for human review, and the
authored map changes only by a human decision recorded in the
ledger. The greybox ladder from the sweep applies to presenting
lens results: same fixed iso camera, flat plots, then prisms, then
colour, then streets, one stage at a time.

Cross-links: `procgen-worlds/osm-blender-r3f-campus-map` (the OSM
import and fix-data-as-data discipline at map scale),
`simulation-vfx/mask-driven-ambient-particle-spawning` (an analysis
layer driving placement on an authored map, the same shape as a
lens), and the companion brief-driven parametric massing workflow
(slider-driven massing from a brief; the massing this remap's
density steps feed into).

## Depth status

PARTIAL (reel summary read firsthand with full transcript and 12
frames; centrality reel summary read firsthand with the on-screen
code; Godot AStar2D, remap, Geometry2D, SurfaceTool, JSON, and
vertex-colour APIs verified against the Godot 4 class
documentation; OSMnx and NetworkX calls verified against their
documentation and maintained secondary sources; no hands-on run of
the Python pre-process or the Godot build was done in this session,
so the per-phase checks are what close that gap; every reel setting
the footage does not show is labeled as a gap or as this skill's
choice, never as the creator's value).
