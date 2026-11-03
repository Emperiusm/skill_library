---
name: normal-maps-parallax-occlusion
description: "Fake surface detail with normal maps and parallax occlusion mapping: bake high-poly detail into tangent-space RGB, know the no-self-shadowing limit, then add a height map and view-dependent UV offset for occlusion-correct depth. Trigger when faking detail on flat surfaces in games."
---

# Normal Maps and Parallax Occlusion: Faking Detail

## Purpose

This skill fakes 3D surface detail on flat geometry in two steps:
normal maps for cheap direction fakery, parallax occlusion mapping
for depth that survives low viewing angles. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it),
and **Why** (the principle). The core method is: bake the detail
once, lie about it forever, and know exactly where the lie breaks.

## Source

Instagram, kennedy_artist ("The Graphics dude") (transcribed from
reel audio with faster-whisper tiny, 2026-11-02; captions unavailable
via API; a non-English intro segment on the POM video untranscribed):

- https://www.instagram.com/reel/DYmJH92Mw-_ — "How we add Details to stuff in Video games"
- https://www.instagram.com/reel/DZcAeqPsX8_ — "Parallax Occlusion Mapping"

Evidence note: two reel-length narrations (about 3 minutes each, an
explicit two-part series: the POM video references "the previous
video" on normal maps); machine transcription, minor word errors
possible.

## Tools used

Tools used: DCC or baker for generating normal and height maps from
high-poly surfaces; game engine material with parallax occlusion
mapping support.

## Phase 1: Bake detail into a normal map

**Do**
1. Create the highly detailed surface, then project its directions
   onto a plane: "we call that plane the tangent space. So that is
   how we move data from a 3D object onto a 2D image and then back
   into a 3D object."
2. Understand the encoding: "digital images store data in 3
   channels, red, green and blue... If we map the 3 directions of 3D
   onto these image channels, red becomes the X axis, green becomes
   the Y axis, and blue becomes the Z axis." Since image channels
   hold 0 to 1 but directions span -1 to 1, the range shifts: -1
   becomes 0, 0 becomes 0.5. A surface facing you reads 0.5, 0.5, 1.
3. Use normal maps for small details only: a normal-mapped bump
   "doesn't cast a shadow" because "it doesn't really pop out."
   "We don't use them for large details. We use them for small
   details where you can't really tell that the details are not
   popping out."

**Check**
- Flat areas of the map: 0.5, 0.5, 1 (the neutral normal)?
- Are the faked details small enough that the missing shadows go
   unnoticed?

**Why**
The normal map is a lighting lie, and the 0.5-neutral encoding is the
part everyone gets wrong once. Its hard limit (no occlusion, no
silhouette change) is what defines its use: small surface detail,
never large forms. The cliff in the demo works because the detail is
fine grain.

## Phase 2: Know the cheap wins normal maps enable

**Do**
1. Use normal-mapped impostors for trees: "we can do fancy stuff like
   creating impostors for trees... Those nuts, they don't exist. And
   the wrinkles, they exist in the normal map texture."
2. Remember the demo that motivates the next phase: with only the
   normal map applied, "the illusion of 3D" is "very surface level,
   and even at a low angle like this one, all the dots are visible,
   which does not make sense."

**Check**
- Do the impostors hold up at their intended distances?
- At grazing angles, does the flatness show?

**Why**
Normal maps are the right tool until the viewing angle defeats them.
The low-angle failure is not a bug to fix in the normal map; it is
the signal to graduate to parallax occlusion.

## Phase 3: Add parallax occlusion for real depth

**Do**
1. Generate a height map alongside the normal map: "a black and
   white texture that stores the height information of a detailed 3D
   surface, with white representing the highest point and black the
   lowest."
2. Let POM shift the texture by view angle: "using this height map,
   the system then shifts parts of the texture around based on the
   viewer's perspective, and this generates parallax, which creates
   the illusion of depth."
3. Understand the mechanism loosely: the system recreates an
   imaginary 3D surface under the flat one from the height map; for
   each viewed point it walks the view vector through layered
   sections of that imaginary surface to find where the ray would
   have hit, then samples the texture there. ("To calculate [the
   exact hit] we would need [a] distance, and the math for that is
   crazy, so what we do is section the entire thing into a bunch of
   layers and check when the view vector intersects with the
   layer.")
4. Verify against the normal-map-only version: with POM enabled,
   "much, much more realistic, and the dots appear and disappear as
   we would expect them to."

**Check**
- At low viewing angles, do occluded dots disappear correctly?
- At very low angles, can you see the individual layers? (Expected
   artifact; acceptable if rare in play.)

**Why**
POM fixes exactly the normal map's failure mode: occlusion at
grazing angles. The layered raymarch is an approximation, and its
artifacts (visible layers at extreme angles) are the price. Know the
price before paying it.

## Phase 4: Choose by cost

**Do**
1. Budget honestly: "because of the math and the fact that every
   texture has to be sampled several times, this system can be a bit
   more expensive than normal maps."
2. Default to normal maps: "the good news is that for most surfaces
   in games, normal maps are actually good enough."

**Check**
- Is POM applied only where low-angle viewing actually happens?
- Everywhere else: normal maps?

**Why**
Detail fakery is a cost ladder, and most surfaces never need the top
rung. POM on every surface is the same mistake as high-poly
everything: paying for fidelity nobody can see.

## AAA studio practice

- **Crytek, Crysis 2 "DX11 Ultra Upgrade" documentation.** Crytek
  reintroduced parallax occlusion mapping "in order to add macro
  details that are not efficiently possible with hardware
  Tessellation." POM "efficiently approximates surface
  displacement in tangent space" (no real geometry displacement),
  and brings self-shadowing to the surface detail (mud, pavement,
  plastic floors in the before/after comparisons). Source:
  Crytek's official DX11 Ultra Upgrade doc (archived):
  https://dn710105.ca.archive.org/0/items/crysis2-files/Files/DirectX%2011%20Ultra%20Upgrade%20Doc/c2_dx11_ultra_upgrade.pdf
- **Crysis 2 DX11 patch analysis (bit-tech).** "Where tessellation
  isn't feasible within the Crysis 2's performance window, Crytek
  has used parallax occlusion mapping instead," quoting Nvidia's
  Ultra upgrade guide: POM gives "an illusion of depth on certain
  textures, as well as adding self-shadowing" while level
  geometry stays unchanged. This is the cost-ladder decision this
  skill's Phase 4 describes, as shipped by Crytek. Source:
  https://bit-tech.net/reviews/gaming/pc/crysis-2-directx-11-patch-analysis/5/

**Agent-executable upgrades**

1. **Material cost-ladder manifest (`materials.json`).** Per
   material: chosen technique (normal-map-only vs POM), the
   justification flag (does low-angle viewing actually happen for
   this surface?), and the height-map parameters for POM
   materials. An automated audit flags every POM material lacking
   a low-angle justification.
2. **Automated gates.** Neutral-normal check (flat areas read 0.5,
   0.5, 1). Grazing-angle artifact scan (render the material at
   extreme low angles in a batch loop and flag visible layering).
   Shader cost check (texture sample count per POM material
   against the shader budget; this converts "can be a bit more
   expensive" into a number).

## The human method, distilled

1. Bake high-poly detail to tangent-space normal maps; 0.5 is
   neutral.
2. Normal maps for small details; they never cast shadows.
3. Impostors ride on normal-mapped lighting response.
4. POM adds a height map and view-dependent offset for grazing
   angles.
5. Default to normal maps; spend POM only where angles demand it.

## Depth status

PARTIAL (transcribed reel audio, two reels about 3 minutes each;
encoding details and the POM mechanism as spoken; no frame-level
verification).
