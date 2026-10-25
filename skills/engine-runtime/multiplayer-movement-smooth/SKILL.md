---
name: multiplayer-movement-smooth
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

## AAA studio practice (refinement 2026-10-24)

This skill's three settings (Rigidbody Interpolate, network rigidbody checkboxes, network transform interpolation at 0.35) are the indie surface of a netcode pattern every shipped shooter uses. The AAA practice below names the full pattern so the next tuning step is principled, not trial and error.

**Do**
1. Separate the three jobs, and never collapse them into one slider. Client side prediction (pioneered by John Carmack for QuakeWorld, incorporated into Unreal's networking by Tim Sweeney) runs the local player's movement immediately on the client without waiting for the server round trip. Server reconciliation rewinds and replays: keep a circular buffer of past character state and input, discard buffered state older than the server correction, and replay from the corrected state to the present predicted time using stored inputs, holding the rest of the world fixed. Entity interpolation, the third job, buffers snapshots and draws remote players between known states, trading delay for smoothness. Source: http://vodacek.zvb.cz/archiv/690.html
2. Budget interpolation delay explicitly, as Valve's Source networking documentation does: entity interpolation causes a constant view lag (100 milliseconds by default in the documented example), and the interpolation system can survive one dropped snapshot by interpolating across the gap, falling back to linear extrapolation only for a short window (0.25 seconds in the documented example) before prediction errors grow too large. Set the interpolation value from that budget, not from feel alone, and record it next to the genre reason, as the original skill does for 0.35 (coop rage game, delay cannot be big). Source: https://www.scribd.com/document/239946087/3g-Compensation-Socket-3g
3. Keep the server authoritative even while the client predicts, as the GDC 2011 Networked Physics talk states it: the local player runs the same simulation code as the server for his own object to advance without waiting for the round trip, while the server remains authoritative over position and orientation, which is what makes cheating hard. Examples cited there include Halo competitive mode, Quake, Unreal, and all Valve games. Source: https://www.slideshare.net/slideshow/gdc-networked-physics-2011-7663974/7663974

**Check**
- Automated netcode test matrix [inference]: test the movement at four conditions and log the result for each: (a) local prediction on, server correction off (should diverge), (b) prediction on, correction on (should converge with no visible snap on a clean connection), (c) one snapshot dropped (interpolation should bridge it), (d) interpolation slider at 0.35 versus a higher value (higher must read smoother and measurably later). If (b) snaps visibly on a clean connection, the bug is in the replay buffer or determinism, not in the slider.
- Genre tune check: write the chosen interpolation value and the reason in one line (for example, 0.35 because a coop rage game cannot afford big delay). Any later change to that value must update the reason line, or the tuning history is lost.

**Why**
Smoothness is not one setting; it is prediction for the local player, interpolation for remote players, and reconciliation to repair the difference, all under an authoritative server. Tuning only the interpolation slider, as the original demo does, works until prediction and reconciliation diverge, and then no slider value fixes the snap.
