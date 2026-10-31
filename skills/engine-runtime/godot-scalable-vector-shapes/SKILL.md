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

## AAA studio practice

Vector input with the renderer enforcing pixel discipline is a shipped
production pattern, twice over: once for pixel art (Dead Cells) and
once for 2D animation at AAA scale (UbiArt). And production has a
known-unsolved failure mode that directly informs the skill's
pixel-snap gate.

**Motion Twin / Dead Cells (2018): 3D pipeline for 2D pixel art.**
Artist Thomas Vasseur's documented pipeline: hand-draw a 2D pixel-art
model sheet first, then build the character and its skeleton in 3D
(3DS Max, exported as FBX) — deliberately crude, because the
character is only ~50 pixels tall in-game, so high-detail 3D work is
cost-inefficient. A custom homebrew renderer converts the 3D mesh to
pixel art by rendering it at very small size **with antialiasing
disabled**, plus cell shading. Renderer-level pixel discipline, not
artist-level: the exact principle of the skill's Subviewport +
pixel-snap approach. Measured payoff: no per-frame redraw, one
animation reusable across models, automatic interpolation frames
(30fps), fast retakes for gameplay tuning, all done by one artist.
(Source: https://www.gamedeveloper.com/production/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-i-dead-cells-i- —
Game Developer deep dive by Vasseur.)

**Ubisoft Montpellier / UbiArt Framework (Rayman Origins 2011, Rayman
Legends, Child of Light, Valiant Hearts): engine-driven 2D.**
The proprietary UbiArt engine takes any scanned, photographed, or
digitized 2D artwork, **separates the imagery into individual pieces,
applies a skeleton and bones as pivot points**, and the animator poses
the model while the system deforms the image automatically —
artist-drawn input, engine-driven animation, exactly the skill's
vector-input/enforced-output principle. Design intent per Michel
Ancel: "let the artists work easily, without thinking about polygons
or textures or sizes, so they could just concentrate on the art" —
the engine owns the technical pipeline discipline. Hardened
acceptance bar: full 1080p HD at a locked **60fps from day one**
(2011), vector-based so assets stay crisp across resolutions.
(Source: https://www.cgw.com/Publications/CGW/2012/Volume-35-Issue-5-Aug-Sept-2012-/Fine-Tooning.aspx —
Computer Graphics World, 2012. Corroborating: Ubisoft Montpellier's
Chris McEntee on the UbiArt tools for Rayman Legends, GDC 2014:
https://www.gamedeveloper.com/design/video-the-tools-used-to-design-i-rayman-legends-i-)

**The known-hard problem:** Dead Cells could not solve flickering
pixels — shimmer when 3D-rendered low-res pixels move or rotate. That
limitation is production-scale evidence that stable rotation is the
skill's load-bearing feature: the skill's Subviewport + pixel-snap
gate exists precisely because even Motion Twin never fully solved
rotation shimmer.

## Agent automation

**Do**
1. **Flicker gate** (agent design, motivated by the Dead Cells
   limitation): rotate and translate the character through one full
   animation cycle while capturing frames, then run a consecutive-
   frame pixel diff over the pixels that should be static. Any
   shimmering pixel with pixel snap on is a failure — the automated
   version of the skill's Phase 1 "do the pixels stay aligned?"
   check.
2. **Renderer-discipline audit** (agent design): a scripted
   configuration assertion that the load-bearing settings are all
   present — Subviewport in the tree, pixel snap enabled, no shader
   overriding the pixel grid. The skill's principle ("alignment is a
   render setting") becomes a config gate that fails the build if a
   setting is missing, rather than a manual reminder.
3. **Merge-first assertion** (agent design): assert in the scene tree
   that DynamicOutline2D's `Geometry2D.merge_polygons` call precedes
   the outline draw and that the outline node sits behind the shapes
   it outlines. The skill's "doubled outlines at overlaps" failure
   mode becomes an ordering check the agent runs before every export.

**Check**
- The flicker gate's acceptance baseline is zero shimmering static
  pixels over the fixture cycle; the fixture animation is committed
  with the project.
- The config audit and merge assertion exit non-zero on failure and
  run headless — no editor open required.

**Why**
Dead Cells and UbiArt both prove the same thing: pixel discipline is
cheapest when the renderer enforces it, and rotation shimmer is the
failure even AAA pipelines never fully solved. These gates make the
skill's two load-bearing settings (pixel snap; merge-before-outline)
machine-checkable instead of remembered.

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
