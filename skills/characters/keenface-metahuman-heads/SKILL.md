---
name: keenface-metahuman-heads
description: "Turn reference photos into production-ready 3D heads with native MetaHuman topology, clean bald base mesh, and full PBR maps (Base Color, Normal, Roughness, Specular) using KeenFace. Trigger when a character pipeline needs a MetaHuman-compatible head from photos."
---

# KeenFace: Photos to MetaHuman-Topology Heads

## Purpose

This skill turns a handful of reference photos into a production-ready
3D head with **native MetaHuman topology** — a clean bald base mesh
plus full PBR maps — that drops into UE or any DCC for rigging,
sculpting, or animation. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: feed photos, get a head that slots
into the MetaHuman pipeline you already have — topology compatibility
is the product, not the reconstruction alone.

## Source

r/vfx, nord_little (KeenTools team) (full announcement comment + post
text + 25-comment thread with demo feedback, 2026-10-30):

- https://www.reddit.com/r/vfx/comments/1xihge4/productionready_3d_heads_with_metahuman_topo
- Tool: https://keenface.ai

Evidence note: deliverables list is the vendor's; texture-resolution
and pricing notes are attributed single-commenter claims, not verified
by this run.

## Tools used

**KeenFace** (keenface.ai) — web tool from the KeenTools team. Inputs:
reference photos, "a few web grabs or full studio shots, doesn't really
matter." Outputs: head mesh in **native MetaHuman topology**, **clean
bald base mesh** (no baked hair, no messy geometry artifacts), full
PBR set: **Base Color, Normal, Roughness, Specular**. Downstream: UE or
any DCC (rigging, sculpting, animation).

## Phase 1: Collect reference photos

**Do**
1. Gather a few reference photos of the subject. The vendor bar is
   deliberately low: "a few web grabs or full studio shots, doesn't
   really matter."

**Check**
- (Inference) The vendor claims "a solid likeness." Photo coverage
  (front/side angles) still determines likeness quality; the vendor
  states no minimum set, so test with your own subjects.

**Why**
Low input bar — casual photos, not a scan rig — is the adoption
strategy.

## Phase 2: Run the web tool

**Do**
1. Feed the photos to KeenFace (web tool).

**Check**
- Does the head come back with a **clean bald base** — no baked hair,
  no geometry artifacts? The vendor lists this explicitly.
- Check texture resolution before committing: one demo user reported
  "the textures produced are really low-res and don't hold up at all"
  (attributed; vendor did not dispute in the thread).

**Why**
Baked hair and messy artifacts are the failure modes this product
claims to eliminate; verify the claim on your own subject.

## Phase 3: Drop it into the MetaHuman pipeline

**Do**
1. Take the head mesh — native MetaHuman topology — into UE or any DCC.
2. Rig, sculpt, or animate as usual.

**Check**
- The honest objection from the thread (attributed): "I'm not gonna
  have the whole studio change our base topology for MetaHuman's one,
  so 'production ready' is a big stretch." Verify the topology fits
  YOUR pipeline before paying.
- Vendor is web-only as presented; one commenter warns "if it's not
  installable locally, you can't rely on it" (attributed).

**Why**
Topology compatibility is the entire value proposition. A studio on a
different base topology gets nothing from the product, however good
the reconstruction is.

## The human method, distilled

1. **Sell the interface, not the algorithm.** The pitch is "native
   MetaHuman topology" — it fits the pipeline you already have.
2. **Low input bar, high compatibility bar.** Casual photos in,
   production topology out.
3. Verify price and resolution yourself: pricing was criticized
   (~$30 for 2 heads, single commenter — not confirmed on-page by
   this run) and texture resolution questioned by a demo user.

## Failure modes

- **Low-res textures:** one demo user found the textures don't hold
  up. Fix: test the demo on your own subject before buying.
- **Topology lock-in:** "production ready" assumes a MetaHuman-based
  pipeline. Fix: confirm your studio's base topology first.
- **Web-tool dependency:** not installable locally (per the thread).
  Fix: treat as a service with availability risk, not as owned
  tooling.

**Depth status:** FULL (vendor announcement with full deliverables
list + 25-comment thread including demo feedback and objections;
price and exact mesh specs are single-commenter claims).
