---
name: ue59-wasm-webgpu-browser
description: "Run Unreal Engine 5.9 in a browser: vibe-code the scene in C++, compile to WebAssembly, render with WebGPU on the mobile-deferred renderer, with a baked-FFT ocean. Trigger when an Unreal scene needs to run in a browser instead of natively."
---

# Unreal Engine 5.9 in the Browser: WASM and WebGPU

## Purpose

This skill reconstructs the author's exact workflow, step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The build's core method is: vibe-code a UE 5.9 scene in C++, compile it to
WebAssembly, render it in-browser with WebGPU.

## Source

Creator: Efficient_Ad8214. Reddit post:
https://www.reddit.com/r/vibecoding/comments/1xwhonw/unreal_engine_59_wasm_running_in_browser/
(r/vibecoding post 1xwhonw, score 51, 13 comments) | 2026-11-15 scout run,
audit 2.

## Tools used

Unreal Engine 5.9 MegaJam Preview, C++, WebAssembly, WebGPU, Unreal
mobile-deferred renderer, custom ocean (four baked FFT wave cascades),
GPT 6 Astra (vibe coding), Blender (Three.js boat model import), custom fog
and reflections.

## Phase 1: Build the scene in UE 5.9, vibe-coded

**Do**
1. Build with Unreal Engine 5.9 MegaJam Preview, in C++.
2. Vibe-code it with GPT 6 Astra (author's words: "Vibe coded with GPT 6 Astra").
3. Reuse the original Three.js boat model, imported through Blender.

**Check**
- Author's claim: "Quite close to the threejs webgpu version."

**Why**
- Reusing the Three.js boat makes the UE build directly comparable to the
  author's earlier three.js WebGPU version. (Inference, labeled.)

## Phase 2: Compile to WebAssembly, render with WebGPU

**Do**
1. Compile the build to WebAssembly.
2. Render in-browser with WebGPU.
3. Use Unreal's mobile-deferred renderer (author's bullet).

**Check**
- It runs in a browser at all. No load time, payload size, or frame rate was
  published by the author.

**Why**
- The mobile-deferred renderer is the cheap path to a browser build: fewer
  features, smaller binary, faster first frame. (Inference, labeled.)

## Phase 3: Ocean, fog, reflections

**Do**
1. Build a custom ocean with four baked FFT wave cascades (author's bullet).
2. Add custom fog and reflections (author's bullet).

**Check**
- Commenter cagonima69 asked the open question: "Do you have footage of what
  it looks like in bad weather and how the boat rides those waves?" No answer
  in the thread. Commenter Shapacap: "itd be crazy if the water actuall
  reacted, or anyuthing else" (sic). The water does not react to the boat in
  the shown footage, as far as the comments establish.

**Why**
- Baked FFT cascades are cheap and good-looking in calm water; reactive water
  is a separate, harder problem. (Inference, labeled.)

## The human method, distilled

1. Port, don't rebuild: same boat, same ocean idea, new engine, direct comparison.
2. Mobile-deferred renderer for the browser, or the binary never ships.
3. Bake the waves; reactivity is a later problem.
4. The question the author did not answer is the real one: payload and load
   time. Commenter RochestieRouzet22: "Unreal WASM builds tend to land in the
   hundreds of megabytes before the first frame while the three.js scene
   probably loads in a few, and for anything in a browser that load time
   decides whether people stick around." Commenter Total-Reasonable: "how are
   you handling streaming and caching (e.g. compressed assets, Brotli, and
   service worker or IndexedDB caching)? That's what decides whether anyone
   beyond you actually sits through it on first visit."

**Depth status:** PARTIAL. Selftext bullets plus 13 comments; no build steps,
no sizes, no frame rates. FULL depth would need the author to publish the
build size, load time, and the ocean setup.
