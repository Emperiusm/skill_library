---
name: mapillary-sam-haiku-facades
description: "Paint procedural facade textures on extruded OpenStreetMap buildings from street photos: Mapillary 360 panoramas, SAM 3.1 segmentation, wall-normal fit against OSM, DEM height offset, Claude Haiku structured descriptions with a second Haiku fix pass. Trigger when real map buildings need recognizable facades without photo textures."
---

# Mapillary to SAM 3.1 to Claude Haiku Procedural Facades

## Purpose

This skill reconstructs the exact workflow chartojs demonstrates for procedurally generating details for real map data, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: extract structured facade descriptions from street photos with a vision model, then paint them as procedural textures on extruded real map buildings.

## Source

Creator: chartojs. Post: "Procedurally generating details for real map data" https://www.reddit.com/r/proceduralgeneration/comments/1xytqcn/ (score 31, 5 comments; full post text and the author's full pipeline comment read) | Live demo: http://reakt.io/dash2.html (Porvoo, Finland; lat 60.39667, lon 25.65521) | 2026-11-18 scout run, audit 3.

## Tools used

Mapillary (street-level 360 photos), SAM 3.1, Claude Haiku (twice), OpenStreetMap, DEM data, GPT Astra (code-modeled props), WebGL 2. Runs in the browser, including an old iPhone 11 (short draw distance).

## Phase 1: Segment the building out of the street photo

**Do**
1. Take street-level 360 panorama photos from Mapillary.
2. Segment using SAM 3.1.
3. Find near-vertical edges in building pixels.
4. Fix camera tilt/pitch.
5. Inspect every image column with building pixels to collect the angle histogram of edges.
6. Fit the wall normal in lon-lat space.

**Check**
- The regression case, named by commenter ArtificialBeingsInc and unanswered in the thread: take a hand-checked pair of adjacent buildings, shift the panorama position by a few metres and its bearing by roughly a degree, then see whether the facade stays matched to the right footprint or jumps to its neighbour. If the evidence is ambiguous, a generic facade or an "uncertain" flag is safer than confidently attaching the wrong one.

**Why**
Mapillary positions are usually several metres off compared to OSM corner positions, and the bearing can be off about a degree. Fitting the wall normal in lon-lat space against OSM data is what corrects that error instead of trusting the photo's stated position.

## Phase 2: Fit the evidence to the map

**Do**
1. Fit the evidence to OSM data for that location (correcting the Mapillary position/bearing error).
2. Fit the building height offset using DEM data.

**Check**
- The facade lands on the right footprint at the right height; the regression case in Phase 1 is the test.

**Why**
A facade on the wrong building is worse than no facade: it is confidently wrong map data. The fit step is what makes the pipeline map data rather than photo decoration.

## Phase 3: Describe the facade with Haiku, then have Haiku fix its own mistakes

**Do**
1. Rectify the image of a wall segment and pass it to Claude Haiku with instructions for how it should be described.
2. Render using the same style as the browser view.
3. Pass to Haiku again for fixing any "unintentional" mistakes.
4. Store the description (the author cuts off before saying where; the storage format is not stated in the thread, so do not assume one).

**Check**
- The author is candid about quality: "They certainly don't look perfect, but seem recognizable, render fast and take less space than equally sharp-looking photo-based textures."

**Why**
Two Haiku passes separate description from correction: the first pass extracts structure, the second pass catches the mistakes the first pass introduced. Procedural textures from descriptions are smaller and faster than photo textures at equal sharpness.

## Phase 4: Generate the rest of the world from OSM, in code

**Do**
1. Generate bridge, tunnel, and fence meshes on the fly from OSM data.
2. Model street furniture, vehicles, and hundreds of plant species in code using GPT Astra.
3. Extrude OSM buildings and paint the Haiku-described facades on as procedural textures and decals.
4. Serve it in the browser with WebGL 2.

**Check**
- It runs on an old iPhone 11, though with short draw distance. Coverage so far: Scandinavia and Baltic countries for the map, facades only in one city (Porvoo). Global coverage and more varied facade test areas are in progress.
- Demo controls (from the author's comment): left button (or one finger) turns the camera, right button (or two fingers) pans, wheel (or pinch) moves backward/forward; on mobile a small joystick sits lower left and a crosshair button upper left enables gyroscope; keyboard uses arrow keys or WASD to turn, number keys for the rest (the comment is cut off at "Number").

**Why**
Everything is generated from map data plus descriptions, so the world scales with the map instead of with an asset library. The iPhone 11 test is the budget check: if it runs there, it runs anywhere.

## The human method, distilled

1. Correct the photo's position against the map before trusting anything in it (metres and a degree matter).
2. Describe, then re-check with the same model: the second Haiku pass exists because the first one makes "unintentional" mistakes.
3. Prefer recognizable and fast over perfect and heavy: procedural textures from descriptions beat photo textures on size and speed.
4. Ship the regression case with the pipeline: the adjacent-buildings shift test is the acceptance test, not an afterthought.

## Failure modes

- **Facade jumps to the neighbour building:** Mapillary position/bearing error. Run the adjacent-buildings shift test; when evidence is ambiguous, use a generic facade or an "uncertain" flag rather than a confident wrong attachment.
- **"Unintentional" mistakes in the description:** the second Haiku pass exists for these. A single-pass description ships them.
- **Coverage gaps:** facades exist only where street photos and OSM agree. Outside Porvoo, buildings currently have no facades; the pipeline degrades to plain extruded buildings, not to errors.

**Depth status:** FULL (full post text + the author's full pipeline comment; the live demo was not exercised). Distinct from skill `city-diffusion-osm-training` (diffusion-trained city layout) and from `osm-blender-r3f-campus-map` (OSM + CSV generation, no street-photo facades).
