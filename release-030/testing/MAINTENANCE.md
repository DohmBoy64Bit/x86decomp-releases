# Future-release maintenance contract

This suite must be updated for every x86decomp-toolkit release. It is intentionally version-pinned so coverage cannot silently shrink.

## Required release procedure

1. Copy the previous suite to the new version without deleting existing tests.
2. Run the old catalog against the new toolkit and record every drift item.
3. Update the toolkit version and package version.
4. Add every new Python module to the feature catalog.
5. Add every new CLI command and its semantic test contract.
6. Add every new schema and Ghidra script.
7. Add new matching/functional workflow states.
8. Add or update adapters for new external integrations.
9. Add targeted regression tests for new behavior and bugs fixed.
10. Preserve all previous command, schema, state, and adapter regression tests unless the release explicitly documents a breaking removal.
11. Run harness self-tests.
12. Run the complete suite in non-interactive strict mode with all release-required adapters supplied.
13. Confirm zero pytest skips.
14. Confirm 100% discovered-public-symbol execution.
15. Do not reduce coverage floors without an explicit rationale and approval.
16. Rebuild wheel, source distribution, and source ZIP.
17. Generate SHA-256 manifests and verify from extracted/clean installs.
18. Update `README.md`, `CHANGELOG.md`, `VERIFICATION.md`, adapter documentation, and this file.

## Drift is a failure

The suite must fail when it discovers an uncataloged or stale command, module, schema, or Ghidra script. Do not automatically rewrite the catalog during a release gate; catalog changes require review because they define the promised test surface.

## Adapter behavior is stable

Future releases must preserve:

- detect before prompt;
- no prompt for detected tools;
- custom-path question only for missing tools;
- explicit consent for installation and network access;
- no redistribution of proprietary toolchains;
- missing integrations reported as `BLOCKED`, never passed or silently skipped;
- detailed version/path/source/diagnostic logging.

## Architecture-map coupling

When the toolkit architecture map changes, update the feature catalog and test plan in the same release. Every new architecture box needs a module/command/contract/live adapter test or an explicit bounded rationale.
