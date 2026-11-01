---
name: open-h3-regenerate-2k-refine
description: "Refine 24fps AI video with NVIDIA's Open-H3-Regenerate-2K in ComfyUI: merged refiner plus LightX2V FL2VA Turbo plus LMS Sharp adapter, noise 0.5 to 0.7 or upscale-only mode, independent windows for long clips. Trigger when H3 or 24fps generated footage needs detail refinement and 2K upscale."
---

# Open-H3-Regenerate-2K for ComfyUI: Refine and Upscale 24fps Video

## Purpose

This skill wraps NVIDIA's Open-H3-Regenerate-2K in ComfyUI custom
nodes (imlo2): take an existing 24fps generation (or native
MiniMax-H3 latents) and run NVIDIA's merged refiner/upscaler over it
with adjustable noise, in independent windows for long clips. Every
phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: **feed
24fps footage, pick a noise level from the comparison ladder, fit the
windows in VRAM.**

## Source

r/comfyui, imlo2, "Open-H3-Regenerate-2K for ComfyUI: refinement
nodes, noise controls and comparison examples" (score 24, 18 comments,
2026-10-30):

- https://www.reddit.com/r/comfyui/comments/1xjbwoe/
- Native Reddit video: v.redd.it/li33sky01lyh1
- Nodes: https://github.com/o-l-l-i/ComfyUI-Olm-Open-H3-Regenerate-2K
- Model card: https://nvlabs.github.io/Sana/Open-H3-Regenerate-2K/
- Model source:
  https://github.com/NVlabs/Sana/tree/sol-engine/models/Open-H3-Regenerate-2K
- Weights: https://huggingface.co/Efficient-Large-Model/Open-H3-Regenerate-2K

Evidence note: all facts below are the author's claims from the post
text plus the author's comment replies (exact parameters, VRAM
numbers, and failure modes). The 18 comments include parameter
discussion and a tested no-stacking rule. No third-party verification
in this audit.

## Tools used

- ComfyUI custom nodes wrapping NVIDIA's Open-H3-Regenerate-2K
  (published merged adapters, Sharp curve branches, learned latent
  upscaler)
- The merged single LoRA is: **refiner + LightX2V's FL2VA Turbo + LMS
  Sharp adapter**, "For these few steps the refiner is merged with
  LightX2V's FL2VA Turbo and the LMS Sharp adapter into a single LoRA"
- Refines existing 24fps video or native MiniMax-H3 latents
- Adjustable noise; upscale-only mode; memory controls
- Example workflows, test clip, and detailed comparison images in the
  repo
- Competing option: Kijai's LoRA (the author thinks it contains the
  refiner only, not the merged turbo/sharp stack)

## Phase 1: Feed it 24fps video or H3 latents

**Do**
1. Load a 24fps video. The node historically raised
   `ValueError("H3 refinement expects 24 fps; resample in your video
   loader first")` on anything else; the author has since added a
   feature so the node can digest different-fps inputs itself.
2. Or feed native MiniMax-H3 latents directly.

**Check**
- The reference example: 1344x768 source refined to 2560x1440, two
  steps from noise 0.5.

**Why**
The refiner is trained on 24fps H3 output; off-rate inputs break its
temporal assumptions. The author fixed the footgun in the node rather
than documenting around it.

## Phase 2: Set noise and mode

**Do**
1. Choose upscale-only mode (adds texture/definition, minimal change)
   or noise mode. The README compares upscale-only vs noise 0.5 / 0.6
   / 0.7, pick your level from the comparison images, not from
   description.
2. For longer clips, process in independent windows (window boundaries
   may show).
3. Do NOT stack another turbo LoRA on top of the merged one. A
   commenter tested Kjai's LoRA + light2x turbo + lms lora manually
   stacked and it looked worse than the merged one: "They already have
   turbo lora unlike Kjai's one so dont stack more turbo."

**Check**
- Faces, jewelry, lettering, and small patterns WILL change under
  noise. Commenters report talking and emotional scenes "get
  butchered"; low-res sources look better after refinement.

**Why**
The merge is the product: refiner + turbo + sharp adapter in one LoRA.
Stacking more turbo on top degrades the result. Noise is a change
budget, and human faces are where the budget gets spent first.

## Phase 3: Fit it in VRAM

**Do**
1. The author tested on Windows, RTX 5090 (32 GB VRAM), 128 GB RAM:
   "probably runs at least on an RTX 4090, and you can dial down a few
   settings to try to make it fit." Smaller cards are unvalidated.
2. Expect high RAM and VRAM consumption; dial the memory controls down
   if VRAM is tight.

**Check**
- Watch VRAM during the first window; reduce window size or settings
  before committing to the full run.

**Why**
The learned latent upscaler plus merged adapters is heavy by design;
the author is explicit that this is a 4090-class tool.

## AAA studio practice

**EA / Petroglyph Games: AI-upscaled FMV shipped in Command & Conquer:
Remastered Collection (released June 5, 2020).** When the original FMV
master tapes proved unrecoverable (the tapes found in EA's archive were
copies of the same low-resolution game files, further degraded by media
decay), the production remastered the cutscenes from the best surviving
source with an AI upscaling algorithm built in collaboration with members
of the C&C community who had already experimented with this. The team
then spent months iterating on resolution, frame-rate conversion, and
reworked audio before locking the result. Three practices map directly
onto this skill:

1. **Source selection is part of refinement.** EA used the console
   (PlayStation / Sega Saturn) MPEG versions of the FMV rather than the
   PC's original-format files, because the MPEG sources upscaled better.
   Translation for this skill: if you have multiple sources (H3 latents
   vs exported video vs an older render), run the noise ladder on the
   highest-fidelity one. The skill's "low-res sources look better after
   refinement" is the same rule from the other direction.
   Sources: https://kotaku.com/ea-went-digging-through-old-90s-tapes-trying-to-remaste-1842131796
   https://www.pcgamesn.com/command-and-conquer-remastered/fmv

2. **Refinement is an iterative comparison loop, not a single pass.** The
   months-long "ironing out" of resolution, 30fps frame rate, and audio
   is the production-scale version of this skill's Phase 2 noise ladder:
   lock the setting from side-by-side evidence, never from a description.
   (Inference, labeled: AAA remaster budgets let them iterate for months;
   the affordable equivalent here is the four-setting ladder on one
   representative window, formalized in A2 below.)
   Source: https://dontfeedthegamers.com/command-and-conquer-remastered-cutscenes-fmv-ai/

3. **Normalize frame rate inside the refinement pass.** Petroglyph's
   pipeline interpolated the 15fps originals to 30fps as part of the AI
   pass. This is the shipped-game version of the skill's 24fps rule:
   temporal assumptions must hold before refinement, so frame-rate
   handling belongs in the same job, not in a separate manual step.
   Source: https://www.pcgamesn.com/command-and-conquer-remastered/fmv

**Lionsgate / Runway: custom AI video model trained on a studio catalog
(announced September 2024).** Lionsgate gave Runway access to its
~20,000-title film and TV catalog to train a custom model exclusive to
Lionsgate, designed so the model "generates cinematic video that can be
further iterated using Runway's suite of controllable tools" and "help
Lionsgate Studios, its filmmakers, directors and other creative talent
augment their work." Initial applications were scoped to storyboard
creation, background design, and special effects. Two practices:

4. **Treat AI video output as an intermediate, never the final.** The
   studio model generates; artists then refine with controllable tools.
   This is exactly this skill's posture: H3 (or 24fps) generation is the
   intermediate, the refiner/upscaler is the controllable second pass.
   Scope the refiner's change budget the way a studio would: decide what
   is allowed to change (texture, definition) and what is not (faces,
   lettering, small patterns; per this skill's Phase 2, those WILL change
   under noise).
   Source: https://www.c21media.net/news/ai-firm-runway-to-mine-lionsgates-library-via-first-major-pact-with-a-studio/

5. **Match the refinement stack to the footage's own look.** Lionsgate's
   custom model exists so generated and processed video stays inside the
   studio's visual world. (Inference, labeled: the community analogue is
   the skill's existing rule, H3 refiner for H3 latents, and never
   stacking a foreign turbo LoRA on top of the merged one; mismatched
   stacks drift the look.)
   Source: https://www.notebookcheck.net/Lionsgate-s-entire-film-catalog-can-now-be-used-to-train-custom-Runway-AI-text-to-video-model.890934.0.html

## Agent automation

Turn the manual checks into executable, logged steps. Every run starts
from a manifest and ends in a log; no full-length run starts before the
ladder is locked.

### A1: Write the run manifest

**Do**
1. Create `run-manifest.json` next to the input with: `input_path`,
   `fps`, `width`, `height`, `mode` (`upscale-only` or `noise`),
   `noise_level` (0.5, 0.6, or 0.7), `window_seconds`,
   `window_overlap_seconds`, `gpu_model`, `vram_gb`,
   `source_provenance` (which source file, and why it is the best
   available, per AAA practice 1).
2. Get fps and size with:
   `ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate,width,height -of default=noprint_wrappers=1 input.mp4`
3. Get GPU with:
   `nvidia-smi --query-gpu=name,memory.total --format=csv,noheader`

**Check**
- The manifest exists and every field is filled; `noise_level` is one of
  the four tested settings (upscale-only, 0.5, 0.6, 0.7), never an
  untested value.

**Why**
The manifest makes the run reproducible and auditable; it is the agent's
equivalent of the production's locked settings.

### A2: Run the noise ladder before committing

**Do**
1. Cut one representative window (5 to 10 seconds, containing a face and
   lettering if the clip has any) and render it at all four settings:
   upscale-only, noise 0.5, 0.6, 0.7.
2. Save the four renders as `ladder/<setting>.mp4` and record the chosen
   setting plus a one-line reason in the manifest.

**Check**
- Compare at 100 percent on faces, jewelry, lettering, and small
  patterns; pick the highest setting whose changes are acceptable. (AAA
  practice 2: lock from evidence.)

**Why**
Petroglyph's months of iteration are unaffordable per clip; a
four-setting ladder on one window is the affordable version of the same
discipline.

### A3: Guard the LoRA stack automatically

**Do**
1. Before queueing, read the ComfyUI workflow JSON (or API prompt) and
   list every LoRA node by name. Abort if any turbo LoRA other than the
   merged `refiner + LightX2V FL2VA Turbo + LMS Sharp` stack is present.
   (This is the tested no-stacking rule from the skill's Phase 2.)

**Check**
- The LoRA-name listing is saved into the run log; zero extra turbo
  LoRAs.

**Why**
A second turbo on top of the merged one measurably degrades the result;
the check is cheaper than a ruined run.

### A4: Check window boundaries

**Do**
1. After processing, extract the last 2 seconds of each window and the
   first 2 seconds of the next, and view the join at 100 percent; record
   "boundary clean" or "boundary visible" per join in the run log.
2. If a boundary is visible, re-render that join with increased overlap
   before the full-length commit. (Inference, labeled: overlap size is an
   operator-set value; the skill's source only reports that boundaries
   "may show.")

**Check**
- Every window join has a logged verdict.

**Why**
Independent windows are the skill's long-clip strategy; the join is its
known failure mode, so it gets an explicit gate.

### A5: VRAM preflight

**Do**
1. Compare `vram_gb` from the manifest against the tested envelope:
   RTX 5090 32GB (tested), RTX 4090 (author's stated
   minimum-ish expectation), smaller cards unvalidated.
2. Below 4090-class, require `window_seconds` to be reduced in the
   manifest before the first window runs; log the reduction.

**Check**
- The first window completes without an out-of-memory error; if it OOMs,
  halve `window_seconds` and retry once, then stop and report.

**Why**
The author's numbers are the only tested envelope; the preflight turns
"dial it down" into a rule.

### A6: Append to the run log

**Do**
1. Append one JSON line per run to `runs.log`: date, manifest id, mode,
   noise level, window count, boundary verdicts, chosen source, outcome
   (shipped / rejected / retried).

**Check**
- `runs.log` exists and the new line parses as JSON.

**Why**
The log is the audit trail: it turns one-off refinements into a corpus
you can learn noise preferences from, the way the C&C team's iteration
built institutional knowledge.

## The human method, distilled

1. **"IMHO it's a bit like SoL-Refiner when it comes to output"**,
   calibrate expectations against a known refiner before adopting.
2. **When users hit the 24fps wall, fix the node** (fps digestion),
   don't write a FAQ.
3. **Ship comparison images** (upscale-only vs 0.5/0.6/0.7) so users
   pick noise from evidence, not vibes.

**Depth status:** FULL (author post text + author comments with exact
parameters, VRAM numbers, and failure modes).
