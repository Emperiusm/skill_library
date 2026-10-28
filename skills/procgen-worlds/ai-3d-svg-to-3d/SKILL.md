---
name: ai-3d-svg-to-3d
description: "Turn vector art into usable 3D: clean closed paths, extrude, bevel, material, light, and export, with the failure modes that break vector input. Trigger when converting logos, icons, or vector illustrations into 3D models."
---

# SVG to 3D: Vector Art to Usable 3D

## Purpose

This skill is the only vector-input workflow in the CustomUse set: it
converts clean 2D paths into 3D through extrusion, with failure modes
that exist nowhere else in the library. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The core method is: clean the paths first,
extrude second, bevel and finish third.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/svg-to-3d-model-workflow

## Tools used

Tools used: vector tools for path cleanup; DCC tools (Blender and
similar) for extrusion, beveling, materials, lighting, and export.

## Phase 1: Clean the paths before extruding anything

**Do**
1. Confirm every path is closed. Open paths cannot extrude into a
   solid.
2. Convert live text to outlines: live fonts do not survive the
   vector-to-3D transition.
3. Remove hairlines at or below about 0.5 px: they extrude into
   geometry too thin to render or print.
4. Resolve self-intersections and overlapping paths before extrusion.

**Check**
- Zero open paths, zero live fonts, zero sub-0.5 px hairlines?
- Does the path set preview as clean closed shapes?

**Why**
Extrusion amplifies path defects: an open path becomes a missing wall,
a live font becomes a missing glyph, a hairline becomes a sliver. Path
cleanup is cheap; post-extrusion repair is not.

## Phase 2: Extrude and bevel

**Do**
1. Extrude to a depth of roughly 10 to 25 percent of the shape's
   width. Shallower reads as flat; deeper reads as a block.
2. Bevel the edges to catch light: a hard extruded edge reads as
   paper-cut, not as an object.
3. Check bevels for self-intersection, especially on tight corners
   and small counters (the holes in letters).

**Check**
- Does the depth read as an object at the intended viewing distance?
- Are bevels clean on tight corners, or do they self-intersect?

**Why**
The 10 to 25 percent rule is the difference between a logo with
presence and a logo that looks like a thick sticker. Bevels are what
make extruded geometry catch light like a real object.

## Phase 3: Material, light, and export

**Do**
1. Assign materials per region: face, side wall, and bevel can carry
   different finishes.
2. Light the asset to prove the extrusion reads in three dimensions,
   not just as a flat shape with an edge.
3. Export in the destination's format (GLB for web and real-time,
   FBX for engine handoff, STL only if the destination is print) and
   verify the import.

**Check**
- Do face, wall, and bevel read as distinct surfaces?
- Does the exported file import at the right scale with materials
  intact?

**Why**
A vector conversion that skips material and lighting proof is a flat
shape with a thickness parameter, not a 3D asset. The import proof
closes the workflow the same way it closes every other skill in this
set.

## The human method, distilled

1. Closed paths, outlined fonts, no hairlines. Cleanup first.
2. Extrude 10 to 25 percent of the shape's width.
3. Bevel to catch light; check tight corners for self-intersection.
4. Material per region, light to prove depth, verify the import.

## Depth status

FULL (article text).
