---
name: godot-silk-vfx-vector-pixelation
description: "Hand-made pixel-art VFX in Godot 4: smooth vector shapes with tonal 3D faking, a pixelation shader on top, silk as dots moving along lines. Trigger when building fluid 2D VFX with a retro pixel look."
---

# I'm making silk-like pixel-art VFX in Godot 4

## Purpose

This skill reconstructs the exact VFX workflow described by StillEnvironmental64 for the Reaper boss rage move in THE INK TOWER, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: *smooth 2D vector shapes with tonal variation, pixelated by a custom shader, animated as dots moving along lines.*

## Source

Creator: StillEnvironmental64 (game: THE INK TOWER — Steam app 5295020, itch.io nathannhu/the-ink-tower)

Source: https://www.reddit.com/r/godot/comments/1xl7xvc/ | r/godot post 1xl7xvc (score 559, 2026-11-01) | video: v.redd.it/bkx0rx8v41zh1

Earlier breakdowns in the same series: ground slam (r/godot/comments/1x8i8fc), lava (r/godot/comments/1xei4ae). The move: the boss turns into silk, stops at 3 spots around the player, leaves a ghost at each ready to swing; one cloth runs through all of them, then the ghosts cut one by one and he cuts last.

Depth: FULL — technique fully specified by the author in post + comments.

## Tools used

Godot 4; 2D vector shapes (smooth, not pixel-drawn); a custom pixelation shader over the whole effect ("Its smooth vector shapes with different tones to mimic the 3d look, and i put a custom shader on top to make it look pixelated"); "its 2d with a pixel renderer". No AI assets (author, replying to a commenter who suspected AI from the step-by-step panels: "Because i dont use AI assets?").

## Phase 1: Steal the motion from film

**Do**
1. Pick a film reference for the motion, not a game reference: the author started from the cloth-trails VFX of the monks (tengu) in the movie *47 Ronin*.
2. Prototype the motion crudely first: the author's first attempts were "a spinning cross that leaves a trail", then "a cloth dragged behind him."

**Check**
- The crude prototype should read as cloth-like motion before any styling is applied.

**Why**
- Motion first, look second. The author iterated motion ("it started from the cloth trails visual effect... First i tried a spinning cross that leaves a trail, then a cloth dragged behind him") before committing to the pixel look, and the process was "mostly trial and error."

## Phase 2: Build the look — vectors, tones, pixelation shader

**Do**
1. Draw the effect as smooth vector shapes (re-poseable, resolution-independent).
2. Vary the tones across the shapes to fake 3D volume — the tonal variation is what mimics the 3D look.
3. Put a custom shader on top that pixelates everything. The game renders 2D through a pixel renderer.

**Check**
- Zoom in: edges must snap to a pixel grid while the underlying shapes stay smooth and re-poseable. The look should stay fluid, not shimmery.

**Why**
- Vector-then-pixelate separates the two hard problems: fluid motion (vectors are cheap to animate) from the retro look (the shader imposes the grid). Commenter Vathrik named the target precisely: "Programmatic pixel art is an interesting artistic challenge as you want to add fluidity but not too much shimmer or detail causing visual noise. You nailed the sweet spot."

## Phase 3: Animate silk as dots along lines

**Do**
1. Animate the silk as dots moving along lines — "most of it is moving dots along lines."
2. Render the back half of each strand fainter than the front, so the strand reads as round — "the rest is making the back half fainter so it looks round."

**Check**
- Freeze a frame: strands should read as tubes, not flat ribbons. If they read flat, the back-half falloff is too weak.

**Why**
- A line with a brightness gradient across its width is the cheapest possible tube; dots traveling along the line give flowing motion without simulating cloth.

## Phase 4: Iterate the money shot by explicit rejection

**Do**
1. For the key moment (ghosts cutting the silk), generate versions and reject each by a named visual reason. The author tried 4: a piece falling off, a whip, a loose end with rags, a fire running along it — "none of them looked right, one was like confetti."
2. Ship the version that reads: the coil around a ghost comes off when it attacks, and the loose silk pulls over to the next ghost.
3. Cut scope that delays the move's start: the boss originally dove in and hit at every stop; the author removed the dive so "the move start[s] right away."

**Check**
- Every rejected version has its failure named ("one was like confetti" = wrong motion language for silk). The shipped version starts immediately — no wind-up spectacle before the readable action.

**Why**
- When the goal is a *feel*, trial-and-error with explicit rejection beats planning. Responsiveness outranks spectacle: the player must read the attack the instant it starts.

## The human method, distilled

1. "Because i dont use AI assets?" — hand-made, stated plainly when challenged.
2. Steal motion from film, not from other games (47 Ronin tengu cloth trails).
3. Reject by look, and name the failure ("one was like confetti").
4. Responsiveness over spectacle: cut the dive so the move starts right away.
5. Publish the breakdown series (ground slam, lava, silk) — each effect gets its own write-up.

## Failure modes

- **Confetti failure:** fire/particle-style motion on silk reads as confetti — the motion language must stay cloth-like (dots along lines), not emissive-chaotic.
- **Shimmer/visual noise:** too much detail or fluidity in programmatic pixel art breaks the look; the shader's pixel grid is the constraint that keeps it clean.

**Depth status:** FULL (author-specified technique; no invented parameters)
