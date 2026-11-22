---
name: godot-stylized-character-shader
description: "Build a stylized anime character shader in Godot 4: hand-paint the textures first, simplify light into base, shadows, ambient occlusion and highlights, modify mesh normals for faces, keep shadow softness adjustable, paint occlusion into the diffuse, and finish with iris emission, subtle SSS and an optional outline. Trigger when a 3D character needs an anime look in Godot, or when deciding whether the style lives in textures or in the shader."
---

# Godot Stylized Character Shader (Anime Look)

## Purpose

This skill reconstructs the exact workflow Fiery_Griffin (FancifulCrow)
shows in the "Recreating the Anime Look in Godot" devlog: paint the
textures first, then simplify the light into four controllable
components instead of simulating it physically. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The core method is: textures carry the style,
the shader controls the light, and every decision that affects the
look is adjustable rather than baked into geometry.

## Source

Creator: Fiery_Griffin / FancifulCrow. Post: "Showcasing my Stylized
Character Shader", https://www.reddit.com/r/godot/comments/1y11lmi/showcasing_my_stylized_character_shader/
(score 190, 43 comments, 25 retrieved). Devlog: "Recreating the Anime
Look in Godot", https://fancifulcrow.itch.io/charactershader/devlog/1791600/recreating-the-anime-look-in-godot
(published 2026-11-20). Audited in the 2026-11-21 scout run, audit 3.
Evidence: the full devlog text plus 25 comments, read firsthand. No
media download was used.

## Tools used

Godot 4, a spatial shader, hand-painted textures (Photoshop, Blender,
or Substance 3D Painter). Named in a comment for secondary motion, not
part of the shader: the Wiggle Bone addon for Godot 4, and Wiggle Bones
for Blender (bake jiggle into animations).

## When to use this skill

- A 3D character needs a 2D anime look in Godot 4.
- The shading looks wrong around the face and the normals are
  physically correct.
- Deciding whether to fix a stylized look in the textures or in the
  shader.
- Adding secondary motion without simulating it in the engine.

## Prerequisites

- A character model in Godot 4 with a spatial shader slot.
- Diffuse maps you are willing to hand-paint. Photographs and scans
  will not carry a stylized look; the author is explicit about this.
- A reference for the intended style (the author cites Zenless Zone
  Zero for painted shading and Marvel Rivals for rim lighting).

## Phase 1: Paint the textures before writing any shader

**Do**
1. Hand-paint the diffuse maps. "We have to resort to the good old,
   grueling process of hand-painting our textures."
2. Use Photoshop, Blender, or Substance 3D Painter to make and
   manipulate the diffuse maps.
3. Break realism deliberately: "rough painterly brushstrokes,
   simplified color patterns, exaggerated details, and deliberate
   imperfections".

**Check**
- Judge the texture before any shader exists. "Shaders alone cannot
  establish a cohesive art style. The underlying textures are what
  give our models much of their visual character." If the unshaded,
  textured model does not read as stylized, no shader will fix it.

**Why**
"Before implementing any shaders, one of the most essential aspects
of achieving a convincing stylized 3D aesthetic is making the right
textures." A photograph is a record of reality; a painted map is a
decision about style, and only decisions carry a look.

## Phase 2: Split the light into four components

**Do**
1. "Rather than aiming for physically accurate lighting, the goal is
   to simplify how light interacts with a character."
2. Break the lighting into four main components: Base, Shadows,
   Ambient Occlusion, Highlights.
3. Base first: "the overall lit appearance of the model, with its
   base color responding to the color and intensity of the light
   illuminating it, before any stylized shadows or additional
   lighting effects are applied."

**Check**
- Show each component separately (base only, then shadows, then AO,
  then specular, then rim), as the devlog does. Each layer must be
  visible on its own before the next one is added.

**Why**
"When drawing an object, artists often simplify lighting into a
small number of discrete tonal values rather than relying on
continuous gradients. This gives them more control over the subject's
final appearance." Four components are the control surface; physical
accuracy is not the goal.

## Phase 3: Fix the normals, then control the shadow transition

**Do**
1. Modify the mesh normals: "physically accurate normals can produce
   undesirable shadow patterns, especially around the faces. So
   artists often modify the mesh normals to produce more visually
   appealing lighting to follow the intended art direction."
2. Keep control over the sharpness of the lit-to-shadow transition:
   "these transitions can be either sharp and well-defined or soft
   and gradual. Having control over this transition allows us to
   achieve different shading styles without having to modify the
   underlying geometry or normals."
3. Expose shadow softness as an adjustable parameter in the shader.
   The author confirms this in a comment reply, after a commenter
   argued harder shadow edges would suit the model's hard outlines.

**Check**
- Compare bad normals vs good normals side by side, as the devlog
  does. Watch for the open defect a commenter reports: "the shadows
  seems to flicker a bit at some moments". That flicker is unresolved
  in the retrieved comments; do not ship past it without checking
  your own build for it.

**Why**
Normals are an art-direction input, not a physical fact: the face
must shade the way the drawing would shade it. A softness parameter
lets one shader serve styles that want hard edges and styles that
want soft ones, without touching geometry.

## Phase 4: Paint the occlusion in, do not simulate it

**Do**
1. Paint the dark regions directly into the diffuse texture: "it is
   better to paint these dark regions directly into the diffuse
   texture to preserve the intended character look."
2. Paint under the arms, between folds of pleated skirts, the belly
   button, and anywhere light has the hardest time reaching.
3. Use the reference: "Games such as Zenless Zone Zero make
   extensive use of painted shading and texture-based details."

**Check**
- The painted AO must be visible in the texture itself, not only in
  the render. The devlog image shows Remielle's hand-painted ambient
  occlusions on the model.

**Why**
Simulated AO follows the geometry; painted AO follows the intended
look. For a stylized character the intended look wins, and painting
it in guarantees it survives every lighting change.

## Phase 5: Split the highlights, then consider quantizing the light

**Do**
1. Divide highlights into specular highlights and rim lighting.
   Specular: "these reflections do not need to follow physically
   accurate behaviour. Instead, we want to be able to adjust and
   paint them." Rim: "a bright highlight along the silhouette of an
   object. This helps separate a character from the background and
   prevents the model from appearing too flat" (Marvel Rivals cited).
2. Consider, but do not assume you will implement, a script that
   "quantizes the light direction on the meshes into discrete
   angular intervals. This way, objects would only receive light
   from specific directions, skipping certain lighting transitions
   that you might not want." The author states this in a comment as
   considered, not implemented. Label it that way in your own notes.

**Check**
- Show specular added, then rim added, as separate steps. The
  quantization idea is a comment-level proposal; treat it as
  unbuilt until you build it.

**Why**
Splitting highlights gives two independent controls (paintable
specular, silhouette rim) instead of one physical reflection model.
Quantizing light direction would be the next control: discrete
directions instead of continuous ones, matching the discrete-tonal-
values principle from Phase 2.

## Phase 6: Finish with emission, SSS, and an optional outline

**Do**
1. Add emission to the irises: "many anime characters in media have
   slightly glowing irises, as they are usually a major focal point
   of the face. We can easily add an emission to our material to
   achieve the effect."
2. Experiment with subsurface scattering: "Even in stylized 3D
   artwork, a subtle amount of subsurface scattering can make a
   noticeable difference, though we should be careful not to overdo
   it."
3. "If you want to go even further, you could try adding an outline
   shader to give a more 2D look to characters."

**Check**
- Judge the finishing touches by eye on the final render, after the
  four lighting components are in place. An iris glow on top of
  wrong shadows reads as a light stuck to the face, not as anime.

**Why**
Finishing touches depend on the lighting being right. They are last
because they amplify whatever the lighting already says.

## Secondary motion: use an addon, do not rebuild the physics

**Do**
1. For jiggle/secondary motion, use the Wiggle Bone addon for
   Godot 4, or bake it in Blender with Wiggle Bones. The author, asked
   about replicating physics: "I don't have any long-term plans to
   replicate their physics. There's a pretty good Wiggle Bone addon
   for Godot 4. Alternatively, you could bake the jiggle into the
   animations themselves rather than simulate it in real time."

**Check**
- The addon or the baked animation must be chosen before the shader
  is finished, so the shader is not asked to carry motion it cannot.

**Why**
Secondary motion is a solved addon problem. Rebuilding it inside a
look-dev shader would couple two unrelated systems.

## Failure modes

- **Shadows flicker.** Reported by a commenter, unresolved in the
  thread. Check your build for flicker before calling the shader
  done; the devlog does not give a fix.
- **Soft shadows on a hard-outlined model.** A commenter argues the
  soft shadows make the model look doll-like against its hard
  textures and outlines. The author's answer is the adjustable
  softness parameter; use it, and judge against the model's own
  outlines, not in isolation.
- **Shader-first, textures-later.** If the look fails, the fix is
  almost always in the painted maps (Phase 1), not in more shader
  code. Re-check the textures before adding shader features.

## AAA studio practice

Arc System Works built Guilty Gear Xrd the same way this skill does, and
in one respect the opposite way. The Xrd team adjusted vertex normals
by hand to simplify shading while keeping the full 40,000-polygon
character shape, because unedited normals produced complex shading
that matched the polygons instead of the cel look they wanted. Face
normals were adjusted vertex by vertex to produce simplified,
intentional shading, shading thresholds were controlled with vertex
colors, and outlines used the inverted-hull method with separate
normals for the hull and for shading. The team also used two textures
per surface, a base texture for lit areas and a tint texture for
shaded areas, rather than painting all the shading into one diffuse
map. Their stated tenet, from technical artist Junya C. Motomura's
GDC 2015 talk, is that handcrafting beat calculation: every visual
element had to be an intentional choice, not a mere calculation
outcome. Sources: Polygon, "See how Guilty Gear Xrd's gorgeous 3D
cel-shaded look was created",
https://www.polygon.com/2015/5/26/8663003/guilty-gear-xrd-cel-shading-making-of ;
Arc System Works design documents (4Gamer/CGWORLD translations),
https://archive.org/stream/GGXrd-design-docs/4Gamer%20-%20The%20Secrets%20of%20GGXrd%27s%20Graphics_djvu.txt

Tango Gameworks went further in the other direction for Hi-Fi Rush:
instead of a per-character shader, the whole game, characters and
environment, runs through a deferred toon renderer in Unreal Engine 4,
with customized and added render passes combined in post-process
volumes, at 60 FPS at native resolution. The team kept modern lighting
features (deferred lights, volumetric fog, ambient occlusion, global
illumination, real-time reflections, bloom) but stylized each one
into the 2D look, including a dedicated toon face-shadow
implementation, a comic shader, and toon light and shadow passes.
Director John Johanas set three style keywords, "Colorful", "Sharp",
and "Clean", and asked for no color gradations and nothing that would
feel 3D. Sources: 80 Level, "The Making Of Hi-Fi Rush's 3D Toon
Rendering Style",
https://80.lv/articles/the-making-of-hi-fi-rush-s-3d-toon-rendering-style ;
Unreal Engine, "Inside the creation of Tango Gameworks surprise hit",
https://www.unrealengine.com/developer-interviews/hi-fi-rush-was-inspired-by-shaun-of-the-dead-and-futurama?lang=es-ES

Two differences from the AAA pattern, stated plainly. First, Xrd
carried the style in vertex properties (normals, vertex colors),
which are resolution independent, and in a separate tint texture;
this skill carries it in hand-painted diffuse maps and painted AO,
which is the author's stated method, not Xrd's. Second, Hi-Fi Rush
is a renderer-level decision for a whole game, not a single
character shader; do not present this skill's spatial shader as the
Hi-Fi Rush approach. No technical source was found for HoYoverse's
Zenless Zone Zero shading (cited in this skill only as the author's
reference for painted shading), so no HoYoverse practice is claimed
here.

### Agent automation

- **Normal-edit record.** For every mesh whose normals are modified
  in Phase 3, record the mesh, the region edited (face first), and
  a before/after render pair from the same camera and light, saved
  with the record. A normal edit with no render pair is not
  finished. (Grounded in Xrd's handcrafted face normals; the
  record format is this skill's own gate.)
- **Component-isolation renders.** Render the character once per
  component from Phase 2 (base only, shadows only, AO only,
  specular only, rim only) from one fixed camera, and keep the
  five renders with the shader parameters used. A component that
  cannot be shown alone has not been isolated. (Grounded in the
  devlog's own separate-component presentation and in Hi-Fi Rush's
  separate toon passes.)
- **Shadow-softness sweep.** Record the shadow-softness parameter
  values tried, with one render per value at the same camera, and
  the chosen value with the reason (hard outline versus soft
  look). Keep the sweep; the flicker defect in the Failure modes
  section is checked against the sweep renders, not by memory.
  (Grounded in the author's adjustable-softness answer; the sweep
  itself is this skill's own gate.)
- **Flicker probe.** Before calling the shader done, capture a
  short frame sequence while the light or camera moves slowly and
  diff consecutive frames outside the moving shadow edge. Any
  flicker in a static region fails the probe. The probe is a
  check, not a fix; the devlog gives no fix, and none is invented
  here. (Agent-designed check, labeled as such; grounded in the
  reported flicker defect.)

## The human method, distilled

1. Textures first: hand-painted maps carry the style; the shader
   cannot establish it alone.
2. Simplify light into four controllable components; do not simulate
   it physically.
3. Normals are art direction: modify them until the face shades the
   way the drawing would.
4. Paint occlusion in; do not compute what the look already decided.
5. Keep the controls adjustable (shadow softness) and the unbuilt
   ideas labeled (quantized light direction, considered only).
6. Secondary motion is someone else's addon; do not rebuild it.

## Depth status

FULL for the method: the devlog text was read in full plus 25
comments; tools, principles, and quoted decisions are all disclosed.
Caveat: no shader code is published in the devlog, and the project
download link in the post was truncated and is unverified, so the
shader itself cannot be reproduced from this skill alone.
