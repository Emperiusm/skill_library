---
name: opsis-comfyui-film-studio
description: "Run a self-hosted AI film studio on ComfyUI: API-format graphs plus .map.yaml become priced forms, a local 12GB path or RunPod serverless path, mock mode by default. Trigger when non-technical users need form-based access to ComfyUI workflows with per-shot cost estimates."
---

# Opsis: Self-Hosted AI Film Studio on ComfyUI

## Purpose

This skill runs Opsis (sanchezrobertodev), an open-source, self-hosted
AI film studio built on ComfyUI graphs: simple forms on top of real
ComfyUI graphs, where an API-format graph plus a small `.map.yaml`
becomes a form with a price estimate. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The core method is: **a ComfyUI API-format graph plus
a `.map.yaml` becomes a priced form; the same studio runs local, on
RunPod, or in mock mode.**

## Source

r/comfyui, sanchezrobertodev, "Opsis: an open-source, self-hosted
Higgsfield-style studio built on ComfyUI graphs" (Apache, score 21, 6
comments, 2026-10-30):

- https://www.reddit.com/r/comfyui/comments/1xjhrq6/
- Native Reddit video: v.redd.it/os8ikk55dmyh1
- Repo: https://github.com/sanchezrobertodev/opsis
- License: Apache (per post title; inference from the title claim)

Evidence note: all facts below are the author's claims from the post
text. The 6 comments are all snark ("slop" accusations, a
backward-feet callout at 0:25, a lamp continuity complaint) with zero
tooling signal; they are recorded as hostile-thread evidence, not
evidence of the tool. No third-party verification in this audit.

## Tools used

- Opsis, self-hosted AI film studio; simple forms on top of real
  ComfyUI graphs
- Local GPU path: Wan 2.2 5B and FLUX.2 klein 4B on a 12 GB card, core
  nodes only
- RunPod path: LTX-2.5, Wan 2.2 14B Fast, VACE, Wan Animate-2, Uni3C,
  Wan-Move on a serverless ComfyUI worker
- Graph-to-form: an API-format graph plus a small `.map.yaml` (which
  node inputs to fill) becomes a form with a price estimate
- Studios: video and image, motion control, object swap, characters,
  faceless studio, cinema studio, 3D blocking
- Mock mode by default (click through everything with no GPU and no
  keys)
- Hosted models optional with your own keys: Veo, Kling, Seedance,
  ElevenLabs

## Phase 1: Pick a studio and a compute target

**Do**
1. Choose a studio: video and image, motion control, object swap,
   characters, faceless studio, cinema studio, or 3D blocking.
2. Run on your GPU (Wan 2.2 5B + FLUX.2 klein 4B on a 12 GB card, core
   nodes only) or on RunPod (LTX-2.5, Wan 2.2 14B Fast, VACE,
   Wan Animate-2, Uni3C, Wan-Move on a serverless ComfyUI worker).

**Check**
- The form shows a price estimate before you run (RunPod path).

**Why**
The 12GB local path uses small models and core nodes only; the heavy
path is priced serverless. The user picks the cost/quality point per
shot.

## Phase 2: Fill the form, not the graph

**Do**
1. Fill the simple form; behind it, the `.map.yaml` maps your inputs
   onto the real ComfyUI graph's node inputs.
2. To add a new workflow, write YAML, not code: API-format graph +
   `.map.yaml`.

**Check**
- New workflows appear as forms with price estimates, with no code
  deploy.

**Why**
"a new workflow is YAML, not code." The graph stays the source of
truth; the form is a generated view.

## Phase 3: Try everything in mock mode first

**Do**
1. Click through every studio in mock mode (the default): no GPU, no
   keys required.
2. Add your own keys only for the hosted models you actually use (Veo,
   Kling, Seedance, ElevenLabs).

**Check**
- The full flow works end-to-end in mock before spending GPU time or
  money.

**Why**
Mock-by-default removes the setup tax; keys are per-model and
optional.

## AAA studio practice

- Weta Digital partnered with Autodesk to productize its proprietary,
  Academy Award-winning VFX tools (Lord of the Rings, Avatar, Game of
  Thrones, Planet of the Apes) as a subscription cloud service embedded
  in Maya: "the first step in the democratization of VFX and animation
  production," giving artists "powerful new effects tools and time-saving
  automation capabilities." Opsis's graph-to-form idea is the same
  democratization move one level down: expert graphs wrapped so
  non-technical users can run them without touching nodes.
  https://creativecow.net/weta-digital-partners-with-autodesk-to-offer-next-generation-creative-cloud-production-pipeline/
- Weta FX and AWS are building AI tools for VFX artists on an
  artist-first principle: "no clunky prompt engineering," systems that
  "respond to the way artists work," with direct manipulation and live
  feedback instead of text-box guessing. The skill's priced-form UI is
  that principle applied to ComfyUI: the graph stays the source of
  truth, and the human only sees inputs that matter, priced.
  https://completeaitraining.com/news/weta-fx-and-aws-partner-on-ai-that-puts-vfx-artists-in/
- Production cost math is per-unit and upfront: cost per frame = render
  time per frame x cost per hour, with the honest version adding boot,
  upload, setup overhead plus a 10-15% buffer for rerenders ("Estimated
  cost = (Setup + Simulation + Rendering + Buffer) x Hourly Rate",
  citing sidefx.com). Opsis's price estimate on the form is this
  practice operationalized: the user sees the number before spending
  GPU time or money.
  https://irendering.net/how-to-calculate-real-cost-per-frame-before-you-hit-render/
  https://irendering.net/how-much-does-it-cost-to-render-a-houdini-shot-in-the-cloud/
- VFX veteran Joseph Bell (years at Industrial Light & Magic) notes the
  biggest driver of VFX budget overruns is not shot complexity but scope
  drift, and recommends budgeting a 15-20% contingency on the VFX line
  (Vitrina's 2026 VFX budget breakdown; Netflix, Warner Bros, and
  Paramount use Vitrina to source VFX vendors). Inference: a priced form
  should log estimate-vs-actual per shot so drift is visible early; that
  is the same discipline at studio scale.
  https://vitrina.ai/blog/vfx-budget-breakdown-2026/

## Agent automation

- Workflow onboarding checklist: for each new API-format graph, verify
  (1) the graph loads as a ComfyUI API-format graph, (2) the
  `.map.yaml` maps every form input to a real node input id, (3) a price
  estimate appears on the form before submit. An agent adds a workflow
  by writing these two files only; the checklist confirms the form was
  generated correctly, no code deploy involved.
- Run ledger: for every RunPod (paid) run, append one row to
  `run-ledger.csv`: shot id, workflow, compute target, model, frames,
  estimated cost, actual cost, variance. Inference: review the ledger
  regularly; persistent variance is a signal the estimate formula needs
  recalibration, not a number to absorb silently.
- Mock gate: no paid run starts without a completed mock-mode pass of
  the same workflow first. The agent treats mock success as the
  acceptance test for real runs; mock failures are fixed in the YAML,
  never in the graph.
- Budget guard: keep `budget-log.md` with per-shot estimate vs actual
  and flag any shot whose actual exceeds its estimate past the 15-20%
  contingency cited above. Inference: this is the agent version of
  Bell's contingency discipline, catching scope drift before it
  compounds.

## The human method, distilled

1. **Forms over graphs**: expose only the inputs that matter, priced.
2. **Three compute targets** (local 12GB / RunPod serverless / mock)
   cover the whole cost curve.
3. **Work in progress, feedback welcome**, the author positions it as
   an open build, not a launch.

**Depth status:** FULL (author post text; the 6 comments are all snark
with zero tooling signal, noted as hostile-thread evidence).
