# Skill: Obi Physics rope with SDF collision (EXAMPLE)

- **What:** Particle-based rope/chain simulation with collision against
  signed-distance fields, giving O(1) collision cost per particle instead of
  per-triangle tests.
- **Pipeline stage:** Gameplay physics (rope, cable, ragdoll-adjacent).
- **Learned from:** "My Cave Exploration Game" devlog (Moonmilk Games),
  r/gamedev, 2026-09-27 run. Public tool: Obi Physics (Unity asset).
- **Evidence:** Devlog reports rope physics via Obi with SDF collision at
  O(1) per-particle cost; chosen over per-triangle collision for performance
  on dense cave geometry.
- **Workflow (compressed):** Bake colliders to SDF volumes → simulate rope
  as particles → collide against SDF (constant cost per particle) →
  verify stability at the target frame budget before shipping.
- **Principle:** Collision cost should scale with the rope, not the cave.
- **Status:** EXAMPLE (marked NEED / watchlist in the sample run).
