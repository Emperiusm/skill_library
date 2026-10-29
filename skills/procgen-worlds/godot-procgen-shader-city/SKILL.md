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

## AAA studio practice

- **Generate the city procedurally, then preserve hand-authored work across iterations.** Insomniac's GDC 2019 talk on procedurally crafting Manhattan for Marvel's Spider-Man describes Houdini-generated sets of assets for roads, buildings, cars, pedestrians, and props, with procedural systems designed to support iteration and dependencies, and later work adding three improvements: preserve hand-authored work if it still meets specifications, place encounter components with higher fidelity, and guide artists to the pieces needing attention. Applied here: the Godot city's grid rules are the procedural layer, and any hand-placed hero building or track feature (like the pipe hole) must survive a regeneration, not be overwritten by it.
  Source: https://www.gamedeveloper.com/design/swing-by-gdc-and-learn-about-the-making-of-i-marvel-s-spider-man-i-from-top-to-bottom
  Source: https://history.siggraph.org/learning/procedural-system-assisted-authoring-of-open-world-content-for-marvels-spider-man-by-santiago/
- **Fake interiors in the shader, and let that be the next step for this skill's window cells.** Marvel's Spider-Man renders interiors behind many building windows with a shader trick: the interior geometry is not there, it is generated by the shader, perspectively correct with real depth, adding liveliness to the city without the performance cost of real rooms. That is exactly the upgrade the thread's commenter proposed (interior mapping for window detail) and the author accepted ("one shader with a cell per window, so faking a room behind each one should drop right in"). The AAA precedent says the cell-per-window shader is the right foundation, and interior mapping is the next layer, not a different technique.
  Source: https://www.gamedeveloper.com/programming/interior-mapping-rendering-real-rooms-without-geometry
- **Let far windows dissolve into emissive glow, and light the night city from them.** The Matrix Awakens city (7,000 buildings) is lit in night mode nearly entirely by emissive building windows, with no placed light sources for the tens of thousands of street lights and headlights, using Lumen global illumination. That is the AAA-scale version of this skill's far-field rule: far windows fading to a soft glow is not a cosmetic choice, it is how a city reads at night at scale.
  Source: https://toptech.news/epic-games-shows-off-unreal-engine-5-with-stunning-simulated-city-in-the-matrix-awakens-demo/

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Add a far-field acceptance render: render the same city view at near, mid, and far camera distances, and verify far windows average toward glow rather than striping; measure it as high-frequency energy in the far render falling below the near render's, not by eye alone.
2. Add a culling check: log tiles drawn versus tiles total per camera position, and verify the 256 m chop actually reduces draw work as the camera moves; a tile count that stays flat while the camera moves means culling is not wired.
3. Add a regeneration-preservation check: hand-place one marker building (or the pipe-hole tower), regenerate the city from the same seed and rules, and verify the marker survives unchanged; a regeneration that overwrites hand work fails, per the Insomniac rule above.
4. Prototype the interior-mapping upgrade as a shader-only step behind the existing cell-per-window structure, gated by the same near/mid/far renders: near windows gain parallax depth, far windows keep their glow fade, and the lit/dark whole-floor rule stays intact.

**Check**
- The city passes only when far windows glow without striping, tile draw counts move with the camera, and regeneration preserves hand-placed work; the two open questions from the thread (detail without vert blowup, shader versus atlas) stay open until measured, and are not answered by assertion.
- The interior-mapping prototype is accepted only if it passes all three existing checks plus a near-window depth check; if it breaks the far glow, it is rejected.

**Why**
A procedural city is mostly seen from far away, and mostly judged by whether it survives regeneration. The far-field render, the culling log, and the preservation check are the three measurements that prove the shader-city idea at city scale, and they turn the thread's two open questions into the next measured experiments instead of guesses.

## The human method, distilled

1. Generate plain, then shade smart: put the visual budget in one shader, not in geometry or textures.
2. Make far-field behavior a first-class rule (fade to glow), not an afterthought, because cities are mostly seen from far away.
3. Ask the two questions that decide the next iteration (detail without verts, shader versus atlas) instead of guessing.

## Depth status

PARTIAL — full post text with grid, tile, floor, and hole numbers, plus the interior-mapping comment exchange; no shader code, no vert counts, and the author's two questions are open.
