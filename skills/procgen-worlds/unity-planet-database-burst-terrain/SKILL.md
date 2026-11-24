---
name: unity-planet-database-burst-terrain
description: "Build a procedural planet in Unity with a lat/lon planet database queried by a Burst CPU mesh generator, starting from an icosahedron subdivided around the camera. Trigger when a planet must be flyable from orbit to the surface and terrain, water, and atmosphere must all read one queryable source. Distinct from exolune-planet-engine, which evaluates terrain per point on the GPU."
---

# Unity Planet Database + Burst Terrain

## Purpose

This skill reconstructs the exact architecture El-Jomo describes for a procedural planet generator in Unity, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: split the planet into a queryable database and a renderer that queries it, and generate terrain on the CPU per vertex from weighted heightmaps sampled by latitude and longitude.

## Source

Creator: El-Jomo. Post: "Terrain, water and atmosphere done for my procedural planet generator" https://www.reddit.com/r/proceduralgeneration/comments/1y2p5ov/terrain_water_and_atmosphere_done_for_my/ (r/proceduralgeneration post 1y2p5ov, score 184, 22 comments, 18 retrieved; the post text is one line and the architecture comes from the author's comments) | Video: 98-second flythrough from orbit to the surface | 2026-11-23 scout run, audit 7.

## Tools used

Unity with a "quite custom fork" of the Universal Render Pipeline (URP), CPU-side mesh generation with Burst, Claude Code ("coded with heavy assistance from Claude Code"). No Unity version, Burst job details, heightmap sources, or performance numbers are stated.

## Phase 1: Split the system into a planet database and a renderer

**Do**
1. Build two parts, in the author's words: "The first part is the 'planet database'. It's basically a data provider for everything regarding the planet queried with lat,lon."
2. "The second part is the rendering which queries the planet database."
3. Terrain is the worked example: "The terrain for instance is a CPU side mesh generation (Burst) that fetches the landscape ID for each vertex based on their lat lon and samples the weighted heightmaps it needs to figure out how high that vertex needs to go."

**Check**
- Every vertex must resolve through the same query: lat/lon in, landscape ID out, weighted heightmaps sampled, height out. The author states the query shape, not a correctness test.

**Why**
A database queried by lat/lon decouples "what the planet is" from "how it is drawn": the renderer asks, the database answers, and terrain, water, and atmosphere can all read the same source. The author does not state this decoupling principle in those words; it is the shape of the two-part design he describes, labelled here as inference.

## Phase 2: Subdivide an icosahedron around the camera

**Do**
1. "I start with an icosahedron (Townscaper uses a hexagon) and subdivide from there."
2. "The one from Townscaper but subdividing around the camera." The author links an accompanying image; it was not read in this run, and its contents are not described here.
3. Note the author's coastline judgement: "I find that it's a good way to build interesting coastlines. Noises always felt too uniform to me." (also with a linked image, not read.)

**Check**
- The flythrough from orbit to surface is the check offered: detail must appear as the camera descends, without the whole planet being subdivided at once. No subdivision depth, vertex count, or frame time is stated.

**Why**
Subdividing around the camera concentrates geometry where it is seen. Starting from an icosahedron rather than a latitude/longitude grid avoids the pole-pinching a lat/lon grid would carry into the subdivision; that pole point is standard reasoning for an icosphere base, stated here as inference only, not as the author's words.

## Phase 3: Keep the game design question open, and the code Claude-assisted

**Do**
1. Do not treat the flythrough as a finished game. The author is explicit that the design is unresolved: "It's definitely very 'arcady' right now. I am thinking a lot about the game design challenges of presenting a player with an earth sized planet that they can feasibly explore without it involving a lot of passive gameplay."
2. Note the provenance: the code is "coded with heavy assistance from Claude Code".
3. On selling or sharing: "Custom built for my quite custom fork of Unity's Universal Render Pipeline. I'm not interested in the support responsibility that comes with selling a product but I will consider putting in on a public repo."

**Check**
- No repository, asset, or licence is offered today. Do not treat this as an adoptable package; the author has only said he will "consider" a public repo.

**Why**
The author's stated reason for not selling is support responsibility, not secrecy about the method: he describes the architecture freely in comments while declining the product role. The Claude Code note is provenance, not a workflow step.

## Failure modes

- **Uniform coastlines:** pure noise heightmaps, which the author says "always felt too uniform". The database/landscape-ID route in Phase 1 is his answer; the linked coastline image was not read, so no coastline parameters are claimed.
- **Whole-planet subdivision cost:** subdividing everywhere instead of around the camera. Phase 2's camera-following subdivision is the bound; no depth or count is stated, so no budget figure is claimed.
- **Mistaking the demo for a package:** there is no repository or sale. Any adoption plan must start from the architecture description, not from a download that does not exist.
- **Passive-gameplay trap at planet scale:** the author's own open design question. An Earth-sized planet that is feasibly explorable without long passive stretches is unresolved in the source; do not claim the generator solves it.

## The human method, distilled

1. Query, don't bake: a lat/lon database plus per-vertex sampling, subdivided around the camera.
2. Prefer the interesting coastline over the uniform noise: the author's stated aesthetic judgement against pure noise for coastlines.
3. Describe the architecture freely, decline the product role: support responsibility is the stated reason for not selling, and a public repo is only "considered".

## AAA studio practice

**Do**
1. Generate the planet from rules and queries, never store it as a baked map. Hello Games' No Man's Sky stores surface data in a mathematical cube that is transposed onto a sphere in game, with algorithms generating noise for height and further algorithms adding positive space (cliffs, stone structures, floating islands) and negative space (caverns, crevasses, valleys), all folded into the cubic data before the sphere transform. (http://www.polygon.com/2017/3/2/14790028/no-mans-sky-was-flat-procedural-world-generation-maths) The skill's planet database is the same idea in Unity terms: lat/lon in, landscape ID and weighted heightmaps out, with the renderer as a querier. A baked heightmap for the whole planet would be the flat-world shortcut Hello Games rejected, because a shared point of interest must resolve identically however a player arrives at it.
2. Choose the sphere base to avoid projection distortion, and say so. McKendrick's team rejected map projections: Mercator stretches land around the poles, and the Peirce quincuncial projection only works when oceans sit where Earth's oceans sit, which does not generalise to arbitrary generated planets. (http://www.polygon.com/2017/3/2/14790028/no-mans-sky-was-flat-procedural-world-generation-maths) The skill's icosahedron subdivided around the camera is the corresponding choice: start from a sphere-like base with no pole pinch, then spend detail where the camera is. The pole behaviour is a recorded check in Agent automation below, not an assumed property.
3. Stream detail around the camera in nested containers, not by loading the whole world. Cloud Imperium's Star Citizen streams hierarchies of object containers in the background in a multithreaded manner: the planet is a container, an orbiting station is another, and points of interest on the surface are further containers, so travel at great speed keeps macro and micro detail without loading screens. (https://www.digitalfoundry.net/articles/digitalfoundry-2020-star-citizen-tech-focus-alpha-3-point-8) The skill's camera-following subdivision plus lat/lon query is the CPU, single-planet form of that pattern: the database answers for the cells the camera needs, at the detail the camera needs, and nothing else is generated.
4. Define biomes as ranges over shared world parameters, then let artist-placed content propagate through matching ranges. In Star Citizen, temperature and humidity work with a height map to map out texture sets across the planet surface; combinations define biomes, and assets an artist places in one location, tied to a biome range, are also found anywhere with a similar biome type, with procedural generation shaping the world from those rules and precedents. (https://www.digitalfoundry.net/articles/digitalfoundry-2020-star-citizen-tech-focus-alpha-3-point-8) The skill's landscape ID plus weighted heightmaps is the same contract: the ID is the biome range, the heightmaps are the shared parameters, and propagation through matching ranges is the behaviour to test, not an accident of sampling.
5. Treat coordinate precision as a first-class design decision, and record it as open if it is open. Star Citizen converted its engine to 64-bit coordinates to enable solar-system-sized spaces, 536,870,912 times larger than a 32-bit float space. (https://www.digitalfoundry.net/articles/digitalfoundry-2020-star-citizen-tech-focus-alpha-3-point-8) No Man's Sky, working on spherical worlds, had to reference each world's centre point constantly to know which way was down from the player's perspective. (http://www.polygon.com/2017/3/2/14790028/no-mans-sky-was-flat-procedural-world-generation-maths) This skill states no coordinate type, origin strategy, or precision plan for an Earth-sized planet. That gap stays labelled as an open decision in the manifest, with the pole and antipode probes below, until the author records an approach. Do not assume float32 lat/lon queries stay precise at planet scale.
6. Prefer rules plus precedents over hand placement at planet scale, and measure the saving honestly. Cloud Imperium remade all of its pre-existing moons and planets in a few months with its new rules-based system, after nearly two years of manual creation. (https://www.digitalfoundry.net/articles/digitalfoundry-2020-star-citizen-tech-focus-alpha-3-point-8) The skill's database is justified the same way only if the determinism and propagation checks below pass: rules that cannot reproduce the same planet twice, or that propagate only where an artist stood, are not the saving Star Citizen reports.

**Check**
- Query stability: the same lat/lon query returns the same landscape ID and height on every run, for every sampled point. A point of interest must resolve identically however it is approached, which is the permanency requirement that killed Hello Games' flat-world attempt.
- Camera concentration: during an orbit-to-surface descent, subdivided cells concentrate around the camera. Subdivision of the far side at surface detail is a failure of the streaming pattern, whatever the frame rate.
- Biome propagation: an asset or landscape type placed in one biome range appears in other sampled locations with the same range, or the manifest records the exception. Propagation that happens only at the artist's placement point is hand placement with a database label.
- Precision recorded: the manifest states the coordinate type and origin strategy, and the pole/antipode probes pass. An unrecorded precision approach is an open gap, not a default.

**Why**
Shipped planet-scale work is a query discipline: a compact ruleset plus a queryable world description, detail streamed around the viewer, biomes as parameter ranges, and precision handled as a design problem rather than discovered at the poles. This skill already has the database and the camera-following subdivision; the AAA practice is to prove query stability, propagation, and precision with tests, since those are the three properties that separate a planet database from a demo that only looks like one from orbit.

## Agent automation

1. **Planet query manifest.** Keep `planet-query-manifest.json`: database version, heightmap sources and weights, subdivision depths, the lat/lon query contract, coordinate type, and origin strategy. A script asserts every vertex height resolves through the lat/lon query path, with no direct heightmap reads bypassing the database.
2. **Determinism hash gate.** Query a fixed set of lat/lon points at a fixed seed, hash the returned heights, and fail the run when the hash changes without a recorded database change. A changed hash with no recorded change is a regression, not a new planet.
3. **Camera-follow subdivision audit.** Log subdivided cells per frame during a scripted orbit-to-surface descent and assert cells outside a recorded radius of the camera stay at base subdivision. The radius is operator-recorded; this skill invents no distance value.
4. **Pole and antipode probes.** Query lat/lon points at the poles, the antipode, and the date-line seam and assert finite, non-degenerate heights with no NaN or duplicated pole vertex fan. A probe failure is a precision or seam bug, and the manifest records the coordinate approach that produced it.
5. **Biome propagation check.** For each landscape ID, query a recorded sample of lat/lon points inside its biome range and assert the same landscape ID returns. A range that returns different IDs at different points is either a range definition error or an unrecorded exception, and the manifest must say which.

**Depth status:** FULL (comment-architecture only). The two-part design, Burst CPU generation, lat/lon query, weighted heightmaps, and icosahedron subdivision are exact from author comments. Missing: Unity/URP fork details, heightmap sources and weights, subdivision depths, vertex counts, frame times, and the linked images (not read). A media download of the 98-second flythrough would show the result, not the undisclosed parameters. Distinct from `exolune-planet-engine`, which simulates plates at startup and evaluates terrain per point on the GPU each frame; this skill queries a database on the CPU.
