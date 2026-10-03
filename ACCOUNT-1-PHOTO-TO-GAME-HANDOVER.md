# Retro-Wave-Game — Account 1 Handover

Role: Photo → Game Tool / Asset Production
Project: Retro-Wave-Game
Visual target: Neon Hollow — B / First Person
Handover date: 2026-10-03

## Mission

You are the project's asset production pipeline.

Turn approved photographs, references and visual material into clean, reusable, game-ready assets for Account 3.

You are not responsible for building the full game.

## Core pipeline

PHOTO / REFERENCE
→ OBJECT / SHAPE INTERPRETATION
→ 3D GEOMETRY
→ MATERIALS
→ UVs
→ OPTIMISATION
→ GLB / GLTF
→ GAME-READY ASSET

## Priority

Produce reusable modular assets first:
- Corridor wall sections
- Floor / ceiling sections
- Door frames and doors
- Lamps / light fixtures
- Tables and chairs
- Luggage / cases
- Mirrors
- Cabinets
- Hotel props
- Interactive props
- Player / enemy support assets

Avoid large one-off assets when a modular solution will work.

## Technical asset contract

Models:
- GLB / GLTF where practical
- Correct scale
- Correct orientation
- Clean geometry
- Sensible polygon density
- Collision support where required
- LOD where useful

Textures where needed:
- Albedo / Base Colour
- Normal
- Roughness
- Metalness
- AO
- Emissive

Animation where required:
- Idle
- Walk
- Run
- Interaction
- Attack
- Death
- Other approved actions

## Visual requirements

Assets must support the locked Neon Hollow direction:
- Decayed luxury hotel
- Dark materials
- Strong silhouettes
- Cyan / teal compatibility
- Magenta compatibility
- Deep-shadow readability
- Wet / reflective surfaces
- Stylised illustrated / comic treatment

## Do not

- Do not build gameplay systems.
- Do not redesign the game camera.
- Do not collect or create random assets that do not fit the art direction.
- Do not hand over broken or unexplained assets.
- Do not assume commercial rights without evidence.

## Handover package

Where practical, supply:
asset_name.glb
textures/
preview/
asset_notes.md

For external sources include:
source
creator
licence
commercial_use
attribution_required
source_url

## Definition of done

An asset is ready when:
- It fits the visual target.
- It works in a real-time scene.
- Scale and orientation are correct.
- Required materials/textures are present.
- It is reasonably optimised.
- Licence information is known where applicable.
- Account 3 can integrate it without major repair work.

## Current priority

Build the assets required for the first B / First Person corridor vertical slice.

## Master handover dependency

Read the newest README-MASTER-HANDOVER.md before starting a new production batch. The master overrides old assumptions.

## Change log

### 2026-10-03
- Account 1 role established.
- Photo → game pipeline established.
- Modular asset strategy established.
- Game-ready asset contract established.
- B / First Person corridor set as the first asset target.

## Blueprint link

Work from the current blueprint: blue print plan/BLUEPRINT-PLAN.md

Check blue print plan/BENCHMARKS.md before starting a major asset batch so asset work stays aligned with the latest confirmed build target.

## Godot 4 foundation update — 3 October 2026

Confirmed engine: Godot 4 with GDScript. All active game code, scenes, shaders and resources belong to retro-wave-game. Project root: project.godot. The repository now has core, features, world, UI, resources, shaders, addons and selected runtime asset folders; see docs/GODOT-STRUCTURE.md.

Completed: Godot-specific folder/settings scaffold, main foundation-notice scene, source/import/cache conventions and Drop Zone integration guidance. Incomplete: first-person controls, corridor, collision, equipment, enemy, UI/audio and platform exports. Known limitation: Godot executable is unavailable here; the scaffold has structural checks only, not an editor/runtime test. No gameplay benchmark is confirmed.

Next actions: import project.godot on the development PC, confirm the Godot stable minor version and target devices, then implement the first-person corridor prototype. Asset producers should provide self-contained GLB and appropriate PNG/WebP/audio exports with licence metadata; integration turns these into Godot scenes/resources. Keep original Adobe/DCC masters in Drop Zone.
