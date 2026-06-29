# Comprehensive test plan for x86decomp-toolkit 0.4.0

## Pinned release surface

The 0.4.0 catalog is generated from source and currently pins:

- 60 toolkit Python modules;
- 514 defined functions and methods;
- 106 CLI commands;
- 52 JSON Schemas after the target-decision contract was added;
- 3 Ghidra Java scripts;
- 31 adapter contracts;
- independent matching and functional workflow states.

The exact machine-readable values in
`src/x86decomp_testkit/data/feature_catalog.json` are authoritative. This document is
validated against that catalog during release packaging so stale counts cannot pass.

## Test phases

1. **Source integrity** — root and nested SHA-256 manifests.
2. **Catalog audit** — exact module/function/command/schema/script/adapter/state inventory.
3. **Contract validation** — JSON Schemas, representative examples, skill frontmatter,
   architecture-map synchronization, and Ghidra Java syntax.
4. **Python compilation** — toolkit, suite, scripts, and tests.
5. **CLI parser surface** — process-level `--help` for every command.
6. **Native regressions** — all toolkit tests, including 0.2 and 0.3.1 compatibility.
7. **Supplemental body execution** — targeted calls that ensure every defined
   function/method body executes at least one line.
8. **Coverage audit** — statement, branch, and AST-to-coverage function-body gates.
9. **No-skip gate** — JUnit must report zero skipped pytest cases.
10. **Harness self-tests** — detection, prompting, installer consent, archive security,
    logging, inventory, reports, and strict exit behavior.
11. **Live adapters** — real import/compile/link/analyze/trace/probe operations for every
    detected external adapter.
12. **Packaging** — toolkit and suite wheels/sdists, clean virtual-environment installs,
    installed CLI checks, and package-data checks.
13. **Production controls** — target templates, project migration/backup/restore/repair,
    durable orchestration, output tamper invalidation, cancellation/concurrency,
    reproducibility, security/SBOM, synthetic corpus, release gate, and service snapshot.

## Result policy

- `PASS`: the declared test completed and its assertions passed.
- `FAIL`: completed but violated its contract.
- `ERROR`: harness or environment error prevented a meaningful assertion.
- `BLOCKED`: a declared external dependency is unresolved.

Blocked tests are visible in reports. In strict mode any `BLOCKED` result returns exit
code `2`. A missing adapter never becomes a pass and never disappears as a pytest skip.

## Execution isolation

Release pytest subprocesses set `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`. Only declared suite
plugins/dependencies participate. External process tests use argument arrays, explicit
timeouts, dedicated work directories, and separate stdout/stderr logs.

## Coverage meaning

Executing every function body proves no defined function was completely omitted from
the suite. It does not prove every branch, input, compiler version, binary layout, or
semantic state. Statement/branch coverage and live target pilots provide separate
signals.
