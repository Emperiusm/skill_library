---
name: syf-motion-blur-pro
description: "Add motion blur with a free OFX plugin: match the algorithm to the motion type (estimation vs analytic linear/rotating/zooming), tune length vs strength, stack instances for complex shots. Trigger when adding motion blur in post."
---

# SYF Motion Blur Pro: Free OFX Motion Blur

## Purpose

This audit reconstructs the exact plugin workflow from the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: two algorithm families, motion estimation for general motion, cheap analytic blurs for pure linear/rotation/zoom, with stacking for complex shots.

## Source

Creator: Syfilms64 / Scrapyard Films / Josh

Source: https://www.youtube.com/watch?v=i4b3CCXf6BQ | 11:05 | r/vfx post 1wqqeks (score 21) | 807 views | 2026-09-28 scout run

## Tools used

Tools used: **SYF Motion Blur Pro** (free OFX plugin, closed-source free binary; author declined the GitHub open-source request in comments: "I'm not smart enough for that yet"); Vegas Pro; DaVinci Resolve; any OFX host. Download: https://scrapyardfilms.com/product/syf-motion-blur-pro/

## Phase 1: Install and apply

**Do**
1. Install; the plugin appears in the video effects tab as **SYF Motion Blur Pro**; drag the default preset onto the clip (verified in Vegas Pro and DaVinci Resolve).

**Check**
- Effect panel shows: support button, Enable GPU Hardware Acceleration, Quality Mode, Vector Strength, Blur Length.

**Why**
- OFX = write once, run in Vegas + Resolve + other OFX hosts (frames confirm Resolve panel with "Enable GPU Hardware Acceleration", "Quality Mode" dropdown, "Vector Strength" 16.00, "Blur Length" 40.00).

## Phase 2: Set up the six test cases

**Do**
1. Author six labeled clips: linear (text moving straight), rotating, zooming, all (combined motion), experimental (same as all, used for stacking), screen recording (zoom in to pan to zoom out, the tutorial-video standard).
2. Play each at default: High Quality, all directions.

**Check**
- The plugin's own benchmark: every claim in the video is demonstrated on this suite.

**Why**
- Quoted principle: "the blur is looking real nice" at speed, but slow-motion review reveals where estimation breaks, the test suite is the benchmark.

## Phase 3: Choose the algorithm per motion type

**Do**
1. **High Quality / Fast Quality**: motion-estimation algorithm; HQ samples many frames before and after, Fast uses fewer, "about two to four times faster" at "really, really good results".
2. **Only Linear / Only Rotating / Only Zooming**: "completely different algorithm that's actually faster", analytic, one direction each. Rotation: Blur Length 3. Zoom: Blur Length 2-2.5.

**Check**
- Rotating test at default: "once the rotations get too fast, you're going to see the motion totally breaking up", switch to the rotating-only algorithm: "almost no issues".

**Why**
- Motion estimation fails on fast rotation; the analytic blur is both faster and more correct when the motion is one-dimensional. Match the algorithm to the motion, not the other way round.

## Phase 4: Tune strength vs length

**Do**
1. **Blur Length** = extent of the blur; **Blur Strength** = sample density, lower strength reveals "the samples... not blurred together anymore" (super-sampling).
2. The plugin uses full GPU + CUDA ("Enable GPU Hardware Acceleration") so stacking is cheap.

**Check**
- Increase length to see the direction of motion; dial back to 0.75 for the screen-recording case, where long blur exposes "artifacting and breaking apart points" and new frames that "need to pick up motion after they at least show themselves".

**Why**
- Strength and length are independent levers: length for direction readability, strength for smoothness.

## Phase 5: Stack instances for complex motion

**Do**
1. Stack three instances on the chaotic "all" clip: Only Linear + Only Rotating (length 3) + Only Zooming (length 2.5); pre-render (Shift+B in Vegas).

**Check**
- "Much better than just the motion estimation algorithm ones... really not breaking apart that much on some of those crazy movements."

**Why**
- Analytic blurs compose: "because this motion blur plugin is so lightweight... you can stack multiple instances", a performance hit, but each instance is cheap.

## AAA studio practice

Post-added motion blur is a standard production slot, not a fix of last resort, and the big engines and post houses treat it with the same split the SYF workflow already uses: separate the motion types, and never let blur leak across a cut.

- **The reference amount is an exposure time, not a slider value.** Natural-looking motion blur at 24 fps comes from roughly a 1/48 second shutter (the 180-degree shutter at 24 fps); going far from 1/48 second reads as choppy or stroboscopic because motion blur is what sells continuous motion instead of a run of still frames. Calibrate SYF's Blur Length against that reference: the goal length is the one that reads like a 1/48 second exposure for the shot's frame rate, not the longest length the plugin allows. Source: https://www.wipster.io/blog/debunking-the-180-degree-shutter-rule
- **Shoot clean, add blur in post, when tracking or keying matters.** Motion blur causes problems for green screen keying, tracking, rotoscoping, and stabilization because the algorithms struggle to find pixels they need when there is too much blur; the standard workaround is to shoot at a higher shutter speed and add motion blur to the finished composite with plug-ins like ReelSmart MotionBlur, Twixtor, or CC Force Motion Blur. SYF Motion Blur Pro occupies exactly that slot in an OFX host: it is the post step, applied after the clean work is done. Source: https://www.wipster.io/blog/debunking-the-180-degree-shutter-rule
- **Engines separate camera blur from object blur and kill blur at cuts.** Unreal Engine's motion blur exposes a Motion Blur Amount and a Max Velocity clamp, a Full Motion Blur switch that disables camera motion blur while object motion blur stays active, and camera rotation and translation thresholds that disable camera blur when the camera moves past them (useful for camera cuts); per-object motion blur scale exists alongside. Unity's HDRP motion blur likewise clamps camera motion vectors separately for rotation and translation. The SYF translation: never apply one blur pass to a whole shot and hope; split camera motion from object motion where the host allows it, and always split at cuts before applying blur, because a blur that spans a cut smears two unrelated motions together. Sources: https://docs.unrealengine.com/udk/Three/MotionBlur.html and https://docs.unity.cn/Packages/com.unity.render-pipelines.high-definition@12.0/manual/Post-Processing-Motion-Blur.html
- **Post blur smears on complex, multi-layer motion; that is the known failure, not a surprise.** The same post-production writeup warns that getting really good results from adding motion blur in post can be hard, with smearing artifacts on complex motion, especially with several layers of moving objects, though results can often look quite convincing depending on footage complexity. This is the production-grade statement of SYF's own finding (Phase 4: long blur on screen recordings exposes artifacting and breaking-apart points). When estimation breaks, the answer is the specialized analytic pass or the stack, not more length. Source: https://www.wipster.io/blog/debunking-the-180-degree-shutter-rule

## Agent automation

Turn the six-test benchmark (Phase 2) into a repeatable, logged suite instead of a one-off demo:

**Do**
1. Write a benchmark manifest before touching a new shot type: one entry per test clip with `clip`, `motion_type` (linear, rotating, zooming, combined, screen-recording), `algorithm` (estimation or analytic), `blur_length`, `blur_strength`, `quality_mode`, and `verdict` (pass, break-up, artifact). The six clips from Phase 2 are the seed entries; add a clip whenever a new motion type appears.
2. Gate the algorithm choice on the manifest, not on feel: run the estimation pass first; if the verdict is break-up or artifacting, switch to the matching analytic pass (Only Linear / Only Rotating / Only Zooming) and record the switch. If a single analytic pass still breaks, stack per Phase 5 and record the stack. A shot ships only with a manifest entry whose verdict is pass.
3. Split at cuts before any blur pass: cut the timeline at every scene cut first, then apply blur per segment, so no blur instance ever spans a cut. [Procedure, not a tool claim: use the host's scene detection or split manually; the rule is the split, not the tool.]
4. Record the reference check per shot: note the frame rate and the target exposure feel (1/48 second at 24 fps as the natural-motion reference) in the manifest entry, and dial length back when the blur reads longer than that reference. The screen-recording dial-back to 0.75 in Phase 4 is the template entry.

**Check**
- Every shipped shot has a manifest entry with algorithm, length, strength, and a pass verdict; any shot whose estimation pass broke names the analytic pass or stack that replaced it.
- No blur instance spans a cut: the segment list and the blur-instance list match one-to-one.

**Why**
Engines and post houses do not tune blur per shot by eye alone; they separate motion types, clamp at cuts, and keep the reference exposure in mind. The manifest makes SYF's already-correct instinct (match the algorithm, then stack) into a checkable procedure that survives the next project.

## The human method, distilled

1. Build the six-test benchmark first; every claim in the video is demonstrated on it.
2. When the general algorithm fails, reach for the specialized one, then stack them.
3. Free distribution via ko-fi support ("Supported by buying me a coffee"), the economic model is stated on the panel itself.

## Depth status

FULL (complete media download + 10 reviewed frames + full captions, 320 segments).
