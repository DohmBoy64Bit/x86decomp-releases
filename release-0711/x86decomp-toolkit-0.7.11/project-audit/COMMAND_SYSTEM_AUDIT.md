# Command-System Audit — x86decomp-toolkit 0.7.11

Evidence: full read of cli.py + canonical.py + all subsystem cli.py; live parser introspection (R-012), live `x86decomp commands` (R-012), COMMAND_REFERENCE diff (R-019 exact match).

## Surface (mechanically Verified)
- One executable `x86decomp` (+ `x86decomp-test` for the harness). Verified: pyproject [project.scripts].
- 166 top-level parsers = 106 flat root commands + 59 canonical capability groups + 1 `commands` catalog. Verified live (R-012).
- 239 canonical routes across the 59 groups. Verified live; matches README/PROJECT_MEMORY/RELEASE_VERIFICATION/COMMAND_REFERENCE claims exactly (R-019).
- Two dispatch styles: flat verb-noun commands (init, inspect-pe, coff-inspect, diff-bytes, ...) handled by cli._run's if-chain; canonical `<group> <action>` routes dispatched via canonical.dispatch to the owning subsystem (governance/reconstruction/native/assembly) with a merged-group ownership table.
- Two compatibility aliases: `hybrid-generate`→`hybrid generate`, `project-check`→`project check`.

## Structure & grouping
- Canonical groups are cohesive and owner-attributed (canonical.py _MERGED_GROUPS resolves shared group/action ownership deterministically, raising on ambiguity — good design).
- Flat commands are grouped by prefix convention (coff-*, db-*, work-*, mcp-*, pipeline-*, project-*, corpus-*, claim-*, workflow-*, target-pack-*) but are NOT sub-parsers — they are flat, so `--help` lists 106 siblings. Discoverability relies on the `commands` catalog + docs/COMMAND_REFERENCE rather than hierarchical help.

## Consistency findings
- CLI-001 (Medium): subsystem/canonical module mains (run_cli) do not catch the x86decomp.errors family → tracebacks on malformed-binary input via those entry points. (Root `x86decomp` catches X86DecompError — clean.)
- CLI-002 (Medium): root `x86decomp` main omits OSError → missing/unreadable input path yields FileNotFoundError traceback + exit 1 instead of structured error + exit 2, across ALL 166 commands/239 routes (runtime-verified R-010). Also the error GRAMMAR differs: root prints `error: <msg>` (plain), subsystems print `{"error","message"}` (JSON) — two formats for one "unified" CLI.
- CLI-003 (Medium): 78 of 106 flat commands have no help= string → bare names in `x86decomp --help` (R-012). Canonical groups DO have help. Hurts new-user discoverability of the primary interface.
- Exit codes: 0 success, 2 handled error (both cli.py and run_cli); uncaught (OSError at root, X86DecompError at subsystem) → 1 via traceback. Stable for the happy path and handled errors; the gaps above are the exceptions.
- Output: all commands emit sorted-key indented JSON to stdout (machine-readable, scriptable, deterministic). Good for automation.

## Per-command documentation coverage
- Every canonical route documented in docs/COMMAND_REFERENCE_0.7.11.{json,md} (exact match to live, R-019) with plan-only annotations.
- Flat commands: help= present on ~28/106; the rest rely on COMMAND_REFERENCE. Argument/option-level docs live in the reference, not in per-command --help.

## Destructive-operation safeguards
- Mutating ops require explicit flags: project-repair/gc default to dry-run (--apply to act); migrate has --dry-run; patch-image requires expected sha256; integration-run host exec requires --allow-host-execution; mcp mutations require allowlist + approval hash. Good consent posture.

## Scriptability
- JSON-everywhere output + stable exit 0/2 for handled paths = scriptable. CLI-002's exit-1 traceback on bad paths is the main scripting hazard (a script checking `==2` misclassifies missing-file as an unexpected crash).

## Summary
Well-architected two-tier command system with an exactly-synced command reference and strong destructive-op safeguards. The three CLI findings (error-contract inconsistency CLI-001/002, missing help CLI-003) are the actionable items; all are Medium and mechanically fixable (unify on run_cli+X86DecompError+OSError; add help= strings).
