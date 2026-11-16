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

## Production practice

Labeled production practice, not AAA: no AAA studio source was found for
warping Voronoi province borders specifically. The nearest anchors are a
shipped indie game using the same warp-the-field idea, and the standard
domain-warping references the author's formula is a special case of.

- **A shipped game warps its Voronoi map with noise the same way (DwarfCorp, Game Developer).** DwarfCorp's continents start from fault lines, build a Voronoi diagram of the fault map ("compute the distance from every pixel to the nearest fault line"), and then "apply random distortion to the Fault Map using Simplex Noise." The game's own framing: "One of the most powerful tools in procedurally generated games is the use of Perlin (or in our case Simplex noise)" ([Game Developer, "How we Generate Terrain in DwarfCorp"](https://www.gamedeveloper.com/programming/how-we-generate-terrain-in-dwarfcorp)). DwarfCorp distorts the distance field; the author distorts the query point. The two are the same idea from opposite sides: never rebuild the Voronoi geometry, bend the field it is read from.
- **Domain warping is the canonical recipe, and the author's formula is a three-octave instance of it (Red Blob Games; Nolithius).** The Red Blob Games recipe stack: "the sample point gets domain-warped first: you offset each coordinate by another noise field, p'=p+noise(p)*s, which bends the ridges into something organic instead of axis-locked" ([Cinevva, open-world browser series, part 27](https://app.cinevva.com/blog/2026-05-13-open-world-browser-part-27-island-and-terrain)). Nolithius's domain-warping guide makes the author's seed discipline explicit: "generate two additional Perlin noise maps for displacement: one for the X values, and one for the Y" ([Nolithius, "World Generation Techniques: Domain Warping"](https://www.nolithius.com/articles/world-generation/world-generation-techniques-domain-warping)). The author's rule (separate seeds per octave and per axis, "so the offset isn't diagonal") is that guide's X/Y split, formalized.
- **The honest gap: province borders at strategy-game scale.** DwarfCorp warps terrain faults; Red Blob warps heightfields. Neither source addresses what the author is doing, which is warping political borders that must stay readable as territories. The 5.5-texel bound is the author's own answer to that gap, and it is what the regression test below guards. No studio source was found that states a border-warp bound for provinces; the bound stays the author's, labeled as such.

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

## Phase 3: Guard the warp with regression tests

The formula is FULL depth and exact. The tests below are what keep it
exact across refactors, and what catch the one failure the bound exists
to prevent: a cell swallowing its neighbor.

**Do**
1. Run the warp-budget test: sample the warp offset on a dense grid over
   the province texture and assert the maximum offset never exceeds 5.5
   texels (3.6 + 1.4 + 0.5). If any sample exceeds it, a constant changed
   and the bound no longer holds.
2. Run the determinism test: same seeds and same province seeds twice
   must produce a byte-identical province map (hash the output). The
   seeds are the map; a map that drifts between runs cannot be shared or
   debugged.
3. Record the border-likeness metric, not as a gate but as a number: total
   warped border length divided by total straight border length on the
   same province set. The author's motivation is "looks like a map, not a
   mosaic"; the ratio is the measurement of that claim. Log it per
   release; if a constants change drops the ratio toward 1.0, the warp
   stopped doing its job.
4. Run the diagonal check: warp a test point with the x-seed and y-seed
   swapped. If the output is identical to the unswapped warp, the seeds
   are not actually separate per axis, and the author's "so the offset
   isn't diagonal" rule is broken.

**Check**
- Max sampled offset is at most 5.5 texels.
- Two runs with the same seeds hash identically.
- The border-length ratio is recorded and above 1.0.
- Swapping x/y seeds changes the output.

**Why**
- The bound is the whole safety argument: bounded warp means the
  topology cannot break. A bound that is never tested is a comment, not
  a guarantee.

## The human method, distilled

1. Warp the query, not the geometry.
2. Bound the warp (5.5 texels) so the topology cannot break.
3. Separate seeds per octave and per axis, or the warp goes diagonal.
4. "Straight cell edges look like a mosaic, not like a map." The fix is three
   octaves of value noise, not a new border algorithm.

**Depth status:** FULL. The author's own comment gives the complete formula,
all six constants, the noise definition, the seed discipline, and the bound.
Three comments total, all read. No download needed.
