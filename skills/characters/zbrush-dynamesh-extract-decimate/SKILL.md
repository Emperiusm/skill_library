---
name: zbrush-dynamesh-extract-decimate
description: "Sculpt a character with zero booleans: one Dynamesh for the whole body, extract pieces out of it, harden edges with remesh/extrude/subdivide, alphas for micro-detail, Decimation Master from 250M to 10M polys, Marmoset Toolbag renders. Trigger when a ZBrush character needs clean extracted pieces without boolean seams."
---

# ZBrush Character Workflow: Dynamesh, Extract, Decimate

## Purpose

This skill follows Clear-Counter-640's character workflow for the
ZBrush 2027 beta testing program: **one Dynamesh for the whole
character, extract the pieces, remesh/extrude/subdivide for sharp
edges, alphas for micro-detail, no booleans anywhere.** Sculpt at
absurd density, decimate with Decimation Master, render in Marmoset
Toolbag. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle).

## Source

r/3Dmodeling, Clear-Counter-640, "3D Character I did for Zbrush 2027
beta testing program" (score 196, 34 comments, 2026-10-30):

- https://www.reddit.com/r/3Dmodeling/comments/1xjls24/
- Native Reddit video: v.redd.it/0ykme5q3vmyh1

Evidence note: all facts below are the author's claims from the post
text plus the author's workflow comments. The 2027-beta tool
specifics are under NDA (stated, not hidden); the geometry workflow
itself is fully described. No third-party verification in this audit.

## Tools used

- ZBrush (2027 beta; the author worked with Maxon directly testing new
  tools, under NDA for the specifics)
- Dynamesh (the whole character starts as one)
- Extract, remesh, extrude, subdivide
- Alphas (for the small details)
- Decimation Master
- Marmoset Toolbag (final renders)

## Phase 1: Block the whole character as one Dynamesh

**Do**
1. Start the entire character as a single Dynamesh.
2. Extract the pieces out of that Dynamesh. The author is explicit:
   "Not a single Boolean actually, it started as a dynamesh for the
   whole character, then making pieces by extracting out of that
   dynamesh."

**Check**
- Pieces separate cleanly with no boolean seams to clean up.

**Why**
Extraction from one Dynamesh keeps every piece in the same sculptural
language; booleans would introduce hard-surface seams into an organic
character.

## Phase 2: Harden edges with remesh/extrude/subdivide

**Do**
1. Remesh, extrude, and subdivide the extracted pieces to get sharp
   edges.
2. Use alphas for the small details.
3. Budget brute-force subdivision instead of optimizing early. The
   author's machine is a 5950X with 64 GB DDR4: "I just needed mesh
   resolution to use some alphas and the only way was to subdivide
   it." Optimization would have taken "10 times more" than the
   brute-force subdivide, and he works 2-3 pieces per day on personal
   time.

**Check**
- Edges read sharp at render distance; micro-detail comes from
  alphas, not geometry.
- Watch the clock: if an optimization pass takes longer than a day of
  brute-force subdividing, subdivide.

**Why**
Topology operations (remesh/extrude/subdivide) carry the form; alphas
carry the detail. On personal time, brute force beats cleverness when
the hardware can take it (5950X + 64 GB DDR4 handled 250M polys).

## Phase 3: Decimate and render

**Do**
1. Decimate the 250M-polygon character with Decimation Master down to
   10M.
2. Export to Marmoset Toolbag for the final renders.

**Check**
- 250M → 10M (25x reduction) with silhouette and alphas intact.

**Why**
Sculpt at absurd density, render at sane density; Decimation Master is
the bridge, Marmoset is the presentation.

## The human method, distilled

1. **"Not a single Boolean"**, extraction over booleans for organic
   hard pieces.
2. **Pick the proportion system before sculpting**: the 8-head ideal
   figure ("that's the ideal proportions most artists use, specially
   for women, that longer legs add more feminine") vs 7.5 heads for a
   realistic street human.
3. The author is shipping a project-based beginner tutorial pack
   (sphere, orange, keyboard, gun, Fortnite-style full character),
   watch his Instagram for the release.

**Depth status:** FULL (author post text + author comments; the actual
2027-beta tool specifics are under NDA, which is stated, not hidden).
