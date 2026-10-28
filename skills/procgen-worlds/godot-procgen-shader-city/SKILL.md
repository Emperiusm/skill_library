---
name: godot-procgen-shader-city
description: "Generate a low-poly Godot city of plain SurfaceTool boxes (~700 buildings a lap) and get all its life from one window shader: 3.6 m floors, whole floors lit/dark like offices, far windows fading to glow, no window textures. Trigger when a procedural city needs to read at distance without texture memory or vert-heavy detail."
---

# Godot Procedural Shader-Window City

## Purpose

This skill reconstructs the low-poly city workflow, step by step, so another agent can build a procedural city the same way. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: generate plain boxes at load time, then let one shader do all the visual work that textures would normally do.

## Source

- Post: "Has anyone else tried building a procedural generated low poly city in Godot?" by CrashBamBoomClick — https://www.reddit.com/r/godot/comments/1xh8vg4/ (score 32, 7 comments)
- Context: a test track for an anti-gravity racer; the track pipe runs through the city.
- Evidence: full post text + comment exchange, 2026-10-28 scout run. No shader code or vert counts are published; the shader cannot be reimplemented from this skill alone.

## Tools used

Godot 4.7 with C#, SurfaceTool (building boxes), one custom window shader (no window textures), native Mac and Windows builds.

## Phase 1: Generate the city on a grid at track load

**Do**
1. Lay the city on a grid of 56 m blocks, 1 to 4 buildings per block, with random heights, colours, and window styles.
2. Generate in C# when the track loads: around 700 buildings a lap.
3. When the pipe hits a tower, split the tower around a 21.5 m hole; the top part floats, with a hexagon ring at every tunnel.

**Check**
- Building count is per lap (~700), not per scene; the city is generated, not placed by hand.

**Why**
Generation at load keeps the track data tiny (a seed and rules, not 700 placed buildings) and makes every lap's city a function of the grid rules.

## Phase 2: Build everything from boxes, chopped for culling

**Do**
1. Make every building from boxes with SurfaceTool.
2. Chop the city into 256 m tiles so culling works.

**Check**
- If distant tiles still cost full draw time, the 256 m chop is not doing its job; culling is the point of the chop, not the boxes.

**Why**
Plain boxes are cheap to generate and cheap to draw; the performance work is spatial (tiles for culling), not geometric detail.

## Phase 3: Replace window textures with one shader

**Do**
1. Use no window textures at all. One shader: 3.6 m floors, whole floors light up or go dark like real offices.
2. Let far windows fade into a soft glow "so you don't get that stripy mess" (author's words).
3. Take the commenter's interior-mapping tip seriously: Roucan suggested interior mapping for window detail ("faking the stuff on the other side of windows"), and the author replied the windows are already "one shader with a cell per window, so faking a room behind each one should drop right in", and that the same trick might fix wall ledges.

**Check**
- Near: individual floors read as lit or dark offices. Far: windows dissolve into glow instead of aliasing into stripes. If far windows still stripe, the fade distance is wrong.

**Why**
A shader window is resolution-independent and costs no texture memory; a texture atlas at city scale either blurs or stripes. The shader also makes the lit/dark office pattern a rule (whole floors), not a painted texture.

## Open questions (not answered in the thread)

1. Verts: "how do you add detail (roofs, ledges, setbacks) without the vert count blowing up?" No answer in the retrieved comments beyond the interior-mapping suggestion.
2. Textures: "has anyone compared that to a texture atlas for a big city? which looked better and ran faster?" Unanswered in the retrieved comments. Do not present either as settled.

## The human method, distilled

1. Generate plain, then shade smart: put the visual budget in one shader, not in geometry or textures.
2. Make far-field behavior a first-class rule (fade to glow), not an afterthought, because cities are mostly seen from far away.
3. Ask the two questions that decide the next iteration (detail without verts, shader versus atlas) instead of guessing.

## Depth status

PARTIAL — full post text with grid, tile, floor, and hole numbers, plus the interior-mapping comment exchange; no shader code, no vert counts, and the author's two questions are open.
