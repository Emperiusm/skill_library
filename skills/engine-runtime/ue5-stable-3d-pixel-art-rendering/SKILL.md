---
name: ue5-stable-3d-pixel-art-rendering
description: "Stable 3D pixel-art rendering in UE5: cubemap-based pixelation post-process, slow cubemap refresh hidden by disocclusion, distance-layered far-field raymarching. Trigger when pixelating 3D views without camera jitter."
---

# I'm rendering stable 3D pixel art in UE5

## Purpose

This skill reconstructs the rendering technique published by Nuphar_Studio for their UE5 pixel-art plugin, step by step, so another agent can implement the same stabilization. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: *pixelate through slowly-refreshed cubemaps, and hide the staleness with disocclusion.*

## Source

Creator: Nuphar_Studio

Source: https://www.reddit.com/r/GraphicsProgramming/comments/1xl3ppu/ (2026-11-01) | video: v.redd.it/96c8ea8760zh1 | Plugin: Fab listing 3a9f54a9-6514-4de7-a212-1955f903061f | Tech demo: https://averdrian0.itch.io/true-pixel-art-3d-tech-demo

Depth: FULL (technique) — the author published the method; per-element parameters beyond the explainer are not public.

## Tools used

Unreal Engine 5 (5.6–5.8 per the plugin docs site); custom post-process plugin (Fab); itch.io tech demo. Built over 3 months after the Project Shadowglass trailers and "the recent 3D pixel art discoveries of Dylan Ebert and Lunar Blank". Author's caveat: "(this is a brief explanation, there is a lot more going on)".

## Phase 1: Kill rotation jitter with cubemap pixelation

**Do**
1. Render the game through a post-process that performs the pixelation as a cubemap lookup: the pixel grid is sampled from cubemaps rather than re-rasterized per frame.
2. Target first-person view first (third-person and top-down also supported).

**Check**
- Rotate the camera in place: pixels must stay locked with no severe flickering from camera rotation.

**Why**
- Rotation jitter comes from re-rasterizing the pixel grid every frame as the camera turns; a cubemap lookup decouples the pixel grid from camera orientation.

## Phase 2: Refresh cubemaps slowly, hide staleness with disocclusion

**Do**
1. Recapture the cubemaps at a slow rate — the author's number is **every 0.25 s** — instead of every frame.
2. Apply the disocclusion technique discovered by Lunar Blank / Dylan Ebert so the render stays fluid despite the 4 Hz capture rate.

**Check**
- Strafe sideways (camera translation): motion must look fluid, not steppy at 4 Hz.

**Why**
- Slow capture is what buys the stable pixel look; disocclusion (reprojecting newly-visible pixels from the stale capture) is what buys back fluidity. The two techniques cover each other's weakness: pixelation wants infrequent re-rasterization, motion wants fresh data.

## Phase 3: Layer by distance with a separate far-field path

**Do**
1. Layer the whole render by distance.
2. Use a different raymarching method for far/background elements — this specifically "solve[s] the non pixel art edges issue of the disoclusion technique."

**Check**
- Look at the horizon: distant edges must pixelate consistently with the foreground, not go smooth.

**Why**
- Disocclusion breaks down where depth complexity is low and distances are large; a separate far-field path keeps the pixel contract everywhere instead of letting the background go soft.

## Phase 4: Route dynamic elements through custom depth + stencil

**Do**
1. Render dynamic elements through a custom depth pass with stencil, separate from the cubemap path.
2. Apply the author's "3D billboard" technique for applicable elements (beyond the brief explainer — consult the plugin docs at dmvergasov-adjacent pages / the Fab listing for the full method).

**Check**
- Moving characters must pixelate identically to static geometry, with no smearing.

**Why**
- The cubemap path is inherently static-scene-friendly; dynamics need their own pass or they smear across the slow capture interval.

## The human method, distilled

1. Build on public discoveries and credit them: the plugin started from Project Shadowglass trailers + Ebert/Blank's disocclusion work.
2. Ship the technique as a product, not a video: Fab listing + a playable itch.io tech demo.
3. Name the one number that makes the tradeoff concrete: the 0.25 s capture rate.

## Failure modes

- **Severe pixel jitter:** what happens without the cubemap indirection — re-rasterizing the pixel grid per frame under camera motion.
- **Non-pixel-art edges at distance:** what happens if you apply disocclusion uniformly — the far field needs its own raymarching path.
- **Smearing dynamics:** what happens if moving elements go through the slow-capture path — hence the custom depth + stencil pass.

**Depth status:** FULL (technique; per-element parameters not public, none invented)
