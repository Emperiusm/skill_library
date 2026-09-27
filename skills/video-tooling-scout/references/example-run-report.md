# Example run report (SAMPLE)

**What this is:** a trimmed excerpt from a real `video-tooling-scout` run
(2026-09-27), sanitized. It shows what every run delivers per the
[`SKILL.md`](../SKILL.md) output contract: gap alerts first, per-inventory
have-vs-need tables, a full-depth video audit, watchlist trending, and
non-goals. Project names are genericized; the videos, tools, and numbers are
real.

**Run facts:** 7 videos scanned across 18 subreddits (2-day window),
1 video deeply analyzed at full depth in this excerpt, captions/metadata
only, zero downloads, zero approval prompts.

---

## Gap alerts (P1/P2)

1. **Per-asset performance budgets + automated engine import validation (P1).**
   Procedural/shader/LOD-heavy content lands in-engine unchecked; no import
   validation gate exists.
2. **Rigging / retargeting stage (P1).** Every asset that should move is stuck
   static. Concrete step: an auto-rig + retarget stage before engine packaging.
3. **Mesh compression standard for shipped assets (P1).** 8-bit UVs, octahedron
   normals, 3-integer vertices; patch-grid UVs. (Recipe direction from a devlog
   whose captions were unavailable, so the exact constants are unverified;
   the direction stands.)
4. **Mesh-refinement stage with deviation metrics, Planer-class (P1).**
   Flatten, sharpen, report deviation, preserve UVs; slots between weld and QA.

---

## Have-vs-need: my primary pipeline (example: Blender + Godot indie project)

| Tool / stage | Found in video | Status | Recommendation |
|---|---|---|---|
| Mesh-refinement stage (Planer-class) | #1 Planer video | NEED | **Adopt now (P1).** Flatten/sharpen with deviation report, UVs preserved |
| Mesh compression recipe (8-bit UVs, octahedron normals) | devlog | NEED | **Backlog (P1).** Adopt as output standard |
| Rigging / skinning / animation retarget | model-revival video | NEED | **Backlog.** Needed when characters move |
| Obi Physics (particle-based, SDF collision) | devlog | NEED | **Watchlist.** Proven rope/ragdoll pattern |
| Deterministic topology via VDBs + math | procedural video | HAVE | Validation, no action |
| LOD generation | voxel video | HAVE | Keep |
| NLE / edit / grade (Da Vinci Resolve) | cinematic video | n/a | **Skip.** Human editing tool |

---

## 1. "Fix Lumpy Photogrammetry Meshes in Blender: Google 3D Tiles" (Nachiket B)

Source: https://youtu.be/m9oxz99Ysp0 | r/photogrammetry post 1wjnwzi (score 223)

**Tools used:** Blender 4.2+; Planer add-on (detects planar regions, snaps
vertices onto fitted planes, rebuilds creases as straight edges and corners as
sharp points; $35 on SuperHive; MIT licensed; plain Python + bpy; only
dependency is numpy, which already ships with Blender).

### Phase 1: Start from the damaged mesh

**Do**
1. Pull a city block from Google Photorealistic 3D Tiles, a drone survey, or any
   photogrammetry pipeline.
2. Confirm the symptoms: walls that ripple, roofs that undulate, ridges that come
   through as saw-tooth, corners that are rounded mush.
3. Reject the usual fixes on their trade-offs: smoothing softens wanted detail;
   remeshing destroys the UVs; decimation smears the baked atlas texture into
   streaks; manual retopology takes a day per building.

**Check**
- The mesh's problems are geometric (planar regions displaced), not shading: a
  smoothing pass would just round the corners further.

**Why**
Every existing fix costs something (detail, UVs, texture, or a day per
building); Planer exists to fix the geometry without paying those costs.

### Phase 2: Run the Planer pipeline (N-panel)

**Do**
1. Install the add-on: Blender 4.2+, Preferences → Add-ons → Install from Disk.
   The panel appears in the 3D Viewport N-panel under the "Planer" tab.
2. Run it on the mesh. Internal order: bilateral normal filtering → planar region
   growing and merging → snap-to-plane with sharp edge and corner reconstruction.
   Regions are gated by area, not face count, so coarse large-triangle tiles
   still qualify.
3. Expected solver behavior:
   - Vertices supported by two planes snap onto the plane–plane intersection
     *line*, so creases come out straight instead of jagged.
   - Vertices supported by three planes snap to the intersection *point* (crisp
     building corners).
   - Topology is preserved on a copy that keeps the original loops, so texture,
     UVs, and material come through untouched: no re-bake, no smearing.
   - Output is always a new `REFINED_` mesh alongside the source; the original
     object is never modified.

**Check**
- Deviation is reported in the status bar as ground truth, not a guess.

**Why**
Flatter is not smoother: "Genuinely planar walls and roof facets. Not smoothed,
solved." Keeping the topology and the original object makes the operation
non-destructive and re-runnable.

### Phase 3: Tune the parameters against the symptoms

**Do** — symptom→fix table from the N-panel settings:

| Symptom | Fix |
| --- | --- |
| Result too rounded, ridges lost | Lower Crease Sensitivity to 0.15–0.20 |
| Not flat enough | Raise Refine Iterations to 3 |
| Small details being flattened | Raise Min Plane Area |
| Nothing gets refined | Lower Min Plane Area |
| Spikes or stretched vertices | Lower Snap Guard |
| Single house or prop, not a block | Lower Min Plane Area to 0.1–0.5 |

**Check**
- Re-run and compare the new report line against the previous one; the
  deviation numbers tell you whether the change stayed faithful.

**Why**
Each parameter targets one failure mode, so tuning is diagnostic rather than
blind tweaking.

### Phase 4: Verify with the report line

**Do**
1. Read the full report line from the status bar: face count in/out, planes
   found, verts snapped (edge, corner), open edges, non-manifold | deviation
   mean / p95 / max in metres. Product-page example:
   `Refined: 14980->14980 faces, 300 planes, 6752 verts snapped (1487 edge,
   129 corner), open edges 4186, non-manifold 4690 | deviation mean 0.024m
   p95 0.121m max 0.741m`
2. Author benchmarks: mean deviation of 7cm on a full city block; on a single
   ~55m building, mean deviation lands around 0.02m, roughly 0.1% of the
   bounding diagonal.

**Check**
- "You are not guessing whether it stayed faithful to the survey; you can read
  it off the report line."

**Why**
A mesh refiner without a deviation report is a guess; the report line is what
makes this a pipeline stage instead of a filter.

### Distilled principles

1. Fix the geometry, not the shading: planar displacement needs solving, not
   smoothing.
2. Never pay for what you can keep: preserve topology, UVs, and the source
   object; output a new mesh.
3. Report deviation or it didn't happen: a stage without metrics is a filter.
4. Gate regions by area, not face count, when the input is coarse survey data.
5. Tune diagnostically: each parameter maps to exactly one failure mode.

---

## Watchlist trending

- Mesh-refinement stage, Planer-class (new 2026-09-27, WATCH)
- Obi Physics rope/ragdoll pattern (new 2026-09-27, WATCH)
- AI video generation via ComfyUI custom nodes (seen again 2026-09-27, WATCH)

## Non-goals (audited, no tooling signal)

- "RAGNAROK ONLINE ZERO GLOBAL FIRST WOE", gameplay footage.
- "Adding DRUG power ups to my Hotline Miami boomer shooter", zero tooling
  keywords, correctly downweighted.
- "Birth of the Universe - Petri Dish Practical Effects", physical practical FX.
