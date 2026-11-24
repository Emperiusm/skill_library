---
name: godot-biome-reactive-procedural-weather
description: "Build procedural weather in Godot 4 where fronts drift with the wind, each biome reacts differently, and grass, trees, and water all read the same global shader parameters. Trigger when weather must arrive visibly as a front instead of switching randomly, and every responder must stay in sync."
---

# Godot Biome-Reactive Procedural Weather

## Purpose

This skill reconstructs the exact workflow ErmanStudio demonstrates for a procedural weather system in a Godot 4 survival game, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: drift weather fronts across the world with the wind, let the biome underneath decide the local response, and drive every responder from one set of global shader parameters.

## Source

Creator: ErmanStudio. Post: "Procedural weather in my Godot 4 survival game: rain rolls in, and every biome reacts differently" https://www.reddit.com/r/godot/comments/1y2xi1m/procedural_weather_in_my_godot_4_survival_game/ (r/godot post 1y2xi1m, score 145, 3 comments; full post text read) | 2026-11-23 scout run, audit 3.

## Tools used

Godot 4, custom sky shader, `FogVolume`, `GPUParticles3D`, global shader parameters, GDScript ("All the logic is plain GDScript"). No shader code, parameter names, values, or weather-timing numbers are stated.

## Phase 1: Drift weather fronts with the wind

**Do**
1. "Weather fronts drift across the world with the wind."
2. Let "the biome underneath decide what happens": "A swamp gets soaked, a meadow gets rain now and then, and the desert mostly just watches clouds go by."

**Check**
- The check the author offers is legibility from the ground: "looking at the sky to check for rain instead of random events is great" (commenter koorosh-m). The player reads the front coming, rather than the weather switching.

**Why**
The author's stated complaint about the alternative is immersion: games that "just randomly switch[] the weather" break it. A front the player can see coming is a forecast, not a random event.

## Phase 2: Ramp the transition instead of switching

**Do**
1. "The rain doesn't just switch on, either: the sky slowly gets darker, the wind picks up, and then it starts pouring." Keep the stated order: darker sky, stronger wind, then rain.

**Check**
- Each stage must be visible in sequence: darkening, wind, pour. No durations are stated.

**Why**
A gradual ramp keeps the weather readable as a process arriving, not a state flipping. The author does not state a numeric ramp time; do not invent one.

## Phase 3: Build the sky, clouds, and rain from four Godot pieces

**Do**
1. "The sky is a custom sky shader."
2. "The clouds near the camera use a `FogVolume` so you can actually fly into them."
3. "The rain is `GPUParticles3D`."
4. "All the logic is plain GDScript."

**Check**
- The `FogVolume` check is fly-through: the player can fly into a near cloud. No cloud density, particle count, or shader parameter is stated.

**Why**
Each piece does one job in the engine's own terms: shader for the sky, volume for flyable clouds, GPU particles for rain, GDScript for the logic that ties them together. No custom C++ or plugin is claimed.

## Phase 4: Drive grass, trees, and water from global shader parameters

**Do**
1. "Global shader parameters let grass, trees and water all react to the same wind and rain."

**Check**
- All three responders must move or change together with the same front: grass, trees, and water reacting to the same wind and rain values, not three separate weather states.

**Why**
One shared parameter set is what makes the biome response coherent: the swamp, meadow, and desert all read the same front, and differ only in how the biome underneath responds.

## Failure modes

- **Weather reads as random switching:** the front is not visible before it arrives, or the transition has no ramp. Restore the Phase 1 front drift and the Phase 2 darkening/wind/pour order.
- **Responders out of sync:** grass, trees, and water are reading separate weather states instead of the same global shader parameters. Route all three through the shared parameters in Phase 4.
- **Water reacting to the player (unanswered):** a commenter asks "how did you make water react to the player?" The author did not answer. The post only says water reacts to the same global wind/rain parameters. Do not claim player-driven water interaction from this source.

## The human method, distilled

1. "Godot made a lot of this really fun to put together." Compose engine-native pieces (sky shader, `FogVolume`, `GPUParticles3D`, global parameters) rather than building a weather engine from scratch.
2. Make weather legible before it arrives: a front the player can watch coming is the forecast, and the ramp is what sells it.

## AAA studio practice

**Do**
1. Drive every responder from one shared weather state, the way Sucker Punch did in Ghost of Tsushima. The studio integrated its global wind direction into nearly every effect, sampled wind speed for extra turbulence, and fed particle systems global wind, wetness, time of day, and terrain and water position data; trees, grass, cloth, and ropes were tuned together so all moved appropriately under the same wind conditions, and rope and cloth simulations used the same wind inputs as foliage and particles. (https://blog.playstation.com/2021/01/12/how-stunning-visual-effects-bring-ghost-of-tsushima-to-life/) That is the shipped-title form of this skill's Phase 4: grass, trees, and water reading the same global shader parameters, differing only in response, never in weather.
2. Prefer volume over accuracy: one wind vector plus noise, not fluid simulation. At GDC 2021, Sucker Punch coder Bill Rockenbeck said the studio was "not doing any real modeling of fluid dynamics": the main wind vector kept a constant direction with magnitude varied from place to place using time-varying Perlin noise, visible as gusts blowing through large grass fields, and in cutscenes and non-Guiding Wind situations a single authored vector varied with the weather. (https://www.gamedeveloper.com/design/using-vorticles-to-simulate-wind-in-i-ghost-of-tsushima-i-) The skill's front drift plus ramp is the same trade: a readable front the player can see coming, with the biome underneath deciding the local response, instead of a simulated atmosphere.
3. Share the wind as a sampled field that responders opt into. Sucker Punch's vorticles are invisible wind-generating particles that output a position, orientation, radius, and wind vector, accumulated into a single small array that particle emitters sample for the accumulated contribution at a point; emitters opt in voluntarily, for relatively few places where it helps. (https://www.gamedeveloper.com/design/using-vorticles-to-simulate-wind-in-i-ghost-of-tsushima-i-) Treat the global shader parameters the same way: one field, sampled by grass, trees, and water, with each responder deciding what to do with the sampled value. A responder that keeps a private wind value is the desync failure in the skill's Failure modes, in shipped form.
4. Let the environment change the expression of the shared wind. In Ghost of Tsushima the wind indicator changes elements with the environment: pampas fluff and grass in fields, leaves in forests, ash in burnt areas. (https://blog.playstation.com/2021/01/12/how-stunning-visual-effects-bring-ghost-of-tsushima-to-life/) That is the biome rule this skill states in Phase 1, with the shared front as the cause and the biome as the expression. The front does not need a per-biome weather state; it needs per-biome response curves reading one front.
5. Make weather legible before it arrives, and keep that legibility as a design decision, not a simulation byproduct. Rockenbeck's wind model prioritised volume over accuracy so millions of vents could blow on a small fraction of PS4 capacity. (https://www.gamedeveloper.com/design/using-vorticles-to-simulate-wind-in-i-ghost-of-tsushima-i-) The parallel, labelled inference, is that the Phase 2 ramp order (darker sky, stronger wind, then rain) is a legibility budget: each stage must be readable at the cost the game can afford, and a stage nobody can read is a stage to cut, not to simulate harder.

**Check**
- Freeze the front and capture all three responders in the same frame: grass, trees, and water must agree on wind and rain values. Any responder showing a different weather state has a private source and fails the gate.
- Gusts travel: a scrolling noise gust visible in a grass field must move with the wind direction, arriving downwind after upwind, in the Rockenbeck Perlin-magnitude pattern. A gust that appears everywhere at once is a switch, not a front.
- No shader in the system declares a local weather uniform that duplicates a global parameter. The global parameter list is the only weather source.

**Why**
Shipped open-world weather is a shared-state discipline, not a solver showcase: one wind, one wetness, sampled by everything, with cheap noise standing in for fluid dynamics and the biome deciding what the shared state looks like locally. The skill's architecture already matches that shape; the AAA practice is to police the single source and the legibility of the ramp, since those are what break first when responders multiply.

## Agent automation

1. **Weather manifest.** Keep `weather-manifest.json` per project: the global shader parameter names, the front's direction and speed as recorded values, the biome response table, and the ramp stage order. A script asserts every responder shader reads only the listed globals for weather, and fails the build when a local weather uniform appears.
2. **Ramp-order probe.** A scripted capture sequence at fixed camera points records the Phase 2 order (sky darkens, wind picks up, rain pours) during a front arrival and logs any stage that appears out of order or simultaneously with another. No durations are asserted, since the author states none.
3. **Biome sweep.** For each biome, an automated capture under the same front state records which responders changed. A biome with no responder change under a front that should soak it is flagged, not assumed dry by design.
4. **Gust-travel check.** Sample the gust field at an upwind and a downwind point and assert the gust peak reaches the downwind point after the upwind point. The check asserts order, not a timing value, since no timing is stated.
5. **Desync gate.** Dump the wind and rain parameter values read by grass, trees, and water for a recorded run of frames and fail the run when any frame shows disagreement. The frame count is operator-set and recorded in the manifest.

**Depth status:** FULL (post-text only). Exact engine pieces and the biome/front/global-parameter architecture are stated. No shader code, parameter names, values, or timings are disclosed; a media download would show the transitions but would not supply the undisclosed shader code or numbers.
