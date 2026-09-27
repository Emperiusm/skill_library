---
name: "browser_backrooms"
description: "Ship procedural 3D in the browser: client-side WebGPU with a WGSL pipeline and GLSL fallback. Trigger when delivering 3D on the web with no install."
---

# procedural backrooms in the browser

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Ship the experience in the browser: client-side WebGPU rendering with a WGSL pipeline and a GLSL fallback.

## Source

Creator: u/pablostanley

Source: https://v.redd.it/v492vggifpqh1 | r/proceduralgeneration post 1wlm2w9 (score 21) | native clip (demo, not tutorial)

## Tools used

Tools used: Browser (client-side), WebGPU via vgpu with a WGSL post-processing pipeline, GLSL fallback for WebGL2.

**Do**
1. Seed the generator and produce, all in the browser: the rooms, furniture, places, and the audio acoustics.
2. Keep generation fully client-side (no server round-trips for world content).

**Check**
- Same seed must reproduce the same rooms, furniture, places, and acoustics.
- Acoustics included: the procedural audio reverb/echo model is part of the seeded output, not a fixed preset.

**Why**
Seeded client-side generation means the game ships as code, not content: infinite backrooms with a static hosting footprint (it lives on vercel.app as a static deploy).

## Phase 1: Generate everything client-side from a seed

## Phase 2: Stream a 3x3 window of 57m sections

**Do**
1. Divide the world into 57m square sections.
2. Stream a 3x3 window of sections around the player (a 171m x 171m active area), loading/unloading as the player moves.
3. Let sections regenerate as the player wanders (regeneration is expected, not a bug).

**Check**
- The active window must follow the player without hitches at section boundaries.

**Why**
A fixed 3x3 window bounds memory and draw cost no matter how far the player roams; regeneration is safe because everything derives from the seed.

## Phase 3: Keep doorways aligned with shared boundary hashes

**Do**
1. When neighboring sections regenerate, align their doorways using shared boundary hashes.

**Check**
- Walk through a doorway into a freshly regenerated section: the doorway on both sides must line up and connect.

**Why**
Independent section generation would otherwise produce doorways that do not meet. A shared boundary hash gives adjacent sections a common reference so their portals agree without either section storing the other.

## Phase 4: Grade the VHS look as a WGSL post pipeline

**Do**
1. Apply the VHS look as a post-processing pipeline written in WGSL with vgpu: warp, tracking errors, chroma offset, and bloom.
2. Provide a GLSL fallback path for WebGL2 browsers.

**Check**
- The look must hold on WebGPU (WGSL) and degrade gracefully on WebGL2 (GLSL).

**Why**
Doing the VHS grade in post keeps the world renderer clean and lets the retro look be tuned independently of the geometry; the GLSL fallback preserves reach on browsers without WebGPU.

## Phase 5: Drive the creature with bounded A* and real frustum visibility

**Do**
1. Move the creature with bounded A* (pathfinding with a bounded search budget).
2. Gate its movement on actual frustum visibility: it only moves when the player really cannot see it.

**Check**
- [Inference] The classic Weeping-Angel rule is enforced geometrically (frustum test), not by timers: if any part of the creature is inside the camera frustum and visible, it freezes.

**Why**
Frustum-gated movement is what makes the scare work: the creature advances only in the player's blind spots, which is exactly the behavior the commenters reacted to ("screamed," "those skinny dudes scared the shit outta me").

## The human method, distilled
1. **Seed covers everything, including acoustics.** Rooms, furniture, places, and audio reverb all derive from one seed.
2. **Bounded active window, unbounded world.** A 3x3 grid of 57m sections streams around the player; memory stays flat.
3. **Shared boundary hashes for portal agreement.** Neighbors agree on doorways through a common hash, not stored state.
4. **Retro look as a separable post stage.** WGSL pipeline (warp, tracking errors, chroma offset, bloom) with a GLSL fallback for reach.
5. **Horror AI keyed to real visibility.** Bounded A* movement gated by an actual frustum check, so the creature only moves unseen.

## Depth status
 DEPTH-LIMITED (author selftext is an architecture summary, not a narrated workflow; the four comments add no technique detail; the linked MIT repo was not audited)

---

# Photogrammetry/SfM + Houdini tooling: reconstructions

Full-depth workflow reconstructions of audited videos, in the style of the cinematic-cavern workflow guide. Each section: source line, tools used, phased Do / Check / Why, distilled principles, depth status. No per-repo have-vs-need judgments. [inference] marks anything not stated in the sources.

---
