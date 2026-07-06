# Agent and contributor operating rules — 0.7.10

## Release model

The active repository represents one release only. Use capability-oriented names and current contracts. Do not add version-specific modules, executables, bridges, installers, overlays, reports, catalogs, tests, or documentation planes.

## Non-negotiable engineering rules

1. Preserve functionality unless a complete tested successor supersedes it.
2. Never introduce placeholders, TODO implementations, fake adapters, empty success paths, or fabricated evidence.
3. Keep `x86decomp` as the only toolkit executable and `x86decomp-test` as the only test-suite executable.
4. Keep all current commands, routes, modules, function and method bodies, schemas, adapters, workflows, and package artifacts inventoried.
5. Keep byte-form assembly as the conservative default; annotated and mnemonic output must remain explicit and evidence-backed.
6. Treat AI and analyst proposals as proposals until the declared evidence gate accepts them.
7. Never conceal contradictions, unknowns, missing adapters, timeouts, unsupported instructions, or blocked integrations.
8. Require explicit authorization before native target execution.
9. Preserve deterministic outputs, content hashes, audit chains, and rollback-safe project operations.
10. Update code, tests, schemas, examples, skill, docs, catalogs, and all four architecture artifacts in one release transaction.
11. Treat local-model output as an untrusted proposal; only deterministic compiler, relocation, and exact-byte gates may accept it.
12. Keep the MkDocs site synchronized with the current parser, source, schemas, adapters, tests, and release evidence.

## Required release gates

- compilation and import checks;
- recursive schema and example validation;
- exact current catalog reconciliation;
- all toolkit and standalone verifier tests with zero skips;
- all current function and method bodies exercised;
- every root command and canonical route process-tested;
- line and branch coverage floors;
- clean wheel and source-distribution builds;
- clean installation and `pip check`;
- extracted archive verification;
- deterministic source archive reproduction;
- no-placeholder and historical-reference scans;
- SHA-256 manifests and final bundle verification.

## Evidence vocabulary

Use observed, derived, proposed, corroborated, accepted, verified, behaviorally tested, symbolically proved, byte identical, rejected, blocked, and unknown precisely. Do not promote one category into another without the declared verifier.
