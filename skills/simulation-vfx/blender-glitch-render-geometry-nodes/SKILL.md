---
name: blender-glitch-render-geometry-nodes
description: "Build a glitch render in Blender 5.3 from a cube and a floor: one noise texture driving roughness and normal strength for puddles, a Layer Weight emissive shader driven by a glitch texture for color and a TV test image for alpha, Geometry Nodes scatter with noise-driven Set Position, one linked node system varied per object with a Store Named Attribute, an extruded transparent shell above 1.0 for glow, and a rotated-cube volume gradient. Trigger when a chaotic VFX scene must stay understandable, or when one shader must vary per object without being copied."
---

# Blender Glitch Render with Geometry Nodes (Max Hay)

## Purpose

This skill reconstructs the exact workflow Max Hay shows in "Creating
a Glitch Render in Blender 5.3": start from a cube and a floor, drive
everything from two textures (one for color, one for alpha), and vary
one shader per object with a stored Geometry Nodes attribute instead
of copying the shader fifty times. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: vibe first, details second; one
shader, many objects; and the two methods the author tried and
abandoned are recorded as failure modes, not as steps.

## Source

Creator: Max Hay. Video: "Creating a Glitch Render in Blender 5.3",
https://www.youtube.com/watch?v=ILR4joGRS6U (17:36, 5,686 views,
uploaded 2026-11-21). Course: https://www.maxhayart.com/cyber-environments-course.
Audited in the 2026-11-21 scout run, audit 7. Evidence: the full ASR
captions (523 segments) plus the description, read firsthand. No
media download was used. The course project files were not retrieved.

## Tools used

Blender 5.3, Geometry Nodes, shader editor (Layer Weight, ColorRamp,
Mix, Transparent, Emission, Volume), Poly Haven textures, Wikipedia
Commons textures (motherboard, glitch, dragonfly diagram, fractal),
Claude (AI texture search, Phase 5), Photoshop (touch-ups), compositor
bloom.

## When to use this skill

- A chaotic, glitchy VFX scene that must stay visually understandable.
- One shader must produce many per-object variations without being
  duplicated.
- Scattering text or objects outward from a center with a
  noise-driven distribution.
- Sourcing real, licensed textures with AI search instead of AI
  generation.

## Prerequisites

- Blender 5.3 (the video's version; the node setup is not
  version-gated in the captions beyond that).
- Two texture sources: a floor texture (Poly Haven in the video) and
  glitch/computer textures (Wikipedia Commons, Unsplash in the
  video), plus a TV RGB test-color image for the cube color.
- A black cube to sit underneath the transparent glitch cube.

## Phase 1: Make the floor read as puddles with one noise texture

**Do**
1. Start "just a floor plane and just a basic texture setup... just a
   texture from Polyhaven. You can use whatever source you want."
2. Run "a noise texture just running into the roughness, but more
   importantly, that same noise pattern runs into the normal map
   strength input."

**Check**
- "This creates areas of high and low normal map strength as well as
  high and low roughness in the same areas. So, it looks like
  puddles on the ground." If the wet areas and the bumpy areas do
  not coincide, the same noise pattern is not driving both inputs.

**Why**
One noise pattern driving two inputs in the same places is what makes
the puddle read: roughness and normal strength agree, so wet and dry
areas are the same areas, not two competing patterns.

## Phase 2: Build the cube shader from a glitch texture plus Layer Weight

**Do**
1. Load a cube with "basic computer textures, some glitch textures.
   So, one of them is just a motherboard and one of them is like a
   glitch just texture from... Wikipedia Commons... one of this
   one's probably from Unsplash."
2. "Using that image texture to drive the alpha and emission color...
   a good base for whatever else comes after that to make some kind
   of like cool techy look."
3. Drive the alpha with the glitch image through a ColorRamp "just
   with a bit more contrast", over a black cube underneath, "so you
   can see through into that".
4. Mix in a Layer Weight node with the ColorRamp adjustment, combined
   with the underlying computer texture "just with a mix color node
   set to multiply".
5. Drive the color with the TV RGB test-color image: "that's actually
   driving just the full color and that's pretty much it."

**Check**
- The viewing angle must change the read: "it is going to be brighter
  on the edges here. And when you look at it head-on, it's going to
  go dark." If the angle does not change the alpha, the Layer Weight
  wiring is wrong.

**Why**
The shader is two textures with two jobs: the glitch texture decides
where you can see through, the TV test image decides what color you
see. Layer Weight makes the transparency view-dependent, so the cube
glows at its edges and goes dark head-on, which is the glitch read.

## Phase 3: Record the two abandoned methods as failure modes

**Do**
1. Do NOT use the UV-map named-attribute image method for this scene:
   the author tried running "the UV map as a named attribute UV map
   run that straight into the image texture in geometry nodes" to
   drive selections on instances, "didn't really go too well and I
   didn't end up using that method in this one here."
2. Do NOT use the screenshot-outliner-to-AI scatter method: the
   author screenshotted the outliner's object list from an older
   project, pasted it into an AI to convert the image to text, and
   tried to scatter one instance per line. "This actually didn't end
   up going the way I wanted... I couldn't really make that work too
   well here... I kind of got sidetracked with trying to figure out
   a system to like get each line to be its own instance."

**Check**
- Both methods are named in the captions as tried and dropped. Do
  not re-try them as if they were the workflow.

**Why**
The author experiments in the open and drops what does not work; the
finished render is not evidence that every method shown in the video
worked. The two drops share a cause: both tried to drive Geometry
Nodes from a text/image list, and neither produced one clean instance
per item.

## Phase 4: Scatter characters with noise-driven Set Position

**Do**
1. Write out the characters "cube" and "x, y, and z" as individual
   letters and scatter them over the cube.
2. "Use a noise texture to drive a set position so it kind of like
   randomly explodes outwards from the cube."
3. Switch fonts and center the text ("trying to get that all
   centered").
4. Feed a glitch texture into the emissive shader on the text, box
   projected: "I've been using that a lot more since in geometry
   nodes you don't really UV maps are kind of hard. So, it's just
   easier to box project everything sometimes."

**Check**
- The scatter must read as "a mess of distributed floating exploding
  out text... expanding outwards in a scattered way from the cube",
  with "random variables and stuff", not as a neat grid. The "weird
  science textbook aesthetic" is the stated vibe check.

**Why**
Noise-driven Set Position is the scatter: one texture, one node,
random outward offsets, no per-letter hand placement. Box projection
is the texture shortcut for Geometry Nodes instances, where UVs are
hard; it trades UV precision for zero setup.

## Phase 5: Pick the dominant color, keep the composition conventional

**Do**
1. "Get the overall vibe like mapped out and figured out before I go
   too crazy into like the individual details of any one object...
   if the rest of the setting looks nice, I know I can make the
   central focal point good fairly easily after that. But if
   everything else is looking trash, it's really hard to make
   anything look good at all."
2. Skew the rainbow TV-test colors toward green: "picking a dominant
   color for the scene is really... even you can use all sorts of
   colors around that, but if you have the dominant color where like
   the majority of the light is like one kind of like one color,
   that'll help a lot with balancing things out."
3. Keep conventional composition rules even in a chaotic render:
   "trying to get even if we're going to do something glitchy and
   crazy, we still want to follow the conventional rules as much as
   we can to try and make it look good in terms of how the
   composition and the colors are."
4. Source real textures with AI search, not AI generation: "I've
   actually been getting the like Claude the AI to like go through
   [Wikipedia Commons] for me and like pick out images that I'm
   specifically looking for with a certain vibe... find... images
   that match when the license that I can use like CC0 images and
   two the basic aesthetic... I don't want to just use an AI
   generated texture here so much. So, if you can use the AI to just
   find real textures, that's kind of I feel like a better use of
   it. Just it's more just like a really targeted search."

**Check**
- The scene must stay "visually understandable" even at maximum
  chaos. Cut detail in the middle when it becomes "a big mess of
  just too much detail... a little bit hard to even understand
  visually what's going on".

**Why**
A dominant color is the balancing mechanism for a rainbow texture:
one color carries most of the light, the rest are accents. AI as a
targeted search for licensed real textures keeps the texture sources
real and licensed, which AI generation would not guarantee.

## Phase 6: Glow with an extruded transparent shell, and grade the volume

**Do**
1. Use one linked Geometry Nodes system on every object ("these all
   every single object here has the same geometry node system linked
   together on it").
2. In that system, extrude the geometry and set the extrusion's
   material to a transparent shader "which has a value a little bit
   higher than one, so that any light going through it actually gets
   brighter", creating the glow. Layered over the Layer Weight
   shader underneath, "the angle you view it at will give you
   different values... the main strength is already like brighter on
   edges that are facing away from the camera", so the outside glows
   while interacting with the light shining down.
3. For the volume gradient: "get a cube, rotate it 90 degrees on the
   Y-axis, and then you just plug a gradient texture straight into
   the volume emission strength, and you can use a map range to
   control it, and then you'll have an upwards gradient... Turn the
   volume to zero and just use the emission only."

**Check**
- The extrusion glow must brighten light passing through it (value
  above 1.0), not just tint it. The volume gradient must read as an
  upwards emissive gradient, "a little video gamey, but it is kind
  of cool sometimes to throw that in" subtly.

**Why**
An extruded shell with a >1.0 transparent shader is a cheap glow:
no bloom pass, no extra light, just a shell that brightens what
passes through it. The rotated-cube gradient is the same idea for
volume: orientation plus a gradient texture, no simulation.

## Phase 7: Vary one shader per object with a stored attribute, then scatter like grass

**Do**
1. In Geometry Nodes, "storing a value in geometry nodes with a store
   named attribute. And then I can actually just change the location
   and rotation by hooking that value up to the shader editor with
   an attribute there. And that controls the shader group... so I
   can control the location and scale on the mapping node per object
   with the geometry nodes store named attribute."
2. Store different values per object "while keeping the shader the
   same between all of them... you want a bunch of variations of like
   the same texture without like 50 different copies of it."
3. Make clusters of cubes with the same Geometry Nodes system (glitch
   texture, transparent outer layer, floating variables), scatter
   them on the ground, and weight-paint the scatter "just trying to
   get it to feel natural and nice, like it's as if it's kind of
   like a plant almost... clusters of grass were growing somewhere...
   where it would naturally accumulate."
4. Duplicate the cube into pillars, change the one that reads too
   much like Ethereum, and keep the layout borrowed from a familiar
   structure: "big important thing in the middle with a bunch of
   pillars... heavenly lighting coming from the top as you might see
   in a church... taking the composition or layout of something
   that's very well known... and turning it into something that's
   completely different."
5. Keep one separated copy of the Geometry Nodes system for the
   "glitch mountains" background piece, tuned less intense and
   greener, so it sits in the background instead of competing.
6. Keep an accident: one frame where a disconnection turned
   everything black "actually looked really cool. So, I ended up
   toning down the emission strength... getting more shifting it more
   towards that vibe of like really dark black facing on that
   Fresnel-like Layer Weight node... a little more contrast... dark
   energy type vibe."

**Check**
- Per-object variation must come from the stored attribute, not from
  duplicated shaders: one shader, many mapping values. The scatter
  must accumulate like grass, not tile like a grid.

**Why**
A stored attribute is the per-object control surface: Geometry Nodes
writes the value, the shader reads it, and one shader serves every
object. Scattering like grass (weight-painted accumulation) makes
even glitch cubes read as a natural distribution, which is why the
scene feels placed instead of random.

## Phase 8: Finish in Photoshop and the compositor

**Do**
1. "Just did a quick run through of Photoshop. Usual touch-ups of
   like just a little bit of contrast, clarity, sharpening, and
   saturation, grain, uh bloom in the compositor as usual in in
   Blender. And then that's pretty much it."

**Check**
- The final render is the check; no render settings, sample counts,
  or compositor node values are stated in the captions. Do not invent
  them.

**Why**
Finishing is a fixed, small routine (contrast, clarity, sharpening,
saturation, grain, bloom) applied after the scene is done, not a
second build pass.

## Failure modes

- **Too much detail in the middle.** The center becomes unreadable.
  Cut detail until the scene is visually understandable again; chaos
  is not a substitute for composition.
- **No dominant color.** A rainbow texture with no dominant color
  reads as noise. Skew toward one dominant color (green in the
  video) and let the rest be accents.
- **Fifty copies of one shader.** Duplicating the shader per object
  is the failure the stored attribute exists to prevent. One shader,
  one stored attribute, many values.
- **UVs in Geometry Nodes.** UV maps are hard inside Geometry Nodes
  in this workflow. Box-project the texture instead, and do not
  spend the session fighting UVs on instances.
- **Re-trying the dropped methods.** The UV-attribute image method
  and the outliner-screenshot scatter both failed on camera. Record
  them as dropped; do not present them as alternatives.

## Production practice

No AAA game-studio source was found for a glitch render, for
Geometry Nodes in production, or for this video's specific
technique, so no AAA claim is made here. What was found is the
older, cross-DCC pattern this skill's stored attribute belongs to:
per-point or per-instance attributes driving shader variation from
one shared material, documented by the vendors whose tools ship it.

SideFX documents the pattern for Houdini scattering: write
attributes such as `orient` and `pscale` to scatter points to
control instances and their shaders, randomize custom attributes
such as `hue` and `saturation` over the points, then read those
attributes out and connect them to the material. Its worked
example keeps color variation subtle on purpose (hue randomized
between 0.9 and 1.1, saturation between 0.7 and 1.0, since 0
would be grayscale), separates the scatter-point stream from the
terrain stream so attributes do not falsify the terrain, and
deletes unneeded attributes afterward to save render resources.
Source: SideFX, "Scattering: Attributes",
http://www.sidefx.com/docs/houdini/heightfields/scatterattribs.html

The same one-material, many-variations rule appears in Unreal
Engine practice: a material uses the PerInstanceCustomData node
and each foliage instance carries its own custom-data value, so
one material can fade or change per instance instead of assigning
a unique dynamic material per instance, which the engine does not
support for foliage (all instances of a foliage type share the
material). Sources: Epic Developer Community Forums, "Micro-tutorial:
Per instance foliage logic/effects using per instance custom data",
https://forums.unrealengine.com/t/micro-tutorial-per-instance-foliage-logic-effects-using-per-instance-custom-data/604191 ;
"Assign unique dynamic material for every single foliage instance",
https://forums.unrealengine.com/t/assign-unique-dynamic-material-for-every-single-foliage-instance-and-modify-them-independently-at-runtime/2077810
(Both are community tutorials on Epic's forum, not Epic studio
practice, and are labeled as such.)

Blender's own manual states the mechanism this skill relies on:
the Attribute node retrieves attributes attached to an object or
mesh, with values varying per vertex, and Object and Instancer
modes look the attribute up per object. Source: Blender Manual,
"Attribute Node",
https://docs.blender.org/manual/en/2.93/render/shader_nodes/input/attribute.html
(The manual page is the 2.93 version; the attribute mechanism is
the one the 5.3 workflow uses, and the version difference is
noted rather than hidden.)

Two differences from the production pattern, stated plainly.
First, Houdini and Unreal vary attributes per scatter point or
per instance; this skill stores one attribute value per object
and drives the shader's mapping node, which is the Blender
object-level analogue, not the same domain. Second, the
Far Cry 5 point-cloud export story (Ubisoft feeding the engine
PNG files and point clouds with attributes per biome) appears
only as a SideFX forum report, not as a verified studio source,
so it is not cited as evidence here.

### Agent automation

- **Attribute manifest.** For every object using the linked
  Geometry Nodes system, record the attribute name, its domain
  and type, the value stored per object, and the shader node
  that reads it. Gate: every object in the set has an entry,
  and the material count for the set is one. A second material
  with the same node tree is a duplicated shader, not a
  variation. (Grounded in the SideFX attribute pattern and the
  Unreal one-material rule; the manifest format is this skill's
  own gate.)
- **Variation sweep.** Render the same object at three stored
  attribute values (low, middle, high) from one fixed camera
  and keep the three renders with the manifest. A value range
  that produces no visible change, or that breaks the read,
  is narrowed before the scene is scattered. (Agent-designed
  check, labeled as such; grounded in SideFX's narrow-range
  hue/saturation example.)
- **Scatter accumulation check.** After weight-paint scattering,
  record the scatter count and check the distribution reads as
  accumulation (denser where painted, sparse elsewhere) rather
  than a grid, from a top-down viewport capture kept with the
  manifest. (Grounded in Phase 7's grass-accumulation rule;
  the capture is this skill's own gate.)
- **Dominant-color sample.** Sample the finished render's
  pixels and record the dominant hue share against the other
  hues, to check Phase 5's dominant-color rule with a number
  instead of only by eye. The target share is recorded per
  scene, not assumed. (Agent-designed check, labeled as such.)

## The human method, distilled

1. Vibe first, details second: map the overall scene before
   detailing any one object.
2. Two textures, two jobs: one drives color, one drives alpha.
3. One shader, many objects: vary it with a stored attribute, do not
   copy it.
4. Name the drops: the UV-attribute method and the outliner-scatter
   method did not work, and the record should say so.
5. Keep chaos understandable: dominant color, conventional
   composition, and a cut when the middle gets too dense to read.
6. AI finds real textures; it does not generate them here.
7. Keep the accident when it looks better: the black frame became
   the darker, higher-contrast direction.

## Depth status

FULL: 523 ASR caption segments plus the description; node types,
wiring, values above 1.0, the 90-degree rotation, and both abandoned
methods are in the captions. Caveat: no render settings or sample
counts are stated, and the course project files were not retrieved.
