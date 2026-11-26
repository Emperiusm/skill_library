---
name: h3md-expression-studio-minimax-h3
description: "Control facial expressions in MiniMax H3 video with the H3MD Expression Studio (free, AGPL-3.0): pick from 25 built-in expressions or tune eyes, gaze, cheeks, and mouth with live-updating sliders, save Expression Only for any face or Character + Expression as a RefMod reference clip the H3MD Director follows like a tiny LoRA, learn an expression from a close-up video up to 6 seconds, then export pictures or a prompt line. DEPTH-LIMITED: post text only; the walkthrough video, node repo, and Civitai workflow were not inspected. Trigger when a prompt cannot describe the exact expression a shot needs."
---

# H3MD Expression Studio for MiniMax H3

## Purpose

This skill replaces prompt-writing for facial expressions with a picked or learned face that MiniMax H3 follows. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: pick or learn an expression as a reusable reference, then let H3 and the H3MD Director follow it.

## Source

- Post: "Prompts can't describe a pout or a held-back smile, so I made a free open-source expression studio for MiniMax H3" by ReferenceFluffy6159 — https://www.reddit.com/r/comfyui/comments/1y4h1sv/ (score 23, 0 comments). Evidence: the full post text (828 characters) only. Walkthrough video (https://youtu.be/mPO_a0q1IfE, English audio, Chinese audio track and subtitles), nodes (https://github.com/1113800942/ComfyUI-H3MD-Expression), and workflow page (https://civitai.com/models/3063662) were NOT inspected in this run; the download allowance was exhausted. Scout audit 2026-11-26, audit 6.

## Tools used

H3MD Expression Studio (new, free, AGPL-3.0); MiniMax H3; the H3MD Director; ComfyUI nodes (ComfyUI-H3MD-Expression). No ComfyUI version, model checkpoint name, VRAM figure, or timings disclosed; none is invented here.

## Phase 1: Pick an expression from the library, or tune one with sliders

**Do**
1. "25 built-in expressions, or fine-tune eyes, gaze, cheeks and mouth with sliders – the face updates live."
2. First image in the post: "same face, expression picked from the library in one click."

**Check**
- The face must update live as sliders move, so the chosen expression can be judged before any video is generated. The post's proof is the before/after pair: library expression vs. what H3 generates following it.

**Why**
The premise is in the title: "Prompts can't describe a pout or a held-back smile." A picked/tuned face is exact where a prompt is approximate; the library makes the exact choice one click.

## Phase 2: Save the expression in the form the next step needs

**Do**
1. "Save Expression Only (works on any face), or Character + Expression as a RefMod – a short reference clip that H3 and the H3MD Director follow, like a tiny LoRA."

**Check**
- Expression Only must transfer to any face (the check is reuse across faces); the RefMod clip must carry both character and expression into H3 (the check is that H3 follows the clip, "like a tiny LoRA").

**Why**
Two save forms serve two jobs: a portable expression for any face, and a character-locked reference clip for a specific person. The RefMod analogy ("like a tiny LoRA") states the intent: small, reusable conditioning, not a full fine-tune.

## Phase 3 (alternative input): Learn an expression from a close-up video

**Do**
1. "Learn an expression from a close-up video (up to 6 s, head motion optional)."

**Check**
- The learned expression must be usable the same way as a library expression (Phase 2 saves). No accuracy measure or example is disclosed.

**Why**
[Inference: learning from video covers expressions no library entry matches, without writing a prompt for them.] The 6-second cap and optional head motion are the only stated constraints; no frame-rate or resolution is stated.

## Phase 4: Export the result as pictures or as a prompt line

**Do**
1. "Export pictures (face only or full body) or copy the expression as a prompt line."

**Check**
- The export must match the face the studio showed live. The prompt-line export is the fallback for workflows that still need text; no prompt-line format example is disclosed.

**Why**
The studio is a front end, not a closed system: pictures for direct use, a prompt line for text-based workflows. Either export carries the exact expression out of the studio.

## The human method, distilled

1. **Show the face, don't describe it:** a library pick or slider tune replaces the prompt for expressions prompts cannot describe.
2. **Make the expression reusable:** save it once (Expression Only or RefMod), follow it many times.

## Depth status

DEPTH-LIMITED. Full post text only; the linked walkthrough video, node repository, and Civitai workflow page were not inspected, and no node settings, checkpoint names, VRAM figures, or timings are disclosed. A media download of the walkthrough would add the spoken node settings and demo timings. Do not present the walkthrough's contents as reviewed.
