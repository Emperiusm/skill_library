---
name: zenith-lens-flare-copernicus
description: "Build physically based lens flare in Houdini Copernicus with Zenith: ray-trace a real lens prescription (built-in 28/50/135/300mm lenses or your own .zmx Zemax file) instead of painting sprites, drive flare from energy-calibrated HDR plate regions or a scene light followed through the camera, occlude with mask or plate alpha, add iris-shaped starburst and veiling glare, render RGB or spectral in Linear Rec.709 or ACEScg on CUDA. Trigger when a flare must belong to the plate optically, not sit on it as a sprite."
---

# Zenith Physically Based Lens Flare for Copernicus

## Purpose

This skill reconstructs the Zenith setup from the author's full feature
spec, step by step, so another agent can follow the same process. Every
phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The video's core method is:
ray-trace a real lens prescription instead of painting sprites, so
ghosts get their shape, color, and position from optics.

## Source

Creator: sergioeren. Reddit post:
https://www.reddit.com/r/Houdini/comments/1xdk0ct/zenith_a_physically_based_lens_flare_node_for/
(r/Houdini post 1xdk0ct, score 32, 3 comments) | 2026-10-25 scout run,
audit 3.

## Tools used

**Zenith** lens flare node for **Copernicus** (Houdini 22.0,
Windows/Linux; beta 0.1.5), **GPU CUDA** (RTX 20-series / Turing or
newer) with CPU fallback, **.zmx Zemax** lens files, **Linear Rec.709
or ACEScg** color. Download/docs: https://sergeneren.com/zenith/
(linked, not retrieved). Open-source implementation of the same paper:
https://github.com/beatreichenbach/realflare (commenter-linked, code
not reviewed this run).

## Phase 1: Pick the lens (built-in or your own prescription)

**Do**
1. Choose a built-in lens: 28 mm retrofocus, 50 mm triplet, 50 mm
   double Gauss, 135 mm telephoto, or 300 mm telephoto.
2. Or load your own .zmx Zemax file.

**Check**
- The flare must change when the lens changes: different prescriptions
  give different ghosts, not a reskinned sprite.

**Why**
- The paper (Hullin et al., Physically-Based Real-Time Lens Flare
  Rendering, SIGGRAPH 2011) is the method: every two-bounce ghost is
  followed (light reflects off one lens surface, travels back, reflects
  again before reaching the sensor), and ghost shape, color, and
  position come from dispersion, Fresnel reflectance, and
  anti-reflection coatings.

## Phase 2: Drive the flare from lights that mean something

**Do**
1. Lights from the plate: bright regions of an HDR plate become lights,
   calibrated so each flare carries that region's energy.
2. Or place a manual light, which can follow a LOP or OBJ light (or a
   sun direction) through the camera, so the flare keeps going after
   the sun leaves the frame. The camera is automatically imported from
   the image metadata in a slap comp.

**Check**
- A plate-driven flare must track the plate's bright regions, not a
  fixed sprite position; a scene-driven flare must persist past the
  frame edge while the light is still in the scene.

**Why**
- Energy-calibrated plate lights are what make the flare look like it
  belongs to the plate rather than pasted on it.

## Phase 3: Occlude, starburst, and color correctly

**Do**
1. Occlude the manual light behind objects with a mask or the plate's
   alpha; it fades smoothly as it slips behind an edge.
2. Add the starburst computed from the iris shape, plus a veiling
   glare halo.
3. Choose RGB or full spectral rendering, in Linear Rec.709 or ACEScg.

**Check**
- Occlusion must fade, not pop; the starburst must follow the iris,
  not a generic 4-point sprite.

**Why**
- Smooth occlusion and iris-shaped starburst are the two tells that
  separate an optical flare from a painted one.

## Phase 4: Ship it within the beta's limits

**Do**
1. Run on GPU (CUDA, RTX 20-series/Turing or newer) or fall back to CPU.
2. Non-commercial: free for personal projects and learning, renders up
   to 1920x1080. Commercial: no resolution limit, unlimited render
   nodes.
3. Expect breakage: "It's a beta, so scenes may break between 0.x
   versions."

**Check**
- The author asks for feedback, bug reports, renders, and lens files
  users want working. A commenter points to the open-source realflare
  implementation of the same paper with custom optimizations; the
  author replies it could be wrapped as an HDA for Copernicus too.
  That commenter implementation is a separate tool, not Zenith, and is
  watchlisted separately.

**Why**
- A beta lens tool is adopted for its optics, not its stability: pin
  the version, expect 0.x breakage, and keep the .zmx files.

## The human method, distilled

1. **Optics, not sprites**: ghosts from prescriptions, not paintings.
2. **Lights carry energy**: plate regions calibrated, scene lights
   followed past the frame edge.
3. **Beta discipline**: free tier capped at 1080p, scenes may break.

**Depth status:** PARTIAL (full post spec + all 3 comments; no video
breakdown, render samples, or performance measurements).
