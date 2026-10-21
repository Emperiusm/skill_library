---
name: "minecraft_world_gen"
description: "Generate massive voxel worlds from one block with deterministic sampling and LOD. Trigger when building large-scale procedural terrain."
---

# The Entire Minecraft World, From One Block to 3.6 Billion km²

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Scale through sampling: build the world from one block with deterministic sampling and LOD so billions of square kilometers stay traversable.
**Core trick (stated by the author):** "No CG or AI, rendered entirely in game and to scale." The world is shown through progressively higher/lower-detail LOD textures generated from the world seed, rendered in a separate dimension mapped 1:1 to overworld coordinates.

## Source

Creator: u/ImolaBoost

Source: https://v.redd.it/zzrkz89e6drh1 | r/proceduralgeneration post 1wonb8q (score 176) | native clip (demo, not tutorial)

## Tools used

Tools used: Minecraft (Java edition implied), a custom mod written by the author, plus the third-party Distant Horizons mod (used in the video for near-field terrain; stops applying at the dimension transition).

## Phase 1: Query the seed, never generate chunks

**Do**
1. Exploit the fact that Minecraft world seeds are deterministic and queryable: you can ask "what would be here" at any coordinate without generating the chunk (author's words).
2. Sample the world generator at a per-LOD granularity ("sampled per x units"; the exact step size is not stated).
3. Bake the sampled world gen onto one massive to-scale texture. Each pixel represents the average of what it represents (terrain type/color of its footprint).

**Check**
- Every portion of the overworld map must be represented, whether previously generated or not.
- At the highest LOD the texture must portray the map at near block-per-pixel accuracy.

**Why**
Rendering the full world in chunks is, per the author, "physically impossible," so the only tractable route is to reduce the world's surface to a 2D summary image built from the same deterministic generator the game itself uses. The average-per-pixel bake keeps each texel honest about its footprint.

## Phase 2: Build the LOD pyramid

**Do**
1. Build progressively higher/lower-detail LOD texture versions of the baked world map.
2. Put the lowest LOD of the entire world on a single plane ("generating the entire world on one plane at the lowest LOD"), which is also much faster than per-chunk approaches.
3. For higher resolutions, keep only local LOD tiles ("I only include local LOD for higher res tiles") instead of one giant high-res texture. Divide the tiles per viewer Y value.
4. Increase tile resolution progressively all the way down to Y=500.

**Check**
- The camera transition at each LOD boundary must stay continuous as the viewer rises.
- Far-field summary must still read as the same world the player walks in (the author confirms every spot on the map is visitable).

**Why**
[Inference] A single texture can never hold block-per-pixel detail for 60M x 60M blocks, so the pyramid trades memory for visibility: one coarse whole-world plane plus local high-res tiles near the viewer. The Y=500 cutoff bounds how far the tile pyramid needs to go before the real world takes over.

## Phase 3: Mount the textures in a 1:1-mapped separate dimension

**Do**
1. Render the LOD textures in a separate Minecraft dimension.
2. Map that dimension's coordinates 1:1 with overworld coordinates, so texture pixels sit exactly over the blocks they summarize.
3. At Y=500, transition back to the overworld dimension (real chunks, Distant Horizons still applies below this point; the author notes Distant Horizons stops applying at the dimension transition).

**Check**
- The seam at Y=500: the last LOD tile must hand off to real terrain without a visible pop.
- Coordinate mapping must be exactly 1:1 so the map and the world never disagree.

**Why**
A separate dimension keeps the fake far-field rendering isolated from real chunk logic (no chunk-gen cost, no entity processing), while 1:1 mapping makes the illusion geometrically honest: "rendered entirely in game and to scale."

## Phase 4: Fly the ascent (the demo itself)

**Do**
1. Move the camera from Y=0 up to Y=20,000,000.
2. As height increases, let the renderer transition through the LOD levels until the entire 60,000,000 x 60,000,000 block world is visible at once.

**Check**
- 60M blocks x 1 m/block = 60,000 km per side, 3.6 billion km² total (title's number; about 7x Earth's surface, per a commenter).
- World gen is bounded by the hardcoded 60M x 60M limit (author's understanding), so the map has a true edge.

**Why**
Height is the zoom control: the demo proves the LOD pyramid is continuous from ground level to whole-planet view in one unbroken shot.

## The human method, distilled
1. **Query, don't generate.** If the generator is deterministic, the cheapest representation of the world is a function call, not geometry.
2. **Average-per-pixel is a legitimate LOD strategy.** Each texel summarizing its footprint keeps the far view honest instead of aliased.
3. **Isolate the illusion in its own dimension.** Real chunk systems and fake map systems share nothing but a coordinate frame.
4. **Height-indexed LOD tiles with a handoff altitude.** Tiles divide per Y value; Y=500 is the seam where the map becomes the world again.
5. **Averaging the same generator twice must agree.** Because both the map and the chunks come from the seed, map and territory cannot disagree (near block-per-pixel at the top LOD).
6. **One plane for the planet, tiles for the neighborhood.** Whole-world-at-once lives on a single plane; high detail is only ever local.

## Depth status
 DEPTH-LIMITED (demo clip with no narration; author disclosed the technique in selftext plus three replies, but exact sampling step, number of LOD levels, and tile sizes were not stated)

---
