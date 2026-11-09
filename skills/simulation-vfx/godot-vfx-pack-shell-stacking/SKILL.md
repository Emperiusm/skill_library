---
name: godot-vfx-pack-shell-stacking
description: "Stack multiple Godot VFX shell effects on one character without z-fighting: give each shell (ice crust, fire, lightning, curse) its own offset distance from the surface, name every addon with its pack prefix in its own folder, and prove all 13 packs in one continuous mannequin walkthrough. Trigger when layering VFX shells on a character or shipping a multi-pack VFX bundle."
---

# Stacking Godot VFX Packs: Shell Offsets + One-Take Proof

## Purpose

This skill reconstructs the exact workflow from gennai777's 13-pack Godot VFX
walkthrough, step by step, so another agent can follow the same process.
Every phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The workflow's core method is: one
mannequin, one take, every addon stacked — and the stacking only works
because each shell sits at its own distance.

## Source

Creator: gennai777.

Source: https://www.reddit.com/r/godot/comments/1xqvpc1/this_poor_guy_took_every_vfx_pack_i_made/
(r/godot post 1xqvpc1, score 72, 10 comments; comment fetch failed this run:
Arctic Shift HTTP 422, old-reddit JSON blocked in the sandbox) |
2026-11-08 scout run. Bundle (13 packs, $29.99):
https://gennai.itch.io/godot-4-vfx-complete-collection. Evidence: full
author post text; no transcript exists for the native Reddit clip.

## Tools used

Tools used: **Godot 4** VFX addons (author's own 13-pack bundle). Packs
named: frost, fire, lightning, sword, curse, blood and wounds, death and
dissolve, sci-fi shields (plus 5 unnamed from the original 10-pack bundle).

## Phase 1: Name and file every addon the same way

**Do**
1. Start every class with its pack's prefix.
2. Give every addon its own folder.

**Check**
- 13 packs coexist in one project without name collisions.

**Why**
- "Names were easy." Prefix + own folder is the whole convention, and it is
  what makes the single-project walkthrough possible. (Author's words.)

## Phase 2: Stack the shells at different distances

**Do**
1. A few packs draw on a thin copy of the mesh pushed out a few millimetres,
   like the ice crust and the fire. These are shell effects: a duplicate mesh
   offset from the surface.
2. Give each shell its own distance from the surface.

**Check**
- Before the fix: "If two sit at the same distance on one character they
  z-fight."
- After: "I gave each one its own distance from the surface, and now they
  stack fine!"

**Why**
- Two shells at the same offset fight over the same depth values; distinct
  offsets give the depth buffer an unambiguous order. (Author's stated
  failure mode and fix; the depth-buffer mechanism is labeled inference.)

## Phase 3: Walk one mannequin through everything, one take

**Do**
1. Put every addon in one project and walk one mannequin through them:
   frost, fire, lightning, a sword, a curse, and he ends up as ash. One take.

**Check**
- All 13 packs render on the same character in one continuous shot; the
  author admits "I went in a bit scared of the single project part lol."

**Why**
- One take on one character is the proof the stacking works: any z-fighting
  or naming collision would show immediately. (Inference, labeled.)

## AAA studio practice

**Shell texturing is the production name for this technique.** Stacking
offset copies of a mesh along its normals to fake volume is shell
texturing, formalized in Lengyel, Praun, Finkelstein and Hoppe's 2001
paper "Real-time fur over arbitrary surfaces" and shipped in games ever
since: fur in Viva Piñata, Dark Souls (Sif) and Genshin Impact, fur in
Biomutant, and the reentry-heating effect in Kerbal Space Program, which
renders the ship multiple times as distorted shell layers. Production
practice: each shell is extruded along the vertex normals, strand
thickness tapers with height, and shell spacing is kept minimal. Known
failure modes at scale: visible layer gaps at grazing camera angles,
severe overdraw with high shell counts, and unexpected interactions
between transparent shells and other transparent objects.
- Source: https://hhoppe.com/proj/fur/
- Source: https://daily.dev/posts/how-do-games-render-fur--sozwggcf4
- Source: https://www.proceduralpixels.com/blog/shell-texturing-vs-raymarching

**Arc System Works, Guilty Gear Xrd (GDC 2015): the inverted-hull
outline is a shell with discipline.** Technical artist Junya C. Motomura
detailed how Xrd builds its outlines from an inverted copy of the mesh
expanded along the normals, rendered darker: the hull's outline width is
varied per-vertex using vertex colors, and the hull uses separate normals
from the ones used for shading, so the outline stays clean while the
shading stays flat. The limit Motomura states explicitly: inverted hull
does not work for inner lines on a surface, which need a different
technique. The lesson for VFX shells: a shell is not just an offset
distance, it is an offset plus its own normal set and its own width
control, and different shell jobs (outline vs inner detail) need
different mechanisms.
- Source: https://www.polygon.com/2015/5/26/8663003/guilty-gear-xrd-cel-shading-making-of
- Source: https://videohighlight.com/v/yhGjCzxJV3E

**Unreal Engine mesh decals: depth bias belongs in clip space, and it
fails at distance first.** Epic's mesh-decal shader pushes the decal
geometry toward the camera by a fixed clip-space amount
(`Output.Position.z += 0.0001f * Output.Position.w`) specifically to
avoid z-fighting, and Epic staff on the forums note the bias should be
exposed per mesh or material rather than hard-coded. The same thread
shows the failure pattern: a decal that looks correct up close renders
in front of the wrong surface when the camera pulls away, because depth
precision is thinnest far from the camera. The lesson for shell stacks:
a fixed world-space offset ("a few millimetres") behaves differently at
different camera distances, so a stack verified only at close range is
not verified.
- Source: https://forums.unrealengine.com/t/about-mesh-decal-issues-in-4-13/372948

**Godot 4.3 reverse Z changes the baseline.** Godot implemented the
reverse-Z depth buffer in 4.3, which the engine team describes as "a
massive improvement to depth buffer precision at no performance or memory
cost" that "significantly reduces the chances of running into Z-fighting
and other depth buffer precision artifacts." The same article warns that
custom shaders writing `POSITION` or `DEPTH` directly in clip space
break under reverse Z and must be rewritten (or, preferably, transformed
through `PROJECTION_MATRIX`). The lesson: a shell stack that z-fights on
Godot 4.2 may be clean on 4.3+ with no offset changes, so record the
engine version with the offsets, and do not hand-tune offsets to fight a
precision problem the engine now solves.
- Source: https://godotengine.org/article/introducing-reverse-z/

**Transparent layering discipline: opaque first, translucent back to
front, additive needs no sort.** The standard ordering rule (OpenGL
advanced notes): draw opaque objects first with depth testing and depth
writes on, then translucent objects back to front with blending on,
depth testing on, and depth writes off, so translucent layers never
occlude each other. The corollary, from the Khronos particle-rendering
discussion: additive-blended effects (sparks, fire glow) are commutative
and do not need depth sorting at all, while alpha-blended shells do.
Applied to this skill (inference, labeled): put opaque shells such as
the ice crust in the opaque pass, alpha-blended shells such as fire in
the transparent pass with depth writes off, and make the fire/lightning
glow layers additive where the look allows, which removes their sorting
from the problem entirely.
- Source: https://www.opengl.org/archives/resources/code/samples/advanced/advanced97/notes/node112.html
- Source: https://community.khronos.org/t/proper-rendering-for-particles/44223

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Write a per-shell offset manifest (`shell_offsets.json`) listing every
   shell: pack name, offset from the surface, render pass (opaque /
   transparent), and blend mode (alpha / additive). A script asserts no
   two shells share the same offset before the walkthrough runs.
   (Inference: no manifest exists in the source; this formalizes the
   author's "each one its own distance" fix.)
2. Run a scripted z-fight sweep: render the stacked mannequin from the
   same camera orbit at three distances (close, mid, far) and save one
   frame per distance per shell combination. (Inference: the distances
   are a test design, not a sourced value; the research only establishes
   that z-fighting is worst at distance.)
3. Record the Godot version in the manifest. If the project is below
   4.3, flag that reverse Z is unavailable and offsets need tighter
   verification; if a shell shader writes `POSITION` or `DEPTH` in clip
   space, flag it for the reverse-Z rewrite described in the Godot
   article.
4. Assign blend modes by the layering rule before the one-take proof:
   opaque shells opaque, alpha-blended shells transparent with depth
   writes off, additive for fire/lightning glow where the look allows.
   (Inference: the mapping of the rule to these packs is the agent's,
   from the OpenGL notes above.)
5. Record the one-take walkthrough headlessly and keep the frames as a
   regression baseline; re-render on any offset change and diff against
   the baseline. (Inference: headless capture is a proposed automation,
   not part of the author's workflow.)

**Check**
- The manifest assertion passes: every shell has a unique offset, a
  pass, and a blend mode.
- No flicker or shimmer appears in any sweep frame at any of the three
  distances; a frame-to-frame pixel diff at a fixed camera shows no
  flickering pixels on any shell.
- The one-take regression diff is clean except for intended changes.

**Why**
- The author's fix ("each one its own distance") only holds if the
  distances are written down and checked mechanically; a manifest turns
  a remembered fix into an enforced invariant.
- Depth precision is non-linear, so a stack that is clean up close can
  still fight at distance; the sweep tests the failure the Unreal decal
  thread documents instead of hoping the one take catches it.
- Reverse Z means the engine version is part of the technique: the same
  offsets behave differently across Godot versions, so the version
  belongs in the manifest, not in someone's head.

## The human method, distilled

1. **Prefix + folder per addon.** Naming discipline is what lets 13 packs
   share a project.
2. **Shells stack by distance, not by luck.** Each shell gets its own offset
   from the surface; equal offsets z-fight.
3. **Prove it in one take.** A single mannequin through every effect is the
   integration test.

## Failure modes

- **Z-fighting between shells at equal offsets.** The failure mode that
  motivated the technique: two shells at the same distance from the surface
  fight. Fix: per-shell offset distances (Phase 2).
- **No shader code for the shells was disclosed.** The offsets are "a few
  millimetres" by the author's description, not measured values; tune the
  spacing per mesh scale and verify visually in one take.

**Depth status:** PARTIAL (full author post text with exact naming
convention, shell technique, failure mode, and price; no shader code for the
shells; comment fetch failed on both fallbacks, so commenter detail is
missing).
