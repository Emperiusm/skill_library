---
name: blender-inverted-hull-outline
description: "Build a toon outline in Blender with the inverted hull method: Solidify modifier with Flip normals and Material Offset 1, a black Emission outline material, a Transparent BSDF mixed by Geometry Backfacing, a second Mix Shader gated by Light Path Is Camera Ray (Ray Length for mirror reflections), 0.003 example thickness, and transparent shadows ON. Works in Cycles and Eevee. Trigger when a Blender character needs a clean toon outline and the first attempt renders black or loses the outline in reflections."
---

# Blender Inverted Hull Outline (Solidify Flip, Backfacing Mix, Camera-Ray Gate)

## Purpose

This skill reconstructs the inverted hull outline workflow from Blender
Secrets' captioned walkthrough, step by step, so another agent can follow
the same process. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: grow a flipped solidify shell around the
mesh, give the shell a black emission material, and use backfacing plus
camera-ray logic to show only the shell's rim as the outline.

## Source

Creator: Blender Secrets. Video:
https://www.youtube.com/watch?v=dybTdt9WXts ("How to do an inverted
hull outline and what if it doesn't work?", uploaded 2026-10-12, 295 s,
9,412 views) | 2026-10-25 scout run, audit 7. Description: "I made a
video before about making a toon outline shader for both Cycles and
Eevee, and I get a lot of questions about it, so I made it again with a
bit more detail."

Second source (2026-10-26 scout run, audit 3 tip 2): Blender Secrets repeats the same method in "5 Tips: Square to Round shapes, Inverted Hull, Reduce polycount, find double geometry, better bevels" (https://www.youtube.com/watch?v=hnHqboUoxxs, uploaded 2026-10-15, 736 s, 11,620 views) and confirms it still works exactly the same way in Blender 5.2, despite viewer reports that it had stopped working. The details that people miss are the ones this skill already records: noodles plugged exactly as shown, Transparent Shadows ON, and Ray Length (not Is Camera Ray) for mirror reflections. No change to the method itself.

## Tools used

**Blender** (author says the method still works in Blender 5.2; captions
are ASR, so the version is reported as captioned), **Solidify modifier**,
**Emission shader**, **Transparent BSDF**, **Mix Shader**, **Geometry
node (Backfacing)**, **Light Path node (Is Camera Ray / Ray Length)**,
**Gaffer add-on** (HDRI lighting), **Cycles** and **Eevee**. Demo asset:
a head from the Blender asset pack (multi-res modifier present, collapsed
and ignored).

## Phase 1: Set up two materials

**Do**
1. Bring in the character mesh (demo: a head from the Blender asset pack,
   scaled up for the video).
2. Create two materials: a skin material for the character, and an
   outline material.
3. Make the outline material a black Emission shader.
4. Collapse or ignore any existing multi-res modifier.

**Check**
- Two materials exist, in order: skin first, outline second. The order
  matters because the Solidify material offset (Phase 2) counts from it.

**Why**
- The outline is a second material on a second shell, not a post effect:
  everything downstream depends on that separation.

## Phase 2: Grow the shell with Solidify (flipped)

**Do**
1. Add a Solidify modifier.
2. Under Normals, click Flip: this flips the thickness, creating the
   outline shell.
3. Under Materials, set Material Offset to 1: this gives the outline
   material to the shell.

**Check**
- With the face orientation overlay on, the character looks inverted
  (the author jokes the character looks "very embarrassed"); turn face
  orientation off and switch to rendered preview (Cycles in the demo)
  to judge the real result.

**Why**
- Flip is the whole trick: flipped normals make the shell's faces
  backfacing from the camera, and backfacing is the signal the shader
  chain (Phase 3) keys on.

## Phase 3: Build the outline shader (Transparent + Backfacing mix)

**Do**
1. Open the shader editor and select the outline material.
2. Add a Transparent BSDF (author's warning: "not a translucent BSDF.
   That is something else").
3. Add a Mix Shader (author's warning: "not a mix color node, but a mix
   shader node. It mixes two shaders").
4. Plug the Emission shader and the Transparent BSDF into the Mix Shader.
5. Add a Geometry node and plug its Backfacing output into the Mix
   Shader's factor.

**Check**
- The flipped faces from the Solidify modifier create the mix between
  the emission and transparent shaders. At this point, switching to
  Eevee "already kind of works," but Cycles does not yet show the
  outline: that is expected, not a failure (Phase 4 completes it).

**Why**
- Backfacing is the rim detector: where the shell faces away, the mix
  shows emission (the outline); where it faces the camera, it shows
  transparent (nothing). The shell's rim is exactly where that
  transition happens.

## Phase 4: Gate on camera rays (Cycles) and tune thickness

**Do**
1. Switch back to Cycles.
2. Duplicate the Mix Shader (Shift-D) and chain it: the first mix's
   output goes to the second mix's bottom input, the Transparent BSDF
   goes to the second mix's top input.
3. Add a Light Path node and plug Is Camera Ray into the second Mix
   Shader's factor.
4. Switch to material preview for faster feedback and adjust the
   Solidify thickness until it looks right; the author's example value
   is 0.003.
5. Turn on denoise in the render settings.
6. Turn on an HDRI with the Gaffer add-on for scene light.
7. In the Render tab under Film, set it to Transparent for a
   transparent background.

**Check**
- After the Is Camera Ray mix, "we have an outline." If the whole head
  is black, the noodles are plugged wrong: the author names this as
  the most common confusion ("some people, they have the shader set up
  like this and the entire head is black. So, it's really important
  here that you plug it in correctly").

**Why**
- Is Camera Ray restricts the outline to what the camera actually sees
  directly, which is why Cycles needs the second mix that Eevee does
  not: without it, indirect rays would paint the shell everywhere.

## Phase 5: Fix reflections, and check the two failure modes

**Do**
1. Test a mirror: set a mirror object to metallic with roughness 0.
   Observe: "there's no outline in the mirror."
2. Fix it: select the head and replace Is Camera Ray with Ray Length
   as the second mix's factor. The reflection now has an outline.
3. Check transparent shadows: "make sure transparent shadows is not
   turned off, but is turned on."

**Check**
- Mirror test before shipping: outline in the direct view AND in
  reflections, or the fix is not applied.
- Transparent shadows ON, noodles exactly as shown, and the method
  works in Eevee and in Cycles (author's closing claim).

**Why**
- Ray Length generalizes the camera-ray test to reflected rays: a ray
  that has traveled (reflected) still qualifies, so the outline
  survives the mirror. Transparent shadows ON is the second silent
  killer: without it, the shell's shadow logic fights the transparency.

## AAA studio practice

The inverted hull is the production method, not a Blender-only trick. Arc System Works' Guilty Gear Xrd team presented it at GDC 2015 as the "Back Method": the model is rendered once expanded and backface-reversed to produce the whole black contour, then rendered again at normal size, and the two are composited so only the contour survives where the expanded version extends past the silhouette. That is exactly this skill's Solidify Flip plus Material Offset shell, generalized to a two-pass renderer. The same GDC material names the failure mode this skill's Phase 5 fixes: when outlines are built on edited normals, the lines thin unintentionally, because the outline cannot be extruded along the edited normals, and subdivided surfaces recalculate normals outright. Arc's answer was to treat outline weight as a designed, per-character property, not a single global thickness, and to accept that each character costs individual tuning (the talk's often-quoted figure is four months per character, outline work included). The algorithm is also taught as the standard inverted-hull outline: duplicate geometry, extrude, flip normals, enable backface culling, so outlines become separate geometry sitting on top of the original.

- Source: https://www.gamedeveloper.com/art/see-i-guilty-gear-xrd-i-s-striking-2d-3d-art-deconstructed-at-gdc-2015 (GDC 2015: Arc System Works, "Guilty Gear Xrd's Art Style: The X Factor Between 2D and 3D")
- Source: https://topic.alibabacloud.com/a/quottranslationquot-nishikawa-quotexperiment-made-by-the-game-graphicsquotquotguilty-gear-xrd-font-colorredsignfont-quot-in-the_8_8_31556834.html (translation of the Xrd art talk: the Back Method, expanded black contour composited with the normal render)
- Source: https://www.scribd.com/document/743898396/GGXrd-AnimeStyleModelTips-pptx (Guilty Gear Xrd character modeling tips: inverted-hull outline thinning on edited/subdivided normals)
- Source: https://15362.courses.cs.cmu.edu/fall2025content/lectures/53_lec-s03/53_lec-s03_slides.pdf (CMU computer graphics lecture: inverted hull outline algorithm)

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Automate the thickness acceptance pass: render the character at three camera distances (close, mid, far) with the chosen Solidify thickness, and measure the outline's screen-space width in each. If the width collapses at distance (the Xrd thinning failure), raise the thickness or switch to a distance-scaled thickness before shipping the asset.
2. Automate the Phase 5 mirror test as a render pair, not a manual look: one render with a metallic roughness-0 mirror in frame, checking outline presence in both the direct view and the reflection, with Is Camera Ray versus Ray Length recorded as the factor used.
3. Automate the silent-killer checks as a settings audit before render: transparent shadows ON in the render settings, material order (skin first, outline second), Solidify Flip enabled, Material Offset 1. Any mismatch fails the audit before a frame renders.
4. Record the final thickness value per character in the asset notes, not as a global default: Arc's lesson is that outline weight is per-character tuning.

**Check**
- Outline width is stable across the three camera distances, or the distance-scaling fix is in place.
- The mirror render shows the outline in both direct view and reflection.
- The settings audit passes (transparent shadows, material order, Flip, offset) before render.
- Thickness is recorded per character.

**Why**
- The inverted hull's known production failure is not a broken shader but a thinning outline discovered late, in a shot where the camera moved. A three-distance render pass plus a settings audit catches both of this skill's failure modes (thinning, whole-head-black) before the asset reaches a scene.

## The human method, distilled

1. **Flip first, shade second**: Solidify Flip plus Material Offset 1
   is the setup; everything else is gating.
2. **Backfacing finds the rim; camera rays confirm it**: two mixes,
   two factors, in that order.
3. **The whole-head-black check**: if the head is black, a noodle is
   wrong, not the method.
4. **Mirrors need Ray Length**: Is Camera Ray alone drops reflections.
5. **Transparent shadows ON**: the setting that silently breaks it.

**Depth status:** FULL (142 caption segments + description; no frames
reviewed, no parameters beyond those the author states on camera).
Distinct from the existing `toon-2d-in-3d-dynamic-texture` skill, which
uses a dynamic texture driven by a target point, a different mechanism.
