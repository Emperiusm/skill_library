---
name: ai-3d-text-to-3d-prompting
description: "Turn text prompts into usable assets: a specificity ladder, candidate selection, the three gaps that break prompts, a 60-second triage, and the rule for switching to a reference once a look is right. Trigger when prompting a text-to-3D tool for production assets."
---

# Text-to-3D Prompting for Production Assets

## Purpose

This skill treats prompting as input craft with a ceiling, not as the
whole pipeline: prompts explore, references lock, and the steps after
the prompt make the asset shippable. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The core method is: specify completely,
triage fast, switch to a reference once a direction is close, and run
the five-step production pass after the prompt.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/text-to-3d-model-prompt-to-production
- https://customuse.com/learn/text-to-3d-model
- https://customuse.com/learn/ai-3d-model-generator

Evidence note: the tail of one member article's lantern example was
read firsthand by the parent agent; all substantive sections were
read.

## Tools used

Tools used: text-to-3D generators (Meshy, Tripo, Rodin and similar)
for exploration and first meshes; image-to-3D tools for locking a
direction; node workflows for the production pass. No single generator
is prescribed: the prompting method is tool-agnostic.

## Phase 1: Specify completely, up the ladder

**Do**
1. Write the prompt up the specificity ladder: object, then form,
   then style, then materials, then use. Name the whole form, not just
   the front: the back, the underside, and the silhouette.
2. State the style explicitly (stylized, low-poly, realistic,
   cinematic) and the use (hero versus background).
3. Mention material regions so they can become slots later.

**Check**
- Does the prompt describe the back and underside, or only the
  photogenic front?
- Could a second artist prompt the same object from this text?

**Why**
Words are a low-bandwidth channel for spatial work. The prompt's job is
to narrow the space of possible meshes; every unspecified surface is a
surface the generator invents.

## Phase 2: Triage candidates in 60 seconds

**Do**
1. Generate several candidates and triage each in about 60 seconds:
   silhouette, proportions, separability of parts, obvious fusions.
2. Pick the cleanest base and discard the rest. Do not nurse a weak
   candidate through repair when a stronger one exists.
3. Run the three-gap check on the pick: geometry gap (is the form
   right?), context gap (does it fit the scene and scale?), export
   gap (can it ship in the required format?).

**Check**
- Did the pick pass all three gaps, or is one gap doing hidden work
  that repair will have to pay for?
- Is the decision recorded, so the team does not re-litigate it?
- Is there a `prompt-manifest.md` with the exact prompt, the
  candidate picked and why, and the three-gap result?

**Why**
Triage speed is the point of text-to-3D: range fast, decide fast. The
three gaps are where prompt-only workflows silently fail, because a
pretty preview can hide all three at once.

## Phase 3: Switch to a reference once a look is right

**Do**
1. The moment a direction is close, stop re-prompting and generate a
   reference image from the prompt (or pick the best candidate render)
   to lock fidelity.
2. Continue from the reference with image-to-3D: the concrete target
   beats further word iteration for matching a specific design,
   character, or product.
3. Chain the methods deliberately: text explores, image locks, node
   workflow finishes. Pure text, text-plus-reference, image-to-3D,
   and node workflows are four methods, not four rivals.

**Check**
- Are you still re-prompting after the direction is settled? If yes,
  you are past the method's ceiling.
- Does the reference capture the look the team approved?

**Why**
Re-prompting past the ceiling is the signature waste of text-to-3D:
each reroll re-opens every decision the previous roll settled. A
reference freezes the approved look so production can proceed.

## Phase 4: Run the five-step production pass

**Do**
1. Prompt (step one, done). Then run the four steps that actually
   ship the asset: inspect and retopologize to clean quad topology
   and a game-ready polycount, generate preserved material slots and
   usable PBR maps, rig if it animates, and validate and export to
   FBX, GLB, or USD that imports cleanly into the target engine.
2. Validate against a production checklist: scale, watertightness
   where needed, UVs, slots, naming, then export (FBX for Unity in
   the worked example).
3. In a node workflow, keep the five steps on one canvas so the next
   variant (a rusted version, a larger hanging version) reruns the
   same graph instead of starting over.

**Check**
- Four of the five steps happened after the prompt. Were they?
- Does the exported file import cleanly at the right scale with
  working material slots?

**Why**
The prompt did real work at step one, but the asset is not shippable
until the other four steps run. Text-to-3D is excellent for ideation,
placeholders, and background props; for heroes, characters, or engine
handoff, the prompt is the first step and the production pass is the
rest of the job.

## Phase 5: Buy on the whole path, not the first mesh

**Do**
1. Before committing to any generator, run one real asset (not a demo
   prompt) through the full path: prompt or reference, generation,
   mesh inspection, retopology, texture pass, export, import, scene
   placement, review, revision.
2. Score the tool on the whole path: usable versus merely impressive
   output, manual cleanup needed, separated PBR maps versus one fused
   image, correct scale and slots on import, single-step reruns versus
   full restarts, and whether a teammate could take over.

**Check**
- Does the tool reduce total time from idea to usable asset, or only
  time to first preview?
- If it only helps the first two steps, is it priced and used as a
  concept tool rather than a production tool?

**Why**
The best generator for production is the one that reduces total
pipeline time, not the one that creates the fastest first preview. A
tool that nails the first minute and leaves eight hours of finishing
has relocated the work, not removed it.

## AAA studio practice

AAA production treats text-to-3D as a first pass inside a human-gated
pipeline, not as a pipeline replacement:

- **Hybrid workflow, generation versus assistance.** The industry
  has adopted a hybrid workflow in which AI accelerates specific
  labor-intensive sub-tasks such as retopology, texture upscaling,
  and set dressing, while the dream of a text-to-world button
  remains technically unfeasible for high-end production; roughly
  half of studios have deployed AI in their pipelines, but the
  distinction that matters is generation versus assistance, with
  human oversight throughout.
  (Source: https://davidasmith.medium.com/the-state-of-ai-in-aaa-game-production-b7d949df4daa)
- **First pass for assets, fine-tuned for continuity.** Neowiz's
  production AI-creator role uses generative AI to produce textures
  and assets, Stable Diffusion and Midjourney for concept drafts,
  and models fine-tuned on studio-owned data to hold visual
  identity, with senior curation and cleanup as the quality gate;
  without that gate, diffusion variance turns a set into patchwork.
  (Source: https://vocal.media/futurism/neowiz-ai-creator-listing-exposes-generative-ai-normalization-in-aaa-production)
- **Simple prompts win; heroes still get validated.** Simple,
  clearly defined prompts beat vague or overloaded ones, and
  complex mechanical assemblies, surface text, and anatomically
  precise characters warp or show odd geometry; for hero assets or
  a demanding AAA pipeline, topology, edge flow, textures, and
  polygon count still get artist-validated, while background
  assets and prototypes may ship with limited post-processing.
  (Source: https://nerdbot.com/2026/10/21/meshy-ai-review-from-basic-text-input-to-functional-3d-models/)
- **Automation (agent-executable):** write a `prompt-manifest.md`
  per asset recording the exact prompt, the candidate picked and
  why, the triage verdict, and the three-gap result, so a rerun
  reproduces the decision instead of re-rolling it; tag every
  generated asset `first-pass` until it clears the production pass,
  and never let a first-pass tag enter source control as a hero;
  log whole-path time (idea to usable asset, not time to first
  preview) per tool so the buy decision uses the number this
  skill's Phase 5 asks for. (Inference: the manifest and tagging
  rules apply the hybrid-workflow sources above to this skill's
  Phases 2-5.)

## The human method, distilled

1. Specify the whole form: back, underside, silhouette, style, use,
   material regions.
2. Triage in 60 seconds; check the three gaps.
3. Switch to a reference the moment a direction is close.
4. Four of five steps happen after the prompt. Run them.
5. Buy on idea-to-usable-asset time, never on preview speed.

## Depth status

FULL (article text).
