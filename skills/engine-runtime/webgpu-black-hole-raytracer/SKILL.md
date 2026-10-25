---
name: webgpu-black-hole-raytracer
description: "Build an interactive, physically-grounded Kerr black-hole renderer in the browser with WebGPU: backwards ray integration through Kerr spacetime per pixel, blackbody disk color with Doppler shift and gravitational redshift, an interactive spin 0 to 0.998 slider, and an Interstellar-style cinematic grade. Trigger when building a browser physics visualization or interactive simulation demo."
---

# WebGPU Black-Hole Ray Tracer (Kerr Spacetime, Interactive)

## Purpose

This audit reconstructs the exact simulation and delivery workflow from
Optimal-Yak-9811's "A spinning black hole you can orbit in your browser"
post and the author's own selftext, plus the community-verified browser
compatibility matrix, step by step, so another agent can follow the same
process. Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The workflow's core method
is: trace every pixel's ray backwards through Kerr spacetime, derive all
visuals from the physics (never paint them), and expose the spin as an
interactive parameter.

## Source

Creator: Optimal-Yak-9811 (r/Simulated post 1x8k3q7, score 92, 8 comments).

Source: https://www.reddit.com/r/Simulated/comments/1x8k3q7/a_spinning_black_hole_you_can_orbit_in_your/
(native Reddit video; 2026-10-19 scout run). Live demo:
https://kerr-black-hole-roan.vercel.app

## Tools used

Tools used: WebGPU compute, Vercel (static hosting), browser orbit controls
(drag to orbit, scroll to zoom). Compatibility floor (author + community
testers): requires Chromium-based browser — Chrome or Edge on desktop, Safari
on macOS 26. Verified working: iPhone (Reddit browser and Safari), Chrome
mobile (Edge and Chromium mobile also work). Verified FAILING: Firefox mobile,
Firefox desktop, Brave on phone. Control panel is missing on mobile (tester on
older Pixel 6 Pro otherwise loads fine and is responsive).

## Phase 1: Set the WebGPU compatibility floor

**Do**
1. Target WebGPU only and declare the compatibility floor in the post. (Author:
   "It needs WebGPU: Chrome or Edge on desktop, or Safari on macOS 26. Not
   tested on phones yet.")
2. Deploy as a static page (Vercel) and invite the audience to report
   per-device results.

**Check**
- Build a compatibility matrix from real testers before calling the demo
  done. Known-good this run: Chrome/Edge desktop, Safari macOS 26, iPhone
  Safari and in-app browsers, Chrome mobile. Known-bad: Firefox (desktop and
  mobile), Brave on phone. Missing control panel on mobile is a known defect
  (author: "I'll make it work on mobiles in the next iteration").

**Why**
WebGPU is still a capability check, not a commodity: the audience IS the test
suite. State the Chromium-only constraint honestly instead of letting users
discover it.

## Phase 2: Backwards ray integration through Kerr spacetime

**Do**
1. For every pixel, trace its light ray BACKWARDS through the spacetime of a
   spinning (Kerr) black hole. (Author: "Every pixel traces its light ray
   backwards through the spacetime of a spinning (Kerr) black hole, so the
   shadow, the photon ring and the disk arching over the top all come out of
   the physics.")

**Check**
- The shadow, photon ring, and disk arching over the top must all EMERGE from
  the integration. If you have to draw the photon ring as an effect, the
  integrator is wrong.

**Why**
Emergent phenomena are the correctness test of a physics solver. Painted
effects would make the spin parameter a lie.

## Phase 3: Physically-motivated disk color

**Do**
1. Color the accretion disk as a blackbody at the temperature actually seen,
   after applying Doppler shift and gravitational redshift. (Author: "The
   disk's color is a blackbody at the temperature you'd actually see, after
   Doppler shift and gravitational redshift.")

**Check**
- The disk side moving toward the viewer brightens (Doppler); the disk
  reddens near the hole (gravitational redshift); background stars bend into
  an Einstein ring. All three must come from the physics: "The disk brightens
  on the side moving toward you, reddens near the hole, and the stars behind
  it bend into an Einstein ring."

**Why**
The Doppler asymmetry and redshift are what make it read as a real black
hole rather than a donut with a glow texture. The asymmetry is the signature.

## Phase 4: Expose the spin parameter and the cinematic grade

**Do**
1. Provide a spin slider from 0 to 0.998. (Author: "At 0.998 the inner disk
   sits so close that most of its light is pulled toward the center.")
2. Add a "Cinematic" mode reproducing Interstellar's warmer, softened look
   (author: "The film's team deliberately toned" — selftext truncated there;
   treat the grade as art direction, not physics).

**Check**
- At spin 0.998 the visual must change dramatically: inner disk pulled toward
  the center. The parameter must be VISIBLY physical; if dragging the slider
  changes nothing, the integration is not responding to spin.

**Why**
An interactive physical parameter is the demo: the user discovers the physics
by dragging, not by reading. Keep the cinematic grade clearly labeled as art
direction so it never pollutes the physics.

## The human method, distilled

1. Derive the visuals from the physics, never paint them: shadow, photon
   ring, disk arch, Doppler brightening, redshift, Einstein ring all emerge
   from one integrator.
2. Ship the URL and let the device matrix come from testers; declare the
   WebGPU floor honestly.
3. Make the parameter the demo: spin 0 to 0.998 as a slider teaches what a
   paragraph cannot.
4. Label the cinematic grade as art direction, not physics.

## Depth status

FULL (author-disclosed simulation recipe with exact physics components and a
community-verified compatibility matrix; no code was published, no parameters
invented).

## AAA studio practice

Sources:
- Double Negative (DNEG) and Kip Thorne, Interstellar Gargantua: the DNGR renderer traced bundles of light (beams), not single rays per pixel, through Kerr spacetime, because single-ray sampling produced flickering stars; the disk arching over and under the shadow, the photon ring, and the Einstein ring all emerged from the integration. https://physicsworld.com/a/decoding-the-dark-arts-of-interstellars-black-hole/
- Double Negative, Interstellar (Guinness/APS accounts): Gargantua was rendered with DNGR solving light propagation around a spinning black hole, and the film deliberately removed the Doppler effect from the final image to make it more comprehensible to viewers. https://www.guinnessworldrecords.com/world-records/418612-most-scientifically-accurate-black-hole-in-a-movie
- WebGPU production practice (general): WebGPU compute shaders enable software ray tracing at interactive rates for simpler scenes even without hardware ray tracing exposed, and frameworks such as Babylon.js and three.js ship WebGPU renderers for production browser 3D. https://terabyte.systems/posts/webgpu-next-generation-graphics-web/

**Do**
1. Keep the emergent-phenomena test as the correctness gate (already in Phase 2), and add the DNEG anti-flicker check: orbit the camera slowly and capture frames; starfield pixels must move smoothly, not flicker or jump, which is the symptom DNEG's beam approach was built to kill. [Inference] A single-ray-per-pixel browser integrator may still flicker at starfield edges; if it does, supersample or jitter-and-accumulate per pixel rather than painting a glow.
2. Label the Doppler choice explicitly, following the film's precedent: Interstellar removed Doppler for comprehension, while this demo keeps it. State in the UI which effects are physics and which are art direction, so the Cinematic grade never silently changes the physics.
3. Automate the compatibility matrix: script a probe page that checks `navigator.gpu`, requests an adapter, and logs adapter, browser, OS, and pass/fail, instead of collecting tester reports by hand. Agent-executable check: run the probe on each target browser and append the row to the matrix; a browser with no adapter is a declared unsupported floor, not a bug.
4. Automate the spin sweep: script spin values 0, 0.5, 0.9, 0.998, capture a frame at each, and diff the inner-disk radius; the 0.998 frame must differ visibly from the 0 frame, or the slider is decorative.

**Check**
- Slow orbit produces no starfield flicker.
- The compatibility matrix has one row per tested browser/OS, generated by the probe, not by anecdote.
- The spin sweep shows a monotonic visible change toward 0.998.

**Why**
DNEG's lesson is that the renderer must earn its phenomena from the physics and then prove it with motion, not stills. The browser version inherits the same burden at interactive rates, plus a capability floor that must be probed, not assumed.
