---
name: ai-3d-studio-team-workflows
description: "Run AI 3D as a team discipline: provenance and project memory, style control, review gates, workspace selection, and the generator-versus-workflow-tool distinction, including a 40-SKU batch example. Trigger when scaling AI 3D from one artist to a studio pipeline."
---

# Studio and Team Workflows for AI 3D

## Purpose

This skill is team-level process, not asset-level technique: it keeps
a studio's AI work consistent, reviewable, and repeatable across
people and batches. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: preserve state, gate by job depth,
review on a shared surface, and choose the workspace by what it
preserves.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/ai-3d-for-studios
- https://customuse.com/learn/ai-3d-workflow-prompt-to-production
- https://customuse.com/learn/ai-3d-workspace
- https://customuse.com/learn/ai-3d-workflow-tool

Evidence note: one member article's FAQ tail was unseen; all substantive
sections were read. One member article's end-to-end example (refinement
branching and export review) was read firsthand by the parent agent.

## Tools used

Tools used: AI generators as nodes or inputs; workflow platforms and
workspaces as the shared layer; DCC tools and engines as destinations.
The workspace choice is the decision this skill informs.

## Phase 1: Preserve state across iterations

**Do**
1. Keep every asset attached to its prompt, reference images,
   intended use, and review notes, instead of letting it become an
   orphaned file in a downloads folder.
2. Preserve project memory across variants: when a team branches a
   second variant (a closed shutter for level variety, a desaturated
   cloth material), palette and scale constraints must carry across
   automatically.
3. Version the workflow, not just the output: a teammate must be able
   to see what changed, when, and why.

**Check**
- Can a teammate take over any asset without asking its author?
- Do variants share constraints, or does each variant re-decide
  palette and scale?

**Why**
A production-ready workflow preserves state across iterations,
supports branching and comparison, and gives collaborators enough
visible context (assets, scenes, version history) to review without
starting from scratch. Without state, every handoff is a cold start.

## Phase 2: Gate depth by job

**Do**
1. Apply the seven gates to team work: generation, inspection, scene
   context, refinement and versioning, export, review, and handoff.
   Most projects become valuable or fall apart in the steps after
   generation, not in generation itself.
2. Set depth by job with a matrix: concept work gets shallow passes,
   hero and shipping work gets the full seven gates. Do not spend
   hero depth on blockouts, and do not ship heroes on blockout depth.
3. Run the handoff test: the asset, its recipe, and its review state
   must all survive a transfer to another team member.

**Check**
- Is the depth for this job written down, or is it decided per asset
  by whoever touches it?
- Does the handoff test pass without the original author in the room?

**Why**
Generation is roughly a minute of a multi-day job; the steps after it
are where the time and money go. A workflow that compounds early speed
is one whose later steps are gated; a workflow that wastes it is one
whose later steps are improvised.

## Phase 3: Review on a shared surface

**Do**
1. Review the setup, not just the output: reviewers see variants and
   change history on one canvas and approve in a single pass.
2. Run the 10-step studio loop for shipping work: brief, generate,
   inspect, gate, refine, version, export, validate, review in
   context, and archive the recipe.
3. Approve variants together: the approved variant and its branched
   sibling are reviewed in the same pass, with the same constraints.

**Check**
- Can a reviewer approve without reconstructing the asset's history?
- Is the approved recipe archived for the next batch?

**Why**
Review is where studio quality is actually enforced. A review surface
that shows only outputs forces reviewers to guess at provenance; a
surface that shows setup, variants, and history lets them approve with
evidence.

## Phase 4: Choose the workspace by what it preserves

**Do**
1. Run the seven-state workspace checklist: does the workspace hold
   prompts, references, assets, scenes, materials, cameras, and
   project state, and can agents and teammates act on all seven?
2. Distinguish a generator from a workflow tool with the scoring
   rubric: a generator produces a candidate mesh; a workflow tool
   produces a finished, validated deliverable plus a repeatable
   recipe, exports to the destination format without re-conversion,
   and enforces a quality bar on topology, materials, scale, and poly
   budget before handoff.
3. Price the decision at batch scale, not single-asset scale: the
   worked 40-SKU batch example is where the difference shows. A single
   creator can live with a one-shot generator and manual cleanup; a
   studio shipping a season of assets needs versioning, shared review,
   and a repeatable process.

**Check**
- Does the workspace hold all seven states, or does state leak into
  chat threads and shared drives?
- At 40 SKUs, does the tool still save time, or does manual cleanup
  dominate?

**Why**
A single asset flatters every tool; a batch exposes every gap. The
workspace decision is really a decision about what survives between
assets: if nothing survives, the studio pays the first-asset price
forty times.

## The human method, distilled

1. State is the product. Orphaned files are not a pipeline.
2. Gate depth by job. Hero depth for heroes, shallow passes for
   blockouts.
3. Review setup, variants, and history together, in one pass.
4. Generator versus workflow tool is decided by what survives: recipe,
   review state, and repeatability.
5. Price tools at batch scale. Forty SKUs expose what one asset hides.

## Depth status

FULL (article text; substantive sections read, one FAQ tail unseen).
