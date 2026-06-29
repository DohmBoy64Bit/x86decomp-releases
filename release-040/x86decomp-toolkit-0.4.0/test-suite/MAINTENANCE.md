# Future-release maintenance contract — baseline 0.4.0

The integrated suite is version-pinned and must be updated for every toolkit release.
Coverage may grow, but it must not silently shrink.

## Required release procedure

1. Update the stable `test-suite/` directory in place; do not delete prior regression tests.
2. Run the previous release catalog and compatibility contracts against the new tree.
3. Update toolkit, suite, skill, schema, architecture-map, and package versions together.
4. Catalog every Python module and every defined function/method, including private helpers.
5. Catalog every CLI command, JSON Schema, Ghidra script, adapter, and workflow state.
6. Add semantic tests for new behavior and permanent regression tests for fixed defects.
7. Preserve earlier command/schema/module/adapter/state contracts unless an explicit,
   migrated breaking change is documented and tested.
8. Run harness self-tests and the complete native-plus-supplemental suite with
   `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`.
9. Require zero pytest skips. Missing live integrations are `BLOCKED`, never skipped.
10. Require every discovered function/method body to execute at least one direct line.
11. Do not lower coverage floors to hide regressions.
12. Run package builds and clean installs for toolkit and suite wheels/sdists.
13. Verify root and nested SHA-256 manifests from an extracted source ZIP.
14. Update all docs, changelogs, verification records, feature catalogs, project memory,
   security records, skill, and four architecture maps.
15. Remove build directories, virtual environments, caches, coverage outputs, downloaded
   adapters, local configs, absolute workstation paths, and generated result histories.

## Drift is a release failure

The suite fails on uncataloged or stale modules, functions/methods, commands, schemas,
Ghidra scripts, adapters, or workflow states. Catalog rewriting is an explicit reviewed
release action, not part of the release gate.

## Stable adapter behavior

Future releases preserve:

- detect before prompt;
- no prompt for detected tools;
- custom-path questions only for missing tools;
- path validation before persistence;
- explicit installation and network consent;
- no redistribution of proprietary toolchains;
- missing integrations reported as `BLOCKED`;
- detailed path/version/source/command/output diagnostics;
- strict exit code `2` when unresolved live contracts remain.

## Architecture-map coupling

The following four artifacts are co-equal and must remain synchronized:

1. `docs/ARCHITECTURE_MAP.md`
2. `docs/ARCHITECTURE_MAP_ASCII.txt`
3. `test-suite/docs/ARCHITECTURE_MAP.md`
4. `test-suite/docs/ARCHITECTURE_MAP_ASCII.txt`

Any changed architecture box must have an owning module, command, schema/contract, test,
and, when external, adapter/live-probe path or an explicit bounded rationale.
