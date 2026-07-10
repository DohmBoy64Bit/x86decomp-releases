# Per-file audit — src/x86decomp/cli.py

## A. Identity
- Path: `src/x86decomp/cli.py`
- SHA-256: `674c6069aa4fcda3240077d81e4c56065db26766d9abf1fa786503be4005edd8`
- Size: 47138 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 450 lines)
Root CLI: _build_parser() registers ~100 flat subcommands + register_canonical_commands(); _run() is a linear if-chain dispatching to ~70 library functions; helpers _print/_path/_int/_json_object; main() with try/except → exit 0/2. Compatibility aliases hybrid-generate and project-check bridge into canonical dispatch.

## C. Correctness
- main() catches (X86DecompError, ValueError, KeyError, TypeError, json.JSONDecodeError) — **OSError is not caught**: any missing/unreadable input file (most commands take paths) produces a full traceback and exit code 1 instead of the documented structured error + exit 2. The 4 subsystem CLIs (post-fix) catch OSError via cli_utils.CLI_ERROR_TYPES; root cli.py was NOT migrated to run_cli in the post-release fix pass (it is absent from the 68-file edit set). Finding CLI-002 (Verified statically; runtime demo scheduled Phase 10).
- Error-payload format also diverges: root prints `error: <msg>` plain text; subsystem CLIs print JSON {"error","message"}. Same command surface, two error grammars (part of CLI-002).
- _int uses int(value,0) — accepts hex/octal; good for RVAs; undocumented in help strings (minor UX).
- Final `raise AssertionError(f"unhandled command")` unreachable if parser and chain stay synchronized; acceptable defensive tail.
- coff-synthesize builds CoffRelocation from JSON with int() casts — KeyError/ValueError on malformed input are caught by main; consistent.
- db-query passes raw SQL + JSON params to AnalysisDatabase.query — by-design scriptability; safety depends on analysis_db (see B06 review).

## D. Documentation
Module docstring OK. All 7 helper/private functions carry the template docstring 'Support X processing for internal toolkit callers.' — presence without content (evidence for DOC-001). Subcommand help strings: ~40 of ~100 have help=, the rest show bare names in --help (UX, Phase 6 will quantify).

## E. Maintainability
~330-line if-chain and 75-import header: workable but every new command touches 3 places (import, parser, chain). Packed statements (semicolons) reduce debuggability (matches prior audit M3; still present in this file — Verified).

## F. AI indicators
Template docstrings; import block ordering oddities (msvc_metadata between linker imports; memory after objdiff) suggest mechanical insertion. Alternative explanation: hand-maintained large file with drift. No provenance claim made.

## I. Testing
tests/ has CLI-focused files (test_production.py etc. — B09 will map coverage). Root-command process audit claimed by release docs.

## L. Findings
- CLI-002 (Medium, Verified): root CLI error contract diverges from subsystem CLIs — OSError uncaught (traceback on missing files) and different error output format.
- DOC-001 evidence.

## M. Verdict
Correctness confidence: high for dispatch wiring; medium for error paths. Priority: near-term (unify via run_cli). Final status: Audited — complete.