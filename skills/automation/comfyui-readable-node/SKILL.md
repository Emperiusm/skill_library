---
name: comfyui-readable-node
description: "Rebuild messy ComfyUI workflows into readable ones with the Readable Node agent skill: six readability rules, full teardown-and-rebuild by a strong model, and a report page with a replay of the rebuild. Trigger when a workflow someone handed you is unreadable, or before handing one off."
---

# ComfyUI Readable Node: Rebuild Messy Workflows Readably

## Purpose

This skill reconstructs the exact workflow nomadoor describes for the
Readable Node agent skill (r/comfyui, 2026-11-09), step by step, so
another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The workflow's core method is: take the workflow
completely apart, figure out what it does, and rebuild it from scratch
to be readable, then show the replay.

## Source

Creator: nomadoor.

Source: https://www.reddit.com/r/comfyui/comments/1xqupum/comfyui_readable_node_an_agent_skill_for_turning/
(r/comfyui post 1xqupum, score 33, 11 comments) | 2026-11-09 scout run.
Skill repo: https://github.com/nomadoor/comfyui-readable-node.
Author's site: https://comfyui.nomadoor.net/
Evidence: complete author post text with exact rules, timings, and
model floor + 10 comments with the author's own clarifications and the
Nuke counterpoint. The video is a demo clip of the skill running.

## Tools used

Tools used: **ComfyUI**, **Readable Node agent skill**, **Claude Opus
5.5** (best; Sonnet noticeably worse).

## Phase 1: Learn the six readability rules

**Do**
1. Don't hide nodes: expand subgraphs, open collapsed nodes, don't
   stack nodes on top of each other.
2. Don't hide wires: no wireless links (Set/Get, Anything Everywhere,
   hidden wires), and no Bento layouts that pack nodes so tightly the
   wires disappear.
3. Left to right: the flow goes left to right, in processing order.
4. One workflow, one task: instead of an all-in-one workflow with
   switches and bypasses, split it into small workflows that each do
   one thing.
5. Keep custom nodes to a minimum: if it can be built with core nodes,
   build it with core nodes.
6. Color appropriately: colors show which function a node belongs to.

**Check**
- A readable workflow is one where "you can tell at a glance what it
  does, it runs reliably, and it's easy to rework. It's not about
  looking pretty. It's about being easy to understand and easy to
  change." (Author, quoted.)

**Why**
The author builds and publishes his own basic workflows for one
reason: readability, even though official templates exist. The six
rules are his definition, stated up front.

## Phase 2: Run the agent skill on a messy workflow

**Do**
1. Give the agent a workflow JSON and ask it to make the workflow
   readable with Readable Node.
2. The agent takes the workflow completely apart, figures out what it
   does, and rebuilds it from scratch: turning Set/Get back into wires,
   swapping custom nodes for core ones, removing redundant nodes,
   splitting bundled tasks, writing notes that explain why each part is
   set up the way it is. (Author comment, quoted in substance.)
3. You get the rebuilt workflow and a report page. In the report, you
   can replay how the AI rebuilt the workflow and read what each part
   does.

**Check**
- Read the report page and replay the rebuild; the replay is the
  verification that the agent understood the workflow rather than just
  rearranging it.
- "Since it aims for a more robust workflow, the output may not always
  match the original exactly." A changed output is expected, not a
  failure, when the rebuild removes a redundant node or splits a
  bundled task.

**Why**
"Why a skill and not a script? As I said above, readability isn't just
a layout problem." Layout alone cannot turn Set/Get links back into
wires or decide a custom node should be a core node; those are judgment
calls, which is why the author built an agent skill instead of a layout
script. The skill also builds an internal layout tool and the AI
operates it: "The AI isn't specifying coordinates one by one."
(Author comment.)

## Phase 3: Mind the costs and the model floor

**Do**
1. Budget time: "It's slow. A workflow of about 25 nodes takes around
   10 minutes, and big ones can take 20-40."
2. Use a strong model: "Claude Opus 5.5 works best; with others, the
   layout may still have a few issues." Even Sonnet "made the results
   noticeably worse." (Author comment.)
3. For local use, give the skill to an agent harness like OpenCode or
   Pi; Ollama is not the route, and "getting it to run well locally
   would be tough." (Author comment.)

**Check**
- If the layout still has issues, the first suspect is the model, not
  the workflow.

**Why**
The skill was built by grinding: the author started from his own site's
workflows, "then collected workflows from around the web and fixed
them, over and over, hundreds of times." The model floor is a measured
result of that grinding, not a preference.

## Phase 4: Use it where handoff happens, not every day

**Do**
1. Use it when trying to understand a workflow someone gave you, or
   when about to hand one off to someone else. "It's less of an
   everyday tool and more something to use when you're trying to
   understand a workflow someone gave you, or when you're about to
   hand one off to someone else." (Author comment.)

**Check**
- Commenter additions to the rules, acknowledged by the author: group
  nodes that belong to the same step in the workflow (the author notes
  the skill does use groups, but "doesn't lean on them much" and would
  like to work on that more), and put nodes that get adjusted regularly
  on the left so the user does not scroll through the whole workflow to
  adjust a prompt, LoRAs, and resolution. The left-to-right rule and
  the adjustable-nodes-left wish contradict each other; the author
  accepts both as open tension.
- Counterpoint from a Nuke background commenter: DAG auto-layout is
  standard in VFX (Nuke has had auto-arrange for over a decade, and it
  is instant), and compositors must write readable scripts "by law"
  because scripts get handed off around the facility. The author's
  reply, in substance: AI can make the judgment calls where layout is
  under-constrained or contradictory (for example, which wire crossing
  to avoid in a non-planar graph), which classic algorithmic auto-layout
  cannot.

**Why**
The author's closing argument for readability itself: "Ask the AI for
what's better said in words, and do by hand what's better done by
hand. If you want to do both in one place, I think ComfyUI's node
graph is a pretty good fit, as long as you can read the workflow."
And the paint-tool analogy: to remove a mole next to someone's eye,
painting over it is faster than typing "remove the mole," which is why
paint tools have not gone away.

## AAA studio practice

Readable Node is a one-person agent skill, but the problem it solves,
a workflow that only its author can read, is a production problem
AAA studios already pay for. Their answers converge on the same
point: the workflow is a long-term production asset, not a sketch.

- **Ubisoft La Forge, CHORD: ComfyUI is the AAA workflow platform,
  chosen for control.** Ubisoft open-sourced its CHORD PBR material
  estimation model with ComfyUI custom nodes because ComfyUI is "an
  efficient framework to build integrated workflows doing texture
  image synthesis, material estimation and material upscaling," and
  because large studios need "a controllable and integratable AI
  workflow platform" rather than another image generator. The
  three-stage pipeline (texture generation, CHORD image-to-material
  estimation, PBR upscaling to 2K/4K) is built as ComfyUI workflows
  that integrate directly into DCC tools and game engines. The
  readability lesson: when the workflow is the pipeline, an unreadable
  node graph is an unmaintainable pipeline, and the nodes must be
  readable by the next artist, not just the author.
  (https://blog.comfy.org/p/ubisoft-open-sources-the-chord-model)
- **Series Entertainment: workflows as long-term production assets.**
  Series rebuilt game and video production around ComfyUI node
  workflows, treating them as long-term production assets rather than
  one-off steps, and built four streamlined pipelines covering the
  full cycle from exploration to production. The result: 100,000+
  assets across games and video, multiple shipped Netflix titles,
  workflows delivering up to 180x faster than manual processes, and
  the same workflows carrying a project from a 512x512 single-emotion
  test to high-resolution batch production. A workflow that cannot be
  read cannot be promoted from test to production; Series' test-to-
  production ladder only works because the graphs are legible enough
  to reuse.
  (https://comfy.org/customers/series-entertainment/)
- **Moment Factory: one operator, templates, low-res-first review.**
  Moment Factory built a custom ComfyUI workflow for architectural
  projection mapping, grounded in real production parameters (20+
  artistic directions, 20-40 iterations each), with outputs
  pre-mapped through architectural surface templates (flat UVs, 360
  layouts, camera-projection setups) and ControlNet enforcing scale
  and spatial logic. They reviewed intentionally low-resolution
  outputs around 2K, generated variations live on site, and once the
  system was stable, one main artist operated inside ComfyUI. Late in
  the process they swapped the surface template and reran the entire
  pipeline without re-authoring a single asset. That swap is only
  possible because the workflow's structure was readable enough to
  re-target: the template is a named, swappable input, not a hidden
  wire.
  (https://blog.comfy.org/p/case-study-how-moment-factory-reimagined)
- **The handoff standard, from the Nuke counterpoint already in this
  skill:** compositors write readable scripts "by law" because scripts
  get handed off around the facility. AAA practice extends that law to
  every node graph: a graph that cannot be read at a glance by the
  next person on the team is not finished, however good its output.

### Agent-executable upgrades

1. **Readability audit script.** Before running Readable Node, parse
   the workflow JSON with a script and emit `readability-report.json`:
   count hidden-wire nodes (Set/Get, Anything Everywhere, wireless
   links), count custom nodes vs core nodes, count nodes stacked on
   top of each other (overlapping coordinates), and check left-to-right
   ordering (node x-coordinates monotonic with execution order).
   Each finding lists the node names. After the rebuild, re-run the
   audit; every count must be lower or zero, and any remaining hidden
   wire must be named in the report with its reason.
2. **Handoff manifest.** Ship the rebuilt workflow with
   `handoff-manifest.json`: workflow JSON path, model used for the
   rebuild (must be Opus 5.5-class or the manifest flags the
   model-floor risk from Phase 3), node counts before/after, the
   report-page URL, and the replay. ComfyUI embeds the full workflow
   JSON in the metadata of every PNG it produces, so any output image
   from the rebuilt workflow is itself a check: drag it back onto the
   canvas and confirm the graph reconstructs identically.
   (PNG-embedded-workflow mechanism per https://www.growthhunt.ai/growth-story/comfyui)
3. **Template-input rule (Moment Factory).** If the workflow takes a
   structural input (a template, a reference image, a mask), it must
   be a named, top-level input node on the left of the graph, never
   buried mid-graph. The audit script checks that every input the
   workflow depends on is reachable within one hop of the left edge.
4. **Test-to-production ladder (Series).** Keep two saved variants of
   the rebuilt workflow: a low-resolution test variant (fast, cheap,
   for iteration) and the full production variant. Both must be the
   same graph with different parameter values, not two different
   graphs; the manifest records both parameter sets so the promotion
   from test to production is a parameter change, not a rebuild.

## The human method, distilled

1. **Readability is understanding plus change, not looks.** At a glance,
   runs reliably, easy to rework.
2. **Rebuild, don't rearrange.** The agent takes the workflow apart and
   rebuilds it; the report page with its replay proves the rebuild
   understood the work.
3. **Name the weak spots up front.** Slow (10 minutes for 25 nodes),
   needs Opus 5.5, output may not match the original exactly.
4. **Use it at handoff boundaries.** Understanding someone else's
   workflow, or handing one off, is where readability pays.
5. **Words for words, hands for hands.** Ask the AI for what is better
   said in words; do by hand what is better done by hand.

**Depth status:** FULL (complete author post text with exact rules,
timings, and model floor + 10 comments with the author's own
clarifications and the Nuke counterpoint; the video is a demo clip of
the skill running).
