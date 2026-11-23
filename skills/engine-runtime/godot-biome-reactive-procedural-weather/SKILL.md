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

**Depth status:** FULL (post-text only). Exact engine pieces and the biome/front/global-parameter architecture are stated. No shader code, parameter names, values, or timings are disclosed; a media download would show the transitions but would not supply the undisclosed shader code or numbers.
