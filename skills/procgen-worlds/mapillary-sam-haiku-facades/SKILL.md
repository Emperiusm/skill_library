---
name: mapillary-sam-haiku-facades
description: "Paint procedural facade textures on extruded OpenStreetMap buildings from street photos: Mapillary 360 panoramas, SAM 3.1 segmentation, wall-normal fit against OSM, DEM height offset, Claude Haiku structured descriptions with a second Haiku fix pass. Trigger when real map buildings need recognizable facades without photo textures."
---

# Mapillary to SAM 3.1 to Claude Haiku Procedural Facades

## Purpose

This skill reconstructs the exact workflow chartojs demonstrates for procedurally generating details for real map data, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: extract structured facade descriptions from street photos with a vision model, then paint them as procedural textures on extruded real map buildings.

## Source

Creator: chartojs. Post: "Procedurally generating details for real map data" https://www.reddit.com/r/proceduralgeneration/comments/1xytqcn/ (score 31, 5 comments; full post text and the author's full pipeline comment read) | Live demo: http://reakt.io/dash2.html (Porvoo, Finland; lat 60.39667, lon 25.65521) | 2026-11-18 scout run, audit 3. Re-scanned 2026-11-19 (score 44, 9 comments): the author's new tree-placement comment is added in Phase 4 below; the post is otherwise unchanged.

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
5. Place trees from map data, not by hand: OSM already maps many individual trees and patches of forest well. Use the Copernicus Global Dynamic Land Cover 2020 raster (10 m, global, annual) for global coverage and eco-region shapefiles for species selection. The author had GPT Sol researching species and habitats within the hundreds of regions for several months; that research is not reflected in the demo yet, until the pipeline is improved to process the entire globe.
6. Place individual trees in a forest semi-randomly using Owen scrambling.
7. Reject sparse evidence: scenes with only 1–2 matched building corners are rejected. The author's first version marked matching building corners by hand; that did not scale, which is why the pipeline moved to the automatic fit in Phase 1.

**Check**
- It runs on an old iPhone 11, though with short draw distance. Coverage so far: Scandinavia and Baltic countries for the map, facades only in one city (Porvoo). Global coverage and more varied facade test areas are in progress.
- Demo controls (from the author's comment): left button (or one finger) turns the camera, right button (or two fingers) pans, wheel (or pinch) moves backward/forward; on mobile a small joystick sits lower left and a crosshair button upper left enables gyroscope; keyboard uses arrow keys or WASD to turn, number keys for the rest (the comment is cut off at "Number").

**Why**
Everything is generated from map data plus descriptions, so the world scales with the map instead of with an asset library. The iPhone 11 test is the budget check: if it runs there, it runs anywhere.

## AAA studio practice

- **Photo evidence plus historian review is how AAA rebuilds a real city (Ubisoft, Assassin's Creed Unity).** Unity's Notre-Dame is a 1:1 scale recreation built from photographs, on-site documentation, and historian consultation over two years ([Substack](https://chrysadeliou.substack.com/p/notre-dame-in-pixels-and-stone)); Ubisoft dedicated about 5,000 man-hours to the cathedral alone, and a quarter of Paris's buildings have fully navigable interiors ([Gameranx](https://gameranx.com/updates/id/23650/article/assassin-s-creed-unity-creating-notre-dame-in-the-game-took-5-000-man-hours/)). The AAA lesson for this skill is the order of operations: evidence first, interpretation second, and a named gap where data is missing. The skill's wall-normal fit against OSM is the indie version of that discipline.
- **At planetary scale, facades come from typology rules, not from photos (Microsoft Flight Simulator + Blackshark.ai).** Blackshark.ai reconstructed 1.5 billion buildings from 2D satellite imagery for Asobo's Microsoft Flight Simulator: footprints detected by computer vision, heights estimated from shadows, then facade details, roof furniture, and so on applied from building-type rules ([M12](https://m12.vc/news/welcoming-blackshark-ai-to-the-m12-portfolio/), [Tech+](https://techplus.co/flight-simulator-2020-provides-a-worldwide-playset-for-architects-and-urbanists/)). Blackshark is open that about 20% of buildings are off, and at that scale QA is statistical, not per-building. The skill's "uncertain" flag is the same idea at city scale: when the photo evidence is ambiguous, a generic facade beats a confidently wrong one.
- **Inverse procedural modeling infers plausible detail the source imagery lacks (academic, Purdue/ACM).** Zhang et al. automatically generate a 3D procedural city model from a segmented satellite image plus road network, population, and coarse elevation data, producing up to 91,000 buildings over 150 km2 with under 1% parcel-area error in the best case ([NSF PAR](https://par.nsf.gov/servlets/purl/10286871)). The method infers "plausible details that are not present in the source imagery" and yields a complete parameterized model. That is the formal version of the skill's Phase 3: a structured description (here from Haiku, there from a neural parcel estimator) drives procedural detail where the photo runs out.

**Agent automation**
- Write a `facade-manifest.json` per building: facade id, OSM building id, Mapillary photo id, fitted wall normal, confidence (high/ambiguous), and an `uncertain` flag. Any building whose confidence is ambiguous ships the generic facade, never a guessed one.
- Script the Phase 1 regression case: for each hand-checked adjacent-building pair, shift the panorama position by a few metres and its bearing by about a degree and assert the facade still attaches to the right footprint. Log pass/fail per pair; a fail quarantines the facade.
- Validate the Haiku description against a JSON schema (required fields: wall material, window pattern, floor count, color palette) before painting; a description missing a required field goes back for the second Haiku pass instead of being painted with defaults.

## The human method, distilled

1. Correct the photo's position against the map before trusting anything in it (metres and a degree matter).
2. Describe, then re-check with the same model: the second Haiku pass exists because the first one makes "unintentional" mistakes.
3. Prefer recognizable and fast over perfect and heavy: procedural textures from descriptions beat photo textures on size and speed.
4. Ship the regression case with the pipeline: the adjacent-buildings shift test is the acceptance test, not an afterthought.

## Failure modes

- **Facade jumps to the neighbour building:** Mapillary position/bearing error. Run the adjacent-buildings shift test; when evidence is ambiguous, use a generic facade or an "uncertain" flag rather than a confident wrong attachment.
- **"Unintentional" mistakes in the description:** the second Haiku pass exists for these. A single-pass description ships them.
- **Coverage gaps:** facades exist only where street photos and OSM agree. Outside Porvoo, buildings currently have no facades; the pipeline degrades to plain extruded buildings, not to errors.

**Depth status:** FULL (full post text + the author's full pipeline comment; the live demo was not exercised). Distinct from skill `city-diffusion-osm-training` (diffusion-trained city layout) and from `osm-blender-r3f-campus-map` (OSM + CSV generation, no street-photo facades). Expanded 2026-11-19 with the author's tree-placement comment (Copernicus land-cover raster, eco-region shapefiles, GPT Sol species research, Owen scrambling, 1–2-corner rejection) from the re-scanned post.
