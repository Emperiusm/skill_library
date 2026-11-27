---
name: unity-urp-procedural-planet-near-surface
description: "Render a procedural planet at near-surface detail in Unity URP with custom shaders and walking: target 60fps on an RTX 3070 at 1440p native, name grass and water as the budget breakers, build clouds from a reference presentation and switch to a cheaper opaque cloud version at distance to prevent TAA shimmering, and report the worst case at the switch point. Trigger when a procedural planet must stay fast on the ground and stable from space."
---

# Procedural Planet Near-Surface Rendering in Unity URP (El-Jomo)

## Purpose

This skill reconstructs the exact workflow El-Jomo shows for near-surface rendering of a procedural planet, with walking added, in Unity with URP and custom shaders. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: set a measured performance target on named hardware, build clouds from a reference presentation, switch clouds by distance, and report the worst case at the switch point.

## Source

Creator: El-Jomo. Post: "Did some work on near-surface rendering of my procedural planet. Took the opportunity to add walking as well" — https://www.reddit.com/r/proceduralgeneration/comments/1y651u9/ (score 142, 13 comments, all retrieved). Video: https://v.redd.it/6cvhyxhfez3i1. Scout audit 2026-11-27, audit 2, PARTIAL.

## Tools used

Unity with URP as a basis; all shaders custom. No Unity version, terrain tool, heightmap method, or ground-texturing method is stated in the post or comments. The linked cloud reference presentation was not watched in this run.

## Phase 1: Set the target and name the breakers

**Do**
1. Target 60fps on an RTX 3070 at 1440p native.
2. Name the budget breakers up front: "Grass and Water are the big budget breakers right now and will need some optimization." (post text, verbatim).

**Check**
- Frame rate on the named hardware at the named resolution. No pass numbers are given by the creator: "I don't have pass numbers but the FPS is around 50 at that point on my 3070 at 1440p" (El-Jomo, on the worst case before the cloud switch).

**Why**
A named target on named hardware turns "needs optimization" into a measured statement. The two named breakers say where the work goes.

## Phase 2: Build clouds from a reference presentation

**Do**
1. Build the clouds from the Red Dead Redemption 2 presentation the creator links in a comment (YouTube link, timestamp 7116). The creator's word for the process is "vibe-coded": "I basically vibe-coded the clouds from Red Dead Redemption 2 based on [this] presentation."
2. Do not claim the presentation's contents: it was not watched in this run, so no step from it is reproduced here.

**Check**
- Clouds read correctly both near the surface and from the far view. The far-view screenshot the creator links was not opened or read in this run.

**Why**
Building from a named reference presentation, and saying so, keeps the cloud method traceable even when the implementation was improvised.

## Phase 3: Switch clouds by distance to prevent TAA shimmering

**Do**
1. When the planet is far away, switch to a cheaper opaque version of the clouds "to prevent TAA shimmering" (El-Jomo, verbatim reason).
2. Accept the worst case just before the switch happens: around 50fps on the RTX 3070 at 1440p.
3. Far planet view: around 70fps on the same hardware and resolution.

**Check**
- Far view frame rate (around 70fps) and the pre-switch worst case (around 50fps), both on the same hardware and resolution.
- Shimmer: the opaque far version exists to prevent it. No shimmer measurement is given.

**Why**
Distance switching trades cloud fidelity for stability at range. The switch point is where the cost is worst, so the worst case, not the average, is the number to report.

## Phase 4: Add walking, and leave the open questions open

**Do**
1. Add walking to the near-surface rendering. The viewpoint is not stated in the retrieved text and is not assumed here.
2. Record the two unanswered commenter questions as open work, not as solved steps: how the heightmap generation was done (a commenter assumes noise and says the result looks better than a basic implementation), and how the ground textures and colouring were done. The creator did not answer either in the retrieved comments.

**Check**
- A future breakdown answers the heightmap question and the ground-texture question with a method, not a guess.

**Why**
Unanswered questions recorded as open protect the next person from building on an invented method.

## Failure modes

- Reporting only the far-view frame rate (around 70fps) and hiding the pre-switch worst case (around 50fps). The creator reports both; the worst case is the honest number.
- Assuming a heightmap method (for example, plain noise) when the creator left the question unanswered. No method is stated.
- Assuming the walking viewpoint. It is not stated.

## The human method, distilled

1. State the hardware, resolution, and frame-rate target before judging the work.
2. Name the two things that break the budget.
3. Switch the expensive thing to a cheaper version at distance, and report the worst case at the switch point.
4. Build from a reference presentation and say so, including the word "vibe-coded".

**Depth status:** PARTIAL. Engine, custom-shader fact, performance numbers, cloud switch, and open questions are grounded in the post and comments. Heightmap generation, ground texturing, and the walking implementation are unknown.
