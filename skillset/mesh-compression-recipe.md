# Skill: Compact mesh output recipe (EXAMPLE)

- **What:** Shrink shipped meshes: 8-bit quantized UVs, octahedron-encoded
  normals, vertices packed as three 32-bit integers; patch-grid UV layout.
- **Pipeline stage:** Engine output / performance (final packaging).
- **Learned from:** "My Cave Exploration Game" devlog (Moonmilk Games),
  r/gamedev, 2026-09-27 run.
- **Evidence:** Devlog describes the three-part recipe (8-bit UVs,
  octahedron normals, 3-integer vertices) as its mesh-compression standard.
  **Caution:** the devlog's captions were unavailable during the audit, so
  the exact constants are unverified; the recipe direction is the takeaway,
  not any specific number quoted elsewhere.
- **Workflow (compressed):** Quantize UVs to 8-bit → encode normals as
  octahedrons → pack vertices as three 32-bit ints → lay out UVs on a
  patch grid → verify against the perf budget before adopting as standard.
- **Principle:** Compression is a standard, not a trick: adopt it as the
  output contract once, then every asset obeys it.
- **Status:** EXAMPLE (marked NEED / backlog P1 in the sample run).
