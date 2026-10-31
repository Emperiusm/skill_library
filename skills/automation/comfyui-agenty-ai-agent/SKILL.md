---
name: comfyui-agenty-ai-agent
description: "Run agentY, a free MIT AI agent that lives inside ComfyUI: builds unseen workflows from web research on cheap/local LLMs, self-judges outputs against the brief, runs parallel agents per shot, and drives Blender/Maya/Houdini/After Effects over MCP. Trigger when an agent should own an image/video/3D workflow."
---

# ComfyUI agentY: An AI Agent That Lives Inside ComfyUI

## Purpose

This skill runs an AI agent that lives inside ComfyUI and owns the
workflow: it researches workflows it has never seen, builds them,
judges its own outputs against the brief, re-renders what misses, runs
parallel agents per shot, and drives DCCs (Blender, Maya, Houdini,
After Effects) over MCP. It runs on cheap or fully local LLMs. Every
phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: brief
the agent, let it research, make judgment explicit, parallelize per
shot.

## Source

r/comfyui, Admirable-Agency-578 posting agentY (full post text,
2026-10-30):

- https://www.reddit.com/r/comfyui/comments/1xirbr2/tired_of_writing_prompts_or_using_expensive/

Evidence note: all facts below are the author's claims from the post
text; the 3 comments are praise-only and add nothing. MCP preset
behavior, re-render quality, and web-research reliability have no
third-party verification in this audit.

## Tools used

agentY — github.com/szprivate/agentY — **MIT-licensed**, Windows and
Apple Silicon. Lives inside ComfyUI with its own image, video, and 3D
viewers. LLM backends: Qwen, DeepSeek (cheap), Ollama, Strata (fully
local, free). **MCP with presets for Blender, Maya, Houdini, After
Effects, and more.** Motion graphics and video editing via remotion.
Slack integration. Tagging system (reuse images created in the system),
project memory, long-term memory.

## Phase 1: Run it on cheap or local LLMs

**Do**
1. Install agentY (MIT; Windows / Apple Silicon builds).
2. Point it at any LLM backend: Qwen or DeepSeek for cheap, Ollama or
   Strata for fully local and free.

**Check**
- Run a familiar brief on the cheapest backend first: does the agent
  still complete it? The product's pitch is "no expensive agents."

**Why**
The agent layer is decoupled from frontier-model APIs: "Runs on any
LLM, including cheap ones like Qwen and DeepSeek, or fully local and
free with Ollama or Strata."

## Phase 2: Brief it, let it research

**Do**
1. Give the agent a brief.
2. It "builds workflows it has never seen, from what it finds on the
   web" — researching node graphs and workflows online rather than
   replaying only built-in templates.

**Check**
- Ask for a workflow type it has never seen; inspect the built graph
  for coherence (node wiring, input types) before executing.

**Why**
This is an agent, not a macro recorder: workflow-building from web
research is the value. The failure mode to watch is a graph that
looks right but miswires a node — always inspect before running.

## Phase 3: Make judgment explicit — loops and reviews

**Do**
1. The agent "judges its own outputs against your brief and re-renders
   what misses."
2. Build "entire agent image generation pipelines with loops and
   pre-planned agent or human reviews, right within ComfyUI."
3. Use the tagging system to reuse images created in the system, and
   project/long-term memory to carry context across sessions.

**Check**
- After a re-render: did the second pass fix the specific miss, or did
  it drift? Compare against the brief, not against the first take.
- For pre-planned human reviews: confirm the agent actually stops at
  the review point instead of continuing.

**Why**
This is the konte pattern (acceptance records, variants instead of
overwrite, explicit review points) shipped as product features rather
than a hand-built harness. Memory + tagging are what let repeated
briefs converge instead of starting cold.

## Phase 4: Parallelize per shot

**Do**
1. "Runs several agents in parallel, one per shot if you like."

**Check**
- Check shot-to-shot consistency (identity, style) across parallel
  agents; parallelism multiplies throughput but can fragment look.

**Why**
One agent's context window is the bottleneck for multi-shot work;
parallel agents per shot remove it.

## Phase 5: Drive the DCCs over MCP

**Do**
1. Enable the **MCP presets for Blender, Maya, Houdini, After
   Effects**.
2. Use the agent to build motion graphics and edit video via
   **remotion**.
3. Use Slack integration for notifications/hand-off where it fits.

**Check**
- In a DCC, verify each agent action against the brief before
  accepting: MCP is a two-way door — the agent can change your scene.

**Why**
This is the MCP-driven-DCC-loop pattern as a shipped product: an agent
inside the workflow tool, driving the DCCs over MCP, with review
points from Phase 3 as the safety rail.

## AAA studio practice

An AI agent that drafts, judges, and iterates production work is not
novel in AAA — it is shipped, measured, and gated. The studio pattern
is always the same: AI proposes, humans dispose, and the loop gets
shorter every year.

**Ubisoft Ghostwriter (La Forge, GDC 2023): AI drafting with human
selection.** Ghostwriter is an in-house AI tool that "generates first
drafts of barks — phrases or sounds made by NPCs during a triggered
event," deliberately framed as drafting support, not writer
replacement. The production loop: scriptwriter creates a character +
interaction/utterance type → the tool proposes a select number of
variations → the writer selects and edits → training uses **pairwise
comparison** (the writer picks between two choices), and "after
thousands of selections made by humans, it becomes more effective and
accurate." Scale-out is per-project: a back-end website called
**Ernestine** "allows anyone to create their own machine learning
models used in Ghostwriter," so each production team tailors its own
AI to its game's narrative needs instead of using one shared model.
(Source: https://news.ubisoft.com/en-gb/article/7Cm07zbBGy4Xml6WgYi25d/the-convergence-of-ai-and-creativity-introducing-ghostwriter —
Ubisoft News, March 2023; presented at GDC 2023.)

**Ubisoft Commit Assistant → Clever-Commit (La Forge, Mozilla
partnership): AI pre-review gates on code.** The prototype was built by
Ubisoft La Forge with Concordia University, transferred to the Ubisoft
Technology Group "to develop, adapt and deploy it to our production
teams worldwide," and **beta-deployed on major AAA titles** (Mozilla
added Rust/C++/JS support). Measurable numbers, from Ubisoft La Forge
via press coverage: catches **6 out of 10 bugs with 30% false
alarms**; bug squashing absorbs **up to 70% of development costs**;
trained on roughly **10 years of Ubisoft code**; estimated to free
**~20% of programmers' time**. The executable pattern is the
pre-commit/pre-review gate — the exact role an agentY review point
should play.
(Sources: https://montreal.ubisoft.com/en/partnering-up-with-mozilla-to-develop-an-ai-coding-assistant/ —
Ubisoft Montreal, 2019;
https://www.gamesindustry.biz/articles/2019-02-13-ubisoft-partners-with-mozilla-on-ai-coding-assistant —
GamesIndustry.biz, Feb 13, 2019.)

**EA SEED: shipped ML systems and agentic QA.** Shipped production ML:
**Swish** in Madden NFL 21 — "one of the first real-time,
player-facing machine learning deformer ever shipped in a game"
(neural-net cloth); **Voice2Face** audio-driven facial animation used
in Battlefield 6 cinematics and EA SPORTS FC 25 crowd chants;
**Reinforcement-Learning Goalkeeper** in EA SPORTS FC 26 (adaptive ML
positioning); Bad Actor Detection across "millions of matches" in Apex
Legends. The agentic pattern: SEED's Battlefield 1 self-learning
agent (2018) started from **30 minutes of human play as
imitation-learning seed**, then ran 6 days of self-play on parallel
machines (**~300 days of gameplay experience**) with the explicit
stated purpose of QA (more crash reports), not shipping bots. The IEEE
CoG 2020 paper by Gordillo et al. documents curiosity-driven RL agents
maximizing game-state coverage for playtesting 3D scenarios —
"automatically mapping reachable/unreachable areas" and detecting
unintended mechanics.
(Sources: https://www.ea.com/en-ca/news/seed-10-year-anniversary — EA,
Nov 2025; https://ieee-cog.org/2021/assets/papers/paper_7.pdf — IEEE
CoG 2020.)

**Marked as unconfirmed:** a named Activision AI-QA-bot product from a
primary source; current Activision QA reporting (Oct 2026) is about
the union contract fight and AI guardrails, not a shipped bot. Cite
SEED/EA and Ubisoft examples, not Activision.

## Agent automation

**Do**
1. **Pairwise-comparison acceptance log** (Ghostwriter pattern, agent
   design): extend the skill's Phase 3 self-judgment into a written
   record. For every brief, the agent logs each candidate-vs-candidate
   comparison it makes (winner, loser, reason) to `acceptance.jsonl`
   before re-rendering. The log is the evidence that judgment
   happened, not the claim that it did.
2. **Web-research wiring audit** (Commit-Assistant pattern, agent
   design): the skill's Phase 2 "inspect the graph before executing"
   becomes a script: walk every node in the researched workflow,
   assert each input's type matches its connected output's type, and
   fail the run on the first mismatch. This is the Commit Assistant's
   pre-review gate applied to node graphs.
3. **MCP action ledger** (SEED QA pattern, agent design): every DCC
   mutation over MCP is logged with a pre/post state diff to
   `mcp-actions.jsonl` — the "crash report" discipline, repurposed as
   an undo trail for the skill's Phase 5 side-effect risk.
4. **Ernestine-style run manifest** (agent design): record which LLM
   backend + agentY build produced each pipeline run in
   `run-manifest.json` (backend name, build version, timestamp, brief
   hash). One backend per project, per Ghostwriter's per-game model
   tailoring — no drifting across runs unrecorded.

**Check**
- `acceptance.jsonl` is non-empty after every run: zero comparisons
  logged means the self-judge step was skipped, and the run fails.
- The wiring audit exits non-zero on any type mismatch; the audit
  script itself is committed to the project, not re-typed per run.
- `run-manifest.json` lets a later run diff "why did this pipeline
  change?" down to the backend or build.

**Why**
AAA doesn't trust AI agents more than agentY's own pitch does — it
trusts them with gates around them. Ghostwriter's thousands of human
selections, Commit Assistant's pre-review catch rate, and SEED's QA
coverage metrics are all the same move: make judgment explicit and
logged. These four upgrades turn the skill's already-explicit review
points into the written, scripted gates studios actually ship.

## The human method, distilled

1. **Free the agent from the expensive model** — Qwen/DeepSeek cheap,
   Ollama/Strata local and free.
2. **Let the agent research before it builds** — "builds workflows it
   has never seen, from what it finds on the web."
3. **Make judgment explicit** — self-grading against the brief,
   re-renders of misses, and pre-planned agent-or-human review points
   are part of the pipeline design, not an afterthought.

## UPDATE 2026-10-31 (agentY UPDATE post)

New details from the r/comfyui UPDATE post (Admirable-Agency-578,
score 69, 10 comments, 2026-10-31):

- https://www.reddit.com/r/comfyui/comments/1xjbipg/

Evidence note: all facts below are the author's claims from the UPDATE
post text plus the author's comment replies. No third-party
verification in this audit.

### Update 1: WorldLabs splats from single images

**Do**
1. Use the WorldLabs API update: generate high-quality splats from
   single generated images.

**Check**
- The splat produced from a single image holds up from multiple
  viewing angles in the viewer.

**Why**
Single-image-to-splat closes the loop: generate the image, splat it,
and review in 3D without leaving the agent's viewer.

### Update 2: grok via its OpenAI-compatible endpoint

**Do**
1. In the settings panel, enter grok's endpoint URL and API key.
2. Restart the agent.

**Check**
- After restart, grok sees the workflow, adjusts the canvas directly,
  builds workflows in separate ComfyUI tabs, and answers in the
  side-panel chat while it works.

**Why**
The OpenAI-compatible endpoint standard makes the backend swap a
settings-panel edit, not a reinstall: any compatible model becomes the
agent's brain.

### Update 3: Annotation tool for visual feedback

**Do**
1. Use the annotation tool to draw directly on images and videos to
   give the agent feedback.

**Check**
- After annotating a miss, verify the re-render addressed the marked
  region, not something else.

**Why**
Drawing on the frame is the fastest feedback channel: it points at
the miss instead of describing it in words.

### Update 4: Uninstall and key reset

**Do**
1. To uninstall: delete the agentY repo folders and the agent custom
   node inside the ComfyUI folder.
2. API keys can be re-set via the settings panel; or re-run the
   installer.

**Check**
- After deletion, the custom node is gone from the node list and no
  agent panels remain.

**Why**
Clean uninstall is a documented procedure, not archaeology: two
deletion targets, keys recoverable either way.

### Update 5: Platform support and Linux status

**Do**
1. Supported: Windows + Apple Silicon (listed builds).
2. `install_agent.sh` covers macOS and Linux, but Linux is **untested
   by the author** , the readme is updated only if a user confirms it
   works.

**Check**
- On Linux: confirm the installer completes and the agent launches
   before relying on it in a pipeline.

**Why**
Untested-on-Linux is stated honestly by the author; a user
confirmation is the acceptance test.

### Update 6: agentY packaged as an MCP itself

**Do**
1. Treat agentY as an MCP: Claude (or another orchestrator) can
   orchestrate multiple agentY instances, which themselves use other
   LLMs.

**Check**
- Multiple agentY instances coordinate on one brief without
  double-working the same step.

**Why**
Agents all the way down: the agent becomes a callable tool for a
larger orchestrator, so per-shot parallelism (Phase 4 of the original
skill) scales across instances.

### Update 7: remotion motion graphics in ComfyUI's own viewer

**Do**
1. Build motion graphics and edit video with remotion, editable inside
   ComfyUI's own image/video/3D viewer.

**Check**
- The remotion timeline edits render back into the viewer the agent
  already owns.

**Why**
Editing inside ComfyUI's viewer keeps the motion-graphics loop in the
same room as the generation loop: no round-trip to a separate NLE.

## Failure modes

- **Miswired researched graph:** a web-researched workflow can look
  right and miswire a node. Fix: inspect the graph before executing.
- **Re-render drift:** the "fix" changes the wrong thing. Fix: compare
  against the brief, keep the first take as the reference.
- **Parallel-agent style fragmentation:** per-shot agents diverge in
  look. Fix: lock style reference (tagged images) before parallelizing.
- **MCP side effects:** the agent edits a DCC scene in a way the brief
  didn't ask for. Fix: review points before destructive steps.

**Depth status:** FULL (author's full post text with the complete
feature list; claims not third-party-verified).
