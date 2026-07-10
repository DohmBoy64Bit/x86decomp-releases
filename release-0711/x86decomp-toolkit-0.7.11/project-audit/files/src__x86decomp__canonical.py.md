# Per-file audit — src/x86decomp/canonical.py

## A. Identity
- Path: `src/x86decomp/canonical.py`
- SHA-256: `57a138c9755a6aad8c2bd3ea5b90ca37d738882fd5860f9a6404cd9c0d21f0b5`
- Size: 11728 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 317 lines)
Canonical command surface: introspects the four subsystem argparse parsers (_subparsers/_source_parsers/_group_parsers/_leaf_parsers), resolves route ownership (_MERGED_GROUPS explicit map → _LATEST_SHARED_OWNER → sole owner, ContractError on ambiguity), computes canonical_routes()/canonical_groups()/command_catalog(), registers `commands` + every group onto the root parser (parents=[source] reuse), dispatch() to owner dispatchers, own build_parser/main via run_cli.

## C. Correctness
- Route-conflict handling is defensive and loud (ambiguous owners raise) — good.
- Relies on argparse private internals (parser._actions, _SubParsersAction, parents=) — fragile across Python versions but pinned ≥3.11; works on 3.11–3.13 per CI claim. Informational risk.
- register_canonical_commands adds --project/--actor at GROUP level while reusing leaf parsers as parents — flag-position coupling; `x86decomp <group> --project X <action>` required ordering. UX quirk to verify in Phase 6 help review.
- command_catalog validates group AFTER filtering (unknown group with owner filter still errors correctly; order harmless).
- Rebuilds all four parsers multiple times per invocation (canonical_groups() calls canonical_routes() which calls _leaf_parsers(); register_canonical_commands calls canonical_groups + canonical_routes per group + _leaf_parsers) — O(groups×routes) parser construction on EVERY CLI start. PERF-001 candidate (measure at Phase 10: `x86decomp --help` latency).

## D. Documentation
Excellent post-fix docstrings (Args/Returns/Raises) — this file is part of the 68-file edit set; night-and-day contrast with cli.py (evidence that DOC-001 was partially remediated in edited files only).

## L. Findings
- PERF-001 (Low, Probable): repeated full parser-tree construction at startup; quantify before recommending.
- Corroborates CLI-001 context (run_cli adoption here but not in root cli.py).

## M. Verdict
Quality: high. Final status: Audited — complete.