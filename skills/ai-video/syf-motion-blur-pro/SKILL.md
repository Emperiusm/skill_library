---
name: "syf_motion_blur_pro"
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

## The human method, distilled

1. Build the six-test benchmark first; every claim in the video is demonstrated on it.
2. When the general algorithm fails, reach for the specialized one, then stack them.
3. Free distribution via ko-fi support ("Supported by buying me a coffee"), the economic model is stated on the panel itself.

## Depth status

FULL (complete media download + 10 reviewed frames + full captions, 320 segments).
