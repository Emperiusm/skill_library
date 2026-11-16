---
name: claude-fable-rust-flight-sim-3d-tiles
description: "Build an open-world flight sim in Rust in about a week with Claude Fable 5.2 (architecture) and Opus 5.5 (code), from plan docs, then replace the procedural world with Google Photorealistic 3D Tiles: measured datum, coverage-mask blending, destructible mesh buildings, and published fps/MB numbers. Trigger when an agent-built game needs a real-world photoreal layer with destruction and honest measurements."
---

# Claude-Built Rust Flight Sim with Google Photorealistic 3D Tiles

## Purpose

This skill reconstructs the author's exact workflow, step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The project's core method is: let Claude build a Rust flight sim in a week
from plan docs, then replace the procedural world with Google's photoreal
mesh where it exists, and measure everything.

## Source

Creator: ImpactIntelligent218. Reddit post:
https://www.reddit.com/r/aigamedev/comments/1xwf9rv/im_a_huge_fan_of_microsoft_flight_sim_2024_but/
(r/aigamedev post 1xwf9rv, score 458, 182 comments; cross-posted
r/vibecoding 1xwdvhf, score 385) | 2026-11-15 scout run, audit 7.
Repo: https://github.com/Rolandjg/fableflight (open source). Plan doc:
`docs/photorealistic-3d-tiles-plan.md` (read in full this run).

## Tools used

Rust, wgpu (the plan doc names WGSL shaders), Claude Fable 5.2
(architecture) and Opus 5.5 (code), Google Photorealistic 3D Tiles (Google
Maps 3D Tiles API), OpenStreetMap (aeroway lines, z14 vector tiles).

## AAA studio practice

- **Microsoft Flight Simulator is the shipped reference for exactly this problem, and it splits the world the same way the plan doc does (Microsoft/Asobo, Blackshark.ai).** Bing Maps photogrammetry "only yielded exact 1:1 replicas of 400 cities — for the vast majority of the planet, though, that data doesn't exist. Microsoft and Asobo Studios needed a system for building the rest." Blackshark.ai reconstructed 1.5 billion buildings from 2D satellite images by computer vision (footprints, heights from shadows), because "at these numbers, you cannot do traditional Q&A anymore" ([TechCrunch, via Blackshark interview](https://socmedtech.com/news-media/techcrunch-128/18/08/2020/)). MSFS 2024 streams about 5 GB per hour from Azure, and its ground-classification ML was trained on 28,000 tiles in four stages ([GamingBolt, MSFS 2024 graphics analysis](https://gamingbolt.com/microsoft-flight-simulator-2024-graphics-analysis-a-gorgeous-sequel-that-needs-more-optimization)). The plan doc's split (photoreal mesh where it exists, procedural world elsewhere, coverage mask blending the two) is MSFS's architecture at one-developer scale: the difference is that MSFS's procedural side is AI-reconstructed buildings, while this project's is hand-built.
- **The datum problem has a standard engine-side answer: georeference, don't reproject (Cesium for Unreal).** Cesium's tutorial for Google Photorealistic 3D Tiles in Unreal: add the tileset through Cesium ion, then "use the CesiumGeoreference component to geoposition your scene on the globe," because "by default, Unreal Engine does not account for many geospatial variables, such as Earth's curvature or its radial direction of gravity." CesiumSunSky supplies realistic light intensity for the relighting step ([Cesium, Photorealistic 3D Tiles tutorial](https://cesium.com/learn/unreal/unreal-photorealistic-3d-tiles)). The plan doc's measured-datum approach (measure the WGS84-to-sea-level offset per area instead of shipping a geoid model) is the same principle with the georeference done by measurement rather than by a component; the check to copy from Cesium is the datum regression below.
- **Photoreal tiles are the slow path in production flight sims, and the tuning knob is screen-space error (Cesium community, flight-sim users).** "Cesium for Unreal has been used for a variety of flight simulators... most of these applications use Cesium World Terrain with Bing Maps Aerial imagery, which have more manageable payloads for real-time flight visualization. Google's Photorealistic 3D Tiles offer high visual fidelity (especially with all the available city photogrammetry), but naturally the higher detail will take longer to load." The recommended tuning: adjust Maximum Screen Space Error (lower number prompts higher detail) and MaximumSimultaneousTileLoads, and disable frustum culling so tiles load outside the camera frustum ([Cesium Community](https://community.cesium.com/t/resolution-streaming-google-3d-tiles/44919/2)). The plan doc's numbers (100 MB a minute over a city, 600-650 MB GPU budget) are the same conversation in measured form; the Cesium knob is what to turn when those numbers are too high.
- **Agentic game dev at AAA is writer-in-the-loop, not hands-off (Ubisoft La Forge, Ghostwriter, GDC 2023).** Ghostwriter, unveiled at GDC 2023, generates first drafts of NPC barks; "the machine learning model learns from each selection" as writers accept or regenerate lines, and it is explicitly not used for cinematics or lore. "Ghostwriter isn't replacing the video game writer, but instead, alleviating one of the video game writer's most laborious tasks" ([Game Developer, GDC 2023](https://www.gamedeveloper.com/marketing/here-are-more-details-on-ubisoft-s-narrative-ai-tools-from-gdc-2023?hl=en-US)). The author's split (Fable 5.2 for architecture, Opus 5.5 for code, plan docs as the interface, human judging the visuals) is the same shape: the model drafts, the human selects and polishes, and the plan doc records what the plan got wrong.

## Phase 1: Build the game with Claude, from plan docs

**Do**
1. Write plan docs first. The repo's `docs/` holds
   `photorealistic-3d-tiles-plan.md`, dated 2026-11-13, with phases 1 to 5
   marked in as a first version.
2. Let Claude Fable 5.2 do architecture and Opus 5.5 do code (author's title:
   "I had Fable 5.2 and Opus 5.5 make my own flight sim!"). Build in Rust,
   in about a week (author's selftext).
3. Keep the project open source and free to download, compile, and play
   (`cargo build --release`, `cargo run --release`).

**Check**
- Commenter Subject_Perception62 asked the process questions the thread never
  answered: "How did you structure the work? Did you write plan docs first
  (like the 3D tiles one in docs/), and roughly how many sessions or tasks
  did it take? How did Claude check the visual output? Did you feed
  screenshots back to it, or did you judge everything yourself and describe
  what was wrong? What made you pick Fable over Opus for the rendering side,
  and did you hit usage limits a lot with the two Plus subscriptions? Did you
  already know wgpu / graphics programming before, or did you learn it along
  the way?" No OP answers appear in the fetched comments. The plan doc itself
  is the evidence that plan docs came first.
- The game is "fairly performant for how detailed the graphics are" and was
  recorded on the author's RTX 3060 (vibecoding cross-post selftext).

**Why**
- Plan docs are the interface between the human and the models: the doc is
  dated, phased, and updated with what the plan got wrong ("What the plan got
  wrong or left open, now settled"). (Inference from the doc's structure, labeled.)

## Phase 2: Ingest Google Photorealistic 3D Tiles

**Do**
1. Fetch Google's photoreal tiles. Settle the format facts first: "No Draco.
   Google serves plain glTF: float positions, u8/u16 indices, 256-1024 px
   JPEGs (one per primitive; a third of the tiles have two or three),
   KHR_materials_unlit, a y-up node matrix. No decoder library is needed; a
   Draco tile would be logged and skipped." (plan doc)
2. Handle billing as sessions: billing is per root request (`root.json`,
   max-age=0); child tiles carry the session in their URLs; tiles say
   max-age=14400; nothing is cached on disk. The usage panel counts roots
   (billed sessions) apart from tiles.
3. Fix the datum. Mesh heights are WGS84 ellipsoidal; the project's heights
   are sea level. Rather than ship a geoid model, measure the offset:
   terrain minus mesh at sample vertices, against fine terrain tiles only,
   taking the densest metre of the upper half of the distribution (roofs and
   trees only pull it down). San Francisco gives +32.4 to +32.7 m downtown
   and in the Marina, matching the EGM96 geoid there (about -32 m). The zone
   stays off until the datum is known.
4. Transform each vertex ECEF to lat/lon/ellipsoid height to the project's
   sphere, on worker threads; draw tiles camera-relative with the datum as a
   radial lift.
5. Blend the mesh into the world: render the drawn tiles top-down each frame
   into a 4096 px coverage mask (red). Terrain, buildings, roads, trees (all
   three kinds), street cars, and airfield pavement discard where the mask is
   set; the mesh and the world dither into each other across a 1.6 km band at
   the 9 km edge of the zone. Airport aircraft, runway lights, and the
   player's aircraft are kept.
6. Handle water: the project's water stays inside the zone. The project's
   terrain water is rendered into the same mask (green, its surface height),
   and the mesh gives way within 2 m (plus 12% of the tile's geometric error)
   of it, so piers, hulls, and bridges stand out of the waves.
7. Relight the photos by the project's sun (since 2026-11-14; before that
   they were lit as albedo, mostly flat: 70% up, 30% the true normal, with
   shadows from the aircraft only). Keep the zone on at night (since
   2026-11-13; before that it shrank to nothing at dusk).
8. Use the zone everywhere by day, including outside cities: "Outside cities
   Google's mesh is still better than ours (real desert and farmland
   colours), so the zone is used everywhere by day."

**Check**
- Verified by flying over San Francisco, KSFO, the Davis farmland, and the
  Nevada desert (plan doc).
- Landing on the KSFO mesh runway and crashing into mesh towers both work
  (physics section).
- The datum, once measured, "only drifts within 4 m (it used to wander tens
  of metres among downtown towers)" after excluding samples on the project's
  own buildings' footprints.

**Why**
- Measure the datum, do not ship a geoid model: one measured offset per area
  is cheaper and more accurate than a global model. (Plan doc's own reasoning.)
- A coverage mask plus a dither band is how two worlds share one screen
  without a visible seam.

## Phase 3: Make the mesh destructible

**Do**
1. On a crash into the mesh, match to the nearest of the project's (hidden)
   footprints within 5 m (`World::photo_building`); it comes down as usual
   (`destruct.rs`).
2. Cut its outlines out of the mesh (`Photo::take_building`, up to 16 cuts in
   the shaders, `photo_cut` in common.wgsl), grown up to 2 m short of the
   neighbours (`World::cut_rings`): nothing above the street there is drawn
   or stands, and the project's own ground shows through.
3. Hand over the finest tiles in memory over the cut (seen or not): split
   their triangles to about a metre (0.3 m round the aircraft's hole), give
   them to the nearest piece of outer wall or roof, and draw them with their
   tile's texture on that piece's slot (`vs_skin` in photo.wgsl), so the real
   building leans, breaks, and falls. Standing walls are not drawn (the mesh
   is the building); pieces move onto the mesh they carry and take its mean
   colour.

**Check**
- The video's crash physics is the point of the post (the author built the
  sim because MSFS 2024's crash physics disappointed him). The plan doc
  records the feature as landed 2026-11-14 (`src/skin.rs`).

**Why**
- Destruction is a cut plus a re-skin: remove the mesh where the building
  was, then re-clothe the falling pieces in the building's own photographed
  texture. Real photos make the wreckage read as real.

## Phase 4: Smooth the pavement

**Do**
1. As each tile is decoded, before its normals and collision grid, smooth the
   vertices on a carriageway (`roads::carriageway`, a little short of the
   kerbs) or on paved runways, taxiways, helipads, and aprons (OSM aeroway
   lines and polygons, z14 vector tiles fetched on the worker threads).
   (Plan doc, 2026-11-13, `src/pave.rs`; the doc continues past where this
   skill quotes it.)

**Check**
- Photogrammetry roads and runways are lumpy ("cars melted into the street,
  half-metre waves, noise"). Smoothing is what makes them drivable and
  landable.

**Why**
- Photogrammetry is honest about what the camera saw, including the noise.
  Pavement needs a separate pass because a road is a designed flat surface,
  not a scanned one.

## Phase 5: Physics on the mesh

**Do**
1. Let `World::ground` return the top of the mesh: a per-tile grid of
   triangles, finest tile first, blended in over 2.5 s when a tile arrives.
   The project's buildings and trees under the mesh are not there for
   collisions either.

**Check**
- Landing on the KSFO mesh runway and crashing into mesh towers both work.

**Why**
- The mesh is the ground where it exists. Blending over 2.5 s hides the
  pop when a finer tile arrives.

## Phase 6: Measure everything, in public

**Do**
1. Measure on the dev machine (RTX 3060, 1600x900): over the Marina, 62-82
   fps with the mesh against 41-47 fps without it ("our buildings and trees
   cost more than the mesh"); the discards cost nothing measurable when the
   zone is off.
2. Budget GPU memory: 600-650 MB (budget 640 MB, least recently drawn first
   out).
3. Budget bandwidth: about 100 MB a minute of downloads over a city once
   loaded (90 MB for the first load).

**Check**
- The mesh is faster than the procedural world it replaces. That is the
  number that justifies the whole feature.

**Why**
- A photoreal mesh that costs less than the procedural buildings is a free
  win; the measurements are what prove it is free.

## Phase 7: Extend the measurement discipline to the tiles

Phases 2 to 6 already measure fps, MB per minute, and GPU memory. The
tile pipeline needs the same treatment for the three numbers that can
silently regress: datum drift, session/billing counts, and the destruction
cut budget.

**Do**
1. Write `tiles-manifest.json` per zone: datum offset measured (with the
   area and the sample method, per Phase 2), billed root sessions counted
   in the usage panel, tiles downloaded, MB per minute over the zone,
   and GPU memory used by tiles.
2. Run the datum regression on every zone change: re-measure the offset
   the plan doc's way (terrain minus mesh at sample vertices, densest
   metre of the upper half). The plan doc's own bound is 4 m of drift
   after excluding the project's own building footprints; if a zone
   drifts more than 4 m, the zone stays off until the datum is
   re-measured, exactly as Phase 2 requires.
3. Run the destruction cut gate: the shader supports up to 16 cuts
   (`photo_cut`); count the live cuts in a crash test scene and fail the
   gate if a scene needs a 17th. The 16-cut limit is a shader constant,
   not a suggestion.
4. Record the tile-quality tradeoff per zone the Cesium way: the maximum
   screen-space error (or the project's equivalent refinement setting)
   that produced the measured fps, so a later reader can reproduce the
   62-82 fps number instead of guessing which refinement level it was.

**Check**
- `tiles-manifest.json` exists per zone with datum, sessions, MB/min,
  and GPU memory.
- No zone drifts more than 4 m from its measured datum.
- No crash test needs more than 16 cuts.
- The refinement setting behind the published fps is recorded.

**Why**
- MSFS's lesson is that at planetary scale you cannot do traditional QA;
  the numbers are the QA. A zone whose datum, billing, and cut budget
  are all in a file is a zone that can be trusted at a distance.

## The human method, distilled

1. Plan docs first, then models, then measurements. The doc records what the
   plan got wrong and what settled it.
2. Measure the datum; do not ship a geoid model.
3. Two worlds share one screen through a coverage mask and a dither band.
4. Destruction is a cut plus a re-skin in the building's own texture.
5. Photogrammetry needs a pavement pass: roads are designed flat, scans are not.
6. Publish the numbers (fps with and without, MB per minute, MB of GPU mem).
   The numbers are the argument.
7. Build the sim you wish existed because the one you love disappoints you
   on one axis (crash physics). Scope the whole project to that axis.

**Depth status:** FULL. Selftext plus 182 comments plus the repo README plus
the full 3D Tiles plan doc with exact numbers, file names, and shader entry
points. The one open thread is the process questions (sessions, visual
checking loop, Fable vs Opus choice, usage limits), which the OP never
answered in the fetched comments.
