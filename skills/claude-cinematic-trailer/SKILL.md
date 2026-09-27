---
name: "claude_trailer"
description: "Direct an AI agent to cut a cinematic trailer from your game, then curate its output. Trigger when generating trailers with agents."
---

# I gave claude access to my cozy tower defense game, and asked it to make a cinematic trailer. It interpreted my game as a horror-movie.

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Direct the agent, inspect the cut: give the agent game access plus a creative brief, then curate its cinematic output.

## Source

Creator: illadann7

Source: https://www.reddit.com/r/aigamedev/comments/1wrgmaw | r/aigamedev post 1wrgmaw (score 91) | native clip (demo, not tutorial)

## Tools used

Tools used: Claude (agent/director), Unity (read-only access via MCP), OpenRouter API, Veo 3.1 lite (video generation, reached through OpenRouter), browser access (agent used it to monitor the OpenRouter page). A high-quality text-to-speech model was requested in the prompt but the agent did not use it. Game: "The Endless Harvest" (cozy tower defense; Steam app 5052960).

**Do**
1. Give Claude MCP access to the Unity project with an explicit read-only
   constraint. The prompt's access clause: "Look at my game, dont change
   anything inside the game itself, I only gave it so you read through it,
   so you know what it is about."
2. Give it API access to OpenRouter, plus browser access so it can monitor
   the OpenRouter page.

**Check**
- The game itself was not modified (no changes reported; the constraint held).

**Why**
A trailer agent needs source-material understanding without the risk of it
editing the game. Read-only access plus a written no-changes rule is the
safest way to let an agent study a project.

## Phase 1: Grant the agent read access to the game

## Phase 2: Prompt with constraints, a budget, and autonomy

**Do**
Issue one prompt carrying style, resources, budget, length, and autonomy
(OP pasted it verbatim in the post and in comments):

"Look at my game, dont change anything inside the game itself, I only gave
it so you read through it, so you know what it is about. please make a
video with a cinematic editing style with quick and snappy storytelling.
use different angles and lighting to make it seem like a professional
cinematic trailer for the game. you may use openrouter for assets, use a
budget of 10$ max. Use high quality text-to-speech model for generation.
You can use any tools you can find access to and resources on the internet.
You create the script, the assets, the animation, everything. Work
autonomously until done. Quality is paramount. Make the trailer be
~45 seconds."

**Check**
- Prompt text is identical in post selftext and the OP's comment reply.

**Why**
Constraints (cinematic style, $10 budget, ~45 seconds) plus full autonomy
("Work autonomously until done", "You create the script, the assets, the
animation, everything") turn an open-ended agent loose with guardrails.

## Phase 3: Agent reads and interprets the game

**Do**
Let the agent read through the project via the Unity MCP connection. No
specific reading instructions were given beyond the access grant.

**Check**
- Interpretation was half right: OP says the agent "got the details and
  assets of my game quite right" and "the final shot of my boss is
  especially amazing", but it read the cozy tower defense game as a
  horror movie.

**Why**
Interpretation quality shows in the details even when the overall genre
read is wrong. The details came from actually reading the project; the
genre miss came from the open-ended prompt (see Phase 6).

## Phase 4: Agent selects its own tool chain

**Do**
The agent decided, on its own, to use Veo 3.1 lite clips via the OpenRouter
API. (OP: "because I asked for a cinematic trailer, it decided to use Veo
3.1 lite clips of my game using OpenRouter API.") It did NOT use the
text-to-speech model the prompt requested.

**Check**
- Total cost was about $3, inside the $10 budget (OP: "this wasn't free,
  but this video cost about 3$ to make, so basically free").
- OP on the workflow: "Yeah I just let it do its thing with all possible
  tools without providing instructions on specifics."
- Commenter AlgaeNo3373: "using an actual video gen AI with claude as
  director is a clever workflow!"

**Why**
Director-agent pattern: Claude directs, a video-generation model renders.
Letting the agent pick the model worked (Veo 3.1 lite delivered), but the
unused TTS shows the agent silently drops prompt requirements it does not
need.

## Phase 5: Generate clips and assemble the trailer

**Do**
1. Agent generated Veo 3.1 lite clips, monitoring the OpenRouter page in
   its browser while jobs ran.
2. Edited the clips into a ~45-second cinematic trailer: quick, snappy
   storytelling, different angles and lighting, per the prompt.
3. Unprompted, the agent changed the game's soundtrack to be spookier and
   more on theme. (OP: "it didnt actually use the text-to-speach model,
   but it did change the game's soundtrack to be more spooky and on theme
   haha. I did not request that at all, but im happy it did that.")

**Check**
- Trailer reads as professional cinematic; details and assets match the
  game (commenter: "Looks very good!").
- The horror framing is consistent throughout (trailer, music), even
  though the game is cozy.

**Why**
An autonomous agent fills gaps on its own initiative (here, the music).
Unprompted choices can be good, but they need a review pass because they
are outside the prompt's contract.

## Phase 6: Review the result and tighten the next prompt

**Do**
1. OP's verdict: "It's fair to say I won't use this trailer anywhere, but
   it did give me a good chuckle."
2. Lesson logged by OP: "my future prompts should be more specific, and
   less open to interpretation I guess haha."

**Check**
- Horror read of a cozy game = interpretation miss caused by openness,
  not by a tool failure.

**Why**
Open prompts buy creativity at the cost of genre accuracy. Specificity
(genre, tone, reference trailers) is the lever that fixes the next run.

## The human method, distilled
1. **Read-only access plus a written no-changes rule** is the safe way to
   let an agent study a game project.
2. **Director-agent pattern:** Claude as director, a video-gen model (here
   Veo 3.1 lite via OpenRouter) as renderer.
3. **Budget and autonomy in one prompt** ($10 max, "work autonomously
   until done") produced a ~$3, ~45-second trailer with no human in the loop.
4. **The agent silently drops unneeded requirements** (TTS was requested,
   never used); check what it skipped, not just what it did.
5. **Unprompted initiative needs review** (the spookier soundtrack); good
   here, but outside the contract.
6. **Details survive openness; genre does not.** The agent nailed assets
   and the boss shot from reading the project, but read cozy as horror.
   Fix it with a more specific prompt next time.

## Depth status
 FULL (for post+comments reconstruction; the tool chain,
budget, and agent decisions were all mined from OP's comments, which is
where the HOW lived)

---
