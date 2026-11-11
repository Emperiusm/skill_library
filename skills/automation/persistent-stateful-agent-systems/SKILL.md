---
name: persistent-stateful-agent-systems
description: "Build a persistent, stateful AI agent system that keeps continuity across sessions: durable state outside the model, files or a state graph as the store, patch diffs with schema versioning, optimistic concurrency per node, provenance with explicit supersession, and rehydration from checkpoints instead of summaries. Distilled from an r/vibecoding thread of builders (festival, AIOS, HALIVRO, opsie, tulipfarm) plus the unsolved problems they report: stale assumptions, dependency invalidation, write conflicts, workspace cleanup, and access control. Trigger when designing long-lived agent memory or a multi-session agent harness."
---

# Persistent Stateful Agent Systems

## Purpose

This skill distills the design patterns that independent builders of
persistent, stateful AI systems converged on in an r/vibecoding discussion
thread, so another agent can design a long-lived agent harness without
relearning the same failure modes. Status: **REFERENCE**. The thread
contains no single reproducible workflow with steps and checks, so this is
a pattern set with checkable rules, not a step-by-step build. Every pattern
has three parts: **Do** (the action), **Check** (how to verify it), and
**Why** (the principle). The core method is: state lives outside the model
in durable, versioned structures, and a new session resumes from a
checkpoint, never from a summary of the last session.

## Source

- Post: "Who else is building persistent, stateful AI systems?" by
  u/Either_Pound1986 —
  https://www.reddit.com/r/vibecoding/comments/1xruvvg/who_else_is_building_persistent_stateful_ai/
  (r/vibecoding, Nov 9, 2026, 27 upvotes, 66 comments; 64 rendered and
  read, 2 never loaded, 1 collapsed, 1 deleted)
- The OP's definition, which the thread holds throughout: not chat history
  or a memory layer, but continuity across sessions, accumulated structured
  state, learning from previous work, and evolution over time.
- Full audit of the thread:
  `~/workspace/your_files/vibecoding-persistent-state-audit-2026-11-11.md`

## Systems named in the thread

- **festival / fest.build** (kincaidDev,
  https://github.com/Obedience-Corp/festival): files on disk, every plan a
  state machine, git plus filesystem only, agents treated as disposable
  workers. Daily use for over a year with real clients.
- **AIOS** (Responsible-Beat2137): deterministic execution backbone grown
  out of a Notion knowledge system. Tools, datasets, databases, and
  knowledge ledgers kept as separate slots. Governance pipeline STONE to
  MASO to STONE (ingest, model validation). Google Drive backend.
- **HALIVRO** (Secret-Creme-19): local-first, structured versioned state,
  explicit authorization, audit trail. Dependency-aware revalidation is the
  stated direction and is explicitly not solved yet.
- **opsie** (RossPeili, https://github.com/arpahls/opsie): embeddings plus
  vector and semantic search, claims 300+ conversations remembered.
- **tulipfarm** (maddhruv, https://github.com/TulipFarm/tulipfarm):
  TypeScript, Postgres for states, sessions, and knowledge, Temporal for
  durable state.
- **aura** (bryany97, https://github.com/youngbryan97/aura): demos plus a
  paper in progress on Zenodo (record 24075466).
- **Codexify** (Resonant_Jones,
  https://github.com/Resonant-Jones/Codexify).
- **Kiro Crew persistent bots** (mikepun-locol,
  https://kiro.dev/blog/crew-bots/): fresh and immature, AWS
  enterprise-leaning.
- **Letta / MemGPT** (lazyEmperer): the commercial reference point, a
  whole company built on exactly this problem.
- **ferrx's unnamed file system**: folders (recipes, releases, scripts,
  tasks) and files (ARCHITECTURE.md, BACKLOG.md, GIT.md, GOTCHAS.md,
  STATE.md, TERMINOLOGY.md, WORKFLOW.md). A new session onboards by
  reading the README.
- **pullboard** (QuantitativeVibes,
  https://github.com/pullboard-dev/pullboard): "an entire software
  factory", claimed 750 GitHub stars in one month. Unverified, and
  challenged in the replies as a meaningless metric.
- Also mentioned: a persistent character on a Raspberry Pi with 107 memory
  objects, Discord channels as the management system agents re-onboard
  from, and a semantic-web graph (1850 nodes, 6781 edges).

## Pattern 1: Durable state lives outside the model

- **Do:** Keep everything the system must remember in durable structures
  outside any model session: files on disk, a SQLite or Postgres state
  graph, or both. The model is a reasoning component that reads and writes
  state; it is not the store.
- **Check:** Kill the session mid-task, start a fresh one with no prior
  context, and confirm it resumes from the checkpoint file or graph, not
  from anything the previous session "remembered".
- **Why:** The model resets, loses context, or gets replaced. A system
  whose continuity depends on one session's memory has no continuity. As
  the OP put it, by the same logic databases would not work because their
  processes occasionally restart.

## Pattern 2: Diffs as patches, with schema versioning

- **Do:** Store state evolution as patches against prior state, not full
  snapshots. Version the schema so old state stays readable as the shape
  changes.
- **Check:** Apply the patch log from empty to current state and confirm
  the result matches the live state byte for byte; then load a state file
  written under the previous schema version and confirm it migrates
  cleanly.
- **Why:** Snapshots drift and bloat; patches keep long-term evolution
  cheap and auditable. Schema versioning is what makes month-old state
  still loadable instead of silently corrupt.

## Pattern 3: Optimistic concurrency per node

- **Do:** When several agents write the same state, give each node a
  version. A write commits only if the version has not changed since the
  writer read it; the loser reloads and retries instead of overwriting.
  Cap the retries (the Jac project does this at the node level with a
  retry limit).
- **Check:** Run two agents writing the same node concurrently and
  confirm no write is silently lost and the loser retries from fresh
  state.
- **Why:** The most-reported bottleneck in the thread was sync conflicts
  on multi-agent writes to one node. Last-writer-wins silently destroys
  work; versioned writes turn the conflict into a retry.

## Pattern 4: Provenance and explicit supersession

- **Do:** Every piece of state carries provenance (where it came from,
  what evidence supports it) and a validity state. New information never
  silently overrides old information: supersession is an explicit rule
  that names what it replaces and why.
- **Check:** Pick any current fact in the store and trace it back to its
  source evidence and the decision that made it authoritative. Then
  supersede it and confirm the old version is still readable with its
  original rationale attached.
- **Why:** Persistence does not imply validity. Without provenance, a
  confident early assumption becomes permanent knowledge just because
  later agents repeated it.

## Pattern 5: Rehydrate from checkpoints, not summaries

- **Do:** A new session reconstructs its working context by reading the
  durable state directly (the graph, the state files, the checkpoint),
  never by reading a narrative summary of the previous session.
- **Check:** After a restart, confirm the session's first actions match
  the checkpoint's recorded pending work, and that no decision in the new
  session rests on a paraphrase of a paraphrase.
- **Why:** Summaries lose precision and inject the summarizer's
  interpretation into the record. The OP's distinction: continuity is
  organized state, not exact memory, and a system that waits to be
  rehydrated through the model's context is fragile.

## Pattern 6: Separate cognition from execution authority

- **Do:** Let any number of cognitive participants propose and verify
  changes, but let execution happen only when the work is authorized or
  verified. A model going off the rails must not gain permission to act
  just because it is confident.
- **Check:** Feed the system a confident but wrong proposal for a
  consequential action and confirm the action does not execute without
  passing the authorization or verification gate.
- **Why:** Reasoning is stochastic and associative; authority must be
  deterministic. Verification gates (tests, reviews, authorization,
  certificates) are what make an autonomous system safe to run.

## Failure modes

- **Stale assumptions compound.** One builder's system got noticeably
  worse around month two until he added a rule: anything the system
  inferred on its own expires unless something confirms it again. Apply
  an expiry rule to all self-inferred state; confirmed facts do not
  expire, inferences do.
- **A bad early write gets carried forward.** Diffing against prior state
  is cheap, but if the diff is all the agent ever reads, it never sees
  the full picture again, and an early error persists forever. Re-read
  the full state on a schedule, not only diffs.
- **Blanket invalidation is as bad as blind trust.** When a fact is
  corrected, invalidating everything downstream creates almost as many
  problems as trusting the stale fact. Propagate invalidation through the
  dependency graph precisely, and distinguish invalidating evidence from
  invalidating a conclusion: a conclusion can stay valid even when one of
  its supports falls.
- **Workspace cleanup eats real state.** Git preserves committed source
  but not unmerged work, test evidence, or discoveries. Decide what must
  survive before deleting anything, separate authoritative source and
  evidence from reproducible outputs, and never give the agent
  unrestricted cleanup authority. Identify and verify safe deletion
  candidates; destructive actions need explicit approval.
- **Verification that only checks itself.** A pipeline whose tests all
  pass can still be subtly wrong. The OP's example: a shape that was
  supposed to be an arc became a straight line while every test passed,
  because the pipeline's own verification had inferred that lines are
  connected. Verify against the requirements, not only against the tests.

## What the thread did not solve

- **Dependency invalidation across agents.** The direction is
  dependency-aware revalidation with verified vs inferred dependency tags,
  but no builder in the thread claims it fully works.
- **Access control inside persistent memory.** No answer in the thread to
  how a querier's clearance is verified per piece of state, or how
  sensitive state is kept out of generalized reasoning and other users'
  summaries.
- **Whether to build at all.** The counterargument in the thread is that
  frontier labs pay high six to seven figures to solve this in their
  harnesses and use the product themselves, so renting theirs for $20 a
  month beats building. The counter to that is that persistence is table
  stakes for any product weaving AI in as a core workflow.

## Agent automation upgrades

These make the patterns checkable by an agent instead of aspirational:

- **state-manifest.json:** one manifest listing every durable state file
  and graph, its schema version, and its provenance source. The agent
  validates the manifest on startup and refuses to run with an
  unmanifested state file.
- **Expiry gate:** every self-inferred fact carries a `confirmed_by`
  field and an expiry. A nightly job lists expired inferences; nothing
  expired is treated as authoritative until re-confirmed.
- **Dependency graph with tags:** every conclusion links to its supports,
  each tagged `verified` (file, link, evidence, prior decision) or
  `inferred`. On a correction, the agent flags exactly the downstream
  items whose supports changed and requires revalidation before
  consequential work continues.
- **Cleanup classifier:** three classes, enforced by path, not by age:
  authoritative (source, evidence, recovery info — never auto-deleted),
  reproducible (build outputs, temp files — deletable), disposable
  (explicitly listed outputs). The agent proposes deletion candidates
  with verification; a human approves destructive deletes.
- **Restart drill:** a scripted test that kills a session mid-task,
  starts a fresh one, and asserts the new session resumes from the
  checkpoint with identical pending work.
