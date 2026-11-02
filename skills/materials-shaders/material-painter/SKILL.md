---
name: material-painter
description: "Paint PBR materials in material-painter, the free open-source Substance Painter alternative: node-graph material design, WGSL custom shader nodes, GPU baking with caching, engine export presets. Trigger when a Substance-free texturing workflow is needed."
---

# material-painter: Free Open-Source Substance Painter Alternative

## Purpose

This skill reconstructs the tool's design from the author's published comments,
step by step, so another agent can evaluate and use it. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The tool's core method is: author materials in a built-in
node graph, extend with WGSL shader nodes, bake on the GPU with caching,
export through engine presets — no proprietary formats anywhere.

## Source

Creator: Admirable-Struggle78 (alla2001 on GitHub).
Reddit post: https://www.reddit.com/r/3Dmodeling/comments/1xkrhq4/i_built_a_free_opensource_alternative_to/
(r/3Dmodeling post 1xkrhq4, score 190, 36 comments) | 2026-11-01 scout run,
audit 1. Repo: https://github.com/alla2001/material-painter

## Tools used

**material-painter** (alla2001/material-painter, free, open source).
Builds: Windows, Linux, Mac (one app for Apple Silicon and Intel; not
notarized yet — first launch: right-click the app and choose Open). The author
wrote it with Claude's assistance: "Claude is not a person, so yeah it's only
me, and I did contribute by debugging and testing so I did help in the
creation process."

## Phase 1: Design the material in the node graph

**Do**
1. Build the material in material-painter's built-in node graph — material
   design happens inside the tool, no external graph editor needed.
2. For custom behavior, write shader nodes directly in **WGSL**.

**Check**
- The graph evaluates live in the viewport; iterate until the material reads
  correctly.

**Why**
- The node graph is the author's named differentiator against ArmorPaint
  ("more mature and battle-tested"): design inside the tool, and WGSL keeps
  custom nodes portable to WebGPU-class targets.

## Phase 2: Bake on the GPU with caching

**Do**
1. Bake textures with the GPU baker.
2. Re-bake incrementally after edits — caching makes unchanged regions
   return near-instantly.

**Check**
- After an edit, re-bake: cached regions should resolve immediately; only
  changed regions recompute.

**Why**
- GPU baking with caching is the second named differentiator. The texture
  bake-test loop is the bottleneck in hand painting; the loop has to be
  cheap or the tool is unusable.

## Phase 3: Export to engine presets

**Do**
1. Export with the built-in presets for **Unreal, Unity, Godot, and Blender**.
2. Verify the exported maps against the target engine's material inputs
   (albedo / normal / roughness / metalness / AO per the preset).
3. If the source material is a Substance file: stop. **`.sbsar`/`.spp` are
   proprietary and cannot be loaded.** Import textures instead.

**Check**
- The exported texture set matches the target engine's expected channels;
  nothing silently dropped.

**Why**
- The author considered importing Substance materials and rejected it on
  copyright grounds ("that seems to be against copyright rules"), so the
  growth strategy is the community making and sharing materials, and the
  interoperability story is export presets instead of format conversion.

## AAA studio practice

AAA texturing standardized on Substance Painter, but the automation doctrine
around it -- bake-first, export presets as contracts, textures as build
artifacts -- transfers to any PBR painter, including an open-source one.

- **Bake-first and preset-export (Splash Damage, Gears Tactics).** The first
  Splash Damage project where Painter became the standard: character smart
  materials "make heavy use of curvature and ambient occlusion maps, so these
  are baked before beginning texturing"; a shared-network Substance Library
  (smart materials, filters, patterns, brushes, and export settings) served
  the internal and outsource teams alike; finished textures were exported
  "using a preset"; custom filters ran built-in QA ("PBR Validation",
  "Tinting Check").
  (https://www.adobe.com/products/substance3d/magazine/destroyed-beauty-texturing-gears-tactics-with-splash-damage.html)
- **Textures as build artifacts (Allegorithmic, GDC 2018 Substance Day).**
  "Substance Automation Toolkit: Building a Future-Proof Material Pipeline":
  automating texture generation, scripting consistent texturing of similar
  objects, and "using a build system to make sure all textures are current
  when 3D models and substance files change."
  (https://80.lv/articles/substance-day-at-gdc-2018/)
- **Version-controlled, build-driven tooling (CD PROJEKT RED, Cyberpunk
  2077).** Custom REDengine-to-Substance bridge ("Remote Browser"), material
  templates via an internal Material Library Manager, pipeline code in
  Visual Studio with their own build system, Helix/Perforce as the data
  repository.
  (https://80.lv/articles/the-texturing-pipeline-in-substance-tools-for-cyberpunk-2077)
- **Channel-mask-driven engine workflows (ILMxLAB, Star Wars: Secrets of the
  Empire, GDC 2018).** Painter-authored multi-channel masks brought into
  Unreal to blend Designer materials -- the export preset is the contract
  between texturing and the engine.
  (https://80.lv/articles/substance-day-at-gdc-2018/)
- **Output templates as shareable contracts (Adobe docs).** Templates control
  naming, channel packing, format, and bit depth; they are saved as
  individual files shareable across users (`assets/export-presets`); the
  `$mesh`, `$textureset`, and `$udim` naming keywords make deterministic,
  machine-checkable naming a first-class feature.
  (https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/export/export-window/output-templates)
- **Headless bake automation (Adobe PySbs batchtools).** The `pysbs.batchtools`
  module wraps the CLI bakers (ambient occlusion, curvature, ...) as Python
  functions with explicit args (output size, dilation, ray counts,
  high/low naming suffixes, format, bit depth) -- the official route to
  CI-style bake loops independent of any GUI.
  (https://helpx-origin.aws116.adobeitc.com/substance-3d-sat/pysbs-python-api/overview/pysbs-batchtools-module.html)
- **Honest gaps:** no named-studio source for AAA production use of Quixel
  Mixer (final offline build released 2026-02-19; its functionality folded
  into Unreal, a dead end for new projects), ArmorPaint, or Material Maker
  as the primary texturing tool -- AAA evidence centers on Painter as the
  standard.
  (https://gamefromscratch.com/epic-games-release-final-free-quixel-mixer/)

## Agent automation

- **Bake-before-paint gate:** script a check that curvature + AO (and normal)
  maps exist on disk and match the low-poly mesh name before texturing
  starts (Splash Damage bake-first convention).
- **Export-template contract check:** store the engine preset/template in the
  project, hash it, and diff against the canonical template before every
  batch export; fail the batch if the template drifted (output templates +
  Gears Tactics shared-library practice).
- **Channel-set validation:** verify the exported map inventory per texture
  set matches the target preset (e.g., Unreal packed: BaseColor, Normal,
  ARM with R=AO / G=Roughness / B=Metallic, packed maps linear with no sRGB)
  and that naming follows the `$mesh_$textureset` keyword expansion.
- **PBR QA pass:** automated check on the exported set mirroring Splash
  Damage's PBR Validation -- base color in plausible luminance range,
  metalness masks binary-ish, roughness present. Thresholds are the agent's
  inference; no studio published theirs.
- **Textures as build artifacts:** on any mesh or material change, re-bake
  and re-export headlessly and fail the check if outputs are stale (GDC
  Automation Toolkit doctrine; CDPR build-system practice).

## The human method, distilled

1. **Ship the tool, grow the asset commons**: the value of a painting tool is
   its materials library — make the community the library (Discord for bug
   reports, releases on GitHub).
2. **Route around proprietary formats** with export presets instead of
   fighting import.
3. **An AI-assisted solo dev can ship a DCC tool**: prompt, debug, test,
   ship. (The thread's own proof: the author built this with Claude.)

## Failure modes

- **Substance lock-in doesn't transfer**: any pipeline relying on `.sbsar`
  procedural graphs has no path into material-painter; plan texture imports
  or rebuilds.
- **Un-notarized Mac build**: first launch requires right-click > Open; this
  is a distribution friction, not a bug.
- **Community-content bet**: the author's strategy assumes a material-sharing
  community forms; today the library is thin (commenter Rikarin's objection:
  "no one will start using it because there's no community/assets available").

**Depth status:** FULL (author's comments carry the feature set, the WGSL /
GPU-bake differentiators, the ArmorPaint comparison, the copyright position,
and the Mac build notes).
