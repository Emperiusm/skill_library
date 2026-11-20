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

## AAA studio practice

- **Pixar USD / Hydra pipeline.** USD's Hydra imaging framework lets artists switch render delegates in the viewport (OpenGL vs RenderMan in the same session), and USDView can stream any USD file and render it with the chosen delegate. RenderMan ships hdPrman, its Hydra delegate, with support for SideFX's Solaris, which is "completely built around USD." karles22 is the same pattern with a different renderer: a Hydra delegate that brings Cycles into the USD/Solaris frame instead of asking the artist to leave it. Source: https://renderman.pixar.com/stories/pixars-usd-pipeline
- **SideFX third-party rendering in Solaris.** Solaris accepts any renderer designed as a Hydra delegate (RenderMan, Arnold, Redshift, Karma) and lets the artist switch delegates in the viewport while navigating a shot. Materials are set up once in a unified USD/MaterialX setup, and Houdini's COPs compositing can combine the best parts of different renderers in one final image. The implication for this skill: the delegate is a swappable choice per shot, and the scene (USD + MaterialX) is the stable asset, not the renderer. Source: https://www.sidefx.com/tutorials/3rd-party-rendering-in-solaris/
- **Tangent Animation, Next Gen (2018, Netflix).** The feature was rendered 100% in Blender Cycles: "effectively 100% Blender" for the core work, with Cycles for all rendering. The production numbers are the benchmark for a Cycles-as-production-renderer claim: 133,920 frames at 24 fps, averaging 3.76 hours per frame, rendered on around 2,500 nodes in roughly 42 days. The look discipline matches this skill's "final images without comping" principle: the look was accomplished in-camera (Filmic colour transform, linear colour space, 3D motion blur and depth of field throughout), Cryptomatte renders were used for compositing, and the composites themselves were deliberately simple, mainly for a consistent look and grunge. Source: https://blenderartists.org/t/new-from-tangent-animation-next-gen-is-this-bender/1116159/38

**Agent-executable upgrades**

1. **Delegate A/B gate.** Before switching a scene to karles22, render the same MaterialX scene in karles22 and in Karma (or the incumbent delegate) at low samples and record per-frame time, sample count, and a side-by-side diff in a `delegate-ab/` folder. The switch is justified by measured speed, not by the effect list: the skill's own failure mode says if the answer is post effects alone, Karma plus the slapcomp with COPs already does that.
2. **Render manifest (`karles22-render.json`).** Delegate, Hydra delegate version, sample count, even-distribution confirmation, per-frame time, peak RAM, kernel-build status, and the list of applied in-render post FX with their parameters. The first-render RAM gate: record peak RSS and confirm the kernel built before judging speed, so the 3070 Ti freeze in Phase 4 becomes a check instead of a surprise.
3. **Volume-look comparison check.** Render one volume-heavy test frame in both karles22 and Karma and log the visual difference. The author warns the look can be different on volumes in v1.0; volume scenes are gated on this comparison before adoption.
4. **In-render post-FX ledger.** Each one-click effect (aberration, grain, halation, glow, streaks) is recorded with its parameters per render in the manifest, so the finished look travels with the scene and is reproducible instead of being a remembered click.
5. **Adoption checklist as a gate.** Linux support, RTX 20-series support, and the DLSS question are tracked as named fields in the manifest with their status (shipped / in progress / unanswered), updated from the author's replies, so a studio-adoption decision reads the current state instead of the v1.0 launch state.

## The human method, distilled

1. One node to learn: a render delegate that needs a manual is a render delegate that will not be tried.
2. Final images without comping: speed plus in-render post FX is the product, not raw path-tracing quality.
3. "Please try it yourself": the author asks for honest feedback on real scenes rather than asserting superiority over Karma.
4. Stay in the conforming frame: Solaris is the only real USD and MaterialX conform software, so the delegate comes to Solaris instead of asking the artist to leave it.

**Depth status:** FULL (full post text + 26 comments, including the author's replies on speed, CPU rendering, Linux, and the 3070 Ti defect report; the native clip is a real-time demo of the same claims).
