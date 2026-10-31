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

## AAA studio practice

The vendor pitch — photos in, pipeline-compatible heads out — survives
production scrutiny on two points (custom sculpts stay the norm;
photo input is legitimate) and gets corrected on one (topology is a
pipeline choice, not a law). Three shipped-title sources:

**Ninja Theory / Senua's Saga: Hellblade II (2024): MetaHuman as
pipeline, not stock heads.** VFX director Mark Slater-Tunstill:
**"None of our faces in the game were MetaHuman creator faces, they're
all custom"** — the studio uses MetaHuman as a pipeline while
sculpting every face custom. That directly answers the thread's
topology-lock-in objection: the production norm is custom heads
through a shared topology pipeline. For in-game (non-cinematic)
facial animation — e.g. the Senua vs Thórgestr beach fight — they
used the **MetaHuman Animator pipeline with head-mounted cameras and
the iPhone technique**: actors watched gameplay footage and recreated
expressions, mapped back onto the custom faces, eliminating full
head-mount performance-capture sessions for those shots. The
3Lateral-derived cubic-motion-processing face rigs handled cinematics;
MetaHuman Animator filled the in-game gap where no pipeline existed.
(Source: https://www.eurogamer.net/digitalfoundry-2024-the-big-senuas-saga-hellblade-2-tech-interview —
Eurogamer/Digital Foundry interview, 2024.)

**Guerrilla Games / Horizon Forbidden West (2022, GDC 2022 "Creating
the many Faces"): head production at scale.** Lead character artist
Arno Schmitz's talk gives a usable throughput bar: **168 high-quality
heads produced in 3 years**. Tech specialist **3Lateral built a custom
"Gene Splicer" tool** that generates new faces by mixing pre-existing
head assets — production-grade topology-compatible head generation,
the AAA analogue of KeenFace's topology goal. **Photogrammetry photos
were used as a LookDev tool for heads** — photo-to-head is an accepted
production input stage, not a novelty. Their reuse-hiding trick has a
named mechanism: the **"faceprint" decal**, whose transparency is
driven by each head's unique cavity map so individual wrinkle
patterns carry through and hide asset reuse — directly convertible
into an executable check (cavity-map uniqueness per head). And a
stated production lesson the skill must adopt: the team reviewed
cinematic-quality rigs in an external viewer and **overlooked how
content looked in-engine and at lower LODs**.
(Source: https://www.gamedeveloper.com/marketing/creating-and-integrating-the-many-faces-of-horizon-forbidden-west —
Game Developer summary of the GDC 2022 talk; Guerrilla session page:
https://www.guerrilla-games.com/read/creating-the-many-faces-of-horizon-forbidden-west)

**Optional, labeled demo claim:** Epic's State of Unreal 2023
MetaHuman Animator demo (GDC 2023) showed Melina Juergens (Senua's
actor) recording facial video on an iPhone and producing a full
animation sequence in ~3 minutes, applicable to any face, with
animator touch-up still expected. The "3 minutes" figure is a demo
claim, not a shipped-production number.
(Source: https://www.pcgamer.com/unreals-new-metahuman-animator-can-turn-an-iphone-video-into-a-scarily-accurate-game-animation-in-three-minutes/)

## Agent automation

**Do**
1. **Custom-face-first acceptance** (Ninja Theory, agent design):
   judge every KeenFace output against the input photos' subject,
   never as a "stock head" — a written comparison step in the
   pipeline: landmark-delta report between input photos and output
   mesh before the head is accepted.
2. **Cavity-map uniqueness check** (Guerrilla "faceprint", agent
   design): when generating multiple heads, hash each head's cavity
   map and fail on duplicates — the scripted version of Guerrilla's
   reuse-hiding discipline, catching copy-paste generation.
3. **In-engine LOD acceptance renders** (Guerrilla's stated lesson,
   agent design): render the head at the game's actual lowest LOD
   and in-engine, not just the hero render. Extend the skill's
   existing texture-resolution check into a three-distance
   acceptance render (hero, mid, lowest LOD) — the demo user's
   "low-res textures don't hold up" complaint becomes a gate with
   distances, not a warning.
4. **Throughput manifest** (Guerrilla's 168-in-3-years bar, agent
   design): log production time per head in `head-manifest.json`
   (photo count, turnaround time, acceptance verdict). Over many
   heads this becomes the project's own throughput benchmark.

**Check**
- All four are scripts with pass/fail output; the LOD renders are
  saved as acceptance images the agent can diff across revisions.
- The cavity-hash check runs before any head reaches the engine.

**Why**
Production treats photo-to-head as a legitimate input stage but
judges it on pipeline fit (Ninja Theory: custom sculpts through a
shared topology), uniqueness (Guerrilla: cavity-driven faceprints),
and in-engine appearance at real LODs (Guerrilla's hard lesson).
These gates turn the skill's thread objections (lock-in, low-res
textures, web-tool risk) from forum arguments into checks that run.

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
