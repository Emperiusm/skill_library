---
name: karles22-cycles-houdini-solaris
description: "Render Blender Cycles inside Houdini 22 Solaris with the karles22 Hydra 2 delegate: one Render Settings node, MaterialX native, even per-pixel sampling, photon caustics, and one-click in-render post FX. Trigger when a Houdini lookdev needs speed and finished images without comping."
---

# karles22: Cycles in Houdini 22 Solaris

## Purpose

This skill reconstructs the exact workflow Nikolaus (immortalartscom) demonstrates for rendering with karles22, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: one node to learn, existing MaterialX scenes switch over with no conversion, and the render is fast enough with in-render post FX that the final image needs no comping.

## Source

Creator: Nikolaus, a 3D/VFX artist from Vienna (u/immortalartscom). Post: "I built karles22 - Cycles in Houdini 22 Solaris, MaterialX native" https://www.reddit.com/r/Houdini/comments/1xza92p/ (score 30, 26 comments; full post text and comments read) | https://tools.immortal-arts.com | 2026-11-19 scout run, audit 2.

## Tools used

Houdini 22 Solaris, Blender Cycles as a Hydra 2 render delegate, MaterialX. Perpetual license, no subscription; free demo is watermarked, testers get a time-limited full version with no watermark.

## Phase 1: Switch a MaterialX scene to karles22

**Do**
1. Add the karles22 Render Settings node. The author states there is only one node to learn.
2. Open an existing MaterialX scene in Solaris. No conversion of shaders or lights is needed; scenes "should match Karma pretty close."

**Check**
- The test the author invites: try it on your own scenes with the free demo and give honest feedback (DM him; testers get a time-limited full version with no watermark, unlike the demo).

**Why**
The author is "mostly an in-camera artist" who missed speed, responsiveness, photon caustics, and post FX "right in the render." Staying in Solaris matters because, in his words, "Houdini Solaris is the only real USD and MaterialX conform software out there."

## Phase 2: Render for speed, not just quality

**Do**
1. Render with karles22 distributing samples evenly: every pixel gets the same base sample count, including dark corners and low-light areas.
2. Use it on scenes mixing challenges (SSS, hair, volumes), where the author claims roughly 2x up to much more than Karma.
3. Everything in the video is recorded in real time, no speed-up (author's claim).

**Check**
- A commenter asked the advantage over Karma, since the post effects are available in the slapcomp with COPs. Author's answer: speed and responsiveness.
- A commenter asked about CPU rendering on a dated 3080. Author: responsive but not fast in rendering; a 3080 "will be smooth and fast enough."

**Why**
Even sample distribution is the mechanism: no region starves while another oversamples, so mixed-challenge scenes finish faster instead of stalling on their hardest part.

## Phase 3: Finish in the render, not in comp

**Do**
1. Apply post effects in the render, one click each: aberration, grain, halation, glow, streaks.

**Check**
- The author's principle: "it's not about being better than other tools, it's about final images without comping."

**Why**
If the look is finished in the render, there is no comp pass to maintain, and the look travels with the scene.

## Phase 4: Know the v1.0 limits before adopting

**Do**
1. Expect a perpetual license, no subscription, when buying. The demo is watermarked.
2. Linux support arrives in the next version (author's reply to a studio-adoption question). RTX 20 series support is being added now.
3. Note the defect report: a tester on a 3070 Ti froze his computer on first render (ran out of RAM) and the kernel did not fully build on setup. The author notes the Apprentice version is not in the specs list.
4. Note the adjacent tool from the same author: a Blender-to-USD exporter that converts a whole scene, including Geo Scatter work, to USD and MaterialX; it will be a separate tool.

**Check**
- A commenter asked for DLSS support like Blender recently got; no answer in the thread.
- A commenter asked for a Blender materials converter as the killer feature, "because there is a ton of materials"; no answer in the thread.

**Why**
A v1.0 tool's limits are part of the workflow: RAM headroom on first render, kernel build on setup, and the missing Linux build decide whether a studio can adopt it yet.

## Failure modes

- **First-render freeze on a 3070 Ti:** the tester ran out of RAM and the kernel did not fully build. Give the first render RAM headroom and confirm the kernel builds before judging speed.
- **Volumes look different:** the author warns the look can be different on volumes in v1.0. Compare a volume-heavy scene against Karma before committing to karles22 for it.
- **"Why not Karma?":** if the answer is post effects alone, Karma plus the slapcomp with COPs already does that. karles22's case is speed and responsiveness, so measure those, not the effect list.

## The human method, distilled

1. One node to learn: a render delegate that needs a manual is a render delegate that will not be tried.
2. Final images without comping: speed plus in-render post FX is the product, not raw path-tracing quality.
3. "Please try it yourself": the author asks for honest feedback on real scenes rather than asserting superiority over Karma.
4. Stay in the conforming frame: Solaris is the only real USD and MaterialX conform software, so the delegate comes to Solaris instead of asking the artist to leave it.

**Depth status:** FULL (full post text + 26 comments, including the author's replies on speed, CPU rendering, Linux, and the 3070 Ti defect report; the native clip is a real-time demo of the same claims).
