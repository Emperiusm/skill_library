---
name: ai-3d-retopology-uv
description: "Repair AI-generated meshes for production: when to retopologize by destination, wireframe checks, and a UV inspection and repair routine with checker textures, overlap overlays, and a second lightmap UV set. Trigger when a generated mesh needs clean topology or usable UVs."
---

# Retopology and UV Repair for AI Meshes

## Purpose

This skill turns generator output (dense triangulated soup with painted
textures) into a mesh with clean topology and usable UVs, in that
order: retopology first, unwrap second, PBR texturing third. Every
phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: decide
by destination, verify with wireframes and checker textures, and never
texture a mesh whose UVs you have not inspected.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/what-is-retopology
- https://customuse.com/learn/uv-unwrapping-ai-3d-models

Evidence note: the sources' substantive sections were read. Retopology
and UV tools named below are the sources' named tools, not an
exhaustive survey.

## Tools used

Tools used: retopology tools (Quad Remesh, QuadRemesher) and UV tools
(xatlas packers, RizomUV), inside DCC tools (Blender, Maya). The chain
is tool-agnostic: any retopology and UV tool that supports the checks
below qualifies.

## Phase 1: Decide whether to retopologize, by destination

**Do**
1. Classify the destination before deciding: a deforming asset
   (character, creature, flexible object) needs edge flow for
   deformation; a static prop needs the simplest-possible topology; a
   print asset needs watertight geometry, not topology at all.
2. Retopologize when the asset deforms, ships in a game, or must be
   edited. Skip it for throwaway blockouts and concept previews.
3. When the mesh is fused, locked in a mid-action pose, or riddled
   with intersections, prefer regenerating from better reference over
   repairing: retopology cannot rescue a base with no usable form.

**Check**
- Can you name the destination and the topology it demands?
- Would a reviewer accept this mesh for that destination as-is? If
  not, is repair actually cheaper than regeneration?

**Why**
Retopology is expensive skilled work. Spending it on a blockout wastes
it; skipping it on a deforming hero guarantees deformation failure
later, where it costs the most to fix.

## Phase 2: Retopologize and check the wireframe

**Do**
1. Auto-retopologize to a quad-dominant cage at the approved budget,
   keeping the high-poly aside for baking.
2. Add manual edge loops where deformation demands them (joints on
   characters, hinges on mechanical parts).
3. Read the wireframe: clean edge flow where the mesh bends, even
   density elsewhere, no pinches or star poles in deformation zones.

**Check**
- Does the wireframe show loops following the forms that move?
- Are triangle density and edge flow even, without the generator's
  appearance-first clumping?

**Why**
Topology is the mesh's skeleton: it decides what can bend, what can be
edited, and what can be baked cleanly. A wireframe check catches what
a shaded preview hides.

## Phase 3: Unwrap with inspectable UVs

**Do**
1. Unwrap after retopology, never before: the unwrap belongs to the
   cage that ships.
2. Place seams where they hide (down a back edge, under an overhang),
   not where the camera lives.
3. Aim for even texel density across materials, so no part of the
   asset goes soft while another stays sharp.

**Check**
- Apply a checker texture: are the squares even across the mesh, or do
  they stretch and squash?
- Run an overlap overlay: are any islands stacked on each other?

**Why**
The chain is retopology feeds unwrap feeds PBR texturing. A bad unwrap
poisons every map baked after it, and the failure shows up as
stretching that no texture edit can fix.

## Phase 4: Repair overlaps and add the lightmap set

**Do**
1. Separate overlapping islands and repack, preserving texel density.
2. Where the engine needs baked lighting, add a second UV set for
   lightmaps with no overlaps at all.
3. Re-run the checker texture and the overlap overlay after every
   repair pass.

**Check**
- Zero overlaps in the lightmap set, and no stretching in the primary
  set?
- Do the maps bake cleanly from the high-poly onto this UV layout?

**Why**
Overlaps in a lightmap set are not a cosmetic issue: they bake one
surface's light onto another. The second set exists precisely because
the texturing layout and the lighting layout have different rules.

## The human method, distilled

1. Destination decides retopology. Never retopo on autopilot.
2. Wireframe before shading. The shaded preview lies about topology.
3. Retopo, then unwrap, then texture. Order is the pipeline.
4. Checker texture and overlap overlay are not optional checks; they
   are the inspection.
5. Regenerate when the base is unrecoverable. Repair has a price
   ceiling, and fused or locked-pose meshes exceed it.

## Depth status

FULL (article text).
