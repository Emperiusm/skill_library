---
name: trochoidal-procedural-ocean-code-drawn
description: "Draw a procedural pixel-art ocean entirely in code at 320x180 with no hand-drawn art: trochoidal waves where longer waves outpace shorter ones and build with wind, shoaling at the beach, underwater light-beam deflection, noise sea floor with current-bent kelp, noise-heightfield clouds, weather as a global palette and lighting change, and seed-generated boid fish with rare mutations. Trigger when water must be a system, not a texture."
---

# Trochoidal Procedural Ocean, Code-Drawn (Cryptoler1)

## Purpose

This skill reconstructs the exact workflow Cryptoler1 shows for a procedural pixel-art ocean: the whole frame is drawn in code, no artwork is done by hand, and one wave model drives the surface, the shoaling, and the light. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: no hand-drawn art, one wave model, weather as a global change, seeds for individuals.

## Source

Creator: Cryptoler1. Post: "Procedural pixel-art ocean" — https://www.reddit.com/r/proceduralgeneration/comments/1y5eva9/ (score 242, 26 comments, 24 retrieved; the post selftext is empty). Video: https://v.redd.it/e19ev15jws3i1. The method is stated entirely in the creator's comments. Scout audit 2026-11-27, audit 4, PARTIAL.

## Tools used

No engine or language is named in the post or in the retrieved comments. A commenter links a Godot underwater post as inspiration; that is the commenter's reference, not the creator's stated engine. Do not assume an engine.

## Phase 1: Draw the frame in code

**Do**
1. Draw the entire 320x180 frame in code. "There is no artwork done by hand." (Cryptoler1, comment, verbatim).

**Check**
- The frame is 320x180. No resolution-scaling or upscaling step is stated.

**Why**
Code-drawn frames make every element (waves, floor, fish, clouds) a parameter of the same system, so weather can change all of them together.

## Phase 2: Build the surface from trochoidal waves

**Do**
1. Construct the ocean surface from trochoidal waves, "wherein longer waves outpace shorter waves and build with the help of winds." (Cryptoler1, verbatim).
2. Let the waves shoal at the beach and deflect the underwater light beams.

**Check**
- Shoaling at the beach and light-beam deflection are visible in the clip. No wave parameters (amplitude, wavelength, wind values) are given, so none are stated here.

**Why**
Trochoidal waves give the surface its shape and its motion in one model: speed differences between long and short waves, wind build-up, and beach shoaling are properties of the wave model, not separate animations.

## Phase 3: Generate the floor, kelp, clouds, and fish from seeds and noise

**Do**
1. Sea floor: noise-generated rocks and sand, with kelp bending due to current.
2. Clouds: noise heightfields.
3. Weather: changes the palette and lighting of everything.
4. Fish: each individual fish generated from seeds (body shapes, colours, fins, and rare mutations), steered as boids. Creator's wording, verbatim: "each individual fish is generated from seeds (their body shapes, colours, fins and rare mutations) and theyre steered boids."

**Check**
- Kelp sway: a commenter asked how the kelp sways so nicely; the creator replied that the sway still reads too much like a current and that the creator will play with it until it looks less like a current. The sway is therefore an open refinement, not a finished recipe.
- Water depth cue: "the water already gets darker and murkier the further out you go" (Cryptoler1). A coral reef further out is planned, not present.

**Why**
Seeds make each fish an individual with rare mutations, while boid steering makes the school move as a group. Noise heightfields make clouds a terrain-like system, so weather can re-palette the whole frame coherently.

## Failure modes

- Hand-drawn art mixed into a code-drawn frame: it breaks the weather-as-global-change property.
- Kelp that reads as a current: the creator's own open defect. Play with the sway until it reads less like a current; no fixed parameter is given.
- Assuming an engine from the commenter's Godot link. The creator never names one.

## The human method, distilled

1. No hand-drawn art: if it is on screen, it is generated.
2. One wave model carries surface, shoaling, and light deflection.
3. Weather is a global palette and lighting change, not a filter on one layer.
4. Admit the weak spot in the thread (kelp sway reads like a current) and name the fix direction.

Music note, from the creator's comment, not a tooling finding: the track is "Childhood Friends" by Juhani Junkala, free to use, found on OpenGameArt.

**Depth status:** PARTIAL. The wave, floor, cloud, weather, and fish methods are stated by the creator. The engine, language, code, and all numeric parameters are unknown.
