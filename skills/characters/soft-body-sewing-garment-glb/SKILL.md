---
name: soft-body-sewing-garment-glb
description: "Design garments from sewing patterns in the browser, simulate them as soft bodies on an animated mannequin, and export free GLB plus textures: set particle resolution before simulating, bake with subdivision and smoothing modifiers, retopo down for low-poly targets, and fit to a Mixamo rig for skinned export. Trigger when a game needs character clothing without a DCC cloth sim."
---

# Soft-Body Sewing Tool: Garment Design to GLB Export

## Purpose

This skill reconstructs the alterproduct soft-body sewing workflow from the
author's post and comments, step by step, so another agent can follow the same
process. Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The core method is: fit the
garment to the rig, not the rig to the garment.

## Source

Creator: Longjellyrun. Reddit post:
https://www.reddit.com/r/threejs/comments/1xtm94g/full_soft_body_simulation_with_sewing_and_free_glb_exports/
(r/threejs post 1xtm94g, score 225, 15 comments). App:
https://alterproduct.com. 2026-11-13 scout run, audit 6.

This is a distinct tool from the Blender fake-sim rigging skill
(`blender-fake-sim-rigging`): that one fakes cloth motion with constraints
inside Blender; this one is a browser garment-design tool with a real soft-body
sim and GLB export. Do not merge them.

## Tools used

**alterproduct.com** (three.js plus babylon.js web app), **Mixamo** rig
(author-side, for the planned skinned export). No sim parameters disclosed.

## Phase 1: Design the garment from sewing patterns

**Do**
1. Design garments in the browser tool from sewing pattern pieces.
2. Create textures for individual sewing pattern pieces.
3. Start from the built-in templates, which "work out of the box and are fully
   editable" (author); ask the author for more templates if the garment type
   is missing.

**Check**
- Each pattern piece carries its own texture; the pieces assemble into the
  intended garment shape.

**Why**
Sewing patterns are the real-world source of truth for clothing; designing
from them keeps the garment plausible instead of shrink-wrapped.

## Phase 2: Simulate on the mannequin

**Do**
1. Simulate the garment on a mannequin, including animated mannequins, with
   live mesh editing.
2. Set the particle resolution before starting the simulation: the author says
   "Amount of triangles depends of the setted particles resolution before
   starting simulations."

**Check**
- The drape reads correctly on the posed mannequin; adjust the particle
  resolution if the cloth is too coarse or too heavy.

**Why**
Particle resolution is the quality dial, and it has to be set before the sim
runs; it cannot be fixed after the fact.

## Phase 3: Bake and export

**Do**
1. After the bake, apply modifiers with subdivision and smoothing corrections.
2. Export with or without those modifiers, as GLB plus textures, free.
3. For low-poly targets, the author's recommended route is to generate at
   mid or high poly, then bake normals and reduce the mesh with a retopo
   algorithm (author, in comments, replying to a low-poly request).

**Check**
- The exported GLB opens with the baked drape and textures intact.

**Why**
A baked drape is a static mesh; the modifiers and the retopo step are what
make that static mesh usable at a game's poly budget.

## Phase 4: Fit it to a rig (planned, commenter-driven)

**Do**
1. Export as a static mesh (or animated pose via shape keys from the baked
   simulation) for now; the current export is "a static (or animated pose -
   shape keys animation from baked simulation) ready for blender auto rig"
   (author).
2. Next step, per the author: skinned export with weights copied from the
   nearest body verts, so the garment "would let it go straight into an
   animation, even if it loses the cloth motion" (commenter PurchaseCommercial34).
   The author confirms: "I'm already using a Mixamo rig, so this sounds
   doable. I'll look into importing Mixamo-rigged models and automatically
   fitting the garments to them."

**Check**
- A skinned export must follow the Mixamo rig's proportions; commenters ask
  for automatic adjustment "based on proportions and such of the mesh," and
  for import of already-rigged hero character models.

**Why**
A static garment is a prop; a skinned garment is a wearable. The rig is the
interface, so the tool should fit to the rig instead of asking the user to
re-rig the garment.

## AAA studio practice

Pattern-based garment authoring is the AAA standard, and Marvelous Designer
is the tool that standard runs on. CD Projekt Red principal character artist
Grzegorz Chojnacki: "Almost all the characters' clothes in Cyberpunk 2077
were created with [Marvelous Designer]." The named technique is the
two-layer approach: a firm fabric preset (e.g. Leather_Cowhide) as the
bottom cloth base, a softer preset (e.g. Nylon_Featherweight) on top with
slightly increased Shrinkage to finalize fold detail; Layer Clone plus
internal lines plus cut-and-sew plus pressure for puffy/cushioned parts
(e.g. V's vest); Trim_Full_Grain_Leather preset for cables, collars, and
zippers, exported as a starting point for the final model. Hard-surface
objects are imported as patterns (Trace 2D Patterns from UV Map) for cloth
on Adam Smasher's pipes and armor plates, and negative pressure plus freeze
keeps cloth from falling off the avatar. Fabric parameters (Bending, Shear,
Buckling) are tuned by hand without changing patterns. Source: Cartoon Brew,
"How Marvelous Designer Helped Bring The Immersive Dystopia Of 'Cyberpunk
2077' To Life",
https://www.cartoonbrew.com/sponsored-by-marvelous-designer/how-marvelous-designer-helped-bring-the-immersive-dystopia-of-cyberpunk-2077-to-life-210422.html
(Sponsored post, but the quotes are firsthand from CDPR's principal
character artist.)

A studio pipeline case study shows the automation model: for complex hero
costumes (layered fabrics, armor, fitted garments, capes), costume design
ran in a simulation feedback loop ("assess clothing before the characters
were fully rigged"), and a project script called AutoSim, after final body
animation, automatically ran Marvelous Designer cloth simulations for
background characters with default settings and saved them directly to
rendered shots, which the CFX lead credited with reduced manual work. Hero
garments were usually driven by the simulated garment in the render;
background characters were rendered from raw Marvelous Designer geometry
because of outfit variation. Source: Marvelous Designer, "Marvelous
Designer Workflow: A Studio Pipeline Case Study",
https://www.marvelousdesigner.com/explore/marvelous-designer-studio-workflow
(Vendor-published case study; the studio name is only inferable via the
linked Digic project page, not stated in the article text.)

Epic's MetaHuman plus Marvelous Designer/CLO workflow documents the
garment-to-rig handoffs: USD garment export (MD to MetaHuman USD Garment
Integration Workflow), importing a MetaHuman in DNA format as an MD avatar,
MD LiveSync 2 to send an animated MetaHuman to MD, simulate clothing, and
send garments back to Unreal, and Chaos Cloth in-engine for runtime cloth
responding to motion, gravity, and wind. Source: Epic Games, "Tailoring for
MetaHumans: CLO and Marvelous Designer to Unreal Engine demo",
https://www.unrealengine.com/news/tailoring-for-metahumans-clo-and-marvelous-designer-to-unreal-engine-demo

The low-density-then-dense discipline is documented in a Gnomon
hero-character workflow (Kasita Wonowidjojo, Character Creation for Games
class taught by Damon Woods): "I took apart real-life sewing patterns to
understand how each garment is constructed and then tried to replicate them
within Marvelous Designer", simulating one garment piece at a time, each in
its own project, importing frozen OBJs of finished pieces as collision/fit
references instead of simulating everything at once. Density discipline:
"I tend to work as low as possible in MD but when I'm happy with the
overall look, I simulate a dense version of the pattern piece to get better
clothing folds." Export thin and unwelded for ZBrush autogrouping, Panel
Loop for thickness, sculpt high poly, then retopology in Maya with Quad
Draw, UV in RizomUV, "explicitly to bake as well as possible." Source: 80
Level, "Game Character Production from a 2D Concept",
https://80.lv/articles/game-character-production-from-a-2d-concept
(Practitioner-grade: a Gnomon student project, not a shipped AAA title; the
method matches AAA practice but the article itself is not a studio source.)

The retopo and bake half is documented in a second 80 Level workflow
(Yuriy Barchuk, Think Tank Training Centre; references Larian's Baldur's
Gate 3 kobolds): after the MD sim and UVs, export flat patterns to ZBrush,
ZRemesh to lower topology, then in Maya overlay flat patterns, fix topology
with Quad Draw, transfer UVs from the old mesh with Transfer Attributes,
then transfer again in UV space to move the retopologized mesh onto the 3D
sim, and Transfer Attributes again "to allow the mesh to conform to my
Marvelous Designer simulation better." Final bake in Marmoset Toolbag 5
("tweak the cage and skew easily"), plus Substance 3D Painter for material
ID; texturing uses baked AO, curvature, cavity, and thickness maps. Source:
80 Level, "How to Make a Scaled Creature Using ZBrush & Marvelous
Designer",
https://80.lv/articles/sculpting-scales-simulating-clothes-for-creature-chef-in-zbrush-marvelous-designer

CRYENGINE's VCloth 2.0 docs state the sim-vs-skin decision rule this skill
needs: "A simulation of a lo-res mesh in combination with the skinning of a
hi-res mesh, which is used for rendering, make it possible for a fast yet
high quality and detailed cloth simulation." Stiff/tight cloth (T-shirts,
trousers, tight-fitting) "don't need a full cloth simulation, since plausible
movement can be achieved by skinning"; swinging cloth (capes, skirts,
jackets, soft attachments) simulates well. Hybrid recommended: skin most of
the garment and simulate only the moving ends. Source: CRYENGINE
Documentation, "Cloth",
https://www.cryengine.com/docs/static/engines/cryengine-5/categories/23756816/pages/25535602

For the planned Mixamo weight transfer, the nearest sourced analog is a
Marvelous Designer to Character Creator handoff (labeled indie/tool-specific,
not AAA, and not a Mixamo source): export the avatar in a usable A-pose,
fit in MD using the fitting suit via Re-target Draping / Auto Fitting,
export unrigged OBJ, then Transfer Skin Weights with a preset, using Lateral
Partitioning to auto-detect left/right garment halves, then the mandatory
cleanup pass, "go through every single [bone], smoothing/adding/subtracting
where appropriate" with weight brushes, testing movement via Edit Pose; not
all bones should carry weight (e.g. hip none; only twist bones on
arms/legs). Garments must be designed/simulated/fitted in A- or T-pose (T
preferred); shirts weighted in a hands-down pose produce "unrecoverable
mess." Source: Versluis, "How to import clothing from Marvelous Designer to
Character Creator",
https://www.versluis.com/2024/09/how-to-import-clothing-from-marvelous-designer-to-character-creator/

### Agent automation

- **Two-pass simulation manifest with a silhouette gate.** Record per
  garment: a low-density pass (silhouette/fit approval) then a dense pass
  (folds only), with the particle/resolution setting per pass. The dense sim
  runs only after the low-res silhouette is approved. (Grounded in the
  Gnomon "work as low as possible... simulate a dense version" discipline
  and CRYENGINE's sim-low/render-high split. Mapping alterproduct's
  "particle resolution set before simulating" to Marvelous Designer's
  low/high-density workflow is an analogy, not a verified equivalence.)
- **Layer-order and freeze checklist.** Manifest per garment: layer list in
  simulation order (base layer first, e.g. firm preset base, softer top),
  fabric preset per layer, freeze state after each layer, and frozen-OBJ
  reuse for upper layers. Check each layer is simulated alone and frozen
  before the next starts. (Grounded in CDPR's two-layer approach and the
  one-piece-at-a-time/frozen-OBJ method.)
- **Bake/retopo and weight-transfer verification checklist.** After the dense
  sim: (a) retopo step naming the tool path (Quad Draw/ZRemesh), UV transfer
  via Transfer Attributes, conform-to-sim transfer pass; (b) Marmoset-style
  bake check naming cage/skew review and AO/curvature/cavity/thickness maps;
  (c) rig-fitting gate: garment fitted in A/T-pose (T preferred), weights
  transferred from nearest body verts, then a pose test plus per-bone weight
  inspection (smooth/add/subtract) before export; (d) CRYENGINE skin-vs-sim
  gate: tight/stiff garments default to skin-only, swinging garments to
  simulation, hybrid where only ends move. Also an AutoSim-style gate:
  re-run simulation only after final body animation is marked ready.
  (AutoSim is Marvelous Designer-specific and must not be presented as
  transferable to alterproduct; no source verifies alterproduct supports
  scripting or batch runs.)

## The human method, distilled

1. Design from real sewing patterns, not from a shrink-wrapped mesh.
2. Set the particle resolution before simulating; it is the quality dial.
3. Bake normals and retopo down for low-poly targets instead of simulating
   at low poly.
4. Fit the garment to the existing rig (Mixamo), because that is where the
   characters already live.

## Failure modes

- **Simulating at low poly.** Low-poly sims look bad and cannot be fixed
  afterwards. Generate mid or high poly, then bake normals and retopo down.
- **Expecting a skinned export today.** The skinned export is planned, not
  shipped. What ships now is a static mesh (or shape-key pose) ready for
  Blender auto-rig.
- **Expecting sim parameters.** The author discloses no solver parameters,
  particle counts, or timings. Treat the sim as a black box with one dial:
  particle resolution.

**Depth status:** PARTIAL (full post text plus all 15 comments; the sim has no
disclosed solver parameters, particle counts, or timings, and the video itself
was not frame-reviewed).
