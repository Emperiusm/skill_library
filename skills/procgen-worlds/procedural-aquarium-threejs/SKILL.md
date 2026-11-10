---
name: procedural-aquarium-threejs
description: "Generate a whole living aquarium at load in one ~650 KB HTML file with Three.js r160: fish meshes as swept profile rings bent by a travelling wave, skins and scales painted one by one on canvas, fish simulated not animated with a gape rule for hunting, and day, night, and weather following the real clock at Lake Fork, Texas. Trigger when building a procedural scene where the generation code must be smaller than the assets it replaces."
---

# Procedural Aquarium (Three.js)

## Purpose

This skill reconstructs the bass aquarium build, step by step, so another
agent can generate a living procedural scene at load with the same method.
Every phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: generate
everything at load, simulate the fish instead of animating them, and let the
procedure be the compression.

## Source

- Post: "Everything in this bass aquarium is generated at load: fish, scales,
  plants, sand, driftwood (Three.js, one HTML file)" by kskbaits —
  https://www.reddit.com/r/proceduralgeneration/comments/1xra7wm/everything_in_this_bass_aquarium_is_generated_at/
  (r/proceduralgeneration, score 23, 4 comments)
- Try it: https://ksk-baits-bass-aquarium.pages.dev
- Live: https://www.youtube.com/@kskbaits/live
- Evidence: full author post text with exact numbers and method, plus 4
  comments with measured memory figures (2026-11-10 scout run). The clip is
  the live tank itself.

## Tools used

Three.js r160; one ~650 KB HTML file; canvas-painted textures (2048x1024
colour map plus matching normal/roughness map per fish, all mipmapped);
full-screen post-processing (bloom, depth of field, motion blur during
strikes).

## Phase 1: Generate the fish

**Do**
1. Build the fish meshes as swept profile rings, "bent by a travelling wave
   per vertex."
2. Paint the skin and scales one by one on a canvas. Each fish gets a
   2048x1024 colour map plus a matching normal/roughness map, all mipmapped.
   (Author comment with measured detail.)
3. No model files, no image files: "Nothing in this tank is a model or an
   image file. It is one ~650 KB HTML file with Three.js r160, and everything
   is generated when the page loads."

**Check**
- The whole tank is about 650 KB, "less than a single 4K texture for one of
  the fish would be. The scales alone would be megabytes as images, but here
  they are a few lines that paint them one by one at load."

**Why**
Procedural generation is compression: the code that paints the scales is
smaller than the scales would be as images, by orders of magnitude.

## Phase 2: Simulate the fish, don't animate them

**Do**
1. Simulate two bass (a largemouth and a smallmouth): they get hungry, hold
   by cover, stalk, and strike with a suction feed "that only takes prey
   whose body depth fits their gape."
2. School the shad; they "burst apart when attacked."
3. Generate the rest at load too: plants, sand, pebbles, driftwood, moss,
   caustics, and the lo-fi music.

**Check**
- "The fish interactions were the part I spent the most time on" (author
  comment). The check is behavioral: hungry, hold, stalk, strike, and a gape
  rule that filters prey by body depth.

**Why**
Simulation gives behavior for free: a strike rule (body depth fits gape)
produces believable hunting without keyframed animation. The gape rule is
the kind of constraint that makes the simulation legible: a viewer can see
why a strike happened or did not.

## Phase 3: Tie it to the real world and measure it

**Do**
1. Day, night, and weather follow the real clock and weather at Lake Fork,
   Texas.
2. Run it 24/7 on YouTube; the chat can drop in shad (!feed) or cast a lure.
3. Measure runtime memory (Chrome, 1080p, counting what the page allocates
   on the GPU): JS heap about 60 MB; GPU roughly 500 MB. "About 340 MB is
   textures, about 190 MB is the multisampled render buffers, and about 30 MB
   is vertex buffers."

**Check**
- "Your compression point holds: 650 KB unpacks into about half a GB. Most
  of it is the painted skins." (Author reply to commenter immersiveGamer.)
  The author's own trim: "The skins could be 1024 wide on mobile with almost
  no visible difference."

**Why**
The 650 KB figure is the shipping size; the 500 MB figure is the runtime
cost. Both are the truth, and the gap between them is the painted skins. A
mobile budget is a texture-resolution decision, not a rewrite. Tying the
scene to a real clock and real weather makes a 24/7 stream different every
time it is watched, for free.

## Failure modes

- **Runtime memory is dominated by the painted skins.** 650 KB of code
  unpacks into about half a GB at runtime, most of it textures. Fix: drop
  the skins to 1024 wide on mobile; the author reports almost no visible
  difference.
- **Post-processing buffers are the second cost.** About 190 MB of the GPU
  total is multisampled render buffers for bloom, depth of field, and motion
  blur during strikes. Fix (inference, labeled): treat the post chain as a
  budget line item of its own, not as free.

## The human method, distilled

1. **Generation is compression.** Code that paints scales beats images of
   scales.
2. **Simulate, don't animate.** A gape rule and a hunger state make hunting
   behavior.
3. **Report both sizes.** Shipping size and runtime memory are different
   numbers; publish both.
4. **The expensive part is the part you spent the most time on.** Fish
   interactions, not the tank.

**Depth status:** FULL (full post text with exact numbers and method + 4
comments with measured memory figures; the clip is the live tank itself, and
a media download would add nothing the post and the live page do not already
state; no download attempted).
