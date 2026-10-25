---
name: godot-csharp
description: >
  Use C#/.NET in Godot 4.7: partial classes extending nodes, the PascalCase lifecycle
  (_Ready/_Process/_PhysicsProcess), [Export] fields, [Signal] delegates as C# events,
  type-safe node lookup, and calling between C# and GDScript. Use when writing Godot game code in
  C# (.cs files, .csproj), needing the Godot .NET build, converting GDScript patterns
  to C#, or wiring Godot signals as C# events.
---

# Godot C# / .NET (4.x)

Write Godot game code in C#: node subclasses, the engine lifecycle, exports, signals as
events, and GDScript interop. Targets **Godot 4.7 (.NET / C#)** and **.NET 8**.

## When to use

- Use when scripting a Godot game in C# (`.cs` + `.csproj`), translating GDScript idioms
  to C#, exposing `[Export]` fields, or wiring `[Signal]` delegates and GetNode<T>.

**When *not* to use:** GDScript-specific syntax → `godot-gdscript`; engine concepts that
are language-neutral (scenes, physics, animation) → the relevant `godot-*` skill. You need
the **Godot .NET build** + the .NET SDK installed; the standard build can't run C#.

## Core workflow

1. **Use the Godot .NET editor build** and install the matching .NET 8 SDK. Creating the first C#
   script generates a `.csproj`/`.sln`. Build with the editor or `dotnet build`.
2. **Every node script is a `partial` class** extending a Godot type (the source generator
   relies on `partial`). The file/class name should match the node script.
3. **Override lifecycle methods in PascalCase** with `double` delta: `_Ready()`,
   `_Process(double delta)`, `_PhysicsProcess(double delta)`.
4. **Expose tunables with `[Export]`**; they show in the Inspector like GDScript `@export`.
5. **Declare signals as `[Signal]` delegates** named `XxxEventHandler`; emit with
   `EmitSignal(SignalName.Xxx, ...)` and subscribe with the generated C# `event`.
6. **Get nodes with `GetNode<T>("Path")`** (or `%Unique`), and call into GDScript with
   `Call`/`Get`/`Set` when needed.

## Patterns

### 1. A node script: lifecycle, [Export], GetNode<T>

```csharp
using Godot;

public partial class Player : CharacterBody2D
{
    [Export] public float Speed = 200.0f;          // editable in the Inspector
    [Export] public float JumpVelocity = -400.0f;

    private const float Gravity = 1200.0f;
    private AnimatedSprite2D _sprite;

    public override void _Ready()
    {
        _sprite = GetNode<AnimatedSprite2D>("AnimatedSprite2D");
    }

    public override void _PhysicsProcess(double delta)
    {
        Vector2 v = Velocity;                       // Velocity is a property here
        if (!IsOnFloor())
            v.Y += Gravity * (float)delta;          // delta is double; cast for float math
        if (Input.IsActionJustPressed("jump") && IsOnFloor())
            v.Y = JumpVelocity;

        float dir = Input.GetAxis("move_left", "move_right");
        v.X = dir != 0 ? dir * Speed : Mathf.MoveToward(v.X, 0, Speed);

        Velocity = v;
        MoveAndSlide();                             // no args, like GDScript 4.x
    }
}
```

### 2. Signals as C# events

```csharp
using Godot;

public partial class Health : Node
{
    // Delegate name MUST end with "EventHandler"; generator creates the event + SignalName.
    [Signal] public delegate void HealthChangedEventHandler(int current, int max);

    private int _hp = 100;

    public void TakeDamage(int amount)
    {
        _hp = Mathf.Max(_hp - amount, 0);
        EmitSignal(SignalName.HealthChanged, _hp, 100);   // type-safe signal name
    }

    public override void _Ready()
    {
        HealthChanged += OnHealthChanged;            // subscribe like a normal C# event
    }

    private void OnHealthChanged(int current, int max) => GD.Print($"HP {current}/{max}");
}
```

### 3. Instancing a scene in C#

```csharp
public partial class Spawner : Node2D
{
    // Load once; PackedScene is the C# equivalent of preload's result.
    private readonly PackedScene _bullet = GD.Load<PackedScene>("res://bullet.tscn");

    public void Shoot(Vector2 at)
    {
        var b = _bullet.Instantiate<Node2D>();       // typed instantiate
        b.GlobalPosition = at;
        AddChild(b);
    }
}
```

### 4. Interop with GDScript nodes

```csharp
public override void _Ready()
{
    Node gd = GetNode("GDScriptNode");
    // Call a GDScript method and read/write its properties dynamically.
    gd.Call("take_damage", 10);
    int score = (int)gd.Get("score");
    gd.Set("score", score + 5);
    // Connect to a GDScript signal by name:
    gd.Connect("died", Callable.From(OnDied));
}

private void OnDied() => GD.Print("entity died");
```

## Pitfalls

- **Forgetting `partial`.** Without `partial`, the Godot source generator can't extend the
  class and `[Export]`/`[Signal]` break with confusing build errors.
- **Wrong method case/signature.** C# overrides are `_Ready`, `_Process(double)`,
  `_PhysicsProcess(double)` — PascalCase and `double` delta (GDScript uses snake_case and
  `float`). A mismatched name just won't be called.
- **`[Signal]` delegate naming.** It must end with `EventHandler`; the engine exposes the
  signal as the name without that suffix and generates `SignalName.X` and a C# `event`.
- **`GD.Print` vs `Console.WriteLine`.** Use `GD.Print`/`GD.PrintErr` to reach the Godot
  output panel; `Console` output may not appear.
- **Value-type structs.** `Vector2`, `Color`, `Transform2D` are structs — mutate a local
  copy (`var v = Velocity; v.X = ...; Velocity = v;`); editing `Velocity.X` directly won't
  compile/persist.
- **Needs the .NET build + SDK.** The non-.NET editor can't run C#; mismatched/missing
  .NET SDK causes build failures. Godot 4.7 targets .NET 8; check current platform
  export notes because Android and other AOT targets can require newer SDK tooling.
- **`QueueFree()` vs `Free()`** — same rules as GDScript; prefer `QueueFree()`. Disposed
  objects throw `ObjectDisposedException` if used after freeing.
- **Export to some platforms differs for .NET** (e.g. extra steps for web/mobile); check
  the .NET export notes for your target.

## References

- For export attribute variants (`[ExportGroup]`, ranges, typed arrays), async with
  `await ToSignal(...)`, `Godot.Collections` vs System collections, custom Resources in
  C#, and project/build setup, read `references/csharp-setup-and-interop.md`.

## Related skills

- `godot-gdscript` — the GDScript equivalents of these patterns.
- `godot-signals-groups` — signal/event architecture (language-neutral).
- `godot-resources` — data resources; the C# `[Export]` + `Resource` pattern.
- `unity-csharp-scripting` — C# in Unity, for developers coming from there.

## AAA studio practice

Note on scope: no AAA studio production case study for Godot C# specifically was found in this research pass, so no such claim is made here. The practices below are drawn from shipped Godot titles and from the C# discipline that production C# codebases share, with sources cited. Do not present this section as a Godot-C# AAA case study.

Sources:
- W4 Games / Godot ecosystem reporting (VentureBeat): Godot titles on Steam grew by more than 50 percent year on year in both 2024 and 2025, and Godot titles earning over $1 million annually rose from two to more than 50 in three years, with W4 (founded by Godot creator Juan Linietsky and core maintainers) providing enterprise tooling and support for studios shipping with the engine. https://venturebeat.com/business/w4-games-raises-18-million-to-accelerate-international-presence
- Shipped Godot titles (Godot 2022 retrospective, as reported): Brotato, Dome Keeper, and The Case of the Golden Idol are named as hit games published with Godot, showing the engine's production path from indie hit to console and multiplayer ports (Dome Keeper was ported to Godot 4 for multiplayer and console releases). https://dev.to/wlz/why-brotato-bet-on-godot-and-gdscript-the-free-2d-engine-behind-a-1-million-copy-potato-4ip7

**Do**
1. Treat the .NET build as a CI gate, not a local habit: script `dotnet build` for the project in CI (or as a pre-push check) so a missing `partial`, a wrong lifecycle signature, or a mismatched .NET SDK fails before it reaches another machine. This is the executable version of the Pitfalls list.
2. Automate the signal-naming check: script a scan of all .cs files for `[Signal]` delegates and fail any delegate whose name does not end with `EventHandler`, and any `EmitSignal` call using a string literal instead of the generated `SignalName.X`.
3. Automate the struct-mutation check [inference, from the value-type pitfall]: grep for direct component assignment on engine properties (for example, `Velocity.X =`) in .cs files and flag each hit for rewrite to the local-copy pattern from Pattern 1, since the direct form fails to compile or persist.
4. Keep the GDScript interop boundary explicit: list every C# to GDScript call site (Call/Get/Set/Connect by name) in one audit pass, and verify each target method and property name exists on the GDScript side, since those calls are stringly typed and fail only at runtime.

**Check**
- `dotnet build` passes clean on a fresh checkout with the Godot .NET editor build and .NET 8 SDK.
- The signal scan and the struct-mutation scan pass with zero hits.
- Every interop call site names a method or property that exists on the target script.

**Why**
Production C# in games is won or lost on the same three things this skill already warns about: the source generator contract (`partial`, `EventHandler`), the value-type discipline, and the stringly-typed interop boundary. Automating those three checks turns the Pitfalls list from advice into a gate, which is what a shipping studio's pipeline does with any language binding.
