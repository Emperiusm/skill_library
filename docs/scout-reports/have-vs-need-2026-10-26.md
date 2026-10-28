# Video tooling scout: have-vs-need, 2026-10-26

Depth mode: **pre-approved** (max 2 media downloads). Depth-escalation usage:
**0 downloads attempted, 0 succeeded, 0 skipped.** No download was needed:
all six audited videos yielded full captions on the captions-first path,
so the allowance was not required and no approval gate was hit by any
download (none attempted).

Scan: **Reddit source down for this run.** The 2-day scan over 23 configured
subreddits returned 0 video posts. 17 subreddits returned HTTP 429 (Too Many
Requests) from Arctic Shift: unity, unrealengine, godot, threejs,
GraphicsProgramming, blender, photogrammetry, gameassets, aigamedev,
comfyui, vibecoding, proceduralgeneration, vfx, shaders, VoxelGameDev,
3Dmodeling, gamedev. The remaining subreddits (houdini, substance3d,
topology, technicalart, RealTimeVFX, Simulated) returned no video posts in
the window. Per the rate-limit hard-stop rule, the Reddit scan was NOT
retried, and no replacement Reddit work was scheduled. This run is
YouTube-only, and a Reddit gap for Oct 24-26 remains; the next scheduled
run should surface whether the 429s clear.

YouTube channel scan: first attempt failed on every channel with an SSL
certificate error (the sandbox egress proxy CA had rotated again since
the 2026-10-25 fix; the skills venv certifi bundle did not contain the
current CA). Fix applied per AGENTS.md: the current Hatch Sandbox Egress CA
(`/usr/local/share/ca-certificates/hatch-egress-ca.crt`) was appended to
the skills venv certifi bundle
(`~/workspace/skills/video-summarizer/.venv/lib/python3.12/site-packages/certifi/cacert.pem`;
pre-change backup at `/tmp/cacert-backup-2026-10-26.pem`, ephemeral).
After the fix the scan completed: 11 channels scanned, 11 videos found in
the 14-day window, 2 warnings, both NOT retried and no cookie workaround
attempted: Ducky3D video `gb8jdGh_LsE` and KaizenTutorials video
`SWs2iltL7rU`, both blocked by YouTube's "Sign in to confirm you're not
a bot" check during full extraction.

## Gap alerts

**No P1 gap alerts today.** Checked against `references/p1-gaps.md` by
keyword and by meaning. Four near-misses, stated plainly so they are not
mistaken for fills:

- Mesh-refinement stage with deviation metrics (aegis P1): the voxel-remesh
  repair (audit 1) and the five-tips mesh cleanup (audit 3) are the most
  mesh-refinement-adjacent evidence the scout has surfaced since the
  Planer-class gap was seeded, but neither reports a deviation metric,
  a flatten/sharpen pass with measured error, or UV preservation numbers.
  They are repair recipes, not a refinement stage. Recorded as evidence
  for the gap, not a fill. The gap stays open.
- Per-asset performance budgets (aegis P1): the five-tips polycount
  reduction (audit 3, tip 3) is a method for cutting geometry on
  real-time models, but it states no tri counts, no texel density, and
  no draw calls. A reduction method is not a budget. Not a fill.
- Rigging / skinning / animation-retarget (aegis P1): the voxel-remesh
  repair notes that space between limbs "will also make it easier to do
  the rigging and to do the texture baking," but that is one sentence
  about spacing, not a rigging, skinning, or retarget stage. Not a fill.
- Art bible / toon law (2d3d P1) and explore-mode lighting bible (2d3d
  NEED): the three-point lighting setup (audit 2) is a citable lighting
  recipe (area lights, rim-first order, fill power 5-10, Track To), and
  the inverted-hull outline is re-corroborated (audit 3, tip 2), but
  neither is a written bible with pillars, palette roles, silhouette
  rules, or a toon-ramp law. Evidence only. The gaps stay open.
- Import validation, mesh compression, AI-vendor acceptance spec,
  MCP-driven DCC loop, skyline fill, Godot import gate: no matches in
  today's tooling.

## Videos deeply analyzed

| # | Video | Creator | URL | Duration | Source |
|---|-------|---------|-----|----------|--------|
| 1 | "Fix Merged Geometry after Voxel remeshing" | Blender Secrets | https://www.youtube.com/watch?v=HOxVKNRnGig | 259 s | YouTube, uploaded 2026-10-17, 19,644 views. Depth: FULL (118 caption segments + description; no frames reviewed) |
| 2 | "How to Make a Three Point Lighting Setup in Blender" | Ryan King Art | https://www.youtube.com/watch?v=sN8hS2vLG4o | 807 s | YouTube, uploaded 2026-10-20, 8,234 views. Depth: FULL (439 caption segments; a clip from the author's Lighting Essentials for Beginners tutorial, not the full tutorial; no frames reviewed) |
| 3 | "5 Tips: Square to Round shapes, Inverted Hull, Reduce polycount, find double geometry, better bevels" | Blender Secrets | https://www.youtube.com/watch?v=hnHqboUoxxs | 736 s | YouTube, uploaded 2026-10-15, 11,620 views. Depth: FULL (221 caption segments; tip 2 repeats the Oct 25 inverted-hull audit, the other four tips are new; no frames reviewed) |
| 4 | "Why you get that 'weird' smearing effect when you shade smooth" | Josh - Blender Bros | https://www.youtube.com/watch?v=SrR8n854D0A | 526 s | YouTube, uploaded 2026-10-19, 18,197 views. Depth: FULL (211 caption segments; an explanation with a fix, not a build workflow; no frames reviewed) |
| 5 | "The Most ANNOYING Modeling Situation in Blender" | Josh - Blender Bros | https://www.youtube.com/watch?v=gQUYQJYs_R8 | 315 s | YouTube, uploaded 2026-10-14, 12,875 views. Depth: FULL (152 caption segments; no frames reviewed) |
| 6 | "Part 1: Creating a Realistic Hamburger (Blender Tutorial)" | Ryan King Art | https://www.youtube.com/watch?v=1inVxY0EYD8 | 1706 s | YouTube, uploaded 2026-10-21, 10,053 views. Depth: FULL (926 caption segments; Part 1 only: buns and seeds; parts 2-5 not audited; no frames reviewed) |

Scanned, not analyzed (YouTube candidates, 8-video cap not reached but
series/duplicate handling applied): the inverted-hull video itself
(`dybTdt9WXts`, already FULL-audited Oct 25 and skilled as
`materials-shaders/blender-inverted-hull-outline`; its reappearance in
audit 3 tip 2 is recorded as corroboration, not a new audit); Ryan King
Art hamburger Parts 2-5 (uploaded Oct 22-25: patty/cheese,
tomato/lettuce, pickles/onions, assembly/lighting/render/compositing;
Part 1 only was audited this run, the rest stay in the 14-day window
for the next run); the two bot-blocked videos above (Ducky3D, Kaizen),
not retried.

## 1. "Fix Merged Geometry after Voxel remeshing" (Blender Secrets)

Source: https://www.youtube.com/watch?v=HOxVKNRnGig | Blender Secrets,
uploaded 2026-10-17, 259 s, 19,644 views. Description: "When doing a
voxel remesh, sometimes geometry gets merged when it's too close
together. If you see it in time, you can simply move those parts further
apart (for example with fingers, you can use the Pose brush) or you can
increase the voxel resolution."

Tools used: **Blender** (Remesh modifier, Voxel Remesh in sculpt mode,
Lasso Face Set, Pose brush, Edit Mode X-Ray, Circle Select, Grid Fill,
Smooth Vertices, Dyntopo, Draw brush, Smooth brush, Shade Smooth).
No Blender version is stated in the captions.

This audit reconstructs the exact workflow from the captions, step by
step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it),
and **Why** (the principle). The video's core method is: if you catch
the merge early, separate the parts before remeshing; if you cannot
undo, cut the fused bridge out in Edit Mode, rebuild the holes, and
re-densify the pinched areas with Dyntopo.

### Phase 1: Diagnose the merge (and prevent it next time)

**Do**
1. Recognise the defect: because the voxel resolution is too low and
   the objects are too close together, they get fused together.
2. If you notice it early enough, decrease the voxel size and make the
   problem disappear that way.
3. When sculpting, keep a bit of space between parts such as fingers.

**Check**
- The fused bridge is the defect: two parts that should be separate read
  as one merged mass.

**Why**
- Voxel remeshing merges what the voxel grid cannot resolve: resolution
  and spacing are the two levers, and both are cheaper than repair.

### Phase 2: Separate the parts in sculpt mode (the early fix)

**Do**
1. In sculpt mode, select a Lasso Face Set and draw a face set around
   the part (a finger in the demo).
2. Go to Brush and choose the Pose brush.
3. Set Rotation Origin to Face Set: this gives a temporary bone you can
   move.
4. Move the part away from its neighbour.
5. Remove the face set with Face Set from Visible.

**Check**
- There is now space between the limbs. The author states the payoff
  directly: "having a bit more space between these limbs will also make
  it easier to do the rigging and to do the texture baking as well."

**Why**
- Separation before remeshing avoids the repair entirely, and the
  spacing pays twice: once for the remesh, once for rigging and baking.

### Phase 3: Cut the fused bridge out in Edit Mode (the late fix)

**Do**
1. Do NOT do this in sculpt mode: go to Edit Mode instead.
2. Turn on X-Ray so you can see through the model.
3. Press C for Circle Select; scroll the mouse wheel up or down to
   increase or decrease the selection radius.
4. Carefully select the fused vertices, right-click to exit Circle
   Select (back to normal box selection), press X and delete all the
   selected vertices.
5. Exit X-Ray mode.

**Check**
- You now have holes where the bridge was. That is expected, not a
  failure: Phase 4 rebuilds them.

**Why**
- A fused bridge cannot be un-merged; it has to be removed and rebuilt.
  Edit Mode with X-Ray is the author's stated place for that surgery
  because sculpt mode cannot delete the bridge cleanly.

### Phase 4: Rebuild the holes (Grid Fill, or Fill plus Triangulate)

**Do**
1. Select a hole: hold Alt and left-click, hold Shift and keep
   Alt-left-clicking until every vertex in the hole is selected, then
   press M and Merge at Center.
2. Alternative hole selection (author's shortcut): hold Alt and
   double-click to select the entire hole at once.
3. Check the selection count with Statistics enabled: the author has
   14 vertices, and because that is an even number, Grid Fill works.
   Press Ctrl-F and choose Grid Fill.
4. If Grid Fill gives a messed-up result, press F9 for the Grid Fill
   options, go back to one, and increase the numbers until the result
   improves.
5. Right-click and choose Smooth Vertices, then press Shift-R a few
   times to repeat the smoothing action until it looks better.
6. Alternative fill (author's second route): press F to fill the hole,
   then Ctrl-T to triangulate; delete any single stray vertex left over.
   Do the same on the second finger.

**Check**
- The author is honest about the intermediate state: "I know that the
  topology looks really crappy right now, but don't worry." Judge the
  rebuild after smoothing (step 5), not before it.

**Why**
- Grid Fill needs an even, closed loop; Fill plus Triangulate is the
  fallback when the loop will not cooperate. Both are means to a closed
  surface, and smoothing is what makes the closure read as surface
  rather than a patch.

### Phase 5: Fix pinched areas with Dyntopo

**Do**
1. Go to sculpt mode and turn on Dyntopo (author: "I'll use these
   settings," settings not stated in captions, so none are claimed).
2. Turn on wireframe in Overlays so you can see what Dyntopo is doing.
3. Brush over the pinched area to add geometry. Pick the Smooth brush
   to smooth; adjust its strength with Shift-F and reduce the amount,
   then brush lightly.
4. Remember the Dyntopo rule the author states: not all brushes add
   geometry. The Smooth brush does not add geometry, it just smooths
   it out.
5. To add denser geometry, go back to the Draw brush and draw with a
   very low strength, or even no strength: it will still add geometry
   even with a strength of zero.
6. Go back to the Smooth brush and smooth the new geometry.
7. Finish with Shade Smooth.

**Check**
- The pinched area reads as surface, not as a crease, and the wireframe
  shows new geometry where the Draw brush passed.

**Why**
- Dyntopo adds resolution exactly where the repair needs it, and the
  Draw-versus-Smooth distinction is the trap: smoothing a pinched area
  without first adding geometry only polishes the pinch.

### The human method, distilled

1. **Catch it early or cut it out**: decrease voxel size or Pose-brush
   separation before remeshing; Edit Mode deletion after.
2. **Holes are a stage, not a failure**: delete, rebuild, smooth, in
   that order.
3. **Dyntopo: Draw adds, Smooth only smooths**: a zero-strength Draw
   stroke still adds geometry.
4. **Spacing pays twice**: limbs apart helps remeshing, rigging, and
   baking.

**Depth status:** FULL (118 caption segments + description; no frames
reviewed; Dyntopo settings not stated in captions and not claimed).

## 2. "How to Make a Three Point Lighting Setup in Blender" (Ryan King Art)

Source: https://www.youtube.com/watch?v=sN8hS2vLG4o | Ryan King Art,
uploaded 2026-10-20, 807 s, 8,234 views. The video is a short clip from
the author's Lighting Essentials for Beginners tutorial, linked in the
description (the full tutorial was not retrieved, so nothing beyond this
clip is claimed).

Tools used: **Blender** (Area lights, Easy HDRI add-on, Environment
Texture, Film Transparent, camera, Track To object constraint),
**Leadenhall Market HDRI** (linked in the description). Subject: one of
the author's character sculpts (Michelangelo's David in the clip).

This audit reconstructs the exact workflow from the captions, step by
step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it),
and **Why** (the principle). The video's core method is: rim lights
first in a dark scene, then a main light on the side the subject faces,
then a dim fill, with a dark HDRI kept only for reflections, and Track To
constraints so every light keeps pointing at the subject while you move
it.

### Phase 1: Build the rim lights first

**Do**
1. Delete all existing lights and start dark.
2. Press Shift-A, add a Light, choose an Area light.
3. In rendered view, move it behind the subject and rotate it on the
   X-axis; scale it up until the edges carry a rim.
4. In Object Data Properties, turn up the power to make it brighter,
   change Shape to Rectangle, and turn up the Y size.
5. Duplicate it (Shift-D), move it to the other side, rotate on the
   Z-axis: rim lights on either side.

**Check**
- The rim pops the character out from the background and shows the
  shape of the character, even with nothing else lit.

**Why**
- The author states the order explicitly: "I like to add rim lights
  first because you can just see them a bit better cuz the scene is
  pretty dark." Rim-first is a visibility order, not a lighting theory:
  in a dark scene, rims are the only thing you can judge.

### Phase 2: Add a dark HDRI for reflections only

**Do**
1. Go to World Properties, click New to add a new world.
2. With the Easy HDRI add-on, click Create World Nodes to add an HDRI;
   or, without the add-on, choose Environment Texture, click Open, and
   open the HDRI (the author's is Leadenhall Market, linked in the
   description).
3. Turn down the sky strength and make it really dark.

**Check**
- The marble (or other reflective material) shows a little reflection,
  but the three-point system still dominates the look.

**Why**
- The HDRI is not the lighting here: it is background ambience and
  reflection fill. Turned down, it stops competing with the three
  lights you are actually designing.

### Phase 3: Place the main light on the facing side, set the camera

**Do**
1. Press Shift-A, add another Area light (the author likes area lights;
   a Sun light would also work, per the author).
2. Rotate and move it to the side the subject faces. In the clip, David
   looks one way, so the light goes on that side.
3. Go to Render Properties, open the Film tab, turn on Transparent, so
   the background is unseen but still lights the scene.
4. Add a camera (Shift-A), move the view where you want it, press
   Ctrl-Alt-numpad-0 to bring the camera to the view, then use the
   camera lock (gizmo icon) to move with the view.
5. In Output Properties, set resolution to 1920 x 1920 (a square image).
6. In Object Data Properties, set focal length to about 80: the author
   tries 100, calls it a little too strong, and settles near 80.
7. Turn off camera navigation once the camera is placed, then turn up
   the main light's power to make it stronger.

**Check**
- The majority of the face is lit, and the face the viewer looks at is
  the face that is lit. The author states the rule: "Usually you do
  want to light the main focus. So whatever you want the person to look
  at when they're looking at the artwork, that's what you want to light
  up."

**Why**
- Main-light placement follows the subject's gaze, not a fixed diagram:
  light on the turned-away side lights a face the viewer cannot see,
  and the subject ends up "looking into darkness."

### Phase 4: Add a dim fill, and keep the shadows

**Do**
1. Duplicate the main light (Shift-D), bring it over, rotate it, bring
   it down, to fill the dark area around the ear.
2. Drag the fill power down: the author suggests "like a five or a 10"
   (units as shown in the video; no absolute wattage is stated).
3. Make the main light a bit brighter again, so the hierarchy reads:
   main brightest, fill dim, rims for edge.

**Check**
- Shadows are present but not black: "the shadows aren't too dark."
  If the face looks flat, the fill is too bright: "because this light
  is pretty bright here, you can't really see the shape of the object
  that well."

**Why**
- The author states the shadow principle directly: "shadows are just as
  important as the light bits cuz the shadows actually show the shape
  of the object." A fill that erases shadows erases form.

### Phase 5: Colour naturally, and control shadow sharpness

**Do**
1. Colour the rims a little blue, or warm: for a natural feel, go cool
   (bluish) or warm (yellow/orange). Avoid super green or super red
   unless the scene has LED or Christmas lighting.
2. On the main light, push slightly toward yellow for warmth, or use
   the Temperature value for more accurate colours. For a fire or
   candle feel on the fill, turn on Temperature and drag it down.
3. To make shadows sharper, scale the light down (and optionally turn
   the power up a little more): smaller light, sharper and more
   dynamic shadow. To make shadows softer, scale the light up and make
   it bright (the author dislikes this look and prefers sharper
   lighting, a stated preference, not a rule).
4. Material matters: the author's procedural marble material can be
   darkened or coloured, which changes how the lighting reads.

**Check**
- The scene reads as natural light (warm or cool), and the shadow edge
  matches the mood you want: sharp for dynamic, soft for gentle.

**Why**
- Natural light in the real world is warm (fire, candle, sun) or cool
  (sky), so saturated hues read as artificial. Shadow sharpness is a
  mood control, driven by light size, not by a separate shadow setting.

### Phase 6: Track every light to the subject, and judge in a clean view

**Do**
1. Select a light, go to Constraint Properties, Add Object Constraint,
   add Track To, use the eyedropper for Target and click the head (or
   whatever object to track).
2. Now grabbing (G) and moving the light keeps it pointing at the
   subject: overhead, side, or any angle, without re-rotating by hand.
   Add Track To to the other lights the same way.
3. Split the window: in the second window, turn off gizmos and
   overlays, so you see the camera view clean while moving lights in
   the first window.
4. Hide all lights and overlays with the Show Overlays toggle when you
   want to judge the lighting alone.
5. For a warm, cosy variant: make the lights warm, scale them up so
   shadows soften, turn the power down to darken, raise world sky
   strength a little for more sky light, and move the main light
   farther to the side: closer blows the shapes out, farther to the
   side reveals the nose, wrinkles, and forehead shapes.

**Check**
- Moving any light never breaks its aim, and the camera view shows the
  lighting change live, without overlays in the way.

**Why**
- Track To turns lighting into positioning: the only decision left is
  where the light sits, not how it is rotated. The far-versus-close
  check is the author's form test: a light too close blows out shapes,
  a light to the side reveals them.

### The human method, distilled

1. **Rims first, in the dark**: judge what you can see before adding
   the main light.
2. **Light the face the viewer sees**: main light follows the subject's
   gaze.
3. **Fill dim, shadows kept**: fill power around 5-10, shadows show
   shape, a flat face means the fill is too bright.
4. **Natural colour, size-controlled shadows**: cool or warm only;
   smaller light, sharper shadow.
5. **Track To, then move**: constrain first, position second, judge in
   a clean camera view.

**Depth status:** FULL (439 caption segments; clip only, not the full
tutorial; no frames reviewed; no absolute power values beyond the
author's 5-10 fill range, and no light distances, are stated).

## 3. "5 Tips: Square to Round shapes, Inverted Hull, Reduce polycount, find double geometry, better bevels" (Blender Secrets)

Source: https://www.youtube.com/watch?v=hnHqboUoxxs | Blender Secrets,
uploaded 2026-10-15, 736 s, 11,620 views.

Tools used: **Blender** (Bevel, Loop Tools Circle and native To Circle,
Shear tool, Subdiv modifier, Solidify modifier, Emission shader,
Transparent BSDF, Mix Shader, Geometry node Backfacing, Light Path node
Is Camera Ray / Ray Length, Gaffer add-on, Decimate modifier Planar,
Triangulate modifier, Merge by Distance, Separate by Selection, Grid
Fill, Auto Merge, Loop Slide, Miter Outer Arc). Blender version: the
inverted-hull tip confirms the method still works in Blender 5.2.

This audit reconstructs the four NEW tips in full, and records the
inverted-hull tip as corroboration of the Oct 25 audit, step by step.
Every phase has three parts: **Do**, **Check**, and **Why**. The video's
core method is: five small, exact Blender fixes, each with a named
failure mode and a named setting that removes it.

### Phase 1 (Tip 1): Model a square-to-round shape

**Do**
1. Take the starting shape, delete two faces.
2. Scale up a bit: press S, X, and 4 on the numpad, then Enter.
3. Press Ctrl-Alt and left-click to select the edges, then Ctrl-B to
   bevel them; scroll the mouse wheel to adjust the loop count.
4. Set Profile Shape to 1 and Segments to 2.
5. Alt-click the loop, right-click, choose Loop Tools, Circle. Note:
   Loop Tools sometimes rotates things, fixable by adjusting the angle,
   but the author now prefers the native To Circle tool, which in his
   experience has a more predictable result with no angle change.
6. Press Ctrl-R to add a single loop in the middle, then right-click
   to cancel the transformation.
7. Use the Shear tool: move the handle a little, then type the value
   in the menu: 45 degrees. This creates a 45-degree angle.
8. Press W to return to the Select tool, Alt-click the loop, set Pivot
   Point to 3D Cursor (so rotation happens around that point), press
   R, Y, 90 to rotate 90 degrees along the Y axis, then set Pivot
   Point back to Median Point (do not forget this step).
9. Add a Subdiv modifier and shade smooth.
10. In Edit Mode, Alt-click a loop, press Ctrl-B to bevel it, scroll
    up, set Width Type to Percent, increase the percentage to 90,
    increase Segments to about 11, set Profile Shape to 0.5 (the
    author personally prefers 0.65 as more interesting).
11. Give it a matcap, select loops with Alt-click, Ctrl-F, Grid Fill,
    press I to inset a little, repeat on the other end, and add a loop
    around the corners as support loops.

**Check**
- The shape transitions from square to round, with support loops at
  the corners holding the subdivided form.

**Why**
- The bevel-plus-circle-plus-shear sequence builds the transition out
  of the existing topology instead of modelling two shapes and
  bridging them: the circle step is what makes the round end round,
  and the 45-degree shear is what makes the transition diagonal
  rather than stepped.

### Phase 2 (Tip 2): Inverted hull outline, corroborated for Blender 5.2

**Do**
- Same method as the Oct 25 FULL audit: two materials (skin, outline
  as a black Emission shader), Solidify modifier with Flip under
  Normals and Material Offset 1, Transparent BSDF plus Mix Shader
  with Geometry Backfacing as factor, second Mix Shader with Light
  Path Is Camera Ray as factor, example thickness 0.003 in Material
  Preview, Gaffer HDRI for light, Render Film set to Transparent,
  mirror fix by swapping Is Camera Ray for Ray Length, Transparent
  Shadows ON.

**Check**
- The author addresses the Blender 5.2 reports directly: "I saw a lot
  of comments from people who say it doesn't work anymore in Blender
  5.2. Fortunately, it still works exactly the same way. There's just
  some details that you really need to pay attention to."

**Why**
- This tip is recorded here as corroboration, not as a new technique:
  the method is unchanged, and the failure modes are the ones the Oct
  25 audit already records (whole head black from wrong noodles,
  transparent shadows off, mirror outline lost). The existing skill
  `materials-shaders/blender-inverted-hull-outline` is expanded with
  this second source (see "skill_library artifacts staged").

### Phase 3 (Tip 3): Reduce polycount on a real-time model

**Do**
1. After a subdivision workflow, identify the waste: flat areas that
   will not deform do not need all their quads; keep quads in the
   rounded, beveled parts.
2. Add a Triangulate modifier first (in the stack, below Decimate).
   Turn on wireframe in Object Mode to see what happens.
3. Set the Triangulate modifier so only n-gons get triangulated (the
   author: "I'm just going to set it to 5. That way only n-gons get
   triangulated," as captioned; no further Triangulate setting is
   stated, so none is claimed beyond that).
4. Drag a Decimate modifier up so it happens BEFORE Triangulate.
5. Set Decimate to Planar, so only the flat parts get triangulated.
6. Limit the effect with seams: the model already has seams (red
   lines); check Delimit so seam-marked edges are not affected.
7. Change the Angle Limit: set it to 1 degree, or even half a degree
   (author's correction: "not percent").

**Check**
- The beveled parts stay mostly quads and keep their shape, while the
  flat parts are reduced quite a bit by triangulation.

**Why**
- Planar decimation with seam delimiting is a targeted reduction: it
  spends triangles where curvature lives and removes them where the
  surface is flat, which is exactly the real-time trade (fewer
  triangles, same silhouette). The Angle Limit is the safety: smaller
  angles preserve more shape.

### Phase 4 (Tip 4): Find and remove hidden geometry

**Do**
1. Recognise the symptom: you press Alt-click to select a loop and
   cannot select the whole loop, and Merge by Distance cannot fix it.
2. Know the cause: in Blender, G moves things and F creates faces, and
   the keys sit next to each other, so an accidental F press creates a
   long face that is almost invisible.
3. Go to Face Selection mode in Edit Mode and box-select only the
   visible geometry. Do NOT press A to select everything: that also
   selects the faces you do not want.
4. Press H to hide the visible selection: now the hidden geometry is
   visible.
5. Press A to select the hidden remainder. Do NOT delete it yet: the
   author warns that deleting and unhiding would destroy the whole
   shape, so undo if you tried that.
6. Press P, Separate by Selection. Press Alt-H to unhide. A second
   object now appears in the Outliner: delete that object.
7. Now select normally and use Grid Fill: everything works.

**Check**
- Alt-click loop selection works again, and Grid Fill completes.

**Why**
- The hidden face is invisible precisely because it hides under the
  visible surface, so the fix is not a merge or a delete but a
  separation: hide what is good, isolate what is hidden, split it into
  its own object, and delete that object.

### Phase 5 (Tip 5): Bevels that distribute evenly

**Do**
1. Even distribution: press Ctrl-B to bevel. If the bevel is not
   distributed evenly along the surface, press F9 for the bevel
   options, change Width Type to Percent, and increase the percentage.
   Instead of eyeballing the stop point, set it to 100.
2. Before beveling to 100, turn on Auto Merge: at 100 Percent without
   Auto Merge, double vertices appear; with Auto Merge on, beveling
   to 100 creates no double vertices. Segments can still be changed.
3. Narrow-to-wide shape: the default here is Offset, not Percent,
   because Percent would give a strange result. If the bevel follows
   the taper and you do not want that, disable Loop Slide: now it
   follows a straight line.
4. Rounded flow: press Ctrl-B, open the options with F9 (Percent vs
   Offset makes no difference here), set Miter Outer to Arc: now you
   get a nice rounded bevel.

**Check**
- At 100 Percent with Auto Merge, no double vertices; with Loop Slide
  off, the bevel runs straight; with Miter Outer Arc, the bevel flows
  rounded.

**Why**
- 100 Percent is a deterministic stop point, not an eyeballed one, and
  Auto Merge is what makes 100 safe. Loop Slide and Miter Outer are
  the two shape controls: one decides whether the bevel follows the
  taper, the other decides whether its outer corner rounds.

### The human method, distilled

1. **Circle, then shear, then pivot**: square-to-round is a sequence,
   not a single tool.
2. **Inverted hull is unchanged in 5.2**: the details (noodles,
   transparent shadows) are the failure, not the version.
3. **Reduce flats, keep curves**: Planar decimation, seam-delimited,
   angle-limited.
4. **Hidden faces separate, they do not merge**: hide the good, split
   the hidden, delete its object.
5. **Bevel to 100 with Auto Merge**: a number beats an eyeball.

**Depth status:** FULL (221 caption segments; no frames reviewed).

## 4. "Why you get that 'weird' smearing effect when you shade smooth" (Josh - Blender Bros)

Source: https://www.youtube.com/watch?v=SrR8n854D0A | Josh - Blender
Bros, uploaded 2026-10-19, 526 s, 18,197 views.

Tools used: **Blender** (Shade Smooth, Shade Auto Smooth / shade smooth
by angle, face and vertex normal display), plus a tutorial-only overlay
plugin the author built for this video (angle and dot-product display,
mouse probe, heat map; not a released tool, and not claimed as one).

This audit reconstructs the explanation from the captions, step by step.
Every phase has three parts: **Do**, **Check**, and **Why**. The video's
core method is: show, with measured angles, why plain Shade Smooth smears
a hard-surface object, and why Shade Auto Smooth does not.

### Phase 1: See the smear on a cube

**Do**
1. Add a cube to a Blender scene and shade it smooth.
2. Observe the result: a nasty smeared mess of shading.

**Check**
- The smear is visible on the cube's faces, worst away from the face
  centres.

**Why**
- The author states the framing up front: everyone knows you can shade
  auto smooth and get on with your life, but this video explains why
  the error occurs on a technical level.

### Phase 2: Measure the angle that causes it

**Do**
1. Display the face normal: a normal coming out of a face at 90
   degrees.
2. Display the vertex normal: a normal coming out of a vertex at what
   looks like 45 degrees.
3. Use the author's overlay tool: three lines (blue, orange, yellow),
   an angle, and a dot-product readout. The blue line follows the face
   normal direction; the red line is the vertex normal line.
4. Read the angle between face normal and vertex normal: 54.7 degrees
   (by dot product; the author notes the math can be fed to Claude
   from the transcript, but the number is what matters here).

**Check**
- The mouse probe confirms the interpolation: closer to the face
  normal, the average is close to 0 degrees and the shading is clean;
  closer to the vertex normal, the average climbs to 54.7 degrees and
  the shading smears.

**Why**
- Plain smooth shading interpolates across that angle: "it's smoothing
  out the object over this angle here." Near the face normal the
  shading is almost aligned, so it looks fine on top; further away,
  the averaged angle grows, and "the more nasty and smeared the shading
  gets because of how that shading is being calculated."

### Phase 3: Apply Shade Auto Smooth and verify the fix

**Do**
1. Switch the overlay view to corner normal, then shade auto smooth.
2. Observe: the shading is now forced to be calculated only from the
   angles, so everything is essentially 0 degrees, with no angle
   between the objects.
3. Test the edge case: move a vertex down slightly and shade smooth
   again: the shading goes crazy (angles 54.6 and 54.7 in the author's
   moved-cube variant). Shade auto smooth on the same moved cube still
   works fine, because the change is within the angle threshold.
4. Adjust the auto-smooth angle value: once the value passes an edge,
   that edge starts smoothing, and the shading degrades again, but less
   badly, because the angle there is shallower.
5. Optionally view the heat map: smooth shading reads perfectly red,
   auto smooth reads clean, which illustrates the same result.

**Check**
- With Shade Auto Smooth, no matter where the probe sits, the angle
  stays at 0 degrees and the shading stays perfect. With plain Shade
  Smooth, it does not.

**Why**
- The author states the conclusion directly: Shade Auto Smooth "forces
  that angle to just be flat at zero, giving you perfect shading." The
  threshold is the control: within it, edges stay sharp; past it, they
  smooth, and the angle value decides which edges those are.

### The human method, distilled

1. **The smear is an angle, not a bug**: 54.7 degrees between face and
   vertex normal on a cube, by dot product.
2. **Probe the interpolation**: clean near the face normal, smeared
   toward the vertex normal.
3. **Auto Smooth flattens the angle to zero**: that is why it works,
   and the angle threshold is what decides which edges smooth.
4. **Model, do not just fix**: the author's closing point is that what
   matters is knowing how to model and use Blender, not the technical
   demonstration itself.

**Depth status:** FULL (211 caption segments; explanation plus fix;
the overlay plugin is tutorial-only and no download or settings for it
are claimed; no frames reviewed).

## 5. "The Most ANNOYING Modeling Situation in Blender" (Josh - Blender Bros)

Source: https://www.youtube.com/watch?v=gQUYQJYs_R8 | Josh - Blender
Bros, uploaded 2026-10-14, 315 s, 12,875 views.

Tools used: **Blender** (loop cut, extrude, Limited Dissolve, bevel
Ctrl-B, Subdivision Surface / sub-D, crease Shift-E, Shade Auto Smooth,
Loop Tools Relax), **Plasticity** (non-polygon modeller, used as the
comparison, not as the Blender workflow).

This audit reconstructs the workflow from the captions, step by step.
Every phase has three parts: **Do**, **Check**, and **Why**. The video's
core method is: when a bevel is geometrically impossible in polygon
modelling, do not force the bevel; build the shape with sub-D and let
the subdivision create the bevel-like transition.

### Phase 1: Build the impossible shape and name the problem

**Do**
1. Build the demo shape: add a loop cut, extrude on X, scale with
   Shift-Z so it does not move on Z, run a Limited Dissolve to get rid
   of the junk.
2. Observe the two problems: a nasty shading error on the side, and
   no space to bevel the area with Ctrl-B, because the edge starts
   overlapping almost immediately.
3. Try the obvious fix and watch it fail: dissolve for more space, and
   the curvature of the cylinder is disrupted; loops cannot run
   through the area.

**Check**
- The bevel cannot be run, and dissolving to make room breaks the
  shape it was meant to preserve.

**Why**
- The author names it: "This is what we call an impossible operation."
  In a polygon modeller, a bevel that overlaps itself on the first
  step has no valid result, and no amount of dissolving creates one
  without breaking the surrounding curvature.

### Phase 2: See the same bevel in Plasticity

**Do**
1. In Plasticity, select the edge and bevel: it bevels straight through
   perfectly, with no issues.

**Check**
- The bevel exists, cleanly, in the non-polygon tool.

**Why**
- Plasticity is not a polygon software, so the operation that is
  impossible on a mesh is trivial on its geometry. The comparison is
  the point: the limitation is Blender's polygon representation, not
  the shape itself. The author recommends using both Blender and
  Plasticity together, and this video is not a claim that Blender
  should replace Plasticity for this operation.

### Phase 3: Build the sub-D workaround in Blender

**Do**
1. Move the shape over, scale it down, and use a lower segment count:
   the author puts it to 16, because sub-D will increase the
   resolution.
2. Add a loop cut, go into the side, box-select the area, extrude on
   X, Shift-Z, just like the original shape.
3. Do NOT dissolve anything this time: good topology is needed to run
   the sub-D, so keep everything as quads.
4. Do NOT use bevels at all: use a sub-D instead, for the actual shape,
   not for topology purposes.
5. Shade smooth, crease the top, and for the bottom fill it into an
   n-gon and crease it with Shift-E.
6. Right-click to Shade Auto Smooth: the bevel-like result is already
   there.
7. Add loop cuts (one or two) to control the area, add a loop to
   tighten it up, keep Shade Auto Smooth, and adjust the angle a
   little to get the result wanted.
8. For more control, move vertices up a bit higher to push the bevel
   up higher and make a more rounded area.
9. Run a Relax with Loop Tools, turn off the regular (setting as
   captioned), slide down, add a couple of loops, for more control
   over the shape.

**Check**
- The transition reads as a clean bevel into the mesh, with the
  surrounding cylinder curvature intact, and the shape can be tuned
  by moving vertices and loops rather than by re-running a bevel.

**Why**
- Sub-D creates the transition by subdivision, not by cutting new
  geometry into a crowded edge: the author states this is "the only
  way you could do something like that in Blender, because that bevel
  operation is physically impossible." Keeping quads is what makes
  the sub-D predictable; dissolving them is what broke the original
  attempt.

### The human method, distilled

1. **Name the impossible operation**: a bevel that overlaps immediately
   cannot be forced, and dissolving to make room breaks the shape.
2. **Plasticity proves the shape is valid**: the limit is the polygon
   representation, not the design.
3. **Sub-D is the Blender answer**: low segment count (16 in the demo),
   all quads, no bevels, crease with Shift-E, Shade Auto Smooth, loops
   for control.
4. **Use both tools**: Blender and Plasticity together, each where it
   works.

**Depth status:** FULL (152 caption segments; no frames reviewed;
Loop Tools Relax "regular" setting is as captioned and not expanded).

## 6. "Part 1: Creating a Realistic Hamburger (Blender Tutorial)" (Ryan King Art)

Source: https://www.youtube.com/watch?v=1inVxY0EYD8 | Ryan King Art,
uploaded 2026-10-21, 1706 s, 10,053 views. Part 1 only: buns and seeds.
Series plan stated in the video: Part 2 burger and cheese, Part 3 tomato
and lettuce, Part 4 pickles and onions, Part 5 assembly, sauce,
lighting, ground, rendering, compositing. The series is explicitly not
for beginners and moves faster, with fewer shortcut callouts, for
intermediate users.

Tools used: **Blender** (Subsurf / Subdivision Surface modifier, Displace
modifier, Principled BSDF, Gradient Texture, Noise Texture, Mix Color
Linear Light, Color Ramp, Bump node, Mapping, Scatter on Surface
Geometry Nodes modifier, weight paint), **Pixabay** royalty-free texture
images (linked in the description; project files with textures are sold
on Gumroad/Patreon), **Krita** (lettuce edge mask via wand transparency,
in a later part, not executed here).

This audit reconstructs Part 1 from the captions, step by step. Every
phase has three parts: **Do**, **Check**, and **Why**. The video's core
method is: build the bun shape with Subsurf plus Displace, paint its
material procedurally from a distorted gradient (toasted top, light
inside), then scatter seeds over only the bun top with a weight-painted
mask.

### Phase 1: Set up the bun shape

**Do**
1. Model the bun, then press Ctrl-2 for a Subsurf modifier (level 2 by
   the Ctrl-2 shortcut, as captioned).
2. Add a Displace modifier, driven by an image texture (from the
   Texturing panel, from image or texture), to make the bun bumpy.
3. Save the project (the author saves mid-tutorial and again after
   the seeds).

**Check**
- The bun reads as a domed, bumpy form, not a smooth primitive.

**Why**
- Subsurf gives the smooth dome, Displace gives the surface
  irregularity: the two modifiers split form and texture, so each can
  be tuned separately.

### Phase 2: Build the procedural bun material

**Do**
1. In the World/Environment setup (for reference textures, as shown),
   choose Environment Texture and open a texture image; for the bun
   material itself, add a new material.
2. Enable Node Wrangler in User Preferences (the author enables it to
   use Ctrl-T): select the Gradient Texture, press Ctrl-T to add
   Texture Coordinate and Mapping nodes, and preview the gradient.
3. Rotate the gradient via Mapping so it runs the right way for the
   bun.
4. Set Principled roughness to 0.9 as the base.
5. Add a Noise Texture and mix it with the gradient to distort it:
   search for Mix Color, choose Linear Light, put the Noise Texture
   factor into B and the Gradient Texture colour into A, preview the
   Linear Light, then turn the Noise factor down to 0.01 so the
   distortion is subtle (gradient still light on top, black below,
   but noisy).
6. Add a Color Ramp after the Linear Light: drag the white and black
   tabs to shape the transition. Colours (author's hex codes, stated
   verbatim): inside/peachy FFCC74, middle brown 8A4722, darkest
   211006. Add a middle tab with Ctrl-click, also brown but lighter
   (the lighter mid-brown tab's hex is not stated separately, so it
   is not claimed).
7. Set the Mapping location to about 0.11 (author: "maybe a point one
   one," dependent on object and origin) and the Mapping scale to
   about 0.4, so the gradient is larger and the transition does not
   happen too quickly: light on the bottom, brown in the middle, so it
   reads as toasted on top.
8. Plug the Color Ramp into the Principled Base Color and preview.
9. Mix in dark noise over the whole material: add another Noise Texture
   with the same Mapping, set Scale to 170 (very detailed), Detail to
   15, Roughness all the way up to 1, through a Color Ramp (black and
   white; the author notes he put colour into the factor in the
   original files, and that factor versus colour makes no practical
   difference here).
10. Add bump: add another Noise Texture for bump, set its roughness
    to 0.65 (as captioned for the bump noise), convert it with a Bump
    node between the noise and the Principled shader, so the bun
    surface has visible bump.
11. Open Subsurface in the Principled shader and set subsurface weight
    to 0.4, for a bit of subsurface scattering in the bread.
12. Result: "our basic bread material." Duplicate it for the bottom
    bun and customise it slightly so it is not identical.
13. Seed material (separate, later in the video): colours CFCFCF and a
    slightly darker 8F8F8F, so the seeds look a little shiny but not
    extremely shiny.

**Check**
- The bun reads as toasted on top (dark brown), lighter inside
  (peachy), with fine dark noise and bump across the surface, and a
  soft subsurface glow rather than a flat plastic look.

**Why**
- The gradient is the toast map (top dark, inside light), the noise
  at 0.01 breaks the gradient's perfection without destroying it, the
  170-scale noise is the crumb detail, and subsurface at 0.4 is what
  stops bread from reading as plastic. Each number is a different
  scale of realism, and they stack rather than compete.

### Phase 3: Scatter the seeds on the bun top only

**Do**
1. Model a seed, rename objects with F2 for organisation: "hamburger
   top bun" (or "bun top"), "seed", "hamburger bun bottom." Rename
   materials the same way.
2. Select the top bun, add a Scatter on Surface modifier (powered by
   Geometry Nodes), choose the seed as the scattered object.
3. Set Density to 10,000 (author: "a 10 with three zeros").
4. Change distribution to Poisson disk, so seeds have space between
   them, and set Minimum Distance to 0.008, so no seeds overlap.
5. In Transform, turn on Randomize, set Rotation Z to 360 degrees (full
   rotation range), and set Scale variation to 0.3, so every seed is
   not exactly the same.
6. In Edit Mode on the seed, select everything and drag it so the
   origin point is more in the centre, so placed seeds sit centred.
7. Weight-paint the distribution mask: go to Weight Paint mode on the
   bun. The viewport lags because of the Subdivision Surface, so hide
   the Subsurf from view (monitor icon) while painting.
8. Paint only the top: red adds weight, Ctrl (blue) erases weight.
   In the Scatter on Surface modifier, under Distribution Mask, click
   the Input Attribute toggle and choose the painted vertex group.
9. Erase until seeds show only on the very top: seeds are not visible
   in the middle where the bun has been sliced, only on the top.
10. Turn the Subsurf view back on, check in rendered view, and if a
    seed sits in a bad spot, change the scatter Seed value (the random
    value under Minimum Distance) until the placement looks better.
    Save with Ctrl-S.

**Check**
- Seeds cover only the bun top, none overlap, rotations and scales
  vary, and no seed sits in the sliced middle.

**Why**
- Poisson disk plus minimum distance is the anti-overlap guarantee,
  weight paint is the placement mask (top only, not the cut face), and
  hiding Subsurf while painting is the performance fix: the mask is
  painted on the low-poly cage, then evaluated on the subdivided
  surface.

### The human method, distilled

1. **Form, then surface, then scatter**: Subsurf plus Displace for
   shape, procedural gradient for toast, scatter for seeds, in that
   order.
2. **Numbers at different scales**: gradient 0.4 for toast, noise 0.01
   for distortion, noise 170 for crumb, subsurface 0.4 for bread.
3. **Scatter is masked, not random**: density 10,000, Poisson disk,
   minimum distance 0.008, rotation Z 360, scale variation 0.3, weight
   paint for the top only.
4. **Rename everything**: organised objects and materials are part of
   the workflow, not an afterthought (F2 renames throughout).

**Depth status:** FULL (926 caption segments; Part 1 only; no frames
reviewed; the lighter mid-brown Color Ramp tab hex, the Displace
texture strength, and the seed mesh itself are not stated in captions
and are not claimed).

## Have-vs-need tables

### Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Mesh-refinement stage with deviation metrics | Voxel-remesh repair, five-tips cleanup (audits 1, 3) | NEED (unchanged, evidence added) | Inventory NEED; fix artifact prepared, not landed | Watchlist: the repair recipes (Pose separation, Grid Fill, Dyntopo re-densify, Planar decimation, hidden-geometry separation) are citable repair patterns for the stage design, but they carry no deviation metrics, so they do not fill the gap |
| Per-asset perf budgets | Five-tips polycount reduction (audit 3) | NEED (unchanged) | Inventory NEED; fix artifact prepared with 3 cited anchors only | Watchlist: do NOT add the Planar decimation method as a budget anchor; it states no tri counts, texel density, or draw calls |
| Rigging / skinning / animation-retarget stage | Voxel-remesh repair spacing note (audit 1) | NEED (unchanged) | Inventory: "No rigging / skinning / animation-retarget stage in the foundry" (2026-09-26 audit); fix artifact prepared, not landed | Watchlist: one sentence about spacing easing rigging is not a stage |
| AI-vendor generation/acceptance spec | (none today) | NEED (unchanged) | Inventory NEED; fix artifact prepared, not landed | No change |
| Automated UE import validation gate | (none today) | NEED (unchanged) | Inventory NEED; fix artifact prepared, not landed | No change |
| Mesh compression + virtual-texture output standard | (none today) | NEED (unchanged) | Inventory NEED; fix artifact prepared, not landed | No change |
| MCP-driven DCC loop | (none today) | NEED (unchanged, P2) | Inventory gap; prior art in `agentic-blender-asset-pipeline` skill | No change |
| Toon outline (inverted hull) | Five-tips tip 2 (audit 3) | NEED (no attach point) | No toon-outline stage in inventory; UE packaging exists but no outline shader standard | Watchlist: method re-corroborated for Blender 5.2, same recipe as Oct 25; transferable as a toon-law reference, not a foundry stage |
| Three-point lighting (area lights, Track To) | Lighting setup (audit 2) | NEED (no attach point) | No lighting stage in inventory | Watchlist: rim-first order, fill 5-10, Track To constraint are a citable lighting recipe for any future render-look work |
| Shade Auto Smooth normal rule | Smearing explanation (audit 4) | NEED (no attach point) | No shading/normal standard in inventory | Watchlist: the 54.7-degree explanation and the auto-smooth-by-angle rule are a mesh-quality check candidate for the foundry QA stage |
| Sub-D impossible-bevel workaround | Annoying modeling (audit 5) | NEED (no attach point) | No hard-surface modelling stage in inventory | Watchlist: sub-D instead of bevels, all quads, Shift-E creases, is a modelling pattern, not a foundry stage |
| Procedural bun material + seed scatter | Hamburger Part 1 (audit 6) | NEED (no attach point) | No procedural material stage in inventory; intake/concept generation exists, but no material authoring stage | Watchlist: gradient-plus-noise toast map, hex codes FFCC74 / 8A4722 / 211006, and weight-painted scatter are citable material/scatter patterns |

### 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Art bible / toon law | Inverted hull corroboration, three-point lighting (audits 3, 2) | NEED (unchanged, evidence added) | Roadmap rec 2; fix artifact prepared, not landed | Adopt as evidence: inverted hull (Blender 5.2 confirmed) as the outline standard, three-point lighting (rim-first, fill 5-10, Track To) as the lighting standard; neither is the bible itself (no pillars, palette, silhouette rules) |
| Explore-mode lighting bible + IC-Light painted-light fit | Three-point lighting (audit 2) | NEED (unchanged, evidence added) | Roadmap rec 19 | Watchlist: the three-point recipe is a lighting-bible candidate section, not the bible; IC-Light fit still unaddressed |
| Production-conversion stage | Voxel repair, five-tips cleanup (audits 1, 3) | NEED (unchanged, evidence added) | Roadmap rec 20 (retopo, UV, rig, LOD, compression); fix artifact prepared, not landed | Watchlist: repair and reduction recipes are conversion-adjacent (cleanup before conversion), but neither is a conversion stage with retopo, UV, rig, LOD, and compression |
| Asset import validation gate | (none today) | NEED (unchanged) | Roadmap rec 9; `qa/asset_validate.py` fix artifact prepared, not landed | No change |
| Shade Auto Smooth normal rule | Smearing explanation (audit 4) | PARTIAL | Sprite render path exists (`tools/gen_iso_sprites.py`); no normal/shading standard | Watchlist: adopt the rule (plain Shade Smooth smears hard surfaces; Shade Auto Smooth by angle fixes it) as a sprite-render QA check |
| Procedural material + scatter | Hamburger Part 1 (audit 6) | PARTIAL | Procedural texture/audio generators exist (`pipeline/proc/`); no material/scatter stage for props | Watchlist: gradient-plus-noise material and weight-painted scatter are patterns for prop materials, if 2d3d ever needs them |
| Sub-D bevel workaround | Annoying modeling (audit 5) | NEED (no attach point) | 2D pixel pipeline; no hard-surface modelling stage | Watchlist: pattern only |

### Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Shader-driven skyline fill | (none today) | NEED (unchanged) | PRD 17.1: no equivalent; every building authored or generated | No change |
| Three-point lighting | Lighting setup (audit 2) | NEED (no attach point) | Blender sprite render path exists (`tools/gen_iso_sprites.py`); no lighting standard | Watchlist: rim-first area-light recipe could standardise sprite lighting, but Desktop City sprites are rendered, not real-time lit; evaluate only if a lighting contract enters the sprite pipeline |
| Procedural material + scatter | Hamburger Part 1 (audit 6) | NEED (no attach point) | `tools/city_*` family exists; no material/scatter stage for props | Watchlist: scatter pattern (density, Poisson disk, weight mask) is transferable to prop placement, if ever wanted |
| Mesh cleanup (voxel repair, polycount, hidden geometry, bevels) | Audits 1, 3 | NEED (no attach point) | No mesh cleanup stage; buildings are static sprites | Watchlist: cleanup recipes matter only if a mesh stage enters the pipeline |
| Rigging | (none today) | SKIP by design | PRD 17.1: buildings need no rigging; animated subjects rig only exported clips | Skip with reason stated, not a gap |

### Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Godot import validation gate + re-measured export budgets | (none today) | NEED (unchanged) | ADR 0003; fix artifact prepared, not landed | No change |
| AI-vendor acceptance spec | (none today) | NEED (unchanged) | Concept-PNG-as-authority convention only | No change |
| Toon outline | Inverted hull corroboration (audit 3) | NEED (no attach point) | Pipeline is mesh/GLB-based with concept-PNG authority; no outline shader stage | Watchlist: outline recipe is Blender-side; a toon-outline standard would need a GLB-round-trip check before adoption |
| Mesh cleanup / shading rules | Audits 1, 3, 4 | NEED (no attach point) | Pipeline stages exist for mesh/GLB; no cleanup or shading standard recorded | Watchlist: voxel repair, Planar decimation, hidden-geometry separation, and the Shade Auto Smooth rule are QA candidates for the mesh pipeline |
| Three-point lighting / procedural material / scatter | Audits 2, 6 | NEED (no attach point) | Concept-PNG authority only; no lighting or material stage | Watchlist: patterns only |

## Watchlist trending

## Watchlist trending
- GPT Astra (mesh split, UV fix, CC0 texture replacement; Blender MCP looping) (first seen 2026-09-28, status WATCH; seen again 2026-09-28, 2026-10-04, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-26) **TRENDING**
- Light Wrangler Blender add-on (gobo lighting rigs) (first seen 2026-09-27, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-26) **TRENDING**
- Procedural galaxy generator (Blender GeoNodes + shaders, point clouds for stars, volumes for nebulae) (first seen 2026-10-09, status WATCH; seen again 2026-10-13, 2026-10-26) **TRENDING**
- Blender inverted hull outline (Solidify flip + Backfacing mix + Is Camera Ray, Blender 5.2) (first seen 2026-10-25, status WATCH; seen again 2026-10-26)
- Blender Geometry Nodes flower motion-design setup (first seen 2026-10-15, status WATCH; seen again 2026-10-22, 2026-10-26) **TRENDING**
- Geometry Nodes upright-billboard flat-line technique (Blender) (first seen 2026-10-22, status WATCH; seen again 2026-10-26)
- Procedural ribbon cables (Blender GeoNodes) (first seen 2026-09-27, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-26) **TRENDING**

Correction to the auto-match above (same handling as prior runs): only
the inverted-hull row is a genuine reappearance today (audit 3 tip 2
repeats the Oct 25 technique and confirms it for Blender 5.2). The other
six rows matched on tokens only, and each row in
`references/tooling-watchlist.md` now carries a bracketed correction
note saying so: GPT Astra (matched on Blender/mesh, never mentioned),
Light Wrangler (matched on lighting; today's lighting is a plain
three-point area-light setup, no add-on), procedural galaxy generator
(matched on procedural; today's procedural work is a bun material, not
galaxies), Geometry Nodes flower setup (matched on Geometry Nodes;
today's GeoNodes work is Scatter on Surface seeds, not flowers),
upright-billboard technique (matched on Geometry Nodes, same reason),
procedural ribbon cables (matched on Geometry Nodes/scatter, not cables).
Genuine new-tool activity (new rows, not reappearances): voxel-remesh
merged-geometry repair; three-point lighting; square-to-round shape;
Decimate Planar polycount reduction; hidden-geometry separation; bevel
tips (Auto Merge 100 Percent, Loop Slide off, Miter Outer Arc);
shade-smooth smearing explanation; sub-D impossible-bevel workaround
plus Plasticity; procedural bun material plus Scatter on Surface seeds.

New watchlist rows appended 2026-10-26 (9): see the rows in
`references/tooling-watchlist.md` dated 2026-10-26 (and synced into the
skill_library staging copy's watchlist in this run; the staging copy
itself is not pushed, see below).

## Gap recommendations (highest leverage)

1. **Voxel repair plus Planar decimation as the mesh-refinement evidence
   pack for Aegis.** Next step: when the `mesh-refinement-stage.md` fix
   artifact is landed, cite audit 1 (Pose separation, Edit Mode
   delete, Grid Fill, Dyntopo Draw-versus-Smooth) and audit 3 tip 3
   (Decimate Planar before Triangulate, seam delimit, Angle Limit
   1 or 0.5 degrees) as the repair and reduction recipes inside the
   stage, and keep the gap open until a deviation metric is added:
   neither audit measures deviation, so neither closes the gap.
2. **Shade Auto Smooth as a foundry QA check.** Next step: add "hard
   surfaces are shaded auto smooth by angle, never plain shade smooth"
   as a candidate check for any mesh QA gate, sourced to audit 4
   (54.7-degree face-to-vertex-normal angle on a cube, 0 degrees under
   auto smooth). Cheap, verifiable, and independent of the larger
   import-validation gate.
3. **Three-point lighting as the lighting-bible seed for 2d3d.** Next
   step: when the art-bible fix artifact is landed, cite audit 2
   (rim-first order, main on the facing side, fill 5-10, Track To
   constraints, cool-or-warm-only colour rule) as the lighting section,
   alongside the inverted-hull outline standard. The bible gap stays
   open until pillars, palette, and silhouette rules exist alongside
   them.
4. **Sub-D workaround as the hard-surface modelling note.** Next step:
   if any repo's modelling guidance ever covers bevels, record audit 5
   (bevels that overlap immediately are impossible in polygon
   modelling; sub-D with all quads, Shift-E creases, and Shade Auto
   Smooth is the Blender answer; Plasticity bevels through directly)
   so the next modeller does not burn time dissolving for space.
5. **Hamburger scatter as the prop-scatter pattern.** Next step: if
   prop placement ever enters Desktop City or Solarempire tooling, reuse
   audit 6 (Scatter on Surface, density 10,000, Poisson disk, minimum
   distance 0.008, rotation Z 360, scale variation 0.3, weight-painted
   top-only mask, hide Subsurf while painting) before building a custom
   scatterer.

## Explicit non-goals (found but correctly skipped)

- The two bot-blocked YouTube videos (Ducky3D `gb8jdGh_LsE`, Kaizen
  `SWs2iltL7rU`): blocked, not retried, no cookie workaround attempted.
- Hamburger Parts 2-5: scanned, not audited this run; Part 1 only was
  audited, the rest stay in the 14-day YouTube window for the next run.
- The inverted-hull video itself: already skilled Oct 25, recorded here
  only via its corroboration in audit 3 tip 2.
- The author's tutorial-only overlay plugin in audit 4: a demonstration
  aid, not a released tool, not watchlisted as a tool.
- Plasticity in audit 5: a comparison tool, watchlisted only as part of
  the sub-D workaround row, not as a new pipeline stage.

## skill_library artifacts staged

- Full report copied to the staging mirror at
  `~/workspace/video-tooling-scout-public/docs/scout-reports/have-vs-need-2026-10-26.md`,
  with the scout-reports README index row added.
- Existing skill `materials-shaders/blender-inverted-hull-outline`
  expanded in staging with a second-source note: the 2026-10-15 "5 Tips"
  video repeats the same method and confirms it still works exactly
  the same way in Blender 5.2 (audit 3 tip 2, this run).
- **No new skill folders staged today, and no push attempted.** Two
  reasons, both stated plainly. First, category fit: today's six audits
  are generic Blender modelling, lighting, shading, and material
  work, and none of the 9 fixed categories fits them cleanly
  (materials-shaders fits only the hamburger material, and forcing
  mesh repair, lighting, and shading into capture, procgen-worlds, or
  engine-runtime would be a misfit; new categories are Ehsan's call
  only). The audits are in this report and on the watchlist, ready to
  convert once Ehsan picks a category or confirms a fit. Second, the
  push is already blocked: the Oct 25 nightly refinement push failed
  403 on lost Contents write access, and the Oct 26 contributor-path
  push failed 403 on missing Workflows scope, with staged work still
  unlanded. Staging six more folders would only grow an unlanded
  backlog, so it is held until token access is restored. The daily
  push cron (~09:18 ET) remains the loop's next step, and it will hit
  the same block until the token is fixed; that fix is Ehsan's, not
  this run's.
