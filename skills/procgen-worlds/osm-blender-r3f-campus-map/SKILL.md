---
name: osm-blender-r3f-campus-map
description: "Build a low-poly 3D map that runs on phones from OpenStreetMap: one Blender Python script generates the campus from footprints plus a CSV and a 30 m DEM, lighting baked to vertex colours and one 2048 px ground texture, glTF Meshopt plus WebP export, React Three Fiber front end, 150k-triangle budget enforced by a CI check script. Trigger when a real place needs a fast, searchable 3D map."
---

# OSM to Blender to R3F Low-Poly Campus Map

## Purpose

This skill reconstructs the exact workflow Roshan Binoj demonstrates for the IIIT Kottayam campus map, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: generate the whole campus from data, bake the lighting once, and enforce a hard budget in CI so phones never pay for realtime shadows.

## Source

Creator: Roshan_Binoj. Post: "I made a low-poly 3D map of my college campus that runs on phones (OSM to Blender to R3F)" https://www.reddit.com/r/threejs/comments/1xyku5f/ (score 38, 7 comments; full post text read) | Live: https://roshanbinoj-iiitk.github.io/iiitk-campus-in-3d/ | Repo: https://github.com/roshanbinoj-iiitk/iiitk-campus-in-3d | 2026-11-18 scout run, audit 1. Inspired by city-in-3D projects, Mumbai 3D in particular.

## Tools used

OpenStreetMap, Blender (one Python generator script), 30 m DEM, glTF with Meshopt + WebP, Next.js (static export), React Three Fiber, zustand, custom shaders (sky, lit windows, colour grading). No named commercial tools.

## Phase 1: Build the campus from data, not by hand

**Do**
1. Feed one Blender Python script three inputs: OSM building footprints, a CSV of floors/colours/roof types per building, and a 30 m DEM.
2. Let the script cut level pads into the hillside and add roads, retaining walls, trees, and the walking network, so the generator rebuilds everything from scratch on every run.
3. Fix what OSM gets wrong in data, not in the mesh: two hostel blocks, their road, and the main forecourt were missing from OSM and some outlines were drawn in the wrong spot. Trace the missing ones from satellite imagery and photos into a separate GeoJSON and add a per-building offset in the CSV to nudge bad outlines.

**Check**
- The generator rebuilds the whole campus from scratch; no hand-placed building survives as a one-off.
- Missing or misplaced outlines are visible in the generated map and traceable to a GeoJSON/CSV entry, not to a manual mesh edit.

**Why**
Data in, mesh out keeps the map maintainable: when OSM or the CSV changes, the campus regenerates instead of needing a remodel. The per-building offset is the admission that map data is approximate, handled as data.

## Phase 2: Bake the lighting, never compute it on the phone

**Do**
1. Bake ambient occlusion into vertex colours.
2. Bake the sun shadow into a single 2048 px ground texture.
3. Export as glTF with Meshopt compression + WebP textures.

**Check**
- Phones render with no realtime shadows at all; the sun follows local time, and at night the windows and street lamps light up (custom shaders, not shadow maps).
- The whole campus model ends up under 800 KB.

**Why**
Baked light is a fixed cost paid once; realtime shadows are a per-frame cost paid on the weakest device. The 2048 px ground texture is the one shadow the map ever needs.

## Phase 3: Enforce the budget in CI

**Do**
1. Set the budget: 150,000 triangles for everything in view, trees included.
2. Run a check script in CI that fails the build if triangles, file size, materials, or textures go over budget.

**Check**
- CI fails loudly on overruns; the budget is a gate, not a guideline.
- Ask for feedback "especially on performance if you try it on an older phone": the check the CI gate cannot do.

**Why**
A budget nobody enforces is a wish. The CI gate is what makes 150k tris and 800 KB a property of the artifact instead of a property of the author's discipline on one day. This is the working pattern behind the Aegis P1 per-asset performance-budget gap and the mesh-compression output-standard gap: the fix artifacts for both exist as FIX PREPARED, and this post is the reference implementation shape for landing them.

## Phase 4: Navigate with data the generator already has

**Do**
1. Export a walking graph with the model; run A* over it for animated walking routes, with uphill legs taking longer.
2. Add building/room search and an orientation tour on top of the same data.

**Check**
- Routes follow the generated walking network and respect uphill costs; search finds buildings and rooms by name.

**Why**
The walking graph is free: the generator already built the walking network, so navigation reuses it instead of maintaining a second map.

## The human method, distilled

1. Generate from data; fix data errors as data (GeoJSON + CSV offsets), never as mesh surgery.
2. Bake once, ship light: vertex-colour AO plus one 2048 px shadow texture replaces realtime shadows.
3. Budgets are CI gates: 150k tris, under 800 KB, fail the build on overrun.
4. Reuse the generator's outputs (walking graph) for features (A* routes) instead of building parallel data.

## Failure modes

- **Missing OSM data:** whole blocks, roads, and forecourts can be absent or misplaced. Trace them from satellite imagery into GeoJSON; never hand-model them.
- **Z-fighting:** commenters report obvious z-fighting in the video ("At least put basic z fighting protection in"). The budget discipline is real; the polish is not. Add z-fighting protection (polygon offset or small vertical separation) before calling the map done.
- **Budget creep:** without the CI check script, the 150k budget decays with every added tree. The gate is the budget.

**Depth status:** FULL (full post text + all 5 top comments read; the native clip itself was not frame-reviewed, and no parameter beyond the author's written breakdown is claimed).
