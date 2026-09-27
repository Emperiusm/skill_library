# Example pipeline inventory (TEMPLATE for video-tooling-scout)
**This file is a worked example.** Copy it to `<your-project>-pipeline-inventory.md`
and replace every row with the truth about your own pipeline. A tool/stage is
HAVE only with the evidence cited next to it. Everything else is NEED until
verified against the repo tree or an audit.

The scout diffs videos against every `*-pipeline-inventory.md` in this
folder: one have-vs-need table per inventory, primary first. Keep one
inventory per pipeline; never reuse one inventory for a different project.

## HAVE: asset pipeline (example: Blender + Godot indie project)
- Blender modeling + sculpting, `.blend` sources versioned in `assets/src/`
- Export script `tools/export_gltf.py` (batch .blend -> .glb)
- UV unwrap via built-in Blender unwrap + xatlas for hero assets
  (`tools/uv_xatlas.py`)
- Texture bake to ORM-packed PBR sets (`tools/bake_orm.py`)
- LOD generation via `tools/make_lods.py` (3 levels, screen-size switched)
- Godot 4.x import presets in `project/godot/import_presets.cfg`
- Import smoke test in CI (`.github/workflows/asset-ci.yml`): opens each
  .glb headless, fails on missing materials

## HAVE: runtime / engine
- Godot 4.x presentation + gameplay (`project/`)
- Deterministic fixed-timestep sim core (`project/sim/`)
- Save/load + settings (`project/systems/save.gd`)

## NEED (verified absent as of the example date)
- No rigging / skinning / animation-retarget stage (characters are
  hand-posed; no retargeting)
- No per-asset performance budgets (no tri-count, texel-density, or
  draw-call limits enforced anywhere)
- No automated Godot import validation gate (assets land in-engine
  unchecked; the CI smoke test only opens files)
- No PBR texture/material import policy or material validation
- No mesh compression standard for shipped assets
- No AI-vendor generation/acceptance spec ("what good means" per asset type)

## How to maintain
- When you add a stage, add the evidence (path, workflow, audit date).
- When a gap is filled, move the row to HAVE with evidence and a date.
- Never mark HAVE on "probably": verify first.
