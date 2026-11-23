---
name: instanced-ground-cover-flower-fields
description: "Build Before the Sun Sets-style ground cover in Godot 4: one low-poly flower model GPU-instanced by the thousand, crossed alpha-masked grass planes with a fixed world normal, vertex-shader wind, and the pixelation, dither, and cel-shading look stack, from the creator's own comment replies. Trigger when a game needs dense flower fields and grass that read at distance without per-plant cost."
---

# Instanced Ground Cover: Flower Fields and Crossed-Plane Grass

## Purpose

This skill reconstructs the ground-cover system behind the game Before
the Sun Sets from the creator's own comment replies plus his showcase
reels, then builds the Godot 4 equivalent, step by step, so another
agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The core method is: one cheap model
instanced by the thousand, crossed masked planes for grass with one
fixed normal so the light never changes per plane, wind done once in
the vertex shader, and the whole picture finished with a three-part
retro look stack (pixelation, dithering, cel shading).

The creator's evidence is thin: three one-line comment replies and
showcase footage, no tutorial, no code, no editor walkthrough. The
Godot construction in Phases 1 to 6 is refinement research, labeled
as such wherever it goes beyond what he said. Nothing in this skill
presents the Godot code as his code. His engine is Unreal; the
transfer to Godot is the work this skill does.

## Source

Creator: beforethesunsets44 (BeforeTheSunSets), game Before the Sun
Sets (Steam wishlist page, PC first). All five creator statements
below were verified verbatim in the raw comment JSON fetched via
`instagram-cli fetch-post-comments` (first page only, 50 comments
per reel; coverage noted per reel in the batch reports).

Comment evidence (quoted exactly, spelling as written):

- Grass recipe, on reel DbLzj42BD_X ("Castle in Flower Field",
  2026-07-24, https://www.instagram.com/reel/DbLzj42BD_X/, 32 of 40
  comments read), answering Αλεξ Νικο's "How'd u do the grass":
  BeforeTheSunSets: "@alexneeku perpendicular planes, masked grass
  texture on each plane, set the normal to x,0 /y,0 /z,1".
- Flower method, on reel Dan0ZPDBUMk ("does this look like dark
  fantasy to you?", 2026-07-10,
  https://www.instagram.com/reel/Dan0ZPDBUMk/, 18 of 20 comments
  read), answering Subclidean's "how you made the flowers/grass":
  BeforeTheSunSets: "thank you! I made a low poly model of the
  flower and used gpu instansing to add a lot of them in the scene".
  Same thread, his design line: "@octoberfault fun>>realism". A
  viewer in the same thread confirms the flowers visibly sway in
  the wind ("the flowers swaying in the wind is so beautiful dude").
- Look stack, on reel Db6J1Mfh21y ("Beat the knight before he beats
  you..", 2026-08-11, https://www.instagram.com/reel/Db6J1Mfh21y/,
  50 of 203 comments read), answering a look question:
  BeforeTheSunSets: "im using ixelating, dithering, and cellshading
  shaders." ("ixelating" is his spelling of pixelating.)
- Pixelated look, on reel DdzVuyghkaQ (2026-09-27,
  https://www.instagram.com/reel/DdzVuyghkaQ/, 38 comments read),
  answering seyit's "How did u give this pixelated appearance to
  your game": BeforeTheSunSets: "shaders and low resolution."
- Same answer, on reel DdUQSfgBgc6 (2026-09-15,
  https://www.instagram.com/reel/DdUQSfgBgc6/, 50 comments read):
  BeforeTheSunSets: "low resolution and shaders!"

Reel evidence (showcase footage, 12 frames each read firsthand,
music only, no narration; summaries under
`~/workspace/custom-skills/local-video-summarizer/work/bts-<shortcode>/`):

- Deubd_sIn2Z ("With vs without flowers..", 2026-10-20,
  https://www.instagram.com/reel/Deubd_sIn2Z/): a locked split-screen
  walk, bare ground on top, flower-dressed ground below. Shows
  placement: dense colour-coded patches (pink spikes, pink carpets,
  white beds, yellow carpets) along paths, at rock bases, and on
  slopes, not evenly spread. Does not show how the flowers are
  placed; the comment above answers that.
- DbLzj42BD_X: a near-static vista of a yellow flower field and a
  white castle. The field reads as dense instanced scatter; no
  combat, no UI, nothing mechanical.
- Dan0ZPDBUMk: a one-hue purple night vista (flower field, castle,
  sword blade at frame edge) with one scripted event, a dragon
  silhouette crossing the sky. The compositional recipe, not a
  technique demo.
- Db6J1Mfh21y: tall pink foxglove flowers hiding a knight until
  close range. The concealment read is the only transferable
  observation; the promised fight is not visible in the sampled
  frames.

Second source (expansion, 2026-11-22): memoryfloater, a Unity
solo dev working on foliage, crowds, and performance. All quotes
below were verified verbatim in the raw comment JSON fetched via
`instagram-cli fetch-post-comments` (first page only, 50 comments
per reel). Reel summaries live under
`~/workspace/custom-skills/local-video-summarizer/work/memoryfloater-<shortcode>/`.

Comment evidence (quoted exactly, spelling as written):

- Hash grow/cull rule, on reel DgAFMl4o27h ("I have some flowers
  for everyone!", 2026-11-21,
  https://www.instagram.com/reel/DgAFMl4o27h/, 50 of 64 comments
  read), answering dhewachmad: memoryfloater: "@dhewachmad the
  shader decides. Every instance id goes through a hash. This
  provides a stable random number per instance which I use to
  decide which ones go and which ones stay. With that it’s always
  the same flowers that grow and cull."
- Pop hiding, same reel, answering jamaliticus: memoryfloater:
  "@jamaliticus it’s not perfectly tuned here but the pop
  disappears when you have some grass texture underneath the
  flowers and set the thinning start distance properly." He adds
  that with the right grow/shrink distribution, growing plants
  hide shrinking ones as the camera zooms out.
- Wind and the patch alternative, same reel, answering
  mrbunnysky: memoryfloater: "@mrbunnysky they already are wind
  reactive and distance based reduction renders faster than
  switching to a patch plus has zero visual pop. Aligning a color
  patch is harder to align and doesn’t allow you to freely mix
  different flowers inside a patch."
- Bleed tool, same reel, answering cynomanic: memoryfloater: "I
  use GIMP, if something is missing I just add it myself. ... You
  could also use AI to generate a script that bleeds your
  textures directly."
- Far-field noise rationale, on reel DfRsg8eIRya ("Far away,
  foliage is just noise", 2026-11-03,
  https://www.instagram.com/reel/DfRsg8eIRya/, 7 of 7 comments
  read), answering inzlps: memoryfloater: "a single flower
  renders to a single pixel (or maybe even less). ... foliage
  technically (depending on distance) is just a noise pattern and
  I could just render that noise pattern itself instead of the
  actual geometry. It’s still experimental though, and finding
  the right values is a pain". On grass: "Haven’t tried it yet
  though. So basically: the grass will also be noise, that’s why
  it should work."

Reel evidence (12 frames each read firsthand; summaries as above):

- DgAFMl4o27h: distance flower-field technique, narrated:
  scale flowers up with distance while thinning the count (one
  shot shows 3.0% drawn), colour-bleed the texture so sampling
  outside the shape returns colour instead of black, and drive
  mip bias plus alpha cutoff from camera distance with on-screen
  shader pseudocode. No parameter values, distances, or
  performance numbers in the video; the selection rule is the
  hash comment above.
- DfMjBGcIPOB ("Every flower is just 6 triangles.", 2026-11-01,
  https://www.instagram.com/reel/DfMjBGcIPOB/, silent showcase):
  the 3-quad cage, two crossed vertical planes plus one
  horizontal head plane, demonstrated across eight species. No
  creator replies in the fetched comments; the overdraw
  counter-argument in the expansion section is viewer material,
  labeled as such.
- DfU1Xt9oNqu ("My improved flower making process in Blender.",
  2026-11-04, https://www.instagram.com/reel/DfU1Xt9oNqu/):
  captioned 5-step process: stem alignment with 2 loop cuts,
  top-view alignment, and shrinking the geometry to the visible
  texture space to cut alpha overdraw. Step 1's caption was not
  captured in the sampled frames and is not reconstructed here.

## Related skills (read before building)

- `procgen-worlds/godot-grass-lod-wind`: the deep grass skill. It
  covers per-blade LOD chains (13/9/5/3 verts with geomorphing),
  travelling gusts, rank-based density falloff, and the carpet
  layer. This skill does NOT repeat that depth. If the field needs
  per-blade LOD, build on that skill; if it needs the crossed-plane
  recipe, the fixed normal, and the look stack, build here. The
  wind in Phase 4 is deliberately the simpler shared-noise version,
  not the LOD-chain version.
- `procgen-worlds/ue-grass-cards-lod`: the same crossed-card idea
  in Unreal (two crossed cards, rotated crosses for volume, LOD
  swap). Useful if the target is Unreal; the card construction
  agrees with the creator's recipe, the engine does not transfer.
- `simulation-vfx/ue-wind-shader-grass`: wind shaders for grass in
  Unreal, the follow-up to the cards skill.
- `characters/godot-stylized-character-shader`: the cel-shading
  treatment for characters (painted textures, four-part light,
  face-normal editing). Phase 5 here covers the environment-side
  ramp only; characters go there.
- `simulation-vfx/godot-silk-vfx-vector-pixelation`: a 2D pixelation
  shader for VFX. Different domain (2D effects), same pixelation
  instinct; do not confuse its canvas-item shader with the 3D
  routes in Phase 5.

## Tools used

Godot 4.x (Forward+ for the look stack; the construction also runs
under Compatibility with the blending caveat in Phase 5); Blender
for the low-poly flower model and the crossed grass planes; one
spatial shader for grass, one for the flower sway; one screen-space
canvas-item shader OR one low-resolution viewport for pixelation
(Phase 5, pick one route).

## Phase 1: Model one flower, not a field

**Do**
1. Model a single low-poly flower: a short stem, a few petals, one
   flower head. The creator's words are "a low poly model of the
   flower". Keep the triangle count in the tens, not the hundreds:
   the model is drawn thousands of times, so every triangle is
   multiplied by the instance count.
2. Build colour variation into the model, not into separate models.
   One mesh, with vertex colours or a small texture atlas for petal
   colours (pink, white, yellow are the palettes in the split-screen
   reel). Per-instance colour (Phase 2) picks the palette per
   instance.
3. Give the flower a real 3D shape, not a flat card. The flowers
   are the near-field dressing the camera walks through; flat cards
   read as paper at close range. The grass planes in Phase 3 are
   the flat ones. Do not mix the two jobs.
4. Keep the flower's origin at ground level (base of the stem).
   Every placement transform in Phase 2 assumes the origin sits on
   the ground.

**Check**
- One flower alone, untextured, reads as a flower at the game's
  camera distance. If it needs its texture to read, it is too
  simple; if it needs more than a glance to read, it is too
  expensive.
- The flower's bounds are tight: no stray vertices far from the
  stem, or the instance culling bounds in Phase 6 lie.

**Why**
Instancing multiplies one mesh. The whole field's cost is one
model's cost times the instance count plus one draw call, so the
model budget is the field budget. One model with per-instance
colour is what makes "a lot of them in the scene" affordable.

## Phase 2: Instance it with MultiMesh, in chunks

**Do**
1. Create a `MultiMeshInstance3D` per chunk of ground, not one for
   the whole map. All instances in one MultiMesh share one LOD
   level and are culled as a whole; one MultiMesh for the map
   means no per-chunk culling and no distance bands. Chunk size
   follows the visibility distances in Phase 6.
2. Set the format BEFORE the count. In code:
   `multimesh.transform_format = MultiMesh.TRANSFORM_3D`, then
   `multimesh.instance_count = N`. Setting the count clears and
   resizes the buffers, and the format cannot change afterwards
   while the count is above zero. (Godot docs, MultiMesh class
   reference.)
3. Fill per-instance transforms with `set_instance_transform(i,
   Transform3D)` in a loop: position on the ground, a random
   Y-rotation, a random uniform scale in a narrow band (0.8 to
   1.2 is a starting range, tune by eye). Unset transforms stack
   every instance at the origin, which reads as one giant flower.
4. Turn on per-instance colour (`use_colors = true`) and set a
   palette colour per instance with `set_instance_color`. This is
   how one mesh becomes pink spikes in one patch and a white bed
   in the next without a second mesh.
5. Use per-instance custom data (`use_custom_data = true`,
   `set_instance_custom_data`) for one float the shader reads: a
   random phase per instance, so the sway in Phase 4 does not move
   in lockstep. The docs describe custom data as four multi-use
   variables passed as a Color; one channel is enough here.
6. Place instances from the authored data, not from a random
   scatter alone: sample the terrain/paint mask for flower zones
   (paths, rock bases, slopes, per the split-screen reel), then
   jitter inside the zone. Pure random scatter puts flowers where
   the composition does not want them; the reel's fields are
   patches, not noise.

**Check**
- `visible_instance_count` caps the draw; set it to the count
  actually filled. An allocated-but-unfilled tail renders at the
  origin.
- Walk the field: no two adjacent flowers share rotation, scale,
  colour, and sway phase at once. If the field looks stamped,
  one of the four randomizations is missing.
- The draw-call count does not grow with the flower count. If it
  does, the flowers are not in a MultiMesh.

**Why**
GPU instancing is the entire performance story of the flower
fields: thousands of instances, one draw call, no per-node cost.
Chunking is what buys culling and distance bands back, since a
single MultiMesh cannot be partially culled.

## Phase 3: Crossed grass planes with one fixed normal

**Do**
1. Build the grass plane mesh: two perpendicular quads crossing at
   the centre (an X from above), each carrying the masked grass
   texture. The creator's recipe is "perpendicular planes, masked
   grass texture on each plane". Two planes are the minimum that
   reads from more than one side; a single plane vanishes edge-on.
2. Paint the grass texture with a hard alpha mask: opaque blades,
   fully transparent gaps. No soft alpha. The texture's alpha
   channel IS the blade shape.
3. Use alpha scissor, never alpha blend, for the grass material.
   In `StandardMaterial3D`: transparency mode Alpha Scissor,
   threshold 0.5 (the docs' default). Alpha scissor is faster
   than blending, has no transparency sorting issues, and the
   cutout casts shadows; blending is for glass and VFX, not
   foliage. (Godot docs, Standard Material 3D.) In a custom
   shader, the equivalent is `render_mode depth_draw_opaque`
   with a `discard` below the threshold, the pattern the
   verified grass-shader reference uses.
4. Disable backface culling on the grass material
   (`cull_disabled`), so both faces of each plane draw. Crossed
   planes with culling on lose half their blades from any angle.
5. Set the fixed normal. This is the creator's third clause,
   "set the normal to x,0 /y,0 /z,1", and the step that makes the
   grass read evenly: every plane shades as if lit from the same
   direction, so no plane goes dark because it happens to face
   away. The Godot equivalent is a derivation, not his code:
   his constant is Unreal Z-up; Godot is Y-up, so the constant
   is (0, 1, 0), and it must be applied in WORLD space, or each
   rotated instance rotates its normal with it and the trick
   fails. In the grass spatial shader, use the
   `world_vertex_coords` render mode (vertex data presented in
   world space) and override the normal in `vertex()`:
   `NORMAL = vec3(0.0, 1.0, 0.0);`. `NORMAL` is an inout vec3
   in the vertex function (Godot docs, spatial shader
   reference). Every plane then shades as facing straight up,
   whatever its rotation.
6. Instance the grass planes the same way as the flowers
   (Phase 2): one MultiMesh per chunk, random Y-rotation per
   instance. The crossed planes plus random rotation are what
   keep the field from reading as a row of cards.

**Check**
- Orbit the camera around one grass clump: the shading must not
  change per plane as the view moves. If one plane of the cross
  goes dark while the other stays lit, the fixed normal is in
  model space, not world space.
- Backface test: view a clump from below the plane line (low
  camera). No blade may disappear; if it does, culling is on.
- Mask test: no soft fringe around blades. A fringe means the
  material is blending instead of scissoring, or the threshold
  is below the texture's edge alpha.

**Why**
A crossed plane has two facings; real lighting shades them
differently and the field strobes as the camera moves. One fixed
normal removes the per-plane variation entirely, which is the
whole point of the trick: the grass becomes a pattern of light,
not a simulation of leaves. Alpha scissor keeps it in the opaque
pipeline, which is what makes thousands of cutout blades cheap
and shadow-casting.

## Phase 4: Wind, once, in the vertex shader

**Do**
1. Drive sway from a scrolling noise texture, not from per-blade
   sine waves. Sample a `NoiseTexture2D` (Simplex, ridged
   fractal) at world XZ, offset by `TIME`, wind direction, and
   wind speed, so gusts visibly travel across the field instead
   of the whole field swaying in lockstep. This is the verified
   pattern from the hexaquo grass series (noise texture, world
   position, TIME offset, bend strongest at the tip).
2. Weight the bend by height: zero at the base, full at the tip.
   Author the grass mesh with a declared UV convention (UV.y = 0
   at the tip, UV.y = 1 at the base, the convention the verified
   grass-shader reference documents) and use `(1.0 - UV.y)` as
   the weight. If the mesh uses the opposite convention, flip
   the weight; do not guess. The Check below catches it.
3. Displace in the vertex function, in world space (the shader
   already uses `world_vertex_coords` from Phase 3):
   sample the gust, multiply by the height weight and a sway
   amplitude uniform, add it along the wind direction. One
   sample, one offset, per vertex.
4. Give every instance a different phase. Read the per-instance
   custom data from Phase 2 (one random float) and add it to the
   TIME offset, or neighbouring instances sway as one sheet.
   The sibling grass skill's per-blade rank is the same idea at
   finer grain; here one phase per instance is enough, because
   the instances are clumps, not single blades.
5. Sway the flowers with the same noise field and the same wind
   direction, weighted by local height so the stem base stays
   planted. The viewer's comment confirms the flowers sway; the
   shared field is what makes grass and flowers read as one wind
   instead of two effects. Keep the flower sway smaller than the
   grass sway: flowers are the heavier object in the shot.

**Check**
- Freeze a frame mid-gust: blades bend, bases do not move. If a
  base slides, the height weight is wrong (or the UV convention
  is flipped).
- Watch a gust cross the field: it must arrive at near, middle,
  and far clumps in order. Whole-field lockstep means the noise
  is sampled in local space or without the TIME scroll.
- Grass and flowers lean the same way in the same frame. If they
  disagree, they sample different fields.

**Why**
Wind is one system, not one effect per plant. A travelling noise
field gives the meadow a direction and a speed for free, and the
height weight is what keeps rooted plants rooted. Per-instance
phase is the cheapest desynchronization there is.

## Phase 5: The look stack (pixelation, dither, cel)

The creator's three words are "ixelating, dithering, and
cellshading shaders", plus "shaders and low resolution" for the
pixelated appearance. Three layers, in this order: geometry is
rendered small or post-quantized (pixelation), colours are cut to
levels with a patterned threshold (dither), light is cut to bands
(cel). Build them as separate toggles; the look is the stack, and
debugging needs each layer alone.

**Do**
1. Pixelation, route A (post-process, the flexible route):
   CanvasLayer at layer 1, full-rect ColorRect with Mouse Filter
   set to Ignore (a full-screen ColorRect otherwise eats every
   click), canvas-item shader reading
   `uniform sampler2D screen_texture : hint_screen_texture,
   filter_nearest, repeat_disable;`, snapping each pixel to its
   block centre with `floor(FRAGCOORD.xy / size)` and sampling
   the centre pixel. `pixel_size` 4 is the documented default;
   1 turns the effect off. UI that must stay sharp goes on a
   higher CanvasLayer. (Verified firsthand from the CC0
   pixelate shader, godotlearning.com.)
2. Pixelation, route B (low-resolution viewport, the committed
   route): put the game under a `SubViewportContainer` with
   `stretch` on and `stretch_shrink` 4 (a 1280x720 window
   renders at 320x180), container texture filter Nearest, HUD
   outside the SubViewport so text stays sharp; or set the root
   viewport stretch mode to `viewport` with integer scale mode.
   Every block is then a real rendered pixel: nothing flickers
   between block centres, and the game is genuinely cheaper to
   render. Coordinates inside the SubViewport are low-resolution
   pixels, and UI inside it is pixelated too. Pick route B when
   the look is the game's identity from the start (this game's
   case: "low resolution and shaders" is the whole answer). Pick
   route A when adding the look to an existing game or as a
   player-toggleable setting. Do not run both at once.
3. Dither: cut each colour channel to a fixed set of levels, with
   a Bayer 4x4 ordered threshold instead of a fixed 0.5. The
   matrix (CC0, same source as route A):
   `0, 8, 2, 10 / 12, 4, 14, 6 / 3, 11, 1, 9 / 15, 7, 13, 5`,
   threshold `(BAYER[cell] + 0.5) / 16.0` per 4x4 block group.
   A colour between two levels becomes a fixed pattern of both,
   17 mixes per interval, so gradients climb in patterned steps
   instead of hard bands. Ordered dither beats random noise
   here: the pattern depends only on screen position, so a still
   picture is identical every frame and only moving things
   change. Keep `palette_steps` at 0 while tuning pixelation;
   dithering does nothing until levels are cut.
4. Cel shading: set the spatial shader render modes
   `diffuse_toon, specular_toon` (verified render modes, Godot
   docs) for the banded-light baseline. For control over the
   band count and softness, use a custom `light()` function with
   a diffuse ramp texture (the godotshaders Complete Toon Shader
   pattern: the ramp curve is what defines the toon look; a
   near-vertical ramp is toon, a linear ramp is realistic).
   Apply the ramp to environment and ground cover; characters
   use the sibling stylized-character skill, which carries the
   face-normal and painted-texture work this skill does not.
5. Texture filtering for the whole stack: Nearest on the masked
   grass/flower textures, no mipmaps on the mask texture or the
   alpha erodes at distance and the far field thins out. Verify
   with the far-field check in Phase 6.

**Check**
- Pixelation alone: block edges are hard squares, never blends.
   A soft edge means linear filtering survived somewhere.
- Dither alone (pixelation off, levels on): gradients show a
   regular pattern, identical frame to frame on a still shot.
   Crawling or fizzing on still frames means the threshold has
   a TIME term in it; remove it.
- Cel alone: light on a sphere or a rock steps through visible
   bands. A smooth gradient means the toon modes are not active
   or the ramp is linear.
- Stacked: the three layers compose without fighting. If the
   dither pattern fights the pixel blocks (pattern per pixel
   instead of per block), the dither is sampling per fragment
   instead of per block; key it to the block coordinate.

**Why**
Each layer does one job: pixelation sets the resolution of the
picture, dither hides the banding that cutting colour levels
creates, cel cuts the light into readable bands. Separate
toggles are what make the stack debuggable; a single combined
"retro" shader hides which layer broke.

## Phase 6: Density discipline (patches, falloff, overdraw)

**Do**
1. Place cover in patches, following the split-screen reel:
   dense beds along paths, at rock bases, and on slopes; bare
   ground between patches. Colour-code patches by zone (one
   palette per patch) so the field reads as designed planting,
   not noise. The reel's fields are the reference: the top half
   is almost bare, the bottom half is beds, and the difference
   is the whole effect.
2. Chunk the field (Phase 2) and give each chunk a visibility
   band with `visibility_range_begin` / `visibility_range_end`
   plus begin/end margins for hysteresis, fade mode Disabled
   (the fastest switch; fades force transparent rendering
   during transition). Near chunks carry grass planes and
   flowers; far chunks carry flowers only, then nothing, with
   the terrain texture carrying the colour underneath (the
   carpet idea from the sibling grass skill: tint the ground
   the flower colours so the far field never reads as bare
   dirt when the instances end).
3. Budget overdraw before adding density. Overlapping alpha-cutout
   blades shade the same pixel many times; the cost that kills
   dense foliage is usually overdraw, not vertex count (the
   Guerrilla deferred-texturing lesson, as recorded in the
   sibling grass skill). Measure with the renderer profiler at
   the densest viewpoint; if the frame cost climbs faster than
   the instance count, thin the far chunks first, never the
   near ones.
4. Cap the instance count per chunk in the ground-cover manifest
   (see Agent automation below) and enforce it at build time. A chunk
   that exceeds its budget fails the build, it does not ship
   and get profiled later.
5. Keep collision out of the cover entirely. Ground cover is
   dressing: no collision on grass or flowers, ever. The
   concealment read in the foxglove reel (a knight hidden until
   close) is a visibility effect of tall dressing, not a
   stealth system; do not bolt gameplay onto it without a
   separate design.

**Check**
- From the game's normal camera height, the far field reads as
  continuous cover: no holes where a chunk ends, no visible
  seam where instances stop. A seam means the ground tint does
  not match the instance colours under the same light.
- The densest viewpoint holds the frame budget with the look
  stack on. If it does not, thin far chunks before touching
  near ones.
- No flower or grass instance has collision. A player snagging
  on a flower is a dressing bug, not a feature.

**Why**
Density is a composition and budget problem, not a scatter
problem. Patches are the composition; chunks plus visibility
bands are the budget; the ground tint is what makes the end of
the instances invisible. Overdraw is the cost most builders
measure last and regret first.

## Expansion: memoryfloater flower construction and distance thinning (2026-11-22)

This section adds a second creator's construction and distance
technique to the skill. It does not replace Phases 1 to 6: the
Before the Sun Sets recipe stays the base construction, and the
memoryfloater material is the cheaper cage construction plus the
distance-thinning system. Creator statements are quoted in the
Source section above; viewer material is labeled unendorsed
wherever it appears; every Godot transfer is derivation, labeled
as such.

### The 3-quad cage: 6 triangles per flower

**Do**
1. Build the flower from exactly three quads: two tall vertical
   quads crossed at roughly 90 degrees through the plant's
   centre, and one horizontal quad at the height of the flower
   head. That is 3 quads, 6 triangles total, regardless of
   species. (Reel DfMjBGcIPOB, wireframe frames read firsthand.)
2. Paint the whole plant onto the textures on those quads: the
   vertical quads carry the side view (stem, leaves, head
   profile); the horizontal quad carries the top-down view of
   the flower head, which is what the player sees from above
   and what stops the flower reading as flat from high angles.
3. Reuse the same cage across species, changing only the
   texture and the cage proportions. The reel demonstrates
   poppy, cornflower, daisy, gentian, columbine, lupine,
   foxglove, and hollyhock on the same cage.
4. Choose between this cage and the Phase 1 modeled flower by
   camera distance, not by taste. The cage is the cheaper
   construction for mid and far fields, where the texture
   carries the read. Where the camera walks through the flowers
   at close range, keep the Phase 1 modeled flower: flat cards
   read as paper up close, and Phase 1 step 3 stands. Do not
   present the cage as a replacement for the modeled flower;
   it is the distance construction for the same field.

**Check**
- From the game's normal camera height, the cage reads as a
  flower from the side and from above. If the top view is
  missing, the head vanishes when the camera looks down; the
  horizontal quad is not optional.
- The triangle count per flower is 6 before any optimisation
  step below. If it is higher, the cage has extra quads that
  the reel's construction does not use.

**Why**
The texture does the work, not the mesh. Three quads instanced
by the thousand cost almost nothing in vertices; the cost moves
to fragment shading of transparent texels, which is the subject
of the overdraw note below.

### Stem alignment and shrink-to-texture

**Do**
1. Align the stem: add 2 loop cuts to the vertical planes, then
   move vertices so the geometry follows the painted stem
   instead of the stem wandering off the plane edges. (Reel
   DfU1Xt9oNqu, Step 2, on-screen caption read firsthand.)
2. Align the top view: rotate the top petal plane and adjust it
   over the edges so the top-down head view lines up with the
   side planes. (Step 3, caption text partly garbled; the
   alignment intent is what the frames show.)
3. Optimise alpha: add more vertices and shrink the geometry to
   the visible texture space, cutting away transparent quad
   area to reduce alpha overdraw. The reel's wireframe frame
   shows triangles hugging petals, stem, and leaves after this
   step. (Step 4.)
4. Keep the creator's side note: more vertices also improve wind
   motion (more deformation points along the stem) and let the
   shape be defined better. The creator admits he was "lazy
   here", meaning the demo does not fully define the shape; do
   not cite the demo's wireframe as the finished silhouette.

**Check**
- The stem texture stays inside the geometry from every side
  angle. Painted stem hanging off a plane edge means Step 2
  was skipped.
- Transparent quad area is cut away around the silhouette. A
  full rectangular quad behind a thin stem means Step 4 was
  skipped, and the overdraw note below applies at full force.

**Why**
Alignment is what keeps a painted plant on its cage, and
shrink-to-texture is what keeps the cage cheap: every
transparent texel the fragment shader shades is cost with no
picture, and cutting the silhouette is the only way to remove
it without adding triangles elsewhere.

### Distance thinning: scale up, thin out, hash decides

**Do**
1. Scale flowers up as the camera zooms out, and at the same
   time REDUCE the number drawn. The reel's one measured shot
   shows 3.0% of flowers drawn at distance, with the field
   still reading dense. Scaling everything without thinning
   overlaps, costs more, and flickers; thinning without
   scaling leaves a sparse field. The pair is the technique.
   (Reel DgAFMl4o27h, narrated, frames read firsthand.)
2. Let the shader decide which instances grow and which cull,
   from a hash of the instance id. The creator's rule, quoted
   in the Source section: every instance id goes through a
   hash, giving a stable random number per instance, so it is
   always the same flowers that grow and the same ones that
   cull. Stability is the whole point: a per-frame random
   reselects every frame and the field flickers.
3. Hide the pop with the creator's recipe, quoted in the Source
   section: grass texture underneath the flowers, the thinning
   start distance set properly, and a grow/shrink distribution
   in which growing plants slowly hide shrinking ones as the
   camera zooms out. The creator says it is "not perfectly
   tuned" in his demo; treat the recipe as the method and the
   tuning as open work, not as solved values.
4. Colour-bleed the flower texture: fill fully transparent
   texels with neighbouring colours, so sampling just outside
   the drawn shape returns flower or stem colour instead of
   black. The creator's tool is GIMP, with a custom addition of
   his own; he also suggests an AI-generated bleed script as an
   alternative. The reel shows the no-bleed failure (black
   fringes when the cutoff drops) against the bled result.
5. Drive mip bias and alpha cutoff from camera distance in the
   shader, using the reel's on-screen pseudocode, reproduced
   here as shown (no parameter values were given, and none are
   invented here):
   `f = saturate((dist - from) / (to - from))`,
   `lod = mip + f * bias`,
   draw if `alpha >= lerp(cutoff, cutoffFar, f)`.
   Lowering the cutoff at distance thickens the stem and head;
   the bleed in step 4 is what keeps that from producing black
   fringes. In the optimal case the creator says alpha overdraw
   can go to zero and the shader can switch to a non-clipping
   variant; that is his claim about his setup, not a measured
   result, and no values for from, to, bias, cutoff, or
   cutoffFar are stated anywhere in the video or the fetched
   comments.

**Godot transfer of the hash rule (derivation, not the creator's
code)**
1. The creator's engine is Unity. In Godot, the spatial shader
   vertex function exposes `INSTANCE_ID` (int, "Instance ID
   for instancing") and `INSTANCE_CUSTOM` (Godot docs, spatial
   shader reference:
   https://docs.godotengine.org/en/4.1/tutorials/shaders/shader_reference/spatial_shader.html).
   Hash the id in `vertex()` to a stable 0-to-1 value, for
   example `fract(sin(float(INSTANCE_ID) * 12.9898) * 43758.5453)`,
   and pass the result to `fragment()` through a varying, since
   instance built-ins are vertex-stage only. This hash line is
   this skill's derivation, not the creator's code; any
   deterministic hash with a uniform output serves the same
   purpose.
2. Compare the hashed value against the distance-driven keep
   fraction: instances below the fraction cull (discard), the
   rest scale up. Because the hash is a pure function of the
   instance id, the same instances grow and cull every frame,
   which is the stability the creator's rule exists to provide.
3. The alternative already present in this skill also works:
   per-instance custom data (Phase 2 step 5) carrying one
   random float per instance, set once on the CPU. The hash
   route needs no CPU data; the custom-data route needs no
   shader hash. Pick one; do not mix both, or two different
   random values decide the same instance.
4. Honest limit: shader-side discard saves fragment and
   overdraw cost, not vertex or instance cost; the culled
   instances are still processed as geometry. True draw
   savings need CPU-side thinning (`visible_instance_count`
   per chunk, or chunk visibility bands as in Phase 6). Do not
   claim the discard alone as the performance win; the
   creator's "renders faster" statement describes his setup,
   and the split between fragment savings and instance savings
   is this skill's analysis, labeled as such.

**Check**
- Zoom the camera out slowly: the same individual flowers grow
  and the same ones vanish at every pass. Reselection between
  passes means the random value is per-frame, not per-instance.
- No visible pop at the thinning start distance with grass
  texture under the flowers. A pop means the start distance,
  the distribution, or the under-texture is wrong, in that
  order.
- At distance, stems stay coloured, never black-fringed. Black
  fringes mean the texture was not bled, whatever the cutoff
  does.

**Why**
A distant flower renders into a few pixels, so the field's job
at distance is pixel density per surviving flower, not flower
count. Fewer, bigger flowers with a stable selection read as
the same field for less fragment cost, and the bleed plus
cutoff shift is what keeps thin stems readable instead of
broken or black.

### Far-field noise pattern (experimental, creator's own label)

**Do**
1. Know the idea and its status before using it. The creator's
   rationale, quoted in the Source section: at distance a
   flower renders to a single pixel or less, which normally
   causes aliasing; since distant foliage is already just a
   noise pattern on screen, render the noise pattern itself
   instead of the geometry. He calls it "still experimental"
   and says "finding the right values is a pain". The reel
   (DfRsg8eIRya) is a visual demo with debug views and no
   speech, code, shader, distances, or numbers.
2. Treat the grass version as untested. The creator's own words
   on grass: "Haven't tried it yet though. So basically: the
   grass will also be noise, that's why it should work." Do not
   present a grass noise pass as proven by this source; it is
   a stated hypothesis, not a result.
3. If the pattern is tried, the Godot form is derivation: a
   density and colour noise in the ground shader whose patch
   distribution matches the near-field foliage distribution,
   swapped in past a tuned distance. No noise function, scale,
   palette, or switch distance is given by the creator; all of
   it is tuning work, and the tuning difficulty is the
   creator's own warning, not an implementation detail.

**Check**
- The far field reads as the same patch distribution as the
  near field, in colour and density. A generic noise that does
  not match the patch layout reads as a different field.
- The switch distance is not visible in normal play. The
  creator moved the switch closer to make it visible for the
  demo; in a shipping field it must not be findable by eye.

**Why**
This is the limit case of the thinning above: when geometry
renders to less than a pixel, the pattern is cheaper than the
geometry. It is recorded here as an experimental direction with
the creator's own caveats attached, not as a phase to build
before the thinning system works.

### Viewer material: the overdraw counter-argument (unendorsed)

Everything in this subsection comes from viewers in the
fetched comments. No creator reply endorses any of it in the
pages read. It is recorded because it is the strongest
objection to the 3-quad cage, and the creator's own Step 4
(shrink-to-texture) is his answer to the same objection.

**Do**
1. Know the objection. Viewer Danny Mačura: with GPU
   instancing, extra triangles are cheap, but transparent-quad
   overdraw is expensive, because the GPU must look up the
   texture for every overlapping transparent triangle to decide
   whether the terrain behind shows. His rule: cut the geometry
   close to the silhouette and balance cutout tightness against
   vertex count. Viewer Abhilash kar, same point in short form:
   stacked plants multiply transparency overdraw and depth-test
   cost; "cut islands to pixels". Viewer Siusiacz: "Use more
   triangles to cutout the siluette."
2. Know the shader-mode rule as a viewer rule, not a creator
   statement. Viewer Costescu Catalin Mihai: use alpha clip
   (discard fragments below alpha 0.5) instead of alpha blend,
   because clip populates the depth buffer and blend causes
   alpha overdraw; and low polygon counts still matter because
   GPUs fill triangles in 2x2 pixel groups, so more edges mean
   more wasted fragment work. His far-distance suggestion
   (one vertical billboard, top texture when the camera looks
   down) and his fresnel edge-cleanup suggestion (viewer
   Thomas: drive alpha with fresnel at grazing angles) are
   likewise unendorsed leads, not verified practice.
3. Know the correction. Viewer "your local heelys pro": the
   flowers are "masked not translucent", which changes how the
   overdraw cost should be reasoned about. The skill's existing
   guidance agrees: Phase 3 already requires alpha scissor, not
   blend, for the grass, and the same rule applies to the cage.
4. Treat the counter-argument as the reason Step 4 exists, not
   as a reason to abandon the cage. The creator's shrink step
   and the viewers' cut-close rule converge on the same
   construction: geometry hugging the visible texture. Where
   they disagree (how many triangles the silhouette deserves),
   the answer is measurement on the densest viewpoint, per
   Phase 6 step 3, not allegiance to either side.

**Check**
- The densest viewpoint's cost is measured, not assumed. If
  overdraw dominates, the fix is a tighter silhouette (Step
  4), not fewer instances.
- The material is scissor/clip, never blend, for both the cage
  and the grass. A blend material on foliage reopens the whole
  objection.

**Why**
The cage's bargain is vertex-cheap and fragment-expensive, and
the objection names the fragment side honestly. Recording it
with its unendorsed status keeps the skill from overselling
the cage while keeping the construction that answers it.

## Failure modes

- **Fixed normal in model space.** Each rotated instance rotates
  its normal with it, and the field strobes. The normal must be
  world space (`world_vertex_coords`), constant (0, 1, 0).
- **Alpha blend on the grass.** Sorting soup, no shadows, and the
  far field shimmers. Alpha scissor, threshold 0.5, opaque
  pipeline.
- **Format set after the count.** `transform_format` cannot
  change once `instance_count` is above zero. Format first,
  count second, transforms third. The docs state the order;
  violating it silently keeps the default 2D format.
- **Unfilled MultiMesh tail.** Instances never given a transform
  sit at the origin as one giant clump. Fill every index or cap
  with `visible_instance_count`.
- **One MultiMesh for the whole map.** No per-chunk culling, no
  distance bands, the whole field pays near-field cost at all
  distances. Chunk it.
- **Wind moving the base.** The height weight is zero at the
  ground. If bases slide, the UV convention is flipped or the
  weight is missing.
- **Lockstep sway.** One phase for the whole field. Per-instance
  custom data is the fix; one float per instance.
- **Post-process pixelation flicker.** Details thinner than a
  block appear and vanish as they cross block centres. Either
  thicken the minimum feature or switch to the low-resolution
  viewport route, where every block is a real pixel.
- **Dither crawling on still frames.** The threshold has a TIME
  term or a random term. Bayer thresholds depend on screen
  position only.
- **Full-screen ColorRect eating clicks.** Mouse Filter must be
  Ignore, and sharp UI belongs on a higher CanvasLayer.
- **Mipmap alpha erosion.** The far field thins as distance
  grows because the mask's alpha averages away in smaller mips.
  Nearest filtering and no mipmaps on the mask texture, then
  re-check the far field.
- **The look stack applied wholesale to a different art
  direction.** Pixelation and dither are identity choices, not
  free dressing. The Valkyrie note below is the standing
  example: the construction transfers, the retro stack does
  not, unless the art direction says so.

## AAA studio practice

- **Sucker Punch, GDC 2021, "Procedural Grass in Ghost of
  Tsushima".** The scene considers just over 1 million blades
  and renders about 83,000 per frame, each animating with the
  wind, in about 2.5 ms end to end, through a compute-shader
  pipeline with per-blade instance data and a two-tier LOD
  that drops three of every four blades at the transition.
  The same system serves pampas grass, burnt fields, and
  flower fields. (As recorded in the sibling skill
  `procgen-worlds/godot-grass-lod-wind`, with sources:
  https://gameindustrylibrary.com/documents/procedural-grass-in-ghost-of-tsushima
  and the GDC Vault talk.) The parallel to this skill: the
  creator's one-model-plus-instancing is the same instinct at
  solo scale, and the 3-of-4 drop is the same coverage problem
  Phase 6 solves with chunks and ground tint. The compute
  route is the documented escalation when instance counts grow
  past what MultiMesh chunks carry.
- **Sucker Punch wind (same GDC work).** Wind prioritizes volume
  over accuracy: one constant-direction vector, time-varying
  noise modulating magnitude so gusts travel, local swirl from
  "vorticles". Phase 4 is that shape at shader scale: one
  scrolling noise field, one direction, per-instance phase.
- **Guerrilla Games, GDC 2022, deferred texturing in Horizon
  Forbidden West.** Denser foliage forced the change because
  the cost was overdraw: alpha-tested geometry shading the
  same pixel many times. The answer was a visibility-buffer
  pre-pass with shading in compute. (As recorded in the
  sibling grass skill:
  https://www.guerrilla-games.com/read/adventures-with-deferred-texturing-in-horizon-forbidden-west.)
  The lesson carried into Phase 6: measure overdraw first when
  a dense field gets expensive; fewer blades is the wrong
  first fix.
- **Low-resolution rendering as a look (the PS1 route).** The
  verified PS1 guide (tested Godot 4.7.2) renders the 3D
  scene into a small SubViewport shown through a
  SubViewportContainer with Nearest filtering, plus vertex
  snapping, affine UVs, nearest textures without mipmaps, and
  a 15-bit colour cut with ordered dither:
  https://anipixels.github.io/guides/godot-4-psx-ps1-graphics/
  That guide's full stack (wobble, affine warp) is more than
  this skill needs; the low-resolution viewport plus Nearest
  upscale is the part Phase 5 route B takes, and the ordered
  dither is the part Phase 5 step 3 takes.

## Agent automation

1. **Ground-cover manifest (`ground-cover-manifest.json`).** One
   entry per zone: model path, mask texture, palette colours,
   instance budget, chunk size, visibility band
   (begin/end/margins), wind parameters (direction, speed,
   sway amplitude, noise texture), look-stack settings
   (pixelation route and size, palette steps, dither on/off,
   cel ramp). Every number in Phases 1 to 6 lives in the
   manifest; tuning never touches the shader.
2. **Budget gate.** At build time, sum instance counts per
   chunk against the manifest budget; a chunk over budget
   fails the build. No chunk ships unbudgeted.
3. **Uniform-lighting check.** Render one clump from four
   compass angles and diff the per-plane brightness. A plane
   whose brightness follows its facing instead of the light
   fails; the fixed normal is in the wrong space.
4. **Rooted-sway check.** Scrub the wind through one gust and
   assert every instance base stays within a small epsilon of
   its placed position while tips move. Sliding bases fail.
5. **Still-frame stability check.** With the look stack on and
   nothing moving, two frames 60 apart must be pixel-identical
   except for the wind field's own motion. Crawling dither or
   flickering blocks fail.
6. **Far-field coverage check.** From the game's normal camera
   height, measure ground pixels covered by instances plus
   ground tint at the falloff distance. Holes fail; the fix is
   ground tint and chunk bands, not more instances.

## The human method, distilled

1. **One model, a thousand instances.** The field is a placement
   problem, not a modelling problem.
2. **Crossed planes, one fixed normal.** Uniform light is a
   choice, not an accident. (Creator: "perpendicular planes,
   masked grass texture on each plane, set the normal to x,0
   /y,0 /z,1".)
3. **Patches, not noise.** Beds along paths, at rock bases, on
   slopes. The split-screen reel is the reference image.
4. **One wind for everything.** Grass and flowers sample the
   same travelling field.
5. **The look is a stack with toggles.** Pixelation, dither, cel,
   each alone before together.
6. **Fun over realism.** The creator's own priority, stated in
   one line: "fun>>realism". When a physically correct choice
   and a readable choice conflict, take the readable one.

## Valkyrie note

The construction transfers directly; the look stack does not
transfer wholesale. Valkyrie's Pellune map is authored with
deterministic seeded scatter on authored masks, so Phase 2's
zone sampling maps onto existing mask data, and the fixed
iso camera makes the crossed-plane plus fixed-normal recipe
especially cheap (one viewing angle, one light direction, no
edge-on vanish to hide). Meadow and forest-floor dressing at
iso distance is exactly this skill's job.

The retro stack is the boundary: Valkyrie's bar is a painted,
full-saturation wallpaper still from the fixed camera, and
pixelation plus ordered dither fight that bar. Do not apply
Phase 5 to Valkyrie unless the art direction changes. The
cel ramp alone is compatible with the painted look and can be
evaluated on its own. Note also that Valkyrie is C#: the
shader work ports as written, but the Phase 2 setup code is
GDScript as documented; the MultiMesh class and method names
are the same in C#, only the syntax changes.

## Depth status

PARTIAL. The creator's evidence is three one-line comment replies
(verified verbatim in raw comment JSON) plus showcase reels
whose summaries state plainly that placement, performance, and
settings are not shown. The crossed-plane recipe, the instancing
answer, and the three-part look stack are his words; every
construction detail, number, and shader line in Phases 1 to 6 is
refinement research derived for Godot and labeled as such, with
firsthand-verified documentation and shader references. The
Unreal-to-Godot normal conversion (Z-up to Y-up, world space)
is a derivation, stated as one. No hands-on Godot test of the
full stack was run for this skill; the checks in each phase are
what closes that gap.

Expanded 2026-11-22 with memoryfloater construction and
distance-thinning material (3-quad cage, stem alignment,
shrink-to-texture, hash-rule thinning, colour bleed, far-field
noise, and the viewer overdraw counter-argument, labeled
unendorsed). The added material is labeled by source throughout,
and the PARTIAL rating is unchanged.
