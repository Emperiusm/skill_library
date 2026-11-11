---
name: procedural-aquarium-threejs
description: "Generate a whole living aquarium at load in one ~650 KB HTML file with Three.js r160: fish meshes as swept profile rings bent by a travelling wave, skins and scales painted one by one on canvas, fish simulated not animated with a gape rule for hunting, and day, night, and weather following the real clock at Lake Fork, Texas. Trigger when building a procedural scene where the generation code must be smaller than the assets it replaces."
---

# Procedural Aquarium (Three.js)

## Purpose

This skill reconstructs the bass aquarium build, step by step, so another
agent can generate a living procedural scene at load with the same method.
Every phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: generate
everything at load, simulate the fish instead of animating them, and let the
procedure be the compression.

## Source

- Post: "Everything in this bass aquarium is generated at load: fish, scales,
  plants, sand, driftwood (Three.js, one HTML file)" by kskbaits —
  https://www.reddit.com/r/proceduralgeneration/comments/1xra7wm/everything_in_this_bass_aquarium_is_generated_at/
  (r/proceduralgeneration, score 23, 4 comments)
- Try it: https://ksk-baits-bass-aquarium.pages.dev
- Live: https://www.youtube.com/@kskbaits/live
- Evidence: full author post text with exact numbers and method, plus 4
  comments with measured memory figures (2026-11-10 scout run). The clip is
  the live tank itself.

## Tools used

Three.js r160; one ~650 KB HTML file; canvas-painted textures (2048x1024
colour map plus matching normal/roughness map per fish, all mipmapped);
full-screen post-processing (bloom, depth of field, motion blur during
strikes).

## Phase 1: Generate the fish

**Do**
1. Build the fish meshes as swept profile rings, "bent by a travelling wave
   per vertex."
2. Paint the skin and scales one by one on a canvas. Each fish gets a
   2048x1024 colour map plus a matching normal/roughness map, all mipmapped.
   (Author comment with measured detail.)
3. No model files, no image files: "Nothing in this tank is a model or an
   image file. It is one ~650 KB HTML file with Three.js r160, and everything
   is generated when the page loads."

**Check**
- The whole tank is about 650 KB, "less than a single 4K texture for one of
  the fish would be. The scales alone would be megabytes as images, but here
  they are a few lines that paint them one by one at load."

**Why**
Procedural generation is compression: the code that paints the scales is
smaller than the scales would be as images, by orders of magnitude.

## Phase 2: Simulate the fish, don't animate them

**Do**
1. Simulate two bass (a largemouth and a smallmouth): they get hungry, hold
   by cover, stalk, and strike with a suction feed "that only takes prey
   whose body depth fits their gape."
2. School the shad; they "burst apart when attacked."
3. Generate the rest at load too: plants, sand, pebbles, driftwood, moss,
   caustics, and the lo-fi music.

**Check**
- "The fish interactions were the part I spent the most time on" (author
  comment). The check is behavioral: hungry, hold, stalk, strike, and a gape
  rule that filters prey by body depth.

**Why**
Simulation gives behavior for free: a strike rule (body depth fits gape)
produces believable hunting without keyframed animation. The gape rule is
the kind of constraint that makes the simulation legible: a viewer can see
why a strike happened or did not.

## Phase 3: Tie it to the real world and measure it

**Do**
1. Day, night, and weather follow the real clock and weather at Lake Fork,
   Texas.
2. Run it 24/7 on YouTube; the chat can drop in shad (!feed) or cast a lure.
3. Measure runtime memory (Chrome, 1080p, counting what the page allocates
   on the GPU): JS heap about 60 MB; GPU roughly 500 MB. "About 340 MB is
   textures, about 190 MB is the multisampled render buffers, and about 30 MB
   is vertex buffers."

**Check**
- "Your compression point holds: 650 KB unpacks into about half a GB. Most
  of it is the painted skins." (Author reply to commenter immersiveGamer.)
  The author's own trim: "The skins could be 1024 wide on mobile with almost
  no visible difference."

**Why**
The 650 KB figure is the shipping size; the 500 MB figure is the runtime
cost. Both are the truth, and the gap between them is the painted skins. A
mobile budget is a texture-resolution decision, not a rewrite. Tying the
scene to a real clock and real weather makes a 24/7 stream different every
time it is watched, for free.

## Failure modes

- **Runtime memory is dominated by the painted skins.** 650 KB of code
  unpacks into about half a GB at runtime, most of it textures. Fix: drop
  the skins to 1024 wide on mobile; the author reports almost no visible
  difference.
- **Post-processing buffers are the second cost.** About 190 MB of the GPU
  total is multisampled render buffers for bloom, depth of field, and motion
  blur during strikes. Fix (inference, labeled): treat the post chain as a
  budget line item of its own, not as free.

## AAA studio practice

The aquarium's three ideas, generation as compression, simulation
instead of animation, and the real world as the clock, each have a
shipped-title precedent. The studios all report both numbers: the
shipping size and the runtime cost.

- **Hello Games, No Man's Sky: generation is compression.** No Man's
  Sky holds over 18 quintillion planets in a 6 GB install at launch,
  most of it audio. The game does not store a pre-made asset for each
  planet; it stores the algorithms and the seeds, generates the
  planet's terrain, flora, fauna, weather, and buildings on the fly
  when the player approaches, and discards the detail when the player
  leaves.
  (https://www.dualshockers.com/no-mans-sky-takes-only-6-gb-on-disk-passed-certification-in-europe-u-s-and-asia/ ;
  https://www.gameslearningsociety.org/wiki/how-is-no-mans-sky-so-small/)
  This is the AAA version of Phase 1: the 650 KB HTML file is the
  recipe, the 500 MB runtime is the baked cake, and the gap between
  them is the painted skins. No Man's Sky states the same gap the
  same way: shipping size and runtime cost are different numbers,
  and the skill's Phase 3 rule, report both sizes, is the studio
  rule too.
- **Giant Squid, Abzu: simulate the fish, don't animate them.**
  Abzu renders schools of tens of thousands of fish dynamically.
  Most fish are animated using mathematical motion in their materials
  alongside morph target posing, which "freed them from needing
  expensive skeletal rigs. This was key to letting us render schools
  of tens of thousands of fish dynamically." Kelp forests use
  procedural motion based on rope simulations and tidal forces. The
  engineering version: 10,000 to 20,000 individually animating fish
  on PS4, as instanced static meshes with a single draw call per
  species, morph target animation for the mouths, and a working
  simulation of the food chain, so predators hunt prey and fish
  break apart and coalesce into schools.
  (https://80.lv/articles/interview-with-the-creative-director-of-abzu?amp=1 ;
  https://www.gamedeveloper.com/design/-i-abzu-i-and-the-challenge-of-conveying-emotions-through-game-design)
  This is the AAA version of Phase 2: the gape rule and the hunger
  states are the aquarium's food chain, and the shad bursting apart
  is the same break-apart behavior Abzu's schools show. The upgrade
  is the instancing rule: one draw call per species, not one per
  fish, and the behavior as a legible rule (a viewer can see why a
  strike happened) rather than keyframed animation.
- **Nintendo, Animal Crossing: the real clock is the game clock.**
  The series was premised on the Nintendo 64DD's real-time clock:
  days and seasons pass according to the calendar, the village is
  blanketed in snow in winter and cherry blossoms bloom in spring,
  different fish and insects emerge depending on the time of year,
  and holidays are celebrated as they occur in real life. The game
  was built so the world keeps living when the player is not playing.
  (https://www.gamespot.com/articles/how-animal-crossing-was-born-from-one-of-nintendos-biggest-flops/1100-6475342/?ftag=CAD-01-10abi2f)
  This is the AAA version of Phase 3: day, night, and weather
  following the real clock at Lake Fork, Texas, is the same design
  decision, a scene that is different every time it is watched for
  free. The lesson is the same one Animal Crossing learned: the clock
  is a gameplay condition, not just atmosphere, so the parity between
  the game clock and the real clock has to be checked, not assumed.
- **Boids, the foundational algorithm (labeled: academic, not a
  shipped-title case).** Craig Reynolds' 1986 boids model gives
  schooling from three steering rules per fish: separation (avoid
  crowding neighbours), alignment (match the average heading), and
  cohesion (move toward the average position). Blender's manual
  documents boids particle systems as "ideal for simulating flocks,
  swarms, herds and schools of various kind of animals, insects and
  fishes or predators vs. preys simulations."
  (https://docs.blender.org/manual/de/2.81/physics/particles/emitter/physics/boids.html)
  The aquarium's shad bursting apart on attack is the separation
  rule firing; the bass stalking is a predator rule on top of the
  same three. No named shipped title was found this run using boids
  specifically for fish schooling in production, so boids is cited
  as the algorithm behind the behavior, not as a studio precedent.

### Agent-executable upgrades

1. **Memory budget manifest.** Keep `memory-budget.json`: one line
   per budget item (painted skins, multisampled render buffers,
   vertex buffers) with the shipping size and the runtime cost side
   by side, following the author's own Phase 3 numbers (JS heap
   ~60 MB, GPU ~500 MB: ~340 MB textures, ~190 MB render buffers,
   ~30 MB vertex buffers). A build that grows any line past its
   budget fails the gate; the mobile 1024-wide skin rule is a gate
   with acceptance renders, not a note.
2. **Simulation-rules manifest.** Keep `sim-rules.json`: the gape
   rule, hunger states, hold/stalk/strike sequence, and burst-apart
   rule as data with their parameters. Acceptance: a strike happens
   only when the prey's body depth fits the gape, and the shad burst
   apart on attack. A rule that cannot be stated as data is not in
   the simulation yet.
3. **Boids parameter record.** Keep the separation, alignment, and
   cohesion weights per species in the manifest, with a burst-apart
   check: trigger an attack and require the school to split and
   re-form. A school that clumps or ignores the attack fails the
   check, which is the failure mode the boids literature warns about
   when alignment overwhelms separation.
4. **Real-clock parity check.** Log the in-game time and weather
   against the real Lake Fork clock and weather per session, and
   fail the gate on drift past a stated threshold. Animal Crossing's
   lesson is that the clock is a gameplay condition; a scene that
   claims to follow the real clock has to prove it.
5. **Texture-resolution ladder.** Render acceptance frames at both
   2048-wide (desktop) and 1024-wide (mobile) skins and diff them.
   The author's "almost no visible difference" becomes a measured
   diff, not an impression, and the ladder is what makes the mobile
   budget a decision rather than a hope.

## The human method, distilled

1. **Generation is compression.** Code that paints scales beats images of
   scales.
2. **Simulate, don't animate.** A gape rule and a hunger state make hunting
   behavior.
3. **Report both sizes.** Shipping size and runtime memory are different
   numbers; publish both.
4. **The expensive part is the part you spent the most time on.** Fish
   interactions, not the tank.

**Depth status:** FULL (full post text with exact numbers and method + 4
comments with measured memory figures; the clip is the live tank itself, and
a media download would add nothing the post and the live page do not already
state; no download attempted).
