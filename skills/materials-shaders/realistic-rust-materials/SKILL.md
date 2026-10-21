---
name: "rust_materials"
description: "Author realistic rust as a layered procedural material system with exposed parameters. Trigger when weathering materials in Substance."
---

# How to Make Realistic Rust Materials

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Drive the DCC with agents: MCP servers loop an agent between Blender and Unreal, and the human inspects every step.
Creator context (from the post and the 80 Level article it links):
Loic Anquetil, Senior 3D and Material Artist at Ubisoft Montpellier; credits
include Rayman Legends Retold, Ghost Recon Breakpoint, and Prince of Persia:
The Lost Crown; also a 3D teacher (Rubika, CG Academy). The reconstruction
below is grounded in the 80 Level article the post advertises as containing
"Loic's behind-the-scenes secrets"
(https://80.lv/articles/desirable-patina-how-to-make-realistic-rust-in-3d);
the post selftext alone only summarizes it.

## Source

Creator: Loic Anquetil

Source: https://v.redd.it/9oiwcc43mhrh1 | r/Substance3D post 1wp51i2 by P_Gresty

## Tools used

Tools used: Substance 3D Designer (primary authoring tool), Substance 3D
Assets (publishes the "Desirable Patina" Signature Collection: 24 assets
covering rust, paint with rust, 3D materials, and procedural texture
generators), the artist's own reference photography.

## Phase 1: Study the material before building anything

**Do**
1. Take your own reference photos whenever you encounter interesting rust in
   everyday life. Stock/reference images are "too distant or stylized" to
   reveal the material's structure.
2. Decipher rust's "surface language": even inside a limited brownish-orange
   range there are micro-variations, tiny shifts in tone, small accents,
   unexpected transitions.
3. Reorder your research: the artist started thinking color exploration would
   be the main area, then shifted to granularity and microstructure. Understand
   rust structurally before tackling its color range.

**Check**
- Can you describe the grain and relief vocabulary, not just the color?
  Production rust references even showed "fluorescent tones, vibrant oranges,
  greens, blues" that read like abstract paintings.

**Why**
"With rust, studying the physical complexity of the material comes before
anything else." Casual looking sees one brownish-orange; the believable
material lives in the micro-detail.

## Phase 2: Establish one foundation material that sets the structural logic

**Do**
1. Build "Coarse Rust Pitting" first. It was the material he struggled with
   most, and it "laid the groundwork for everything else."
2. Nail three relationships: the breakup patterns, the relationship between
   height and roughness, and how color variation interacts with surface detail.

**Check**
- The foundation is solid before anything layers on top. Once it is, "the
  rest of the collection could become more fluid and playful."

**Why**
One solved structural core unlocks everything downstream: peeling paint,
blended corrosion stages, dirt and accumulation. Time, exposure, and
environment then "begin to tell the story of an object."

## Phase 3: Build the noise generators from scratch, fast-mockup first

**Do**
1. Work primarily with single grayscale outputs; focus on blending noises
   together.
2. Loop: study references, take photos, make quick mockups in Designer; once
   you like the result, rebuild it properly in procedural form.
3. Borrow the collage mindset from his graphic-design background (physically
   painting and scanning surfaces in earlier jobs): take disparate elements,
   mix, transform. Test question he asked himself: "If I take a wood texture,
   recolor and distort it, can it become rust?"
4. Target the noises that carry weathered metal: patina, erosion, and water
   streaks; also corrosion flaws.

**Check**
- Do the noises simulate water streaks and corrosion flaws while staying fully
  procedural?

**Why**
"Noises are fundamental resources in material creation. We always need them."
Building them from scratch is both control and craft; production schedules
normally deny him the time.

## Phase 4: Reverse-engineer the built-in nodes instead of fighting them

**Do**
1. Open Designer's graphs and base noises, access their internal data, modify
   them, add parameters, rebuild parts of their logic. "All the noises in this
   project went through that reinterpretation."
2. Keep graphs clean and organized: clean structure, logical grouping, clarity.
   Chaotic "spaghetti" graphs "aren't helpful to other artists."

**Check**
- [inference] Another artist can open the graph, follow the logic, and modify
  it. "Even if the result looks complex, it shouldn't feel intimidating."

**Why**
"Nothing is truly closed" in Designer, and "reverse engineering is one of the
most powerful ways to learn." Taking shortcuts that make sense "isn't
cheating, it's efficiency"; production deadlines are real.

## Phase 5: Layer the corrosion story, keep the graphs readable

**Do**
1. Introduce peeling paint, blend stages of corrosion, add subtle dirt and
   accumulation on top of the foundation material.
2. Keep every graph organized and readable as you layer, per Phase 4.
3. Balance: materials must be expressive but "production-ready and adaptable";
   they "need to be parametrized, reused, and shared." A material should look
   good AND be controllable.

**Check**
- Expressive but adaptable: can the parameters serve art direction, gameplay
   needs, and realistic constraints, not just self-indulgence?

**Why**
In production, materials serve a defined framework. His professional mindset
"returned quickly": the collection had to balance artistic exploration with
functional utility.

## Phase 6: Work the toolbox, not the system

**Do**
1. Deliberately break the controlled, analytical habit: mix noises
   instinctively, plug nodes together "just to see what would happen," stop
   overthinking.
2. Treat each node as a brush, a pair of scissors, a texture stamp. "You mix,
   you test, you react."

**Check**
- Some experiments are terrible, some are incredible. Keep the incredible
   ones: "Some of those experiments are now part of my daily workflow."

**Why**
Total mastery killed his spontaneity ("I could visualize a material and
instantly know how to build it. There was no room left for accidents or
surprises. That's a dangerous place for an artist."). Designer as a creative
toolbox is what makes it approachable.

## Phase 7: Publish as a reusable collection

**Do**
1. Ship the 24 assets as the "Desirable Patina" Signature Collection on
   Substance 3D Assets, with clean, organized graphs so other artists can
   open, study, reorganize, hack, and rebuild them.

**Check**
- The work "continues beyond the collection" when someone opens a graph,
  modifies it, and creates something new.

**Why**
Shared, parametrized, readable materials compound; locked black boxes do not.

## The human method, distilled

1. Study before building: understand the material structurally
   (microstructure before color).
2. Take your own references; stock photos are too distant or stylized.
3. Solve one foundation material that establishes the structural logic
   (breakup, height-to-roughness, color-to-detail), then layer fluidly.
4. Mock up fast, rebuild properly once it reads right.
5. A small node set used intelligently beats ultra-technical graphs; you do
   not need custom functions everywhere or Pixel Processor nodes in every
   direction.
6. Reverse-engineer built-in nodes; nothing is closed, and shortcuts that make
   sense are efficiency.
7. Clean, organized graphs are a feature: readability for the next artist.
8. Treat Designer as a creative toolbox, not a technical system; leave room
   for accidents.
9. Balance exploration with utility: expressive, but parametrized,
   production-ready, and shareable.

## Depth status
 FULL (grounded in the 80 Level article the post itself links
as the source of the behind-the-scenes method; the clip and post selftext
alone would be thin, since the post has 0 comments).

---
