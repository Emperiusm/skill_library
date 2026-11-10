---
name: blender-floaters-hard-surface-detail
description: "Fake hard-surface detail in Blender with floaters: model the base form clean, place separate small meshes (cylinders, vents, rings) on the surface instead of cutting booleans, sell the seam with a bevel, and unify with consistent materials. Trigger when a mech, prop, or hard-surface model needs dense detail without topology debt."
---

# Floaters: The Hard-Surface Detail Cheat Code in Blender

## Purpose

This skill reconstructs the workflow from Josh's "Floaters - The
BIGGEST 3D Modeling Cheat Code" (Blender Bros, YouTube, 2026-11-02),
step by step, so another agent can follow the same process. Every phase
has three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The workflow's core method is: fake
the detail with separate meshes sitting on the surface instead of
cutting it into the mesh.

## Source

Creator: Josh - Blender Bros.

Source: https://www.youtube.com/watch?v=2qdCIDZbF8s | Uploaded
2026-11-02 | 449 s (7:29) | 87,239 views | 2026-11-09 scout run.
Description links: Mech Head Design in Plasticity
(https://www.blenderbros.com/mech-head-design-in-plasticity/),
MaterialWorks Texturing Plugin.
Evidence: 12 frames extracted from a downloaded copy of the video
(download 2 of 2 in this run's pre-approved allowance; no approval gate
fired), plus the video description. No captions were retrievable and no
transcript lines are quoted.

## Tools used

Tools used: **Blender**; **Plasticity** (for the mech head design
course the video ties into, per the description).

## Phase 1: Model the base form clean

**Do**
1. Model the base form (here, a mech head) as a clean, simple shell
   with good topology. The frame shows a smooth dark head with a few
   large forms and a wireframe overlay showing even quads.
2. Do not cut vents, panels, or bolts into the base mesh.

**Check**
- The base reads as the finished silhouette with no surface detail yet;
  if the silhouette is wrong, no floater will fix it.

**Why**
The base mesh carries the shape; everything else is decoration.
Cutting detail into it would destroy the clean topology and multiply
the modeling time.

## Phase 2: Model floaters as separate pieces

**Do**
1. Model each detail as its own small mesh: cylinders, vents, rings,
   greebles. The frames show cylindrical floaters and ring segments as
   separate objects in the outliner (Scene Collection, Cylinder
   entries).
2. Keep floaters simple: a cylinder with a beveled edge reads as a vent
   housing; a ring segment reads as a panel line.

**Check**
- A floater in edit mode (frame 6) shows its base edge loop selected
  along the surface it will sit on; the loop must follow the base
  curvature.

**Why**
A floater is a cheat in the honest sense: it looks like modeled detail
from every normal viewing angle, but it cost a cylinder and a bevel
instead of a boolean and a topology repair.

## Phase 3: Place floaters on the surface, do not boolean them in

**Do**
1. Place each floater on the base surface so it intersects slightly; the
   intersection is hidden by the bevel and the viewing angle.
2. A frame shows a floater hovering above the surface, selected and
   outlined in orange, before placement: position first, then drop it
   onto the surface.
3. The right panel shows a Bevel modifier (Angle limit, Segments) on
   the floater: the bevel catches the light and sells the intersection.

**Check**
- Orbit the model: a floater that reads from the front but floats
  visibly from the side is placed wrong. The frame showing the finished
  head from a three-quarter view is the check; floaters sit flush and
  the seams read as panel lines.
- The finished wheel/hub frame shows hex bolts and ring segments placed
  as floaters around a central disc: the detail is dense, but every
  piece is a separate simple mesh.

**Why**
Booleans create topology debt (n-gons, shading breaks, cleanup).
Floaters create no debt: each piece is independent, movable, and
deletable. The technique trades a small amount of geometric honesty
for a large amount of speed, and the trade is invisible in the render.

## Phase 4: Material the assembly as one

**Do**
1. Apply materials after placement; the frames show a material panel
   (metalness/roughness) and a material preview on the finished head
   and hub.
2. Keep the floater materials consistent with the base: same metalness
   and roughness range, so the pieces read as one object.

**Check**
- The material preview thumbnail must match the viewport: if a floater
  reads as a different material, it stops being detail and becomes a
  stuck-on piece.

**Why**
Materials unify the assembly. The eye forgives separate geometry when
the surface response is consistent.

## AAA studio practice

Floaters are not a YouTube shortcut; they are standard high-poly
practice in AAA asset production, where the high poly exists only to
be baked down. The studio version of this skill adds two things the
video does not: the normal-matching rule, and the bake contract.

- **Elite3D / Call of Duty: Infinite Warfare: floaters as the
  high-poly default.** Prop artist Boy Sichterman (Elite3D, first
  title Call of Duty: Infinite Warfare) on his hard-surface method:
  "Because the highpoly models I create will be baked down later on
  a low poly, I can make heavy use of so called 'floaters'. Floaters
  are small details that float on top of the base geometry, with the
  edge faces having the same face normal as the underlying geometry.
  When baked down, no seam will be visible, and it will seem as if
  they blend with the surface. Floaters speed up the highpoly process
  a lot since you don't have to fit a trazillion edgeloops in the base
  model." The normal-matching clause is the part the video leaves
  implicit: a floater whose edge faces do not share the base normal
  will show a seam in the bake.
  (https://80.lv/articles/boy-sichterman-getting-hard-surface-right)
- **Intersecting vs separate floaters, and the bake contract.** The
  floater-baking guide distinguishes two kinds: intersecting floaters
  for extruded details (the important information is on the element
  peaks), and separate floaters for concavities, holes, and scratches
  that must not touch the main mesh, or the bake fails on the deepest
  part. Two contract rules follow: floaters must be attached to the
  same mesh/object as the base when using "Bake by mesh name" in
  Substance Painter or Marmoset, or the baker will project them onto
  the wrong surface; and the bake distance is a measured setting, not
  a default (the guide's working example uses 0.03 Max Frontal
  Distance in Substance Painter, with Max Rear Distance left alone,
  because holes made of floaters are only calculated by the frontal
  cage).
  (https://artechu.com/blog/Epqo/understanding-high-poly-floaters-for-baking-details)
- **The AAA pipeline framing: floaters are a bake-prep step, not a
  modeling style.** The AAA 3D pipeline baking guide lists "create
  the floating geometry" as part of preparing the high poly: place
  cylinders or complex shapes on top of the model instead of embedding
  them; because floaters are not connected to the model, they can be
  baked onto normal maps without causing artifacts or issues with the
  geometry. The same guide's warning is the mirror image: floating
  geometry in the *low* poly is a defect that causes baking artifacts,
  so the floater discipline applies to the high poly only, and the low
  poly stays clean.
  (https://www.gdp.academy/article/complete-guide-to-the-3d-pipeline-4-baking)

### Agent-executable upgrades

1. **Floater inventory manifest.** Keep `floaters.json` next to the
   .blend: one entry per floater with name, type (intersecting for
   extrusions, separate for concavities), base mesh, and bake target.
   A floater with no type entry fails the gate; the type decides
   whether it may touch the base mesh.
2. **Normal-match check.** Before baking, run a Blender Python check
   over every floater: each edge face of the floater must share the
   underlying base face normal within a small tolerance (the
   Sichterman rule). Floaters that fail are listed by name with the
   offending face; fix the placement, do not raise the tolerance.
3. **Bake-distance gate.** Record the Max Frontal Distance (e.g.
   0.03) and the baker (Substance Painter, Marmoset) in the manifest.
   Run a test bake on one small patch of the model first and inspect
   the normal map for seams before baking the whole asset; a seam in
   the patch means the floater placement or the distance is wrong,
   not the bake.
4. **Bake-by-name check.** Verify by script that every floater and
   its base mesh share the mesh-name prefix the baker matches on
   (e.g. `mechhead_high` and `mechhead_high_floater_01`), so the
   "Bake by mesh name" step cannot project a floater onto a different
   low-poly piece.
5. **Three-angle acceptance render.** After placement, render the
   assembly from front, three-quarter, and side. A floater that reads
   from the front but floats visibly from the side fails and is
   re-placed; the side view is the check the video's finished-head
   frame performs by eye, made repeatable.

## The human method, distilled

1. **Silhouette first, detail second.** The base mesh carries the shape;
   floaters carry the detail.
2. **Never boolean what you can float.** A separate mesh costs a
   cylinder; a boolean costs topology repair.
3. **Bevel sells the seam.** The bevel modifier on each floater is what
   makes the intersection read as a designed edge.
4. **Materials unify.** Consistent metalness and roughness make separate
   pieces read as one object.

**Depth status:** PARTIAL (12 frames from a downloaded copy with
verified technique and visible modifier settings; no captions; no
spoken principles are quoted because none were retrieved; the
Plasticity course link in the description is the mech-head source, not
a step in the video).
