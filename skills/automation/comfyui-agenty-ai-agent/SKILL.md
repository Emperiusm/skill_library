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

## The human method, distilled

1. **Free the agent from the expensive model** — Qwen/DeepSeek cheap,
   Ollama/Strata local and free.
2. **Let the agent research before it builds** — "builds workflows it
   has never seen, from what it finds on the web."
3. **Make judgment explicit** — self-grading against the brief,
   re-renders of misses, and pre-planned agent-or-human review points
   are part of the pipeline design, not an afterthought.

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
