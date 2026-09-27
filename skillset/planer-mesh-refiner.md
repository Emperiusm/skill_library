# Skill: Planer-style mesh refinement (EXAMPLE)

- **What:** Detect planar regions in a lumpy photogrammetry mesh, snap
  vertices onto fitted planes, rebuild creases as straight edges and corners
  as sharp points. Non-destructive: outputs a new `REFINED_` mesh, keeps
  topology/UVs/texture.
- **Pipeline stage:** Mesh cleanup / QA, between weld and final QA.
- **Learned from:** "Fix Lumpy Photogrammetry Meshes in Blender: Google 3D
  Tiles" (Nachiket B), https://youtu.be/m9oxz99Ysp0, r/photogrammetry,
  2026-09-27 run.
- **Evidence:** "Genuinely planar walls and roof facets. Not smoothed,
  solved." Product-page report line:
  `Refined: 14980->14980 faces, 300 planes, 6752 verts snapped (1487 edge,
  129 corner) | deviation mean 0.024m p95 0.121m max 0.741m`. Tool: Planer
  add-on, $35 on SuperHive, MIT licensed, Blender 4.2+, numpy only.
- **Workflow (compressed):** Start from the damaged mesh → run the N-panel
  pipeline (bilateral normal filtering → planar region growing/merging →
  snap-to-plane) → tune per symptom (Crease Sensitivity 0.15–0.20 for lost
  ridges, Refine Iterations 3 for not-flat-enough, Min Plane Area 0.1–0.5
  for single props) → verify with the deviation report line.
- **Principle:** Fix the geometry, not the shading; report deviation or it
  didn't happen.
- **Status:** EXAMPLE (marked NEED / adopt-now P1 in the sample run).
