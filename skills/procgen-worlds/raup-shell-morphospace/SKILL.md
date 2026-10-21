---
name: "raup_shell_morphospace"
description: "Generate every seashell from three numbers: David Raup's morphospace (flare, verm, spire), built as a Blender geometry-nodes / TouchDesigner generator with cellular-automaton or reaction-diffusion pigment patterns, plus a StyleGAN3 latent-space museum when parametric dimensions explode. Trigger when building parametric 3D generators, morphospace-style variant exploration, or seeded procedural assets."
---

# Raup Shell Morphospace

## Purpose

Reconstruct the exact workflow for generating every seashell (and ones that
never existed) from three parameters, so an agent can follow the same process
on a new parametric 3D generator. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The core method throughout: learn the growth rule, parametrize it, walk the
parameter space, and switch to a learned latent space when the parameter count
explodes.

**Source:** "The Museum of All Shells - Every Shell Is The Same Formula" by
Matige KunstIntelligentie (9:13). https://youtu.be/j4Ecdgn9GLg
Blender and TouchDesigner files: author's Patreon (announced in the video
description, "will be available on Patreon shortly").

**Tools used:** Blender (geometry nodes); TouchDesigner; StyleGAN3; Elektron
Digitone (music). Sources: Richard Dawkins, *Climbing Mount Improbable*; Hans
Meinhardt, *The Algorithmic Beauty of Sea Shells*; David Raup, "Geometric
analysis of shell coiling"; domain information from Angela at the Shell museum
in Doesburg.

**Depth status:** FULL (240 caption segments + metadata + description; media
download was YouTube bot-blocked, but the transcript is parameter-dense and
self-sufficient)

## When to use this skill

- Building a parametric 3D generator from a natural growth rule (shells,
  horns, spiraling plants).
- Setting up morphospace-style variant exploration where a tiny parameter set
  generates a navigable space with named empty regions.
- Deciding between more parameters and a learned latent space for a
  generative-asset problem.

## Prerequisites

- Blender with geometry nodes (or any parametric 3D tool) for the formula path.
- TouchDesigner for the visualization/installation path.
- StyleGAN3 (or equivalent) if the learned-space path is used.
- Read Raup's three parameters cold before writing any node: flare, verm, spire.

## Phase 1: Establish the growth model

**Do**
1. Model the shell as the product of a single organ, the mantle, which "adds
   material at its opening".
2. The innermost part of the coil is "the same shape as the animal was born
   with, sitting there untouched". Every animal "carries its own infant form
   around with it".

**Check**
- State the formula plainly: the shell is "a recording of that formula
  followed thousands of times".

**Why**
Growth happens only at the margin. The whole shape is one rule, iterated.

## Phase 2: Define the three morphospace parameters (Raup)

**Do**
1. **Flare**: the logarithmic-spiral expansion ratio per turn. Quoted: "A
   flare of two means that the spiral doubles in size every completed turn.
   A flare of a thousand means that the spiral opens out a thousandfold per
   turn." (flare 1000 -> cockle-like, no longer spiral-looking)
2. **Verm**: "the ratio between the distance from the center of the spiral
   to the inner edge of the tube and the outer edge of the tube." The
   snug-fit rule, quoted exactly: "If you want a snug fit, you take the verm
   to be one over the flare." Above that leaves gaps ("the gapier it gets,
   the less it looks like a snail, and the more it looks like a worm";
   *verm* from *vermiform*, "wormshaped"); below that the turns overlap.
3. **Spire**: "the rate at which the coil creeps up the Z-axis." High spire
   gives "a turret like the turretella"; spire of zero keeps everything on
   one plane like the nautilus.

**Check**
- Verify against real shells: "for real shells, this overlap is a problem
  because solid objects can't occupy the same space." The nautilus solves it
  by letting "the new tube wrap around the coil already there. So, the new
  cross-section comes out with a bite taken out of it."

**Why**
Three numbers generate every shell on a beach. When a parameter has a
physical meaning (overlap is impossible), enforce it as a rule, not a
suggestion.

## Phase 3: Build the generator

**Do**
1. Start with a line of points. Each point gets theta going from 0 to 2π.
2. Turn the line into a circle: x = cos(theta), y = sin(theta). "Scaling
   theta sets how many turns the line makes around the circle."
3. Introduce flare: "Multiply x and y by flare to the power of how many
   turns we've made and we get our logarithmic spiral. The spiral is the
   outer edge of our shell."
4. Inner edge = outer edge times verm. Halfway between the two sits the
   center line ("that's our center line"). Subtract center from outer to get
   radius; double it for diameter.
5. Place a circle with that diameter on every point of the center line, each
   rotated to face along the direction of that line.
6. Height: "Each point moves up by its distance from the axis times the
   spire."
7. Treat the number of turns as another parameter (author: "I kind of
   cheated. The number of turns is actually another parameter").

**Check**
- Circles must be oriented along the center line; height must scale with
  distance from the axis, not uniformly.

**Why**
Each free parameter is a museum direction: "Walk east to west and shells
open out faster and faster which is flare. Walk north to south as shells get
wormier which is verm. And if you walk up the shells turn into cones which
is spire."

## Phase 4: Admit the unfilled volume (falsifiability)

**Do**
1. Note that filling Raup's cube with real shells leaves "less than half of
   the volume" occupied, and ask why: shells too weak or too costly to build,
   or mutations never available.

**Check**
- Keep the empty space visible; it is data, not a bug.

**Why**
A generative space is only honest if the impossible regions stay on the map.

## Phase 5: Add pigment patterns

**Do**
1. Encode simple patterns as elementary cellular automata: look at three
   neighboring blocks, decide dark or light for the next block. 3 blocks x
   dark/light = 8 combinations; a rule is a dark/light choice for each =
   **256 possible rules**.
2. The textile shell "looks like" **rule 30**.

**Check**
- Real shell patterns come from "a continuous reaction diffusion process",
  so "we need to add infinite rows instead of just 256".

**Why**
Discrete rules approximate; continuous processes are the truth. Name which
one you're using and its cost.

## Phase 6: Walk the latent museum (StyleGAN3)

**Do**
1. "I trained the style GAN free model on tens of thousands of images of
   shells."
2. "Each latent vector has 512 numbers and every combination of numbers
   creates a different shell." Smoothly walk through the 512-dimensional
   space.

**Check**
- The walk must be smooth (interpolation is continuous in latent space).

**Why**
When parametric dimensions explode (turns, cross-section shape, pattern
rules), stop adding museum wings and switch to a learned space. The author's
stated reason, kept verbatim as the principle: "museums aren't exactly
getting a lot of funding in the Netherlands these days."

## The human method, distilled

1. **Find the growth rule, then the parameters** (mantle-before-formula).
2. **Name parameters by what changes when you walk** (the museum-direction
   metaphor).
3. **Quote the constraint rules exactly** (verm = 1/flare for a snug fit;
   overlap is impossible in reality).
4. **Show the empty volume** (<half of Raup's cube occupied by real shells)
   as data.
5. **Prefer learned spaces when parametric dims explode** (StyleGAN3,
   512-dim latent, tens of thousands of training images).
6. **Admit what's left out, with its cost** ("museums aren't exactly getting
   a lot of funding").

## Failure modes

- Hiding the empty regions: a morphospace with only the pretty corners is a
  demo, not a tool; keep the unoccupied volume visible.
- Adding parameters instead of switching to latent space: each new dimension
  (turns, cross-section, pattern) multiplies the museum; past 3-4 dims,
  train a StyleGAN instead.
- Using rule 30 where reaction-diffusion is the truth: the 256-rule automaton
  is an approximation; real shell patterns need the continuous process
  (Meinhardt).
