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
