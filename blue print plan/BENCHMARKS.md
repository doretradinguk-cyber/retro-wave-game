# Retro-Wave-Game - Benchmark Registry

A **BENCHMARK** is a confirmed, working project state used as a rollback point.

## Immutable rule

Once a benchmark is confirmed, its record is not rewritten to describe later work.

If the project later breaks, roll back to the benchmark's recorded commit/build and continue from there.

## Benchmark checklist

A benchmark should normally include:

- [ ] Build loads
- [ ] Core requested feature works
- [ ] No blocking errors
- [ ] Visual test completed
- [ ] Gameplay test completed
- [ ] Performance checked
- [ ] Known issues recorded
- [ ] Exact Git commit recorded
- [ ] Blueprint revision recorded
- [ ] Build/reference evidence recorded

## Planned benchmark ladder

### BENCHMARK-000 - Foundation
**Status:** NOT YET CONFIRMED

Target: repository/application foundation loads reliably.

### BENCHMARK-001 - First-Person Corridor Prototype
**Status:** NOT YET CONFIRMED

Target: first-person camera, movement and collision work in the corridor prototype.

### BENCHMARK-002 - Neon Hollow Visual Lock
**Status:** NOT YET CONFIRMED

Target: lighting, wet floor, reflections, emissive fixtures, atmosphere and stylised treatment demonstrate the target.

### BENCHMARK-003 - Playable Corridor Slice
**Status:** NOT YET CONFIRMED

Target: playable corridor loop with room, interaction, equipment, UI and ambience.

### BENCHMARK-004 - Enemy Encounter Slice
**Status:** NOT YET CONFIRMED

Target: enemy encounter works inside the playable corridor.

### BENCHMARK-005 - Vertical Slice Complete
**Status:** NOT YET CONFIRMED

Target: polished end-to-end vertical slice.

## Confirmed benchmarks

No gameplay benchmark has been confirmed yet.

When the first working benchmark is created, add:
- ID
- Name
- Date
- Git commit/tag
- Blueprint revision
- Build reference
- Test results
- Known issues
- Rollback notes
