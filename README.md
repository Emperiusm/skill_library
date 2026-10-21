# skill_library

[![CI](https://github.com/Emperiusm/skill_library/actions/workflows/ci.yml/badge.svg)](https://github.com/Emperiusm/skill_library/actions/workflows/ci.yml)
[![License: PolyForm Noncommercial 1.0.0](https://img.shields.io/badge/license-PolyForm%20Noncommercial%201.0.0-2C4DC4)](LICENSE.md)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-2C4DC4)](https://www.python.org)
[![Dependencies: none](https://img.shields.io/badge/dependencies-none-0F7B5F)](https://github.com/Emperiusm/skill_library)

A library of executable skills, grouped by category under [`skills/`](skills/): each
`skills/<category>/<name>/` directory is one skill, a `SKILL.md` playbook that teaches
one workflow end to end. [`video-tooling-scout/`](video-tooling-scout/)
is the tool that learns them: it watches Reddit for tooling videos and turns each one into a
skill. [`skillset/`](skillset/) holds compressed knowledge cards from scout runs (reference
notes, not executable skills).

## The skills

67 skills and counting, in 9 categories. The full list lives in [`skills/`](skills/), which grows with every daily scout run. New this run (2026-10-20): [`toon-2d-in-3d-dynamic-texture`](skills/materials-shaders/toon-2d-in-3d-dynamic-texture/SKILL.md) (classic DBZ cel look in 3D: fake light direction with a target point instead of a real light, drive the drawn cel shapes on a dynamic texture, verify with extreme-zoom closeup animation; neither inverted hull nor grease pencil), [`phosphor-command-code-drawn-procgen`](skills/procgen-worlds/phosphor-command-code-drawn-procgen/SKILL.md) (Phosphor Command pattern: everything drawn by code, no sprites or textures, deliberate phosphor-CRT radar-scope aesthetic; generate operations per contract with a persistent base-builder layer), [`greenscreen-plate-production-keying`](skills/capture/greenscreen-plate-production-keying/SKILL.md) (pro-level greenscreen plates for keying practice: cinema camera, ProRes RAW, in-frame tracking markers, deliberately kept motion-blur/defocus plates, lighting/camera/costume planning so artists build full 3D worlds around the plates). New this run (2026-10-19): [`procgen-racing-track-generator`](skills/procgen-worlds/procgen-racing-track-generator/SKILL.md) (Freeway Fever track recipe: seed polygon, subdivide-and-displace midpoints at segment right angles, bezier handles for smooth curves, bend straight mesh segments along them; intersections plus highway interchanges), [`webgpu-black-hole-raytracer`](skills/engine-runtime/webgpu-black-hole-raytracer/SKILL.md) (interactive Kerr black-hole renderer in the browser with WebGPU: backwards ray integration per pixel, blackbody disk with Doppler shift and gravitational redshift, spin slider 0 to 0.998, Interstellar cinematic grade; Chromium-only reality: Firefox and Brave fail), [`ascii-raymarched-world-grid`](skills/engine-runtime/ascii-raymarched-world-grid/SKILL.md) (single-file raymarched web game on a 2048x2048 one-byte-per-cell material grid: settlements placed first, Dijkstra slope-cost road baking, per-ray material lookup with no SDF). Previous (2026-10-17): New this run (2026-10-17): [`seeded-squad-sim-deterministic-replay`](skills/engine-runtime/seeded-squad-sim-deterministic-replay/SKILL.md) (seeded exactly-reproducible browser sim: one seed determines terrain/weather/forces, separate RNG streams per system, hashed event log plus replay checking, per-soldier deterministic decisions from perception plus morale/cohesion, squads reach platoon HQ through a radio operator). Previous (2026-10-16): [`minimax-h3-refmod-identity-comfyui`](skills/characters/minimax-h3-refmod-identity-comfyui/SKILL.md) (MiniMax H3 character-consistent image generation without LoRA training: bake identity into a RefMod file from 8 photos, then prompt scenes; 8 steps / 6 min, 25 steps / 14 min at 1.8 MP), [`godot-decoupled-rules-json-movie-maker`](skills/engine-runtime/godot-decoupled-rules-json-movie-maker/SKILL.md) (engine-decoupled rules library plus JSON content plus Movie Maker scripted re-shoots: rules as small classes behind a name-to-builder dictionary, ingredients as JSON rule lists, trailers re-shot from the same scripted run). Previous (2026-10-13): [`procedural-pixel-creature-generator-seed-web`](skills/procgen-worlds/procedural-pixel-creature-generator-seed-web/SKILL.md) (seed-driven web pixel-creature generator: one number grows a named creature from 35 body types across 8 sizes 8-1024 px, 8 animations, 7 palettes; mask-plus-cellular-automata growth; PNG/GIF/sprite-strip/12-creature-sheet exports with shareable seed URLs); [`procedural-galaxy-generator-blender`](skills/procgen-worlds/procedural-galaxy-generator-blender/SKILL.md) expanded with Phase 8 (dust lanes as layered volume roles: absorption dust, emission background stars, emissive-particle foreground stars). Previous (2026-10-12): [`ue58-gradient-animated-materials`](skills/materials-shaders/ue58-gradient-animated-materials/SKILL.md) (four gradient-driven UE 5.8 animated materials from one texture pack: matrix-code streaks, dissolve-swap, glow-with-transition, gradient wipe), [`spirula-3dgs-anti-floater-capture`](skills/capture/spirula-3dgs-anti-floater-capture/SKILL.md) (clean 3D Gaussian splats: capture for the move at 4K60, SfM normal/depth estimation, Mild training floater suppression), [`substance-painter-3dspace-blur-filter`](skills/materials-shaders/substance-painter-3dspace-blur-filter/SKILL.md) (kill UV seams with a baked-Position-Map 3D-space blur; bake it down on weak machines), [`nomad-blender-live-link`](skills/automation/nomad-blender-live-link/SKILL.md) (verify the Nomad Sculpt live link to Blender both directions before depending on it; tube tool, brush stroke editing, lattice tool, saved undo history), [`recursive-tree-spawner-parameter-space`](skills/procgen-worlds/recursive-tree-spawner-parameter-space/SKILL.md) (parameter ranges as art direction for procedural trees, plus the prefab to AutoLOD to GPUInstancer/impostors production stack and the LOD-from-recipe alternative). Previous (2026-10-11): [`avatar-model-comparison-harness`](skills/ai-video/avatar-model-comparison-harness/SKILL.md) (evaluate lip-synced AI avatar models with a fixed-input comparison harness: same portrait plus same driving audio, one fixed prompt template, persistent reference cell, per-cell setting labels, and a named failure-mode taxonomy; doubles as an AI-vendor acceptance-spec template). Previous (2026-10-09): [`minimax-h3-character-swap-nomask-lowvram`](skills/ai-video/minimax-h3-character-swap-nomask-lowvram/SKILL.md) (MiniMax H3 character swap with no masking: Character Swap LoRA at 0.4 MP / 8 steps on 6 GB VRAM, reference-latent motion anchoring), [`procedural-galaxy-generator-blender`](skills/procgen-worlds/procedural-galaxy-generator-blender/SKILL.md) (Blender geometry-nodes galaxy generator: point-cloud stars, volumetric far-field glow with energy-preserving crossfade, 3D gravitational lensing, instanced deep-field domains), [`godot-procgen-city-glb-export-schema`](skills/procgen-worlds/godot-procgen-city-glb-export-schema/SKILL.md) (schema-first glb export for Godot procgen cities: document custom glb properties so others can write importers), [`handdrawn-foliage-alpha-cards`](skills/materials-shaders/handdrawn-foliage-alpha-cards/SKILL.md) (hand-drawn foliage as alpha cards: one texture, 1300 faces, hard-edge brush plus masked-opacity material). Previous (2026-10-08): [`minimax-h3-selflift-long-video`](skills/ai-video/minimax-h3-selflift-long-video/SKILL.md) (seamless long-video stitching without color shift), [`runevision-voronoi-terrain-stack`](skills/procgen-worlds/runevision-voronoi-terrain-stack/SKILL.md) (Voronoi macro-cell terrain + runtime instancing stack), [`houdini-net-break-topo-wedge`](skills/simulation-vfx/houdini-net-break-topo-wedge/SKILL.md) (net-break FX with TOPs wedge parameter sweeps), [`baradur-env-breakdown`](skills/simulation-vfx/baradur-env-breakdown/SKILL.md) (labeled-stage VFX environment breakdown assembly); [`omnichar-portable-characters`](skills/characters/omnichar-portable-characters/SKILL.md) expanded with the timbre-only voice-consistency recipe.

## The tool

[`video-tooling-scout`](video-tooling-scout/SKILL.md): the scout that learns the skills above.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/hero-dark.svg">
  <img alt="video-tooling-scout pipeline: Scan Reddit for video posts, Summarize from captions, Extract tooling, Diff against your pipeline inventory, Report have-vs-need." src="docs/assets/hero-light.svg" width="100%">
</picture>

***video-tooling-scout turns "what are other people using to make game assets?" into a maintained,
evidence-based answer.** It watches the subreddits you choose for video posts, extracts the tooling
each video demonstrates (software, plugins, pipeline stages, automation), and diffs it against your
own pipeline inventories to produce per-pipeline have-vs-need tables with gap recommendations. It
never posts, comments, or votes. It only reads.*

> [!NOTE]
> **What ships today is the read loop:** scan → summarize → extract → diff → report, plus the
> append-only watchlist with trend detection and a keyword/meaning-matched P1/P2 gap-alert list.
> What is deliberately not here: any posting or commenting, any automatic tool installation, and any
> download of video files in scheduled runs. See [Status](#status-and-evidence).

<table>
<tr>
<td valign="top" width="33%">

***Get going***
- [Install](#install)
- [Quick start](#quick-start)
- [Schedule it](#scheduling)

</td>
<td valign="top" width="33%">

***How it works***
- [The map](#the-map)
- [Scan](#1-scan)
- [Summarize](#2-summarize-captions-and-metadata-only)
- [Extract and diff](#3-extract-tooling-4-diff-against-your-inventories)
- [Watchlist trending](#watchlist-trending-and-gap-alerts)

</td>
<td valign="top" width="33%">

***Why you can trust it***
- [Why it exists](#why-it-exists)
- [Status and evidence](#status-and-evidence)
- [Security and known limits](#security-and-known-limits)
- [Licence](#licence)

</td>
</tr>
</table>

## The map

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/hero-dark.svg">
  <img alt="The scout loop: 1. Scan subreddits via Arctic Shift, 2. Summarize from captions/metadata with no downloads, 3. Extract tools/plugins/stages, 4. Diff against your pipeline inventory, 5. Report have-vs-need with gap alerts." src="docs/assets/hero-light.svg" width="100%">
</picture>

The loop is one direction: Reddit → your reports directory. The scout's only persistent state is
`video-tooling-scout/references/tooling-watchlist.md`, which is append-only: entries are never deleted, only annotated
(adopted, superseded, skipped, seen-again dates). A claim of "your pipeline has this" requires
evidence (a file path, a CI workflow, or an audit citation); "probably has it" is treated as NEED
until verified.

## Why it exists

Scrolling game-dev subreddits for tooling ideas doesn't scale, and memory doesn't either: the same
interesting tool resurfaces three times and nobody notices it's a trend. video-tooling-scout
externalizes that memory. It scores posts by tooling relevance (not just votes), summarizes each
video from captions and metadata, extracts every named tool and pipeline stage with a source quote,
and compares the findings against a written inventory of *your* pipeline, so the output is "here's
what you're missing" instead of "here's what's popular".

| Principle | What it means in practice |
|---|---|
| **Evidence over vibes** | A tool is HAVE only with repo evidence. A tool is recommended only with a source quote from a video or its comments. |
| **Reads only** | No posting, commenting, voting, or tool installation. The public web is read through public APIs. |
| **Scheduled runs never ask** | Cron/ unattended runs are captions-and-metadata only and must never trigger approval or login prompts. Downloads happen only in interactive runs, and only with the operator's explicit per-video go-ahead. |
| **Memory is append-only** | The watchlist and the gap list are annotated, never rewritten. History survives the operator's changing mind. |

<details>
<summary><b>Vocabulary</b></summary>

| Term | Meaning |
|---|---|
| **Scan** | `video-tooling-scout/scripts/scan_videos.py`: pulls recent video posts from `video-tooling-scout/subreddits.yaml` via the Arctic Shift public API and ranks them by tooling relevance × engagement. |
| **Pipeline inventory** | A `video-tooling-scout/references/*-pipeline-inventory.md` file describing what your pipeline already does (HAVE) and verified-absent gaps (NEED). Copy [`video-tooling-scout/references/example-pipeline-inventory.md`](video-tooling-scout/references/example-pipeline-inventory.md) to start. |
| **Have-vs-need** | Per-inventory table marking each found tool HAVE / PARTIAL / NEED with pipeline evidence and a recommendation (adopt now / backlog / watchlist / skip + why). |
| **Gap alert** | An extracted tool that matches [`video-tooling-scout/references/p1-gaps.md`](video-tooling-scout/references/p1-gaps.md) by keyword *or* meaning. Reported at the very top of the run report and the operator summary. |
| **Watchlist** | [`video-tooling-scout/references/tooling-watchlist.md`](video-tooling-scout/references/tooling-watchlist.md): the keep-on-the-side list of interesting tools. `video-tooling-scout/scripts/trend_watchlist.py` annotates reappearances; three or more sightings flag a tool TRENDING. |
| **Operator** | The human running the scout. Only the operator approves downloads; scheduled runs never ask. |

</details>

## Install

| You need | For |
|---|---|
| **Python 3.11+** on `PATH` | Everything. There are **no runtime dependencies**: every script is standard-library only (`urllib`, `json`, `re`), so installing it can't hit a resolver conflict. |
| `git` | Cloning, and the CI compile check |
| A captions-capable video summarizer (optional) | Deeper YouTube/Vimeo analysis. The loop works without one: captionless videos fall back to metadata + description, and native Reddit videos are analyzed from post text and comments. |
| A reports directory of your choice | Run output, e.g. `~/video-tooling-scout-reports/` |

```bash
git clone https://github.com/Emperiusm/skill_library.git && cd skill_library
python3 -m py_compile video-tooling-scout/scripts/*.py   # the whole gate: stdlib only, compiles clean
```

Copy the templates before your first run:

```bash
cp video-tooling-scout/references/example-pipeline-inventory.md \
   video-tooling-scout/references/my-pipeline-inventory.md
# then edit my-pipeline-inventory.md, p1-gaps.md, and
# video-tooling-scout/subreddits.yaml
```

## Quick start

New here? Read [`video-tooling-scout/references/example-run-report.md`](video-tooling-scout/references/example-run-report.md) first:
it's a full real run (24 videos, every one audited at full depth) showing exactly what each step below produces. Then:

```bash
# 1. Scan the last 2 days of your subreddits, ranked by tooling relevance.
python3 video-tooling-scout/scripts/scan_videos.py 2 > /tmp/scan.json

# 2. Summarize the top videos (captions/metadata; your summarizer of choice),
#    or pull the comment threads where the tooling details live:
python3 video-tooling-scout/scripts/fetch_comments.py <post_id>:<num_comments> [...]

# 3. Extract tooling per video (software, plugins, stages, automation),
#    each with a source quote, and diff against your inventories.

# 4. Flag reappearances on the watchlist (appends "seen again <date>"):
python3 video-tooling-scout/scripts/trend_watchlist.py --date 2026-09-27 "<tool 1>" "<tool 2>" ...

# 5. Write the report (have-vs-need-YYYY-MM-DD.md) to your reports directory
#    and append genuinely new tools to
#    video-tooling-scout/references/tooling-watchlist.md.
```

See [`SKILL.md`](video-tooling-scout/SKILL.md) for the full operator playbook: the workflow steps, the output
contract every run delivers, and the operating rules (including the approval rule).

## How it works

### 1. Scan

`video-tooling-scout/scripts/scan_videos.py` reads `video-tooling-scout/subreddits.yaml` (hand-editable; one subreddit per line, no `r/` prefix), pulls recent
posts from each via the Arctic Shift public API (`https://arctic-shift.photon-reddit.com`), and
keeps video posts: YouTube / Vimeo links and native Reddit video. Posts below `min_score`
(default 20) are dropped. Each survivor is scored:

- **Tooling relevance:** keyword hits against a built-in list (blender, houdini, substance, rig,
  retopo, UV, LOD, nanite, bake, mocap, comfyui, text-to-3d, geometry nodes, CI/CD, …).
- **Engagement:** score capped at 500, scaled down. Posts with **zero** tooling keywords get only
  20% of the engagement contribution, so a viral pure-eye-candy clip can't outrank real tooling
  content on votes alone.

Output is ranked JSON to stdout: title, author, URL, permalink, score, comment count, tooling
keyword hits, and a relevance number. Deep analysis is capped (default 8 videos per run).

### 2. Summarize (captions and metadata only)

- **YouTube / Vimeo:** your captions-first summarizer. Never invent transcript lines or tool
  mentions. If a video has no captions, use its metadata + description and move on.
- **Native Reddit video:** the clip is short; the signal is in the post text and the comments.
  `video-tooling-scout/scripts/fetch_comments.py <post_id>[:num_comments]` pulls top comments from Arctic Shift, and when
  Arctic Shift returns zero comments for a post that has some (a known index coverage gap), it
  falls back automatically: old Reddit JSON first, then the PullPush API. Also check YouTube
  demo/tutorial links found in the comments; they often contain the real breakdown.

The default loop **never downloads video or model files**. The approval rule is in
[`SKILL.md`](video-tooling-scout/SKILL.md): scheduled runs are strict (kill anything that hits an approval gate,
never retry); interactive runs may download a captionless video for transcription only with the
operator's explicit per-video go-ahead, capped at 3 per run, with a per-host 3-prompt kill guard
so a retry loop can never recur.

### 3. Extract tooling, 4. Diff against your inventories

Per video, reconstruct the full workflow: exact tools used, a phased workflow with `Do`,
`Check`, and `Why` per phase, exact parameters/values/costs/benchmarks where the captions,
comments, or metadata support them, and the human/process principles underneath. Never
invent transcript lines or parameters; label inferences clearly. Videos that can't reach
full depth on captions/metadata alone are marked `DEPTH-LIMITED` with the reason stated.
See [`SKILL.md`](video-tooling-scout/SKILL.md) for the complete audit standard. Then diff against every `video-tooling-scout/references/*-pipeline-inventory.md`: one
have-vs-need table per inventory, primary first, each tool marked HAVE / PARTIAL / NEED with
pipeline evidence and a recommendation (adopt now / backlog / watchlist / skip + why). A tool
can be NEED for one pipeline and HAVE for another; the tables say so.

### Watchlist trending and gap alerts

After extraction, `video-tooling-scout/scripts/trend_watchlist.py --date YYYY-MM-DD "<tool>" ...` compares tool names
against the watchlist (case-insensitive substring + token overlap, both directions), appends
"seen again <date>" to reappearing rows in place, and prints a "Watchlist trending" snippet for
the report. A tool seen three or more times is flagged **TRENDING**.

Separately, every extracted tool is checked against `video-tooling-scout/references/p1-gaps.md` by keyword **and**
by meaning. Matches become **gap alerts** at the very top of the report and the operator's
summary, never buried in the tables.

## Scheduling

The loop is designed for a daily cron: scan the prior two days, deep-analyze up to 8 videos,
diff against all inventories, check gap alerts, detect trending tools, update the watchlist,
write a dated report. Two constraints for scheduled runs:

1. **No approvals, ever.** Captions and metadata only. If a command hits an approval gate, kill
   it and skip the item; never retry. If a host prompts repeatedly, stop hitting it for the rest
   of the run.
2. **Explicit paths.** Cron workers don't inherit your shell `PATH`; resolve `python3` (e.g.
   `/usr/bin/python3`) and any script paths explicitly in the crontab.

Example:

```cron
18 8 * * * cd /path/to/skill_library && /usr/bin/python3 video-tooling-scout/scripts/scan_videos.py 2 > ~/video-tooling-scout-reports/scan-$(date +\%F).json
```

(Adapt to your full run wrapper; the report writing and watchlist update are operator steps per
[`SKILL.md`](video-tooling-scout/SKILL.md).)

## Status and evidence

| Component | Status | Evidence |
|---|---|---|
| `video-tooling-scout/scripts/scan_videos.py` | Implemented, live against Arctic Shift | Ranked JSON output; zero-tooling-signal downweight verified in runs |
| `video-tooling-scout/scripts/fetch_comments.py` | Implemented, fallback chain verified | Old Reddit JSON bot-walled from some sandboxes; PullPush recovered comments in testing |
| `video-tooling-scout/scripts/trend_watchlist.py` | Implemented | Appends "seen again" in place; TRENDING flag at 3+ sightings |
| Watchlist / gap list | Append-only by convention | `trend_watchlist.py` never deletes; `p1-gaps.md` maintained the same way |
| CI | `py_compile` on `video-tooling-scout/scripts/*.py` | [`.github/workflows/ci.yml`](.github/workflows/ci.yml) |
| Tests | None beyond compilation | Honest limit: no unit test suite ships yet |

**Not implemented:** automatic posting/commenting (deliberately out of scope), automatic tool
installation, video downloading in scheduled runs, a web UI, multi-operator support.

## Security and known limits

The threat model and what's deliberately not defended are in [`SECURITY.md`](SECURITY.md).
The short version:

| Limit | What it means |
|---|---|
| **Third-party APIs are trusted, not verified** | Arctic Shift, PullPush, and Reddit JSON can be down, rate-limited, or stale. Runs degrade gracefully and say so; they don't verify the APIs' answers. |
| **Captions are author-supplied** | They can be wrong. Every extracted claim should carry a source quote so the operator can check. |
| **Watchlist matching is fuzzy** | Token-overlap matching can near-miss. Matches are surfaced for the operator, not trusted blindly. |
| **No test suite** | The gate is `python3 -m py_compile video-tooling-scout/scripts/*.py`. Behavioral regressions are caught by the operator reading reports, not by tests. |
| **The example inventory is fictional** | `video-tooling-scout/references/example-pipeline-inventory.md` is a template. Your have-vs-need tables are only as honest as the inventory you write. |

## Documentation

| Document | What it covers |
|---|---|
| [`SKILL.md`](video-tooling-scout/SKILL.md) | **The operator playbook.** Workflow steps, output contract, operating rules. This governs a run. |
| [`video-tooling-scout/references/example-run-report.md`](video-tooling-scout/references/example-run-report.md) | **A finished run, in full.** Read this first: gap alerts, per-inventory have-vs-need tables, trending, non-goals, and a full-depth workflow audit for every one of the 25 audited videos. This is what your runs should look like. |
| [`skillset/`](skillset/) | **The library.** Durable skill cards promoted from run reports: what each learned skill does, where it was learned from, the evidence, the compressed workflow. Four example cards included. |
| [`video-tooling-scout/references/example-pipeline-inventory.md`](video-tooling-scout/references/example-pipeline-inventory.md) | Template pipeline inventory (HAVE with evidence, verified NEED). Copy and fill in. |
| [`video-tooling-scout/references/p1-gaps.md`](video-tooling-scout/references/p1-gaps.md) | Gap-alert template: format, example rows, maintenance rules. |
| [`video-tooling-scout/references/tooling-watchlist.md`](video-tooling-scout/references/tooling-watchlist.md) | The append-only watchlist; 3 labeled example rows show the format. |
| [`video-tooling-scout/subreddits.yaml`](video-tooling-scout/subreddits.yaml) | Hand-editable subreddit list and scan defaults. |
| [`SECURITY.md`](SECURITY.md) | Threat model, known limits, how to report a vulnerability. |

## Contributing

The short version:

- **Standard library only.** Every script must run on `python3` with no installs.
  A dependency added to look sophisticated is supply-chain surface bought for nothing.
- **`python3 -m py_compile video-tooling-scout/scripts/*.py` must pass.** CI enforces it.
- **Keep it read-only.** No posting, commenting, voting, or downloading in the default
  loop. Proposals that add outbound actions need an explicit operator-approval design.
- **Don't invent evidence.** Summaries cite sources; HAVE requires a cited file path,
  workflow, or audit.
- **By submitting a contribution you agree it may be distributed under the PolyForm
  Noncommercial licence** (see [`LICENSE.md`](LICENSE.md)).

## Security reporting

Please don't open a public issue for a vulnerability. Use GitHub's **private vulnerability
reporting** (the repository's *Security* tab → *Report a vulnerability*). What the project
defends, and what it doesn't, is in [`SECURITY.md`](SECURITY.md).

## Licence

video-tooling-scout is **source-available** under the [PolyForm Noncommercial License
1.0.0](LICENSE.md). It isn't open source.

| | |
|---|---|
| **Free** | Non-commercial use: research, experiments, personal study and hobby projects, and use by charities, educational institutions, public research organisations and government. Keep the `Required Notice:` line from [`LICENSE.md`](LICENSE.md) with any copy you share. |
| **Paid** | Commercial use, including internal use inside a company. Contact the copyright holder for a commercial licence. |
