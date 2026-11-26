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

## The human method, distilled

1. **Answer the per-pixel question, not the camera question:** latitude of the curtain, not latitude of the viewer.
2. **Take the numbers from the real phenomenon:** 64/54/50-degree oval edges, Kp levels, 111 km per degree scaled to 3 km.
3. **Cheap gates before expensive marches:** if a test can skip the march, it runs first, cheapest first.

## Depth status

FULL from the author's full post text. No shader code, Bevy version, or frame-time measurement was disclosed, and none is invented here. The planet is "a planet the full size of Earth" (author's words); no radius value is stated.
