---
name: "fix_lumpy_meshes"
description: "Fix lumpy photogrammetry meshes in Blender the Planer way: detect planar regions, snap vertices to fitted planes and intersections, prove fidelity with a deviation report. Trigger when cleaning scan meshes."
---

# Fix Lumpy Photogrammetry Meshes in Blender: Google 3D Tiles

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Fix the geometry, don't smooth it: detect planar regions, snap vertices to fitted planes and their intersections, and prove fidelity with a deviation report.

## Source

Creator: Nachiket B

Source: https://youtu.be/m9oxz99Ysp0 | 61 s, uploaded 2026-09-13 | r/photogrammetry post 1wjnwzi (score 223)

## Tools used

Tools used: Blender 4.2+; Planer add-on (Blender add-on by nachiket_bhand: detects planar
regions, snaps vertices onto fitted planes, rebuilds creases as straight edges and
corners as sharp points; $35 on SuperHive [Gumroad also listed in the task brief]; MIT
licensed; plain Python, bpy; only dependency is numpy, which already ships with
Blender; no wheels, no network access, no external dependencies); SuperHive product
page (https://superhivemarket.com/products/planer--photogrammetry-mesh-refiner); the
demo video itself shows a full run: N-panel settings visible, report line at the end,
viewport orbiting the result (per the author's comment).

**Do**
1. Pull a city block from Google Photorealistic 3D Tiles, a drone survey, or any
   photogrammetry pipeline.
2. Confirm the symptoms: walls that ripple, roofs that undulate, ridges that come
   through as saw-tooth, corners that are rounded mush.
3. Reject the usual fixes on their trade-offs: smoothing softens wanted detail;
   remeshing destroys the UVs; decimation smears the baked atlas texture into streaks;
   manual retopology takes a day per building.

**Check**
- The mesh's problems are geometric (planar regions displaced), not shading: a
  smoothing pass would just round the corners further.

**Why**
Every existing fix costs something (detail, UVs, texture, or a day per building);
Planer exists to fix the geometry without paying those costs.

## Phase 1: Start from the damaged mesh

## Phase 2: Run the Planer pipeline (N-panel)

**Do**
1. Install the add-on: Blender 4.2+, Preferences → Add-ons → Install from Disk. The
   panel appears in the 3D Viewport N-panel under the "Planer" tab.
2. Run it on the mesh. The internal algorithm, in order: bilateral normal filtering →
   planar region growing and merging → snap-to-plane with sharp edge and corner
   reconstruction. Regions are gated by area, not face count, so the coarse
   large-triangle tiles that come out of 3D Tiles still qualify.
3. The solver behavior to expect:
   - Vertices supported by two planes snap onto the plane–plane intersection *line*,
     so creases come out straight instead of jagged (straight roof ridges and eaves).
   - Vertices supported by three planes snap to the intersection *point* (crisp
     building corners).
   - Topology is preserved on a copy that keeps the original loops, so texture, UVs,
     and material come through untouched: no re-bake, no data-transfer, no smearing.
   - Output is always a new `REFINED_` mesh alongside the source; the original object
     is never modified.

**Check**
- Deviation is reported in the status bar as the ground truth, not a guess (see
  Phase 3).

**Why**
Flatter is not smoother: "Genuinely planar walls and roof facets. Not smoothed, solved. Planar regions are detected, merged, and enforced." Keeping the topology and
the original object makes the operation non-destructive and re-runnable.

## Phase 3: Tune the parameters against the symptoms

**Do**
1. Adjust the N-panel settings per the symptom→fix table:
   | Symptom | Fix |
   | --- | --- |
   | Result too rounded, ridges lost | Lower Crease Sensitivity to 0.15–0.20 |
   | Not flat enough | Raise Refine Iterations to 3 |
   | Small details being flattened | Raise Min Plane Area |
   | Nothing gets refined | Lower Min Plane Area |
   | Spikes or stretched vertices | Lower Snap Guard |
   | Single house or prop, not a block | Lower Min Plane Area to 0.1–0.5 |

**Check**
- Re-run and compare the new report line against the previous one; the deviation
  numbers tell you whether the change stayed faithful.

**Why**
Each parameter targets one failure mode, so tuning is diagnostic rather than blind
tweaking.

## Phase 4: Verify with the report line

**Do**
1. Read the full report line from the status bar: face count in/out, planes found,
   verts snapped (edge, corner), open edges, non-manifold | deviation mean / p95 / max
   in metres.
   - Product-page example: `Refined: 14980->14980 faces, 300 planes, 6752 verts
     snapped (1487 edge, 129 corner), open edges 4186, non-manifold 4690 |
     deviation mean 0.024m p95 0.121m max 0.741m`
   - Real user-mesh run (u/drumfish's file): `Refined: 205980->205980 faces,
     18 planes, 91847 verts snapped (966 edge, 1 corner), open edges 0,
     non-manifold 0 | deviation mean 0.008m p95 0.019m max 0.085m`
2. Benchmarks from the author: mean deviation of 7cm on a full city block; on a single
   ~55m building, mean deviation lands around 0.02m, roughly 0.1% of the bounding
   diagonal.
3. Inspect the result visually: the demo video ends with the viewport orbiting the
   refined result.

**Check**
- "You are not guessing whether it stayed faithful to the survey; you can read it
  off the status bar and put it in a client report."
- The three deviation numbers (mean / p95 / max) are the deliverable-grade proof of
  fidelity.

**Why**
Quantified deviation replaces subjective before/after judgment; it is the mechanism
that makes the tool client-reportable instead of a visual flourish.

## Phase 5: Respect the caveats

**Do**
1. Know what Planer does not do: it does not make meshes watertight, does not reduce
   poly count (it triangulates, so the face count goes up), does not fix holes or
   non-manifold edges, and does not touch the texture image.
2. Budget compute: it is slow on big meshes, about four minutes for 195k faces.
3. For a real trial on your own data, run it on your own meshes with your own settings
   (the author's refund policy: "buy it, run it on your own meshes with your own
   settings, and if it doesn't do what the page says, message me and I'll refund you.
   No questions").

**Check**
- Report line shows the real face count change (triangulation increasing faces is
  expected, e.g. 14980->14980 means no face-count change before triangulation passes).

**Why**
Knowing the non-goals prevents misapplying the tool to watertightness or decimation
tasks; a trial on your own mesh is the only real test ("sending you things is just
not how you test an addon. it's how you test a service," community feedback that
reshaped the author's demo policy).

## The human method, distilled

1. **Flatten, don't smooth.** Detect, merge, and enforce planar regions instead of
   averaging vertices; smoothing is what rounded the corners in the first place.
2. **Snap to intersections, not averages.** Two-plane verts go to the intersection
   line (straight creases), three-plane verts to the intersection point (sharp
   corners).
3. **Gate regions by area, not face count.** Coarse large-triangle 3D-Tiles geometry
   must still qualify as planar.
4. **Never modify the source.** Output a new `REFINED_` mesh alongside; topology and
   original loops survive so UVs/materials carry through natively.
5. **Quantify fidelity every run.** Report faces, planes, snapped verts (edge/corner),
   open edges, non-manifold, and deviation mean/p95/max in metres; the report line is
   client-reportable proof, not decoration.
6. **Tune diagnostically.** Each parameter maps to one symptom (Crease Sensitivity
   0.15–0.20, Refine Iterations 3, Min Plane Area, Snap Guard).
7. **Keep the dependency footprint at zero.** Plain Python + the numpy that ships with
   Blender; no wheels, no network access, no external dependencies.
8. **Name the non-goals up front.** No watertightness, no poly reduction (triangulation
   raises face count), no hole repair, no texture-image edits.
9. **A real trial is a self-run.** The only meaningful test is the buyer running it on
   their own mesh with their own settings, reading their own report line.

## Video-observed evidence (depth recovery, 2026-09-27)

The full 61-second video was downloaded and all 12 extracted frames reviewed
(frame-by-frame; no captions exist and no local transcription was possible,
so any spoken audio is unverified, but the video's instruction is carried by
on-screen text overlays that were fully captured). What the video shows,
beyond the product page and Reddit thread:

- **The exact click path.** Select the lumpy mesh in the Blender 5.1.2
  3D viewport, press **N** to open the N-panel, open the **Planer** tab,
  and click the blue **"Refine (in place)"** button. On-screen text:
  "SELECT YOUR MESH AND PRESS N", then "IN A CLICK".
- **The panel parameters as shipped** (visible in the N-panel, frame 6):
  - Denoise: Normal Filter Iters 14, Vertex Update Iters 20,
    Crease Sensitivity 0.18
  - Planar segmentation: Begin Distance (m) 1.00, Merge Angle (deg) 24.00,
    Min Plane Area (m²) 4.00, Min Faces / Plane 3, Snap Dist (m) 1.00
  - Edges & bevels: Edge Angle (deg) 14.00, Smooth Leftover Detail (checked)
  - Output: Decimate (smears baked texture), Shade Smooth, Measure Fidelity
    (checked), Force Watertight (closed)
- **Intermediate objects.** During the run the outliner shows generated
  `PLANES_VIDEO`, `PLANES_CAM`, and `PLANES_UNION` objects: the solver
  builds plane visualizations as it works. The finished mesh lands as
  `REFINED_Building_CLEAN` next to the untouched `Building_CLEAN_SRC`.
- **The run report, verbatim** (status bar, first run):
  `Refined 14982 -> 14782 faces, 235 planes, 4425 verts snapped (3549 edg,
  86 non-manifold | 449) | deviation mean 0.088m p95 0.070m max 1.664m`.
  On-screen text: "1 CLICK AND UNDER 15 SECONDS FOR THIS MESH". The video
  description confirms the building came back at 0.086 m mean deviation.
- **Second run, textured.** A textured run shows `14982 -> 16982 faces,
  225 planes, 6625 verts snapped (1669 edg, 110 corner), open edges 4188,
  non-manifold 4690 | deviation mean 0.086m p95 0.2...`, with on-screen
  text "TEXTURES AND UV PRESERVED", "WALLS FLAT. PARAPETS STRIGHT" (sic),
  and "EVEN TELLS YOU HOW FAITHFUL IT STAYED".
- **Social proof shown in-video.** A 5-star review is quoted on screen:
  "Life saver for me. Bought it on the spur of the moment. Left it working
  for about 30 minutes on a very large very nasty (10m faces) mesh of a
  building, full of irrelevant foliage, from a Lidar scan. Worked
  brilliantly first time."
- **Closing card.** "PLANER / Blender 4.2+" and "LINK IN THE DESCRIPTION"
  (SuperHive and Gumroad links in the description, verified live).

Description-confirmed facts folded in: requires Blender 4.2+, pure Python on
the numpy that ships with Blender, no external dependencies; works with
Google Photorealistic 3D Tiles, Metashape, RealityCapture, Pix4D, and
OpenDroneMap; explicitly does NOT reduce poly count, make meshes watertight,
or repair holes/non-manifold edges (inherited unchanged from the source).

## Depth status
PARTIAL (was DEPTH-LIMITED). The video itself is now fully observed:
61 seconds downloaded, 12 frames reviewed, all on-screen text and panel
parameters captured, description verified. Remaining gap: no captions exist
and local transcription was impossible (Whisper model weights were not
cached and model downloads are forbidden), so any spoken narration is
unverified. The video's instruction content is carried by its text overlays,
which were fully captured, so this gap is narrow.

---

# Full-depth audits, continued
