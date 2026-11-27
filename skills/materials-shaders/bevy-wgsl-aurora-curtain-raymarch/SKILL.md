---
name: bevy-wgsl-aurora-curtain-raymarch
description: "Place an aurora by the latitude of the curtain each pixel looks at, not the camera's, in Bevy/WGSL: raymarch curtains in the sky pass at about 3 km of curtain per degree, roll the oval from the real 64/54/50-degree edges, dim and redden with distance (brightness 0.15 + 0.85 x activity), read striation off both horizontal axes, and gate the march cheapest-first so daylight, clouds, and caves skip it. Trigger when a sky aurora must stay on the horizon at mid-latitudes instead of drawing overhead."
---

# Bevy/WGSL Aurora Curtain Raymarch

## Purpose

This skill places an aurora where it belongs: on curtains in the sky, judged by the latitude of the curtain each pixel looks at. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: per-sample curtain latitude, a real oval, distance dimming and reddening, and cheap gates before the expensive march.

## Source

- Post: "Placing an aurora by the latitude of the curtain each pixel looks at, not the camera's" by Hazmadd — https://www.reddit.com/r/GraphicsProgramming/comments/1y4qt3h/ (score 25, 6 comments). Evidence: the author's full post text (1,868 characters, all five sections with exact numbers), corroborated on the two headline techniques by a commenter. Game: Steadfall (Bevy/WGSL, a planet the full size of Earth). AI disclosure in the post: "No generative AI". Scout audit 2026-11-26, audit 5, FULL.

## Tools used

Bevy; WGSL (sky-pass shader, raymarched). No Bevy/WGSL version named. No shader code, frame-time measurement, or radius value was disclosed; none is invented here.

## Phase 1: Place curtains by per-sample latitude, not camera latitude

**Do**
1. Make the curtains a field around the camera, raymarched in the sky pass.
2. For each sample, work out the latitude of the curtain being looked at, at about 3 km of curtain per degree (the real 111 km per degree scaled down by the curtains' height), with north as -Z.
3. Under the oval, change nothing. South of it, light only the curtains toward the pole; they are far and low, so the display sits on the horizon.

**Check**
- A storm at 41 degrees latitude must sit on the horizon, not draw a full display overhead. The first version's failure is the test: it gated by camera latitude with a wide oval falloff and drew overhead displays "far from where a real aurora reaches".

**Why**
An aurora is a place, not a camera effect. Gating by camera latitude answers "where am I?" instead of "what latitude is that curtain at?" The 3 km-per-degree scale is the author's stated compression of the real 111 km per degree to curtain height.

## Phase 2: Roll the oval from the real auroral oval

**Do**
1. Set the oval's equatorward edge to about 64 degrees on a quiet night, 54 at Kp 7, 50 at Kp 9.
2. Roll an activity level each night. A storm is activity above 0.7 and lands a few nights a year.

**Check**
- Quiet nights keep the oval near 64 degrees; storms push it to 54/50 degrees at the stated Kp levels. Storms stay rare: a few nights a year, not every night.

**Why**
Real oval behaviour is the spec. Activity as a nightly roll makes storms events rather than a permanent sky feature.

## Phase 3: Dim and redden with distance

**Do**
1. Dim a far curtain by its long, low path through the air: under half brightness at 30 km.
2. Shift it red with distance, since what survives of a distant display is its red top.
3. Set brightness to 0.15 + 0.85 x activity, scaled so a storm overhead is a few times brighter than a quiet arc.

**Check**
- A distant display is dim (under half at 30 km) and red-shifted. A storm overhead reads a few times brighter than a quiet arc. The anti-pattern is a "flat green wash": uniform green at all distances and activities.

**Why**
Distance through air causes both effects: the long low path eats brightness and leaves the red top. The 0.15 floor keeps a quiet arc visible; scaling with activity makes storms feel like events.

## Phase 4: Read ray striation off both horizontal axes

**Do**
1. Read striation off both horizontal axes, not one world axis.
2. Spread it around the channel's median for gaps between rays.
3. Walk its phase along the height axis by whole turns so nothing jumps once a cycle.

**Check**
- An east-to-west curtain shows distinct rays with gaps instead of smearing into a band. The phase walk must not jump once per cycle.

**Why**
One-axis striation assumes one curtain orientation. Both horizontal axes make the ray pattern orientation-independent, and whole-turn phase steps keep the cycle continuous.

## Phase 5: Gate the march, cheapest test first

**Do**
1. Before any marching, run these gates, cheapest first: not airless; sky reachable (no aurora in caves); sun at least 9 degrees down (full strength by 13); cloud cover under 0.55 (gone by 0.85); an oval within 16 degrees.
2. If any gate fails, skip the march entirely.

**Check**
- Daylight, clouds at/above 0.85, caves, and a distant oval must all skip the march. The thresholds above are the exact stated values; do not soften them.

**Why**
Raymarching is the expensive step; every gate in front of it is cheaper than the march. Cheapest-first ordering means common rejections cost almost nothing.

## AAA studio practice

No named AAA studio was found publishing an aurora-oval shader with the 64/54/50-degree edges, Kp levels, or gate thresholds this skill uses, and none of those numbers is claimed as a studio standard. They stay the author's. The practices below are the production-grade versions of this skill's two structural ideas (a physical sky pass, and cheap gates before an expensive march), each cited to its source.

- **A sky effect in production is a physical atmosphere pass, decoupled from screen resolution, not a camera-space wash.** Epic's Sky Atmosphere work (Sébastien Hillaire, SIGGRAPH 2020) moved from ray marching without multiple scattering and without aerial perspective, and from model-fit skies that only work from the ground, to lookup-table models that support views from space, dynamic time of day, and aerial perspective, with new low-resolution LUTs that maintain high-frequency features and decouple atmosphere rendering from final screen resolution, scalable from mobile to high-end PCs by tweaking LUT resolution and sample count. The lesson for this shader is the same decoupling this skill already uses in miniature: the aurora is placed in world/sky space (curtain latitude), not camera space, and its cost must be measured independently of resolution. The author's per-sample latitude, distance dimming, and reddening are the aurora-specific form of that physical placement; the LUT decoupling is the production mechanism this WGSL shader does not claim to use. Source: https://blog.selfshadow.com/publications/s2020-shading-course/hillaire/s2020_pbs_hillaire_slides.pdf
- **Volumetric sky rendering in production is budgeted in milliseconds and gated by cheap tests, with the expensive march last.** Guerrilla's Nubis volumetric cloud system rendered dynamic volumetric skyboxes in under 2 milliseconds on PlayStation 4 for *Horizon Zero Dawn*, and was expanded for *Horizon Forbidden West* into fly-through clouds and fast-spinning superstorms with internal lighting, solving ray-march acceleration and temporal artifacts as the cost of moving the effect closer to the player. The discipline transfers directly: state the march cost as a measured budget, keep the march out of cases it cannot improve (daylight, caves, heavy cloud), and treat any expansion of the effect's range as a new budget negotiation, not a free parameter change. The under-2ms figure is Nubis on PS4, not this shader's budget, and must not be copied into this skill as its target. Source: https://www.guerrilla-games.com/read/nubis-evolved
- **Raymarched auroras outside AAA use the same curtain idea, which corroborates the march but not the numbers.** An 80 Level writeup of a Godot aurora borealis effect describes a raymarching shader with a NoiseTexture, presented as memory-efficient, from an indie studio (Miskatonic Studio). It corroborates that raymarching is a known route to this look in Godot, and it supplies no oval, Kp, brightness, or gate values. Treat it as corroboration of the technique only. Source: https://80.lv/articles/realistic-aurora-borealis-effect-made-in-godot-engine

**Agent automation**

Write `aurora-manifest.json` beside every build, with exactly these fields: oval edge degrees used, activity roll and storm threshold, brightness formula inputs (floor, activity multiplier), gate thresholds exactly as stated (sun 9 degrees down, full strength 13, cloud cover 0.55 gone by 0.85, oval within 16 degrees), measured march time in ms on the test machine, and storm nights logged. Fail the run if the march time is empty or copied from Nubis: no frame-time measurement was disclosed for this shader, and none may be invented. Then run these gates in order: (1) horizon gate, reproduce the author's failing test, a storm at 41 degrees latitude must sit on the horizon, not overhead, and record the result; (2) gate-skip gate, force each gate condition in turn (daylight, cloud at or above 0.85, cave, distant oval) and record that the march is skipped in each case [inference: forcing gate conditions in a test harness is agent design, built from the skill's own gate list]; (3) distance gate, capture acceptance renders of a distant display and record dimming below half brightness at 30 km and the red shift, against the stated values; (4) storm-frequency log, record every night rolled and every storm, because "a few nights a year" cannot be verified in one run and must accumulate in the manifest. No shader code, Bevy/WGSL version, or radius value may be entered into the manifest, because none was disclosed.

## The human method, distilled

1. **Answer the per-pixel question, not the camera question:** latitude of the curtain, not latitude of the viewer.
2. **Take the numbers from the real phenomenon:** 64/54/50-degree oval edges, Kp levels, 111 km per degree scaled to 3 km.
3. **Cheap gates before expensive marches:** if a test can skip the march, it runs first, cheapest first.

## Depth status

FULL from the author's full post text. No shader code, Bevy version, or frame-time measurement was disclosed, and none is invented here. The planet is "a planet the full size of Earth" (author's words); no radius value is stated.
