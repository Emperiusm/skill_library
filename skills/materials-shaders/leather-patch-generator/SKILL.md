---
name: leather-patch-generator
description: "Generate leather patch materials with a parametric Substance generator. Trigger when authoring reusable material generators."
---

# Leather Patch Generator

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Generate materials, don't paint them: a parametric leather-patch generator with exposed controls.

## Source

Creator: Javadrajabzade

Source: https://v.redd.it/9vqa8ywo21rh1 | r/Substance3D post 1wn37iv

## Tools used

Tools used: Substance 3D (implied by the r/Substance3D subreddit; the
post title says "Generator"). Portfolio:
https://www.artstation.com/a/56020938. The single comment is a reaction
("This is great!!"), not a technical question.

**Do**
1. Build the leather as a procedural material generator (Substance graph
   style): exposed parameters for variation rather than a fixed texture.
2. Generate leather patches from the system: the deliverable is the
   generator plus its outputs, cross-posted to ArtStation as a portfolio
   piece.

**Check**
- Regenerate with different seeds: does the leather read as leather
   (grain, cracks, pores) in each variant?
- [inference]: no parameter names, node names, or values are given in any
   source, so no exact numbers can be reconstructed.

**Why**
A generator post is a portfolio move: the tool is the artifact. With no
tutorial content, the workflow cannot go deeper than this.

## AAA studio practice

The author's generator is thin on specifics, so this section adds only general, sourced Substance production practice, clearly labeled as such, not as the author's undisclosed parameters:

- A production leather graph is built from a small node vocabulary: Adobe's leather tutorial builds from Cells 3 and BnW Spots noises, Levels filters, a Height to Normal filter, and a Gradient Map driving base color, with roughness and height derived from the same levels chain. Source: https://www.creativebloq.com/advice/create-a-leather-material-in-substance-designer
- The generator pattern itself is Adobe's documented SBSAR workflow: expose chosen parameters (seed, grain, crack, wear) from the graph, publish the package as SBSAR, and downstream tools (Unity, Unreal via the Substance plugin) read those exposed parameters and regenerate variants without reopening Designer. Sources: https://experienceleague.adobe.com/en/docs/substance-3d-designer/using/substance-graphs/manage-parameters/exposing-a-parameter and https://experienceleague.adobe.com/en/docs/substance-3d/ecosystem/game-engines/unity/changing-parameters
- Naughty Dog's The Last of Us Part I material work (GDC session by Jonathan Benainous and Jared Sobotta) shows the production payoff: procedural generators in Substance Designer, authored once, speed up authoring a large material count across a team. Source: https://www.gdcvault.com/play/1029357/Adobe-Developer-Summit-The-Material

**Do (agent-executable; general practice, not the author's values)**
1. Expose, at minimum, a Random Seed parameter plus one parameter per visible variation axis (grain scale, crack density, wear amount); label each exposed parameter with a human-readable name, since exposed parameters are edited by other artists, not by the graph author.
2. Publish as SBSAR and verify in a second application (engine or Substance Player) that changing the seed regenerates a new leather variant that still reads as leather, and that no exposed parameter is static-only (static parameters are hidden after cooking, per Adobe's docs).
3. Batch-check: render the generator at 3 seeds and confirm grain, cracks, and pores survive in each variant, per the skill's existing Check, before calling the generator done.
4. Keep the graph readable (grouped, labeled nodes), per the same cleanliness rule the realistic-rust skill documents from production practice; a generator other artists cannot open is not a reusable tool.

**Check**
- The SBSAR exposes seed plus variation parameters, regenerates distinct valid variants, and opens readably in Designer.
- [Inference, labeled]: none of the above parameter names or values are claimed to be the original author's; they are the minimum set a production generator needs.

## Phase 1: Author a procedural leather material [inference: reconstruction]

## The human method, distilled

1. **A generator is the portfolio piece.** When the post is the tool itself,
   the outputs prove the parameter space.
2. **Showcase posts carry no workflow signal by themselves.** Without a
   breakdown, questions, or author explanation, reconstruction stops at the
   tool category.

## Depth status
 DEPTH-LIMITED (one clip, one reaction comment, one
ArtStation link; no parameters, nodes, or method stated; nothing further can
be honestly reconstructed)

---
