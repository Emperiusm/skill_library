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

**Depth status:** FULL (comment-architecture only). The two-part design, Burst CPU generation, lat/lon query, weighted heightmaps, and icosahedron subdivision are exact from author comments. Missing: Unity/URP fork details, heightmap sources and weights, subdivision depths, vertex counts, frame times, and the linked images (not read). A media download of the 98-second flythrough would show the result, not the undisclosed parameters. Distinct from `exolune-planet-engine`, which simulates plates at startup and evaluates terrain per point on the GPU each frame; this skill queries a database on the CPU.
