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

## AAA studio practice

AAA crowd, city, and shared-world work runs on the same three disciplines this skill uses at indie scale: one instanced draw for a whole population with variety painted per instance, distance-tiered detail so far things cost almost nothing, and a shared deterministic clock so every viewer computes the same world instead of syncing state.

- **Ubisoft, *Assassin's Creed Unity* (GDC 2015).** Ubisoft's crowd system managed up to 10,000 NPCs by tiering them into high-fidelity autonomous NPCs near the player, mid-range puppet NPCs, and long-range low-resolution meshes, with pooled assets and pre-calculated paths in a deterministic "Shepherd" container; only about 120 of the up to 12,000 agents were rendered with high-resolution models, and the crowd system consumed only about 5% of the RAM budget in the GDC summary.
  (https://www.gamedeveloper.com/programming/video-behind-the-massive-crowds-of-i-assassin-s-creed-unity-i-)
  (https://www.cs.upc.edu/~npelechano/abstract_prePrintCGF2015Survey.pdf)
  The direct parallel: one instanced mesh for the whole pond, variety in the fragment shader, and far stations hidden until near are the same tiering, at pond scale. The production upgrade is Ubisoft's explicit tier table: record which tier each population sits in at which distance, instead of one hide/show distance for everything.
- **Wube Software, *Factorio* (Friday Facts #76) and Ensemble Studios, *Age of Empires* (GDC 2001).** Factorio runs lockstep multiplayer in which each peer runs the full simulation and only player actions travel over the network, so traffic stays at a few hundred bytes per second whether the map holds hundreds or millions of objects, at the price that any nondeterminism accumulates into a desync. The same architecture powered *Age of Empires*: Bettner and Terrano's "1500 Archers on a 28.8" showed commands-only networking lifting the ceiling past 1,500 units where sending positions capped it near 250.
  (https://direct.factorio.com/blog/post/fff-76)
  (https://gamedev-canon.alekseiprikhodko.com/m04-netcode-taxonomy.html)
  The direct parallel: the shrine's shared clock is lockstep without the multiplayer, a deterministic function of time so every visitor sees the same shoal with no fish state synced. The production upgrade is Factorio's: treat any clock-dependent behaviour as a determinism contract, and test it by comparing two clients at the same clock value, not by watching one client swim.
- **Insomniac Games, *Marvel's Spider-Man* (GDC 2019) and Epic Games, *The Matrix Awakens* City Sample.** Insomniac procedurally authored Manhattan with systems that generated streets, curbs, sidewalks, and building spaces from street curves and instanced modular building-kit components onto surfaces, while preserving hand-authored work whenever it still met specifications across city-layout iterations. Epic's City Sample carried the same idea to streaming scale: a 4.138 by 4.968 km city with 7,000 simulated buildings and 35,000 walking pedestrians, built by procedural rules (Houdini among them) so changing an input rule redefined the whole city, with World Partition and Nanite streaming the result.
  (https://history.siggraph.org/wp-content/uploads/2022/09/2019-Talks-Santiago_Procedural-System-Assisted-Authoring.pdf)
  (https://gamesbeat.com/epic-games-shows-off-unreal-engine-5-realism-with-stunning-the-matrix-awakens-demo/)
  The direct parallel: baking each area into one toon mesh and hiding far stations is the same bake-and-stream commitment at shrine scale. Insomniac's lesson is the preservation rule: a bake must be regenerable from its inputs without destroying hand work, and a baked area that cannot be rebaked after an edit is a liability, not an optimization.

**Agent automation**

1. **Instancing manifest.** Keep `instancing-manifest.json` per build: pond draw-call count (one), triangles per fish (638), variety count (12), and the per-instance painting mechanism (fragment shader). A check asserts the pond still draws in one call and the variety count still reads from the shader output, not from added meshes or textures.
2. **Outline kept-list audit.** Keep the outline kept list as a checked file: every listed object gets an outline, every unlisted object gets none, and the list is countable. A check asserts the outline pass reads the list and does not walk the scene a second time per frame; an outline appearing on an unlisted object, or a second traversal, fails the audit.
3. **Shared-clock parity check.** Record a shoal-position hash at fixed clock values from two independent loads of the build, and compare the hashes. Identical clock values must produce identical hashes; differing hashes mean the clock is not the only input (per-visitor timers, unsynced randomness, or frame-dependent motion have leaked in), and the shared-world claim fails until the leak is found.
4. **Bake and visibility ledger.** Keep `bake-ledger.json`: one mesh per area, the bake inputs for each, and the hide distance per station. A check asserts far stations contribute no draw calls until approached and that every baked mesh can be regenerated from its recorded inputs. The unanswered real-time-shadows question in Phase 4 stays open in the ledger until it is answered by inspection, not assumed.

## The human method, distilled

1. **State the budget in the post.** 638 triangles a fish, one instanced mesh, one mesh per area: budgets stated are budgets that can be checked.
2. **Determinism is a feature.** A shared clock makes every visitor see the same shoal; no fish-state sync needed.
3. **Keep the list, skip the second walk.** Outlines from a kept list, not a second scene traversal.
4. **Direct and review the AI code.** The author states the assistants were directed and reviewed, not left to ship alone.
5. **Bake and hide.** One mesh per area, far stations hidden until near: the phone budget is a visibility budget as much as a triangle budget.

## Depth status

PARTIAL — full post text with exact numbers, architecture, and in-video timestamps. No shader code, no three.js version, no frame-time numbers, and the real-time-shadows question is unanswered. The playable build at app.omairi.online is the verification surface for the claims above; this skill does not claim measurements the post does not state.
