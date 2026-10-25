---
name: ro-engine-neural-vs-scripts
description: "Test game AI empirically: pit deterministic behavioral scripts against a learned policy in a custom engine and measure which wins. Trigger when evaluating game AI approaches."
---

# I built a Ragnarök Online engine to test if a neural network can beat deterministic scripts

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Test the question empirically: pit deterministic behavioral scripts against a learned policy in the same engine and measure which wins.

## Source

Creator: u/Known_Chip8544

Source: https://v.redd.it/23mmjd2nsrqh1 | r/RagnarokOnline post 1wly4u6 (score 53) | native clip (demo, not tutorial)

## Tools used

Tools used: Godot (custom Ragnarök Online prototype engine built by the author). Per-character behavioral scripts (author-built; deterministic baseline and reinforcement-learning neural network teams are both authored by the author, with AI assistance for learning neural networks, per his own account).

**Do**
1. Define the target: a "fake player" good enough to beat an experienced PvP player.
2. Inspired by the concept of "fake players" (the author cites a post about Ragnarök Offline that he tested and got hooked on).

**Check**
- **[inference]** The question is falsifiable only if "beat" is measured in matches, which leads directly to the match framework below.

**Why**
A concrete opponent (deterministic scripts, then a real PvP veteran as the eventual goal) turns a vague AI interest into a benchmark.

## Phase 1: Set the question: can a fake player beat a veteran?

## Phase 2: Build the testbed: custom RO prototype in Godot

**Do**
1. Build a custom Ragnarök Online prototype engine in Godot.
2. Give it the ability to select characters and assign their behavioral scripts per character.

**Check**
- The testbed must support symmetric team setup: same roster available to both sides, differing only in behavior logic.

**Why**
A prototype instead of the real RO client means full control over characters, scripts, and match conditions. Per-character script assignment is the mechanism that lets two *different* control schemes fight each other.

## Phase 3: Build the deterministic baseline: Team A

**Do**
1. Field a 2v2 (Champion + Professor/Scholar on each side).
2. Assign deterministic scripts with explicit roles: the Professor focuses on crowd control/debuffs; the Champion focuses on kills.

**Check**
- Baseline behavior is inspectable and repeatable: role-based, no learning involved.

**Why**
The deterministic scripts are the yardstick. They encode *known-good* strategy (CC/debuff setup into a kill role), so the RL agent is measured against competent play, not random play.

## Phase 4: Build the challenger: Team B, reinforcement-learning neural network

**Do**
1. Train a reinforcement-learning neural network to control the same 2v2 roster.
2. The author notes he knows "almost nothing about neural networks" and used AI assistance to learn and develop it.

**Check**
- **[inference]** Training progress is judged by match outcomes against Team A, not by loss curves (the author reports results in match terms only).

**Why**
RL is the hypothesis: learned behavior vs. authored behavior. AI-assisted development is the author's stated path given his starting skill level.

## Phase 5: Run the symmetric match and observe

**Do**
1. Run a symmetrical 2v2 match: Team A (deterministic) vs. Team B (RL neural network).
2. Watch the outcome: Team A "completely rolls over" Team B; the neural network "hasn't figured out how to handle the deterministic strategy yet."

**Check**
- Symmetry (same roster, same match conditions) isolates the variable under test: behavior logic.

**Why**
A symmetric 2v2 removes roster excuses. The decisive win establishes the current state: authored role-based strategy beats the early RL agent, and the experiment continues toward the eventual goal (a fake player that can beat a real human PvP veteran).

### Community notes

- Alone_Conference7144 (score 4) advised running training in "simulated time," warning the author will "not get any results in a meaningful amount of time" at real-time speed. No reply from the author in the data.
- Kyruka (score 2) described a parallel idea: an LLM-driven team with full game guides vs. a team that only knows basic concepts, competing in WoE to see if the AI discovers strategies the guides never mention, with separate exp/drop rates for bots vs. humans.

## The human method, distilled

1. **Fix the question first.** "Can a fake player beat a veteran" becomes "can Team B beat Team A," which is measurable.
2. **Build the arena before the agent.** A controllable prototype with script assignment is the precondition for the whole experiment.
3. **Benchmark against competence, not randomness.** The deterministic baseline uses real roles (CC/debuff → kill), so a win means something.
4. **Symmetry isolates the variable.** Same roster, same match; only the control logic differs.
5. **Report the negative result.** "The network hasn't figured it out yet" is the finding; it defines how far training still has to go.
6. **Simulated time is the training bottleneck** (community advice): real-time matches are too slow to produce meaningful RL results.

## Depth status
 DEPTH-LIMITED (demo clip, not tutorial; no network architecture, training regimen, reward function, Godot implementation details, or match count given. The experimental method is fully reconstructable from the post text; everything beneath the match description is [inference] or community suggestion.)

---

## AAA studio practice

Sources:
- Ubisoft, For Honor (GDC 2025 session, as listed): scripted bots traditionally took around four weeks per hero to define; the production team trained reinforcement-learning bots by self-play against existing scripted bots and themselves, combined RL with behavior trees into hybrid bots, added action masking for designer control, and shipped the hybrid bots after testing them against their scripted counterparts. https://thetoolsmiths.org/2025/03/12/gdc-2025-toolsmiths-guide/
- Embark Studios, ARC Raiders (GDC talk, as reported by 80 Level): enemy AI blends learned locomotion with behavior trees, with reinforcement learning used for the physics-driven movement problem while higher-level behavior stays authored and controllable. https://80.lv/articles/inside-the-magic-of-machine-learning-that-powers-enemy-ai-in-arc-raiders

**Do**
1. Keep the scripted baseline as the shipping yardstick, exactly as For Honor did: do not retire Team A when Team B exists; every RL checkpoint must play the symmetric match against Team A and log win/loss, not just loss curves.
2. Train in simulated time, not real time (the community advice in this skill, now backed by the For Honor self-play pattern): run headless matches at accelerated tick rate with rendering disabled, and log matches per hour as the training throughput metric.
3. Automate the benchmark harness: script N symmetric matches per checkpoint (same roster, same map, seeds varied), write results to a CSV with checkpoint id, seed, winner, and match length, and fail the checkpoint if it regresses against Team A.
4. Hybridize before shipping, following both studios: keep behavior-tree roles (CC/debuff into kill) as the outer structure and let the learned policy choose within masked actions, so designers keep an inspectable, tunable layer.

**Check**
- The harness reproduces the original finding on demand: Team A beats the early Team B checkpoint.
- Training throughput is measured in matches per hour, and it rises when rendering is disabled and tick rate is accelerated.
- No checkpoint is promoted on loss curves alone; promotion requires match wins against Team A.

**Why**
Both production cases converge on the same lesson: learned policies do not replace authored behavior, they are measured against it and then hybridized with it. The symmetric match in this skill is already the right benchmark; automation turns it from a one-off demo into a repeatable gate.
