---
name: claude-code-agent-office-threejs
description: "Turn Claude Code session logs into a live three.js office where each session is a team lead, each sub-agent is a character at a role-based desk, and status is glanceable: A* pathfinding, canvas-texture monitors, LED status encoding, and a low-power throttle so it can stay open all day. Trigger when several agent sessions run in parallel and tab-hopping through terminals is how status gets checked today."
---

# Claude Code Agent Office in Three.js

## Purpose

This skill reconstructs the exact system xzinkx demonstrates for visualising Claude Code sessions as a live three.js office, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: read the logs Claude Code already writes, turn each session and sub-agent into a character in a three.js office, and make status glanceable instead of tab-hopping through terminals.

## Source

Creator: xzinkx. Post: "I turned my Claude Code sessions into a live Three.js office. Every sub-agent walks in, works at a desk and walks back to report when it's done" https://www.reddit.com/r/threejs/comments/1y2ofun/i_turned_my_claude_code_sessions_into_a_live/ (r/threejs post 1y2ofun, score 20, 24 comments; full post text and author replies read) | Live demo (made-up data): https://zinkxx.github.io/agent-office/ | Code: https://github.com/zinkxx/agent-office | 2026-11-23 scout run, audit 8.

## Tools used

Claude Code (session logs as the data source), React 19, three.js r170, A* pathfinding, canvas textures, MIT licence, "fully local". No log format, polling interval, or frame-time numbers are stated.

## Phase 1: Read Claude Code's local logs

**Do**
1. "It reads the local logs Claude Code writes and turns every session into a team lead and every sub-agent into a character that walks in, sits at a role-based desk and reports back when it's done. Idle ones end up on the sofa or the console in the lounge."
2. Keep the system "fully local". No log path, file format, or read interval is stated; do not invent one.

**Check**
- The mapping must hold for the cases the author names: session to team lead, sub-agent to character, idle to sofa or console. A session waiting on input must be distinguishable at a glance (see Phase 3).

**Why**
The logs already exist; the office is a visualisation over them, not a new agent harness. The author does not state this "no new harness" principle in those words; it follows from "reads the local logs" plus "fully local", labelled here as inference.

## Phase 2: Animate low-poly articulated characters with A* and canvas-texture monitors

**Do**
1. "Low-poly articulated characters with animations per activity (typing, reading, walking over to a colleague)."
2. "A* pathfinding so they walk around the desks instead of through them."
3. "The monitors are canvas textures that change with what the agent is doing (code, terminal, search)."
4. "The server rack LEDs blink with the share of busy agents, and the floor LED strip turns yellow when someone is waiting on me."

**Check**
- Pathing must route around desks, not through them. Monitors must match the agent's current activity. The floor strip must be yellow exactly when someone waits on the user.
- A commenter confirms a status encoding independently: "You get a little blue circle on the ones waiting on input. And grey circle when they're working" (romansamurai). The author does not confirm or deny those colours in a reply; treat them as a commenter's observation, not the author's spec.

**Why**
Every visual element encodes one status fact: activity (animation plus monitor), busyness share (rack LEDs), waiting-on-user (floor strip). The office is a status board first and a playground second, in the author's own framing: "for me it's mostly a glanceable status board: with 4–5 sessions in different terminals, a character waving at the lead is faster to spot than tabbing through to find which one is waiting on input."

## Phase 3: Throttle rendering so it can stay open all day

**Do**
1. "Rendering slows down when the tab is unfocused and stops when it's hidden, so it can stay open all day." The author repeats the point in a reply: "it has a low-power mode, throttles when the tab isn't focused and stops rendering entirely when it's hidden, so in a background tab it mostly idles."
2. Accept the scope limit the author states with it: "if it doesn't fit your workflow, it doesn't... definitely a niche thing, and a fun excuse to build a 3D office".

**Check**
- A hidden tab must stop rendering entirely; an unfocused tab must throttle. No throttle rate or power figure is stated.

**Why**
An always-open status board must cost almost nothing when nobody looks at it. Low-power mode is what makes "stay open all day" viable; without it, the 3D renderer would, in a critic's words the author accepts, "kill your laptop".

## Phase 4: Respect the fan-out shape of real Claude Code work

**Do**
1. Build for the fan-out the author describes, not for parallel writers: "in claude code a lot of sub-agents are read-only helpers: an explore agent searching the codebase, a plan agent, a reviewer reading the diff, and they report back to the one session that actually edits. multiple sessions are usually different projects, and each project gets its own room."
2. Do not fold in the parallel system another commenter (q_tech_x51) describes (virtual HQ, chief of staff, real tool usage, 2D plus three.js versions). That is a different person's system, not this project's method.

**Check**
- The office must show the actual fan-out: read-only helpers reporting to one editing session, different projects in different rooms. Parallel writers on the same files would be, in the author's words, "a merge conflict factory", and the office does not claim to solve that.

**Why**
The visualisation is honest only if it matches how the sessions actually work: helpers that read, one session that edits, projects kept in separate rooms. The office makes "that fan-out visible", in the author's words.

## Failure modes

- **Characters walk through desks:** the A* pathing in Phase 2 is not routing around obstacles. The desks must be obstacles in the pathfinding grid, not decoration.
- **Status unreadable at a glance:** monitors, LEDs, or the floor strip are not encoding the current state. Every element must carry exactly one status fact (Phase 2); decoration that encodes nothing is the failure.
- **Laptop cost of an always-open tab:** the low-power mode in Phase 3 is missing or incomplete. A hidden tab must stop rendering entirely.
- **Wrong scope:** "if your flow is one terminal and you read the main session at the end, you honestly don't need it" (author). A single-session flow is not the problem this system solves; building it there adds a renderer for no status gain.
- **Parallel writers on the same files:** the office does not solve merge conflicts. Do not present the fan-out visualisation as a collaboration tool for simultaneous editors.

## The human method, distilled

1. "it's also just a fun three.js playground, which is honestly half the reason it exists". The method is half status board, half playground, and the author is explicit about both halves.
2. Scope honesty as a design habit: "if your flow is one terminal and you read the main session at the end, you honestly don't need it."

**Depth status:** FULL (post-text plus author replies). Stack, log source, animation/pathing/monitor/LED encoding, and low-power behaviour are exact. Missing: log format and read interval, A* grid details, character rig details, and any performance numbers. A media download of the short clip would show the office in motion but would not supply the undisclosed log/parsing details.
