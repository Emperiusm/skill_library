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

## AAA studio practice

**Rare, Sea of Thieves (SIGGRAPH 2018).** "The Technical Art of Sea of Thieves" (Ang, Catling, Ciardi, Kozin) describes an FFT ocean implementation following Tessendorf 2001: water colour from scattering approximations blending deep-water and sub-surface colours by view angle, sun direction, and a wave-peak mask generated from the FFT choppiness offsets; foam generated at wave peaks and around intersecting objects, progressively blurred to simulate dispersion, blended with artist-authored textures; and foam generation modified by water state, calm, normal, or stormy, with stormy water showing more foam. Shallow-water detail (deck splashes, waterfalls) runs as a separate GPU surface simulation. Source, read firsthand: https://history.siggraph.org/wp-content/uploads/2022/09/2018-Talks-Ang_The-Technical-Art-of-Sea-of-Thieves.pdf — Honest distinction: Rare's solver is FFT/spectral, not the trochoidal sum-of-waves model this skill uses, so no FFT parameter is imported. The portable lesson is architectural: one wave field drives the surface, the colour, and the foam, and the foam behaviour changes with a named water state. Apply it here: the trochoidal field must drive the surface, the shoaling, and the light-beam deflection from the same height values, and weather must be a named state that changes foam/colour behaviour, not a filter applied afterwards.

**Naughty Dog, Uncharted (SIGGRAPH 2012 / GDC 2012).** "From a calm puddle to a stormy ocean: rendering water in Uncharted" (Gonzalez-Ochoa, Holder, Cook) classifies water by type, puddles to ocean storm, and uses a different render engine per type: calm/semi-moving bodies on non-LOD meshes, open ocean on a hierarchical LOD system with displacement, flooding on a skinning-plus-particles mechanism. The ocean system drove gameplay: in Uncharted 3 the water drove the cruise ship, which in turn moved the player, enemies, effects, and physics objects, and all parameters were artist-controlled. Source: https://history.siggraph.org/learning/from-a-calm-puddle-to-a-stormy-ocean-rendering-water-in-uncharted-by-gonzalez-ochoa-holder-and-cook/ (slides: https://www.slideshare.net/slideshow/water-technologyofunchartedgdc2012/12977478) — The portable lesson is classification plus coupling: name the water type before choosing the technique, and let the same wave field that draws the surface also move what floats on it (here: the boid fish and the kelp). A fish school that ignores the wave field it swims in repeats the fake Naughty Dog's ocean-drive avoided.

**Agent automation (agent-written checks, no creator values invented).** Three checks, all recorded per run in `ocean-checks.json`: (1) Single-field contract probe: sample the generator's wave-height function at shared probe points and assert the surface displacement, the shoal height at the beach, and the light-beam deflection all read the same height value at the same point and time; this requires the height function to be exposed and named in the code, and if it is not, record that as a gap instead of faking the probe. (2) Weather sweep: render the same frame under every weather state and assert the palette/lighting shift is global (mean colour shift measured in every region: sky, surface, floor, fish), failing if only one layer changed. (3) Kelp acceptance pair: keep the creator's open defect as a named check, before/after render pairs for each sway change, judged against the creator's own criterion (reads less like a current); no sway parameter is invented here.

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
