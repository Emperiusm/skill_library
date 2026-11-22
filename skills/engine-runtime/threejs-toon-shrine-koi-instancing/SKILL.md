---
name: threejs-toon-shrine-koi-instancing
description: "Build a walkable, phone-playable three.js shrine with a toon look: koi as one instanced mesh (638 triangles per fish, varieties painted per instance in the fragment shader), a 3-step toon ramp plus a kept-list ink-outline pass, each area baked into one toon mesh with far stations hidden until near, and a shared clock so every visitor sees the same shoal. Trigger when a browser 3D scene must look hand-drawn and run on phones."
---

# Three.js Toon Shrine: Instanced Koi, Kept-List Outlines, Baked Areas

## Purpose

This skill reconstructs how PhilosophyOnly893 built a walkable Japanese shrine in three.js that plays on phones: the anime look comes from a toon ramp plus an ink-outline pass, the koi come from one instanced mesh, and each area is baked into one mesh with far stations hidden until approached. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: build everything cheap enough for a phone, then make the cheapness look deliberate.

## Source

- Post: "I built a walkable Japanese shrine in three.js - toon shading, ink outlines, plays on phones" by PhilosophyOnly893 — https://www.reddit.com/r/threejs/comments/1y1ly4w/i_built_a_walkable_japanese_shrine_in_threejs/ (r/threejs post 1y1ly4w, score 33, 2 comments)
- Playable build: https://app.omairi.online (free, no sign-up)
- Evidence: full post selftext + comments, 2026-11-22 scout run, audit 5. No three.js version, renderer settings, shader code, or frame-time numbers were disclosed. Do not invent them.

## Tools used

three.js. Online presence: Cloudflare Workers + Durable Objects. Code "written with AI coding assistants that I direct and review" (author). No versions stated.

## Phase 1: Build the koi as code, in one instanced mesh

**Do**
1. Build the koi in code, with no model file: "one instanced mesh for the whole pond, 638 triangles a fish, twelve varieties painted per instance in the fragment shader, swimming as a travelling wave in the vertex shader."
2. Drive koi paths from a shared clock, "so every visitor sees the same shoal".

**Check**
- The budget is stated per fish (638 triangles) and per pond (one instanced mesh). Count draw calls for the pond: one. Variety is checked in the fragment shader output (twelve varieties), not in twelve meshes or textures.
- The shared clock is checkable: two visitors at the same clock value see the same shoal positions. If shoals differ between visitors, the clock is not shared.

**Why**
One instanced mesh turns a pond of fish from N draw calls into one, and per-instance fragment-shader painting turns variety from N textures into one shader. A shared clock turns a simulation into a deterministic function of time, which is what makes a shared online presence coherent without syncing fish state between visitors.

## Phase 2: Get the anime look in two passes, without walking the scene twice

**Do**
1. Shade with a 3-step toon ramp.
2. Draw ink outlines in a pass fed by a kept list, "instead of walking the scene twice a frame".

**Check**
- The outline pass must not double scene traversal per frame; the kept list is the mechanism that avoids it. Only listed objects get outlines, so the outline budget is explicit and countable.

**Why**
A kept list is cheaper than a second traversal and more controllable: outlines are a decision per object, not a tax on the whole scene. The toon ramp (3 steps) is what makes the shading read as anime rather than smooth; the outline is what makes the shapes read as ink.

## Phase 3: Grow the world procedurally, on the real calendar

**Do**
1. Generate trees procedurally: sakura, maple, ginkgo, pine, cedar, bamboo.
2. Run four seasons that "follow the real calendar". Run the shrine clock on Japan time: fireworks at 20:00 JST, yokai parade at midnight.
3. Offer multiple ways to move through the world (author's in-video timestamps): 0:17 running as a shiba, 0:22 flying as a bird, 0:26 diving into the koi pond, 0:39 lantern night, 0:47 fireworks over the sea.

**Check**
- Season and clock behaviour are observable in the playable build. The author invites device reports ("I'd love to hear how it runs on your device"); phone playability is the acceptance test, not desktop frame rate alone.

**Why**
Procedural trees + calendar seasons turn one authored shrine into a place that changes without new assets. The Japan-time clock makes the shared world feel shared: everyone gets fireworks at the same real time, not at a per-visitor timer.

## Phase 4: Bake areas, hide the far ones, serve presence from the edge

**Do**
1. Bake "each area into one toon mesh".
2. Hide far stations until the visitor gets near.
3. Run online presence on Cloudflare Workers + Durable Objects.

**Check**
- One mesh per area + distance hiding is the phone-playability mechanism: far geometry costs nothing until approached. Verify by counting what is drawn at a distance vs up close; far stations must contribute nothing until near.
- Open question, unanswered in the retrieved comments (commenter xzinkx): "Do you use any real-time shadows, or is the lighting fully baked into the toon meshes?" The post does not say. Do not assume baked lighting; ask or inspect the build before copying the lighting approach.

**Why**
Baking is a commitment: it trades per-object flexibility for per-area cheapness. Distance hiding is what makes that commitment affordable on phones without shrinking the world. Edge presence (Workers + Durable Objects) keeps the shared clock and visitor state without a dedicated game server.

## The human method, distilled

1. **State the budget in the post.** 638 triangles a fish, one instanced mesh, one mesh per area: budgets stated are budgets that can be checked.
2. **Determinism is a feature.** A shared clock makes every visitor see the same shoal; no fish-state sync needed.
3. **Keep the list, skip the second walk.** Outlines from a kept list, not a second scene traversal.
4. **Direct and review the AI code.** The author states the assistants were directed and reviewed, not left to ship alone.
5. **Bake and hide.** One mesh per area, far stations hidden until near: the phone budget is a visibility budget as much as a triangle budget.

## Depth status

PARTIAL — full post text with exact numbers, architecture, and in-video timestamps. No shader code, no three.js version, no frame-time numbers, and the real-time-shadows question is unanswered. The playable build at app.omairi.online is the verification surface for the claims above; this skill does not claim measurements the post does not state.
