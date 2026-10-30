---
name: godot-scalable-vector-shapes
description: "Draw Godot pixel art with vector shape tools: ScalableVectorShape2D nodes rendered through a Subviewport with pixel snap so pixels never rotate, plus a DynamicOutline2D node using Geometry2D.merge_polygons for clean merged outlines. Trigger when an artist can't draw pixels but needs rotation-stable pixel art."
---

# Scalable Vector Shapes 2D: Vector-Drawn Pixel Art in Godot

## Purpose

This skill produces pixel art without drawing pixels: build the
character from vector shape tools (ScalableVectorShape2D nodes), render
through a Subviewport with pixel snap so pixels stay aligned through
rotation, and add outlines with a custom DynamicOutline2D node that
merges polygons before outlining. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: vector input, pixel-art output — let
the renderer, not the hand, enforce the grid.

## Source

r/godot, ScalableVectorShapes (post text + author's own comments,
2026-10-30):

- https://www.reddit.com/r/godot/comments/1xiyqcl/so_i_cant_draw_but_at_least_the_pixels_don

Evidence note: post text and 16 comments; the DynamicOutline2D node
source is not disclosed beyond Geometry2D.merge_polygons. The tool
itself (Scalable Vector Shapes 2D by renevanderark) is on the Godot
Asset Library.

## Tools used

**Scalable Vector Shapes 2D** (Godot Asset Library, by renevanderark).
Author-built **DynamicOutline2D** tool node: draws an outline around
multiple assigned shape nodes (author placed it behind the hat and the
forehead), uses **Geometry2D.merge_polygons** under the hood.
**Subviewport** for rendering. Godot **pixel snap**.

## Phase 1: Draw with shape tools, not pixels

**Do**
1. Build the character from **ScalableVectorShape2D** nodes — shape
   tools and a compositor, not hand-drawn pixels.
2. Render through a **Subviewport** with **pixel snap on**.
3. "No Shaders, No AI, just a Subviewport and Scalable Vector Shapes
   2D."

**Check**
- Rotate the character: do the pixels stay aligned? "I was just
  experimenting with using my vector editor to produce pixel art, but
  it's really just godot that renders this stuff so well aligned (as
  long as the pixel snap is on)."

**Why**
The pixels don't rotate because the renderer enforces the grid, not
the artist. Alignment is a render setting, not an art skill — which is
why the author's self-deprecation ("So I can't draw") is answered by
the top comment: "ur literally drawing just with shape tools and a
compositor this is a valid art discipline."

## Phase 2: Add a merged outline node

**Do**
1. Create a tool node, **DynamicOutline2D**, that draws an outline
   around multiple assigned shape nodes.
2. Assign the shapes that need outlining; place the node behind them
   (author: behind the hat and the forehead).
3. Merge the shapes with **Geometry2D.merge_polygons** before drawing
   the outline.

**Check**
- Where shapes overlap (hat meets forehead), is the outline continuous
  instead of doubled? If doubled, the merge step is missing or the
  node ordering is wrong.

**Why**
Outlines drawn per-shape would double up at overlaps; merging the
polygons first gives one clean outline around the union.

## The human method, distilled

1. **Let the engine do the discipline.** Pixel snap alignment is a
   renderer setting, not an art skill.
2. **Build the missing tool instead of faking it.** The author wrote
   DynamicOutline2D rather than hand-drawing outlines.
3. **A new process is a valid discipline.** Different people solving
   common problems in surprising ways is the point (top comment:
   "The world is more interesting when different people approach
   solving common problems in surprising and unexpected ways").

## Failure modes

- **Rotating/misaligned pixels:** pixel snap off. Fix: enable it —
  it's the load-bearing setting.
- **Doubled outlines at overlaps:** shapes outlined before merging.
  Fix: Geometry2D.merge_polygons first, then outline the union.
- **Outline on the wrong layer:** DynamicOutline2D must sit behind the
  shapes it outlines.

**Depth status:** PARTIAL (post text + author's comments; node source
not disclosed; no parameters beyond merge_polygons and pixel snap).
