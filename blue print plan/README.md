# Retro-Wave-Game - Blue Print Plan

This folder is the **living blueprint system** for the game.

## Source of truth

- `BLUEPRINT-PLAN.md` = living master blueprint.
- `DECISION-LOG.md` = decisions that are OPEN, LOCKED or REOPENED.
- `BENCHMARKS.md` = immutable rollback-point registry.
- `BLUEPRINT-PLAN.pdf` = generated visual snapshot of the current blueprint.

## How updates work

1. Update the master blueprint.
2. Increase the blueprint revision.
3. Add a dated entry to the change log.
4. Update affected team handovers.
5. Test the build.
6. When a working state passes the benchmark requirements, create a new BENCHMARK.
7. Record the exact Git commit, blueprint revision and test state.

## Benchmark rule

A benchmark is an **immutable working point**. Never rewrite an old benchmark to describe newer work.

New work moves forward from the latest benchmark.

If later work breaks the project, roll back to the most recent known-good benchmark, repair from there, then create a new benchmark.

## Workshop method

We will walk through the OPEN decisions in order and lock them one by one. The blueprint can therefore become more precise without blocking development.
