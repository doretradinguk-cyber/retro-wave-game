# Retro-Wave-Game — Account 3 Handover

Role: ChatGPT Game Builder / Lead Integration
Project: Retro-Wave-Game
Visual target: Neon Hollow — B / First Person
Handover date: 2026-10-03

## Mission

You are the project's main game-builder and integration account.

Turn the assets, research and specifications from Accounts 1 and 2 into the actual playable game.

## Main responsibilities

Own:
- Game architecture
- Scene structure
- Player controller
- Camera
- Interaction
- Collision
- Lighting
- Materials
- Rendering
- VFX
- Enemy systems
- UI
- Audio integration
- Game states
- Performance
- Build/testing
- Final asset integration

## Primary target

Build around Neon Hollow concept B — First Person.

Desired result:
dark decayed hotel + illustrated 3D presentation + cyan/teal + hot magenta + wet reflections + neon emissive lighting + cinematic horror atmosphere.

## Development strategy

Do not build the whole game before proving the visual/technical foundation.

First build a single polished corridor vertical slice.

FIRST-PERSON PLAYER
→ HOTEL CORRIDOR
→ 5–10 DOORS
→ NEON LIGHTING
→ WET REFLECTIVE FLOOR
→ ONE ROOM
→ ONE ENEMY
→ FLASHLIGHT
→ WEAPON
→ INTERACTION
→ BASIC UI + AUDIO

## Rendering priorities

Lighting:
- Cyan / teal practical lights
- Hot magenta practical lights
- Deep controlled shadows
- Emissive materials
- Selective accent lighting

Materials:
- Wet floor
- Reflective surfaces
- Worn wood
- Painted walls
- Metal
- Glass
- Carpet/fabric

Atmosphere:
- Controlled bloom
- Atmospheric fog/depth
- Strong contrast
- Reflections
- Stylised/comic treatment
- Cinematic colour grading

## First-person stack

PLAYER
→ CAMERA
→ HANDS
→ WEAPON / EQUIPMENT
→ FLASHLIGHT

The corridor should create a strong vanishing point and use lighting/reflections to guide attention.

## Asset integration

Account 1 supplies generated game assets.

Account 2 supplies researched/licensed assets and supporting technical material.

Account 3 integrates, tests and replaces placeholders.

Use modular reuse:
ONE WALL → MANY WALLS
ONE DOOR → MANY DOORS
ONE LAMP → MANY FIXTURES
ONE MATERIAL → MANY COMPATIBLE SURFACES

## Performance

This is a tight-budget project.

Prefer:
- Reusable assets
- Instancing where appropriate
- Efficient textures
- Sensible polygon counts
- LOD where useful
- Controlled post-processing
- Efficient lighting
- Streaming/loading where helpful
- Mobile-aware fallbacks where required

Do not add expensive rendering features without measuring their visible value.

## Testing

Test the actual game/build for:
- Movement
- Camera
- Interaction
- Collision
- Lighting
- Reflections
- Materials
- Enemy behaviour
- UI
- Audio
- Loading
- Performance
- Asset compatibility

## Missing assets

Do not stop engineering work because a final asset is missing.

Use a temporary placeholder with similar dimensions/material purpose, complete the system, then replace it when Account 1 or 2 supplies the final asset.

## Current priority

Build and prove the B / First Person corridor vertical slice.

The goal is a playable scene that visibly demonstrates the intended Neon Hollow look before full expansion.

## Definition of done

A feature is done when:
- It works in the actual game.
- It has been tested in the actual scene/build.
- It does not introduce avoidable regressions.
- It fits the locked art direction.
- It is reasonably performant.
- Remaining issues are recorded in the handover.

## Master handover dependency

Read the newest README-MASTER-HANDOVER.md before major work. The master overrides old assumptions.

## Change log

### 2026-10-03
- Account 3 role established.
- Game-builder/integration responsibilities defined.
- B / First Person vertical slice made the first engineering target.
- Rendering priorities established.
- Modular asset integration rules established.
- Performance and testing responsibilities established.

## Blueprint link

The living game blueprint is: blue print plan/BLUEPRINT-PLAN.md

Use blue print plan/DECISION-LOG.md for requirements and blue print plan/BENCHMARKS.md for confirmed working rollback points.

## Godot 4 foundation update — 3 October 2026

Confirmed engine: Godot 4 with GDScript. All active game code, scenes, shaders and resources belong to retro-wave-game. Project root: project.godot. The repository now has core, features, world, UI, resources, shaders, addons and selected runtime asset folders; see docs/GODOT-STRUCTURE.md.

Completed: Godot-specific folder/settings scaffold, main foundation-notice scene, source/import/cache conventions and Drop Zone integration guidance. Incomplete: first-person controls, corridor, collision, equipment, enemy, UI/audio and platform exports. Known limitation: Godot executable is unavailable here; the scaffold has structural checks only, not an editor/runtime test. No gameplay benchmark is confirmed.

Next actions: import project.godot on the development PC, confirm the Godot stable minor version and target devices, then implement the first-person corridor prototype. Asset producers should provide self-contained GLB and appropriate PNG/WebP/audio exports with licence metadata; integration turns these into Godot scenes/resources. Keep original Adobe/DCC masters in Drop Zone.
