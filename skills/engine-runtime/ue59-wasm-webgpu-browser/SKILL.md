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

## AAA studio practice

- **The web target is now official, and it is the author's exact stack (Epic, UE 5.9 MegaJam Preview, Nov 9, 2026).** Epic's roadmap: "Unreal Engine builds and runs projects in the browser on WebAssembly and WebGPU, so a project ships to the web from the same editor and the same content as every other platform." Two rendering tiers: desktop targets UE's "mobile deferred" renderer, mobile targets "mobile forward"; full "desktop deferred" is under investigation. Current limitations: only code-based projects are supported, and building for web needs a source build ([Epic Developer Community Forums, Web Platform roadmap](https://forums.unrealengine.com/t/web-platform-experimental/2852880)). The author's choice of C++ project + mobile-deferred renderer is exactly the supported path, not a workaround.
- **The web platform code itself was agent-written (Epic, 80 Level).** "A handful of people directed fleets of agents to port the AI tooling from our UE6 development branch and implement Web as a target platform. Agents wrote the web platform code, starting from UE4's retired HTML5 platform, with engineers directing, reviewing, and testing the work." Epic is candid that "parts of the web renderer are prototypes we plan to refactor before the full 5.9 release" (planned 2027), and the Preview had a shorter QA period ([80 Level](https://80.lv/articles/unreal-engine-5-9-preview-is-out-it-was-built-with-ai)). Treat anything built on the Preview as a prototype: pin the engine version, and re-test on every Preview drop.
- **An independent UE 5.8 build already runs a full gameplay stack in the browser.** A community port compiled Epic's official UE 5.8 Game Animation Sample to multi-threaded WebAssembly and WebGPU: "Core engine systems, math libraries, and Chaos physics compile to multi-threaded WebAssembly. We leverage `-msimd128` autovectorization to ensure skeletal matrix transformations, blend stacks, and quaternion math do not fall back to scalar software emulation." Telemetry was recorded on a 15 W 12th-gen Intel i5 laptop with integrated Iris Xe graphics at a native 1080p canvas ([Epic Developer Community Forums](https://forums.unrealengine.com/t/running-ue-5-8-natively-in-the-browser-via-webassembly-webgpu-game-animation-sample/2838620)). The author's ocean scene is a lighter load than that sample; if the sample runs, the scene's bottleneck is payload, not the renderer.
- **Payload is the decision, and it is measurable (independent load study, Nov 2026).** A measured study of 48 Chrome page loads of a UE 5.9 Wasm build, with Brotli compression and explicit cache policies, put the first-load download at about 50 MB. The study's framing: keep the Unreal project when the editor, code, and assets matter more than the download; use three.js when the download decides ([dev.to](https://dev.to/alicia_lu/threejs-vs-unreal-engine-for-web-3d-which-should-you-ship-in-the-browser-47lc)). The commenters' "hundreds of megabytes" fear is the uncompressed figure; publish the Brotli number, not the raw one.
- **The official alternative is Pixel Streaming, and the choice is a concurrency decision (Epic forums).** Pixel Streaming runs the game on a server GPU and streams video to the browser: reliable for low concurrent-player counts, but cost grows with every concurrent player and latency is inherent. The WebGPU route runs on the player's own hardware with no per-minute cost, but performance varies per player and some UE features will not work; for a small project the forum advice is to keep it light (small textures, simple materials, no Lumen or Nanite) ([Epic Developer Community Forums](https://forums.unrealengine.com/t/best-approach-for-running-a-small-unreal-project-in-a-web-browser/2835437)).

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

## Phase 4: Ship with a measured web-build gate

The author's thread never answered the payload question. Make the numbers
part of the build, so the next build answers it in public.

**Do**
1. After every packaged web build, write `web-build-manifest.json` next to
   the build with: engine version (pinned, e.g. 5.9 MegaJam Preview CL),
   packaged size in bytes, Brotli-compressed size in bytes, time to first
   frame in seconds (measured in Chrome, fresh profile, cache cleared),
   and FPS on the reference machine.
2. Measure time to first frame and FPS on the weakest machine you can reach,
   not the dev machine: the UE 5.8 Game Animation Sample port published
   telemetry on a 15 W i5 laptop with integrated graphics at 1080p, and that
   is the bar to beat or match.
3. Record the delivery decision in the manifest: WASM/WebGPU (player's
   hardware, no per-minute cost) or Pixel Streaming (server GPU per
   concurrent player). Revisit the decision when expected concurrent users
   change; it is a concurrency decision, not a taste decision.
4. On every Preview engine drop, re-run the gate before calling the build
   good: Epic says parts of the web renderer are prototypes to be refactored
   before the full 5.9 release.

**Check**
- The manifest exists for the build being shared, and its Brotli size is the
  number quoted anywhere the build is linked. Never quote the uncompressed
  size.
- Time to first frame and FPS are from the reference machine, with the
  machine named in the manifest.
- If Lumen or Nanite is enabled, the gate fails: the forum guidance for
  small web projects is to keep them off.

**Why**
- The commenters were right that load time decides whether people stick
  around, and wrong about the number until someone measures it. A manifest
  turns the argument into a file.

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
