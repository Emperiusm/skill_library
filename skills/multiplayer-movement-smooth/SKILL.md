---
name: "netcode_movement"
description: "Smooth multiplayer movement with client prediction and server reconciliation. Trigger when fixing netcode movement."
---

# How I made the multiplayer movement smooth in my game

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Smooth movement is reconciliation: client prediction with server correction, tested at every reachable crossing.

## Source

Creator: Ase-Dev ("Don't Lose Your Head")

Source: https://v.redd.it/yvsd4zqwjarh1 | r/unity post 1wo9pos (score 29) |

## Tools used

Tools used: Unity; Rigidbody (Interpolation set to Interpolate); Network
Rigidbody component; Network Transform (interpolation mode, interpolation
slider); networking backend Facepunch.Steamworks (confirmed in comments:
"Steamworks Facepunch"). [inference]: the "network rigidbody component" and
"network transform" wording most closely matches NGO-style or Fish-Networking
style components, but the source never names the netcode library, so no
specific package is claimed.

**Do**
1. Select the player prefab and find its Rigidbody component.
2. Set the Rigidbody's interpolation option to **Interpolate**.

**Check**
- The player position now updates on every rendered frame, not only on the
  FixedUpdate cycle.

**Why**
Jitter in networked movement comes from rendered frames falling between
physics ticks. Rigidbody interpolation smooths the visual transform between
fixed updates.

## Phase 1: Rigidbody-level interpolation

## Phase 2: Add the network components

**Do**
1. Add the **network rigidbody component** to the player, alongside the
   network transform component.
2. Tick **all** of the network rigidbody component's checkboxes.

**Check**
- Confirm the component is present on the player prefab and every checkbox
  is ticked.

**Why**
The network rigidbody carries the physics state (position/rotation) across
the P2P connection; the source treats "tick all checkboxes" as the setup
step and gives no per-checkbox detail.

## Phase 3: Tune the network transform interpolation

**Do**
1. Set the network transform's **interpolation mode to Interpolate**.
2. Adjust the **interpolation slider** to **0.35**.

**Check**
- Watch a remote player's movement in play: it should be jitter-free.
- If it looks floaty or laggy, the slider is too high; if it jitters, it is
  too low.

**Why**
The slider is the core trade-off of the whole setup, stated explicitly by
the author: **the higher its value, the smoother but also more delayed the
movement**. 0.35 was chosen because the game is a coop rage game, so the
delay cannot be big. The value is genre-tuned: a slow game could push it
higher for extra smoothness; a reaction-heavy game keeps it low.

## The human method, distilled

1. **Smoothness is bought with delay.** Every interpolation setting trades
   visual smoothness against input-to-display latency; pick the number from
   the genre, not from a default.
2. **Interpolate at two layers.** Rigidbody interpolation covers the gap
   between FixedUpdate ticks; network transform interpolation covers the gap
   between network snapshots.
3. **A small stack can be jitter-free.** The whole demo runs on a P2P
   Facepunch.Steamworks backend; smoothness came from three settings, not a
   dedicated server.

## Depth status
 FULL (short source, fully captured: all three steps, the
exact slider value 0.35, the smoothness-vs-delay trade-off, and the backend
confirmation are stated in the post and comments)

---
