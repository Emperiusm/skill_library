---
name: city-diffusion-osm-training
description: "Train a diffusion model from scratch on rasterized OpenStreetMap data to generate conditioned 512x512 city layouts, extend maps with context preservation, and build worlds in a custom editor. Trigger when generating city layouts that need real spatial statistics."
---

# CityDiffusion2: Diffusion Models for Procedural Cities

## Purpose

This skill trains a diffusion model **from scratch** (no pretrained
checkpoint) on rasterized OpenStreetMap data so it generates city
layouts with real spatial statistics — conditioned on rural/urban/water
mix, extendable while preserving context — and edits them in a
purpose-built editor. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle). The
core method is: pixels now (diffusion needs them), vectors later
(engines need them), and train bespoke when the domain is
off-distribution.

## Source

r/proceduralgeneration, bart1259 (full post text + 23-comment technical
thread, 2026-10-30):

- https://www.reddit.com/r/proceduralgeneration/comments/1xinh91/diffusion_models_for_procedural_cities
- Code: https://github.com/bart1259/CityDiffusion2
- Dataset: https://huggingface.co/datasets/bart1259/netherlands_512_2m
- Model: https://huggingface.co/bart1259/CityDiffusion2

Evidence note: architecture hyperparameters and training compute are
not disclosed; everything below is the author's stated method plus
attributed community discussion.

## Tools used

Custom diffusion model, **initialized with random weights and trained
from scratch** on the Netherlands dataset (the author's phrasing:
"Pretrained from random weights on the dataset" — read as: no
pretrained checkpoint). OpenStreetMap vector data, Netherlands.
Rasterization script **`02_mill_tiles`** (in the repo's training
folder). Stable Diffusion VAE — **tried for fine-tuning, abandoned**:
"the VAE decoding was blurry (which makes sense as SD was probably not
trained on maps)." Author's custom editor for building worlds.

## Phase 1: Rasterize the map vectors into images

**Do**
1. Take OpenStreetMap vector data for the Netherlands.
2. Rasterize it with the `02_mill_tiles` script (in the training
   folder). "Road networks are also rasterized the same way."
3. Produce **512x512 tiles representing 1km x 1km**.

**Check**
- Look at the training sample
  (CityDiffusion2 repo, docs/training_data.png): roads, rural/urban
  areas, and water must be legible as pixels.

**Why**
Diffusion on the vector representation is "likely impossible" — the
author's own judgment, confirmed by commenter thattiguy. Pixels are
the tractable representation for diffusion; vectors are the roadmap
(Phase 4).

## Phase 2: Train from scratch — do not fine-tune Stable Diffusion

**Do**
1. Initialize a diffusion model with **random weights** and train from
   scratch on the rasterized Netherlands dataset.
2. Predict noise **on pixels directly**, not latent noise.

**Check**
- If outputs look map-blurry, the VAE is the suspect: the author's
  failed experiment (fine-tuning SD with its VAE) produced blurry
  decodings.

**Why**
SD was "probably not trained on maps"; training the VAE alongside
would have taken too long, "so I changed it up to just predicting
noise on pixels." The author's ML-fundamentals principle, stated
after pushback in the thread: when the domain is off-distribution,
train bespoke with full control over dataset, architecture, training,
and regularization — versus "just slopping output from a
general-purpose AI with some alignment prompt."

## Phase 3: Generate conditioned layouts, extend with context

**Do**
1. Condition generation on **rural/urban/water mix settings**.
2. Generate 512x512 (1km x 1km) city layouts.
3. Use the author's editor to create custom procedural worlds: the
   model can "extend a map while preserving existing context."

**Check**
- Extend an existing map: does the continuation preserve context
  (roads continue, density matches)?

**Why**
The model is an authoring assistant, not a one-shot generator; the
editor is part of the product, not an accessory.

## Phase 4 (roadmap, author-stated): go vector

**Do**
1. Accept the current limit, stated by the author: "The model only
   considers a 1km x 1km area for context so it has no understanding
   of what roads are major or if it should continue a river."
2. Planned: train a **mini LLM** to generate maps as **vectors** — "so
   its easier to use for downstream applications" (a game engine can
   consume vectors directly). One proposed ordering: pretrain to build
   road networks first, then propose zoning, then building locations.
3. The author is still working out "what the training objective should
   look like" for the vector model.

**Check**
- (Inference) Judge any vector attempt on road-network connectivity,
  not pixel plausibility.

**Why**
Pixels are the stepping stone; the destination is engine-consumable
vectors. The author invites training-objective ideas — the ordering
of vector data (roads -> zoning -> buildings) is the open design
question.

## AAA studio practice

The skill's core bet — real spatial data in, procedural city out — is
exactly how AAA city pipelines start, except production keeps humans in
the loop and defers ML.

**Esri CityEngine: OSM-data-in city authoring.** CityEngine is a
procedural 3D modeling tool whose gaming/VFX customers include Turn 10
Studios and EA. The vendor-published workflow mirrors this skill's
premise: "grab an area of the world… import the 3D terrain data from
Esri and the OpenStreetMap data to quickly create a 3D city that you
can further modify to fit your needs" — OSM raster/vector data in,
procedural 3D city out. Its production round-trip is worth copying:
hand-made hero assets come in from Maya/3ds Max, the procedural
environment is modeled around them, and everything exports back out
individually or together into the DCCs or the game engine.
(Source: https://80.lv/articles/esri-cityengine-generating-global-urban-landscapes —
80 Level interview with Esri's Woody Hynes, SIGGRAPH 2016.)

**Embark Studios "Building Creator" (THE FINALS, ARC Raiders): modular
Houdini pipeline.** Technical artist Adrian Björkerud's Building
Creator is a set of interoperable HDAs: artists assemble buildings
from reusable Feature Nodes (walls, floors, roofs, windows, doors),
and every building starts from a blockout mesh as the shared spatial
context for all nodes. The automation gates are the transferable
part: blockout-to-fractured-asset turnaround of **4–6 minutes per
change**, **100+ unique buildings** produced across both games, and
collision plus occluders fully automated with "no manual work."
Their fracturing discipline is a concrete gate this skill can cite:
assets are pre-fractured in Houdini with seams hidden until damage
occurs; real-time fracturing was rejected as "too costly and
unpredictable for fast-paced multiplayer."
(Source: https://80.lv/articles/how-embark-studios-built-procedural-environments-for-the-finals-using-houdini —
80 Level, March 2026.)

**Ubisoft "Building a better Paris" (Assassin's Creed Unity): data-first
authoring.** World level design director Nicolas Guerin studied
**150+ city maps over ~3 months** to ground the 1789 Paris layout —
the AAA version of training on real map data. Layout discipline:
"radial scale" — **1:1 recreation at the city core, 1:3 mid-city,
1:6 outer**, landmarks kept in true relative position, city divided
into **seven districts**, total surface space **21.4 sq km**.
Hand-authoring benchmark: level artist Caroline Miousse spent roughly
**2 years** building Notre Dame 1:1, working with a historian.
(Source: https://cassiescerbo.s3.uk.io.cloud.ovh.net/news/building-a-better-paris-in-assassin-s-creed-unity.html —
republished Ubisoft story, Oct 31, 2014; corroboration:
https://www.destructoid.com/paris-will-be-the-true-star-of-assassins-creed-unity/.)

**Marked as inference, not verified:** this run found no named-studio
production case of *diffusion/ML* used specifically for city-layout
generation — diffusion-for-cities remains a research/hobby frontier,
which is what makes the skill's from-scratch training the defensible
move. Also unverified: the frequent claim that CityEngine was used on
AC Unity's Paris; confirmed only for AAA gamedev customers generally.

## Agent automation

**Do**
1. **Dataset manifest gate** (agent design): before training, write
   `dataset-manifest.json` pinning the OSM extract date, region
   bounding box, tile size (512x512 = 1km x 1km), and tile count. Any
   regeneration run re-asserts byte-identical raster output from the
   same manifest.
2. **Blur gate** (agent design): run an advisory variance-of-Laplacian
   sharpness check over a generated-layout sample; reject the batch if
   median sharpness falls below the acceptance renders — the scripted
   version of the skill's VAE-blur failure mode (same sharpness-column
   technique used in the library's adaptive-frame-extractor).
3. **Vector-roadmap connectivity gate** (agent design; the author
   invites training-objective ideas, so the gate is ours, not the
   author's): on any future vector output, export the road network as
   a node/edge list and assert the major-road graph is a single
   connected component. Judge vector attempts on connectivity, never
   on pixel plausibility (per the author's Phase 4 check).
4. **Context-preservation regression** (agent design): the skill's
   Phase 3 "extend while preserving context" becomes a scripted test —
   extend a fixed fixture map, then assert road-centerline continuity
   and density-delta bounds at the tile boundary before accepting.

**Check**
- All four gates are scripts that exit non-zero on failure; none
  require a human to eyeball a render.
- The blur gate's acceptance threshold comes from the skill's own
  training_data.png sample, never from an invented number.

**Why**
Production city pipelines are data-in plus gates, not data-in plus
hope. These gates convert the skill's stated failure modes (blurry
decodings, broken networks, unverifiable context preservation) into
the Embark-style automated turnaround the AAA sources demonstrate.

## The human method, distilled

1. **Train bespoke when the domain is off-distribution.** General
   pretrained models fail on maps; training from scratch on the
   domain data is the answer, stated plainly.
2. **Representations first, in order.** Pixels now because diffusion
   needs them; vectors later because engines need them.
3. **Admit the context limit.** 1km x 1km with no notion of major
   roads or continuing rivers — the author's caveat, not the
   critics'.

## Failure modes

- **Blurry decodings:** the VAE route. Fix: train on pixels directly;
  fine-tuning SD's VAE on maps is the known-bad path.
- **Plausible pixels, broken networks:** 1km context can't carry major
  roads or rivers across tiles. Fix: context-preserving extension in
  the editor (current) or the vector roadmap (future).
- **Pretrained-from-random confusion:** the author's phrase confused
  readers. Fix: read it as "no pretrained checkpoint; trained from
  random weights on the domain dataset."

**Depth status:** FULL (author post text + 23-comment technical thread
with detailed ML answers; hyperparameters and compute undisclosed).
