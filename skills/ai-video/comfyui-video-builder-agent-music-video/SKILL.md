---
name: comfyui-video-builder-agent-music-video
description: "Let a Claude Sonnet agent build a full music video inside ComfyUI through MCP: one prompt briefs the whole job, the agent creates Krea2 reference images, lyrics, a YUE2 song, the story, and every scene prompt, runs the Video Builder overnight, reviews each scene's frames, and re-runs bad scenes up to 3 times, with no post-edits. Includes the verbatim one-prompt brief and the reference-anchoring failure mode. Trigger when a full AI music video needs to be produced agentically rather than scene by scene."
---

# ComfyUI Video Builder Agent Music Video

## Purpose

This skill reconstructs the agent music-video workflow from the
author's post, step by step, so another agent can follow the same
process. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The video's
core method is: one prompt to an agent that drives ComfyUI through
MCP, the agent does everything (refs, lyrics, song, story, prompts),
runs overnight, reviews its own frames, and re-runs bad scenes up to 3
times, with no post-edits.

## Source

Creator: Cheap_Credit_3957. Reddit post:
https://www.reddit.com/r/comfyui/comments/1xfh9a4/sonnet_55_created_a_music_video_in_comfyui_fully/
(r/comfyui post 1xfh9a4, score 143, 60 comments) | 2026-10-27 scout
run, audit 5. Builder:
https://github.com/vrgamegirl19/comfyui-vrgamedevgirl (a 2-pass
workflow in the Beta2.0 workflows folder uses the same settings for a
single scene; the full video needs the builder). Same author and
builder as the storyboard-grid skill
(`minimax-h3-storyboard-grid-reference`); this skill is the
agent-driven variant, where the agent owns every creative decision
from one prompt, rather than the human prompting shot by shot.

## Tools used

**Claude Sonnet 5.5** (agent), **ComfyUI Video Builder UI custom node
+ MCP feature** (the author's builder), **Krea2** (text-to-image
reference images), **YUE2** (song generation), **MiniMax H3** (video;
same builder and settings family as the storyboard-grid skill).

## Phase 1: Prompt once, and let the agent own the whole job

**Do**
1. Open the Video Builder UI custom node MCP feature; do not open
   ComfyUI itself (the author states: "I didn't even have to open
   ComfyUI").
2. Give Sonnet 5.5 one prompt: "Create a theatrical rock/metal music
   video with creative costumes. Female singer."
3. Let Sonnet do the following on its own, using a Skill and the
   Video Builder MCP: use the Krea2 text-to-image workflow to create
   the reference images of the full band and the locations; create
   the lyrics; create the song using YUE2; create the full story;
   create all the prompts for every scene.

**Check**
- The author is explicit about authorship: "Claude created this, not
  me" and "I did not make this video. Claude made it. It created the
  ref images as well."

**Why**
- The single prompt is the whole brief: everything downstream (refs,
  lyrics, song, story, scene prompts) is agent-owned, which is what
  makes this a different workflow from the hand-prompted grid method,
  even though both use the same builder.

## Phase 2: Run overnight, then review and retry (up to 3 times)

**Do**
1. Let Sonnet run the builder overnight.
2. After the video is done, let Sonnet review each scene by looking
   at the frames, checking for issues and prompt compliance.
3. If Sonnet finds issues, it fixes the prompt and re-runs that scene,
   until it gets it right, up to 3 times.
4. Ship what you wake up to: no post-edits.

**Check**
- Every scene has passed a frame review (or exhausted its 3 retries);
  the author notes the result "still has its issues" and that Claude
  "went a bit overboard with the theatrical aspect i asked for," but
  that it did what was asked.

**Why**
- The retry cap is the quality contract: 3 retries bounds the
  overnight run, and the frame review is the acceptance check.

## The human method, distilled

1. **One prompt, whole job**: the agent owns refs, lyrics, song,
   story, and prompts; the human owns the single brief.
2. **Review is a loop, not a look**: frame review, fix prompt,
   re-run, capped at 3 retries per scene.
3. **No post-edits is a claim, not a boast**: the shipped video is
   what the loop produced, issues included.
4. **The builder stays editable**: the project can be opened inside
   the video builder afterwards and any element changed by hand.

## Failure modes

- **Reference anchoring**: when using ref images for both characters
  and locations, the model "seems to anchor to the ref images" and
  prompt additions (presets, aesthetics) "do nothing," per the author
  in comments. This is a stated limit of reference anchoring, not a
  bug to work around by prompting harder.
- **Theatrical overreach**: the agent can overdo the requested tone
  (the author: Claude "went a bit overboard with the theatrical
  aspect i asked for"). The brief's adjectives are load-bearing; keep
  them restrained.
- **Issues remain after the cap**: 3 retries is a bound, not a
  guarantee; the shipped video still has issues by the author's own
  account.

**Depth status:** FULL (complete agent workflow, single prompt quoted
verbatim, tool chain, overnight run, review loop with retry cap, and
a stated failure mode; the builder repo itself was not inspected, so
no node-level settings beyond the 2-pass workflow pointer are claimed).
