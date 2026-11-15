---
name: voronoi-border-warp-province-maps
description: "Bend Voronoi province borders with 3 octaves of value noise: warp the classified point instead of moving the edges, with exact constants (lambda 26/10/4.5, a 3.6/1.4/0.5, max offset 5.5 texels). Trigger when Voronoi cell edges look like a mosaic instead of a map."
---

# Domain-Warped Voronoi Province Borders

## Purpose

This skill reconstructs the author's exact workflow, step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The method's core idea is: do not move the edges; move the point being
classified.

## Source

Creator: No-Confidence-8651. Reddit post:
https://www.reddit.com/r/proceduralgeneration/comments/1xw8ztn/voronoi_borders_are_too_straight_so_i_bend_them/
(r/proceduralgeneration post 1xw8ztn, score 102, 3 comments) | 2026-11-15
scout run, audit 8.

## Tools used

C++ and OpenGL (author's game, Contours of War, a grand strategy game).
Provinces are Voronoi cells.

## Phase 1: Warp the classified point

**Do**
1. Define the warp: p' = p + sum a_i * n(p / lambda_i), in province-texture
   texels, over three octaves:
   - i = 1: lambda = 26, a = 3.6
   - i = 2: lambda = 10, a = 1.4
   - i = 3: lambda = 4.5, a = 0.5
2. Define n as value noise in [-1, 1]: an integer hash at the 4 lattice
   corners, bilinearly blended with smoothstep weights s(t) = t^2 (3 - 2t).
3. Give each octave its own seed, and give x and y different seeds too, "so
   the offset isn't diagonal" (author).
4. Look the cell up at the warped point: cell(p) = argmin_k ||p' - s_k||, a
   normal Voronoi lookup at the warped point.

**Check**
- The warp is continuous and gentle: the offset never exceeds
  3.6 + 1.4 + 0.5 = 5.5 texels, small next to a cell. (Author's bound.)
- Straight cell edges stop looking like a mosaic and start looking like a map.
  (Author's motivation: "Provinces in my grand strategy game (Contours of
  War, C++/OpenGL) are Voronoi cells. Straight cell edges look like a mosaic,
  not like a map.")

**Why**
- Moving the edges means rebuilding geometry. Moving the classified point
  means the same lookup, one warp earlier. The warp is bounded, so no cell
  can swallow its neighbor; the borders bend but the topology holds.
  (Inference from the author's bound, labeled.)

## Phase 2: Consider the spline alternative (commenter)

**Do**
1. Read commenter habarnam (score 6): "Have you tried using the voronoi
   nodes as nodes for some splines? Have a look at this one
   (https://gasiulis.name/new-spline/)."

**Check**
- Unanswered in the thread; the author did not reply in the fetched comments.

**Why**
- Splines through Voronoi nodes would give smooth, editable borders instead
  of warped ones. It is the alternative design, not the chosen one. (Inference, labeled.)

## The human method, distilled

1. Warp the query, not the geometry.
2. Bound the warp (5.5 texels) so the topology cannot break.
3. Separate seeds per octave and per axis, or the warp goes diagonal.
4. "Straight cell edges look like a mosaic, not like a map." The fix is three
   octaves of value noise, not a new border algorithm.

**Depth status:** FULL. The author's own comment gives the complete formula,
all six constants, the noise definition, the seed discipline, and the bound.
Three comments total, all read. No download needed.
