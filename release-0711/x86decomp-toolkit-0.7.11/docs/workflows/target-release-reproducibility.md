# Target-Release Reproducibility

**Technical objective:** Full target-release acceptance pipeline — project verification, reproducibility manifest creation and verification, security and dependency auditing, SBOM generation, convergence analysis, and release-gate evaluation.

**Game:** Starfall Arena (fictional MOBA, x86 PE32, MSVC 2017, 5.4 MB executable).

---

## Overview

Starfall Arena is approaching its public matching-decompilation release. The project lead must certify that the current project state is reproducible, secure, dependency-clean, and convergent with the original binary. The release gate enforces a formal acceptance contract: every required gate must pass before the release is authorized.

You will learn:

1. How to verify project integrity as a release precondition.
2. How to create and verify a reproducibility manifest with tool snapshots.
3. How to audit source trees, dependencies, and generate an SBOM.
4. How to measure image convergence against the original binary.
5. How to evaluate the release gate with all required evidence.

---

## Prerequisites

| Requirement | Detail |
|---|---|
| **Binary** | `games/starfall-arena/starfall_arena.exe` — PE32 x86, 5.4 MB |
| **Project** | `games/starfall-arena/project/` — matching decompilation at 85% convergence |
| **Tool snapshot** | `games/starfall-arena/project/config/tools.json` |
| **Compiler profiles** | 3 profiles (MSVC 2017 /O2, /Ox, /O1) |
| **Evidence store** | 2,400+ evidence records, 300+ verified claims |
| **Workflows** | 1,800+ function workflows in `matched` or `functional` stages |

---

## Starting directory structure

```
games/starfall-arena/
├── starfall_arena.exe
└── project/
    ├── project.json
    ├── original/
    │   └── starfall_arena.exe
    ├── build/
    │   ├── candidates/
    │   └── relink/
    ├── config/
    │   ├── tools.json
    │   └── compiler-profiles/
    ├── evidence/
    ├── functions/
    ├── reports/
    │   ├── convergence/
    │   ├── reproducibility/
    │   └── security/
    └── src/
        ├── matched/
        └── functional/
```

---

## Step 1: Verify project integrity

```console
$ x86decomp verify-project games/starfall-arena/project/
```

**What happens:** Full project integrity check — validates `project.json`, binary SHA-256, all databases, content store, memory ledger, and directory structure. This must pass before any release-gate evaluation.

Expected output:
```json
{
  "project_id": "x86d-starfall-001",
  "architecture": "x86",
  "valid": true,
  "failures": [],
  "schema_version": 3,
  "checks_passed": 18,
  "memory_event_count": 342
}
```

Snapshot tools to capture the current environment:
```console
$ x86decomp snapshot-tools --output games/starfall-arena/project/config/tools-release.json
```

---

## Step 2: Create and verify a reproducibility manifest

```console
$ x86decomp reproduce-create games/starfall-arena/project/ \
    games/starfall-arena/project/reports/reproducibility/reproduce-2026-07-11.json \
    --required-tool ghidra \
    --required-tool cl-msvc-2017 \
    --required-tool lld-link
```

**What happens:** `reproduce-create` builds a reproducibility manifest that records:
- **Project identity:** `project_id`, SHA-256 of the original binary, schema version
- **Tool requirements:** Declared `--required-tool` entries matched against the tools snapshot
- **Input hashes:** SHA-256 of every source file in `src/matched/`, `src/functional/`, and `src/staging/`
- **Compiler profiles:** Hashes of all compiler profile JSONs
- **Evidence store state:** Digest of the evidence store index
- **Content store state:** Digest of the content-store root
- **Reproduction instructions:** The sequence of commands needed to rebuild from source

Verify the manifest:
```console
$ x86decomp reproduce-verify games/starfall-arena/project/ \
    games/starfall-arena/project/reports/reproducibility/reproduce-2026-07-11.json
```

**What happens:** `reproduce-verify` re-checks every hash in the manifest against current project state:
- Every source file hash matches the recorded value
- Tool requirements are satisfied
- The content store and evidence store indices match
- The original binary hash matches

!!! success "Reproduction manifest is a contract"
    A verified reproducibility manifest means a different analyst with the same tools and the manifest can reproduce the project state bit-for-bit. This is the foundation of release certification.

---

## Step 3: Security audit the source tree

```console
$ x86decomp security-audit games/starfall-arena/project/src/ \
    --report games/starfall-arena/project/reports/security/source-audit.json
```

**What happens:** `security-audit` scans every source file in the directory tree for declared security checks:
- Hardcoded secrets or keys
- Unsafe standard library usage (e.g., `strcpy`, `gets`, `sprintf` without bounds)
- Integer overflow patterns in arithmetic
- Missing null checks at trust boundaries
- Format string vulnerabilities

Audit dependencies:
```console
$ x86decomp dependency-audit \
    --executable pip-audit \
    --timeout 300 \
    --report games/starfall-arena/project/reports/security/dependency-audit.json
```

**What happens:** `dependency-audit` runs the installed `pip-audit` adapter against the project's Python dependencies, capturing known-vulnerability reports. `--timeout 300` gives a five-minute window for network-dependent vulnerability database lookups.

---

## Step 4: Generate SBOM and verify release manifest

```console
$ x86decomp sbom-generate games/starfall-arena/project/reports/security/sbom-2026-07-11.json
```

**What happens:** `sbom-generate` produces a software bill of materials covering:
- Toolkit version and its direct dependencies
- Registered compiler toolchains
- All source files with their SHA-256 hashes and declared provenance
- Content-store object inventory
- Evidence store entries (count, not content)

Verify the release hash manifest:
```console
$ x86decomp release-manifest-verify games/starfall-arena/project/ \
    --manifest games/starfall-arena/project/reports/reproducibility/reproduce-2026-07-11.json
```

**What happens:** `release-manifest-verify` cross-references the reproducibility manifest against the current project. It verifies every source hash, tool reference, and artifact digest declared in the manifest. Any mismatch is a release blocker.

---

## Step 5: Analyze image convergence

```console
$ x86decomp convergence-analyze games/starfall-arena/project/original/starfall_arena.exe \
    games/starfall-arena/project/build/relink/starfall_arena_reconstructed.exe \
    --profile games/starfall-arena/project/reports/analysis/layout-profile.json \
    --report games/starfall-arena/project/reports/convergence/convergence-2026-07-11.json \
    --history games/starfall-arena/project/reports/convergence/history.json
```

**What happens:** `convergence-analyze` compares the original and reconstructed images byte-for-byte. Key metrics:
- **Total bytes matched:** How many PE bytes are identical
- **Byte-match percentage:** Convergence ratio (e.g., 84.7%)
- **Section-level breakdown:** Per-section match percentages (`.text` might be 91%, `.rdata` 78%, `.data` 55%)
- **Function-level detail:** Per-function match status from the workflow database
- **Delta from previous:** Change since the last history entry

The `--history` flag appends this report to a cumulative history file, enabling trend charts over time.

Record convergence as evidence:
```console
$ x86decomp evidence-add games/starfall-arena/project/ \
    --kind observed \
    --source convergence-analyze \
    --locator "starfall_arena.exe:convergence-2026-07-11" \
    --assertion "Overall image convergence at 84.7%; .text section at 91.2% byte-identical" \
    --independent-group group-convergence \
    --file games/starfall-arena/project/reports/convergence/convergence-2026-07-11.json
```

---

## Step 6: Run benchmarks against the release candidate

```console
$ x86decomp benchmark-run games/starfall-arena/project/config/benchmarks/release-corpus.json \
    --report games/starfall-arena/project/reports/benchmarks/release-bench.json
```

**What happens:** `benchmark-run` executes the declared benchmark corpus against the current project state. For a release, the benchmark corpus typically includes:
- Compilation speed of representative functions
- Match rate across compiler profiles
- Relink correctness
- Byte-diff speed on large functions

---

## Step 7: Evaluate the release gate

```console
$ x86decomp release-gate games/starfall-arena/project/ \
    --reproduction-manifest games/starfall-arena/project/reports/reproducibility/reproduce-2026-07-11.json \
    --security-report games/starfall-arena/project/reports/security/source-audit.json \
    --convergence-report games/starfall-arena/project/reports/convergence/convergence-2026-07-11.json \
    --require-workflows \
    --require-verified-claims \
    --report games/starfall-arena/project/reports/release/gate-2026-07-11.json
```

**What happens:** `release-gate` evaluates an explicit target-release acceptance contract. Each flag adds a required condition:

| Flag | Gate condition |
|---|---|
| (always) | Project is valid (`verify-project` passes) |
| `--reproduction-manifest` | Manifest verifies successfully |
| `--security-report` | No high-severity findings in the security audit |
| `--convergence-report` | Convergence meets or exceeds a project-configured threshold |
| `--require-workflows` | All function workflows are in `matched` or `functional` status (no `not_started`) |
| `--require-verified-claims` | All claims are in `verified` or `accepted` status |

Expected output:
```json
{
  "release_id": "rel-starfall-2026-07-11",
  "gate_passed": true,
  "gates": {
    "project_valid": {"passed": true},
    "reproducibility": {"passed": true, "manifest_verified": true},
    "security": {"passed": true, "high_severity_findings": 0},
    "convergence": {"passed": true, "byte_match_pct": 84.7, "threshold": 80.0},
    "workflows_complete": {"passed": true, "matched": 1412, "functional": 388, "not_started": 0},
    "verified_claims": {"passed": true, "verified": 347, "unverified": 0}
  },
  "blockers": []
}
```

---

## Step 8: Compare against previous release corpora

If this is not the first release, compare against prior baselines:

```console
$ x86decomp corpus-compare \
    games/starfall-arena/project/reports/benchmarks/release-bench.json \
    games/starfall-arena/project/reports/benchmarks/release-bench-2026-06-01.json \
    --report games/starfall-arena/project/reports/benchmarks/release-comparison.json
```

**What happens:** `corpus-compare` diffs two benchmark corpus reports, highlighting:
- Functions that regressed (previously matched, now mismatched)
- Functions that improved (newly matched)
- Compilation-time deltas
- Any toolchain or flag differences between releases

---

## Expected state after each stage

| Stage | Key deliverable |
|---|---|
| **verify-project** | `valid: true`, zero failures |
| **reproduce-create** | Reproducibility manifest JSON with all input hashes |
| **reproduce-verify** | Verified manifest — all hashes re-checked |
| **security-audit** | Security report — zero high-severity findings |
| **dependency-audit** | Dependency vulnerability report — pip-audit output |
| **sbom-generate** | SBOM JSON — full software inventory |
| **release-manifest-verify** | Release manifest verification — all hashes match |
| **convergence-analyze** | Convergence report — 84.7% with section breakdown |
| **release-gate** | Gate evaluation — all gates `passed: true` |

---

## Verification checklist

- [ ] `verify-project` returns `valid: true`
- [ ] `reproduce-verify` passes — all source and tool hashes re-check
- [ ] `security-audit` report shows zero high-severity or critical findings
- [ ] `dependency-audit` shows no known vulnerabilities in dependencies
- [ ] `sbom-generate` output covers all source files, tools, and content-store objects
- [ ] `release-manifest-verify` confirms all declared hashes
- [ ] `convergence-analyze` reports above the project's threshold
- [ ] `release-gate` returns `gate_passed: true` with all sub-checks passed
- [ ] `corpus-compare` shows no regressions from prior releases

---

## Common failure cases and recovery

| Failure | Cause | Recovery |
|---|---|---|
| `reproduce-verify` hash mismatch | Source file modified after manifest creation | Re-run `reproduce-create`; lock sources with the `source lock` canonical command |
| `security-audit` finds `sprintf` usage | Legacy matched code preserves original patterns | Document in evidence as "preserved for matching parity"; gate accepts documented exceptions |
| `release-gate` fails on convergence | Relinked image has drifted due to changed compiler profile | Re-run `linker-plan` and `relink` with the updated profile |
| `release-gate` fails on workflows | Functions still in `not_started` status | Bulk-update via `workflow-update` for any stubs that are intentionally deferred |
| `dependency-audit` timeout | pip-audit cannot reach vulnerability database | Increase `--timeout`, or run on a machine with network access |
| `release-manifest-verify` fails | Content-store objects moved or deleted | Rebuild missing artifacts or re-create the manifest from current state |

---

## Related reference pages

- [Reproducibility](../concepts/reproducibility.md)
- [convergence-analyze](../commands/convergence/convergence.md)
- [Reproducibility Commands](../commands/convergence/reproduce.md)
- [release-gate](../commands/convergence/release-gate.md)
- [security-audit / dependency-audit](../commands/security/audit.md)
- [sbom-generate / release-manifest-verify](../commands/security/release.md)
- [benchmark-run](../commands/ground-truth/benchmarks.md)
- [Corpus Commands](../commands/ground-truth/corpus.md)

---

## Optional extensions

1. **Automated release pipeline:** Create a `pipeline-create` manifest with stages for each gate (verify-project → reproduce-verify → security-audit → convergence-analyze → release-gate) and run it with `pipeline-run`. The orchestrator records each stage's success/failure.

2. **Multi-compiler reproducibility:** Generate a synthetic corpus (`corpus-generate`) and compile it under all registered toolchains with `compiler-lab`. Verify that the release build environment produces identical output across machines.

3. **Test-bundle sealed release:** Create a hash-sealed test bundle for the release:
   ```console
   $ x86decomp test-bundle-create games/starfall-arena/project/reports/release/bundle.tar.gz \
       --artifact "reproduce=reports/reproducibility/reproduce-2026-07-11.json" \
       --artifact "convergence=reports/convergence/convergence-2026-07-11.json" \
       --artifact "sbom=reports/security/sbom-2026-07-11.json" \
       --authorization "Release 2026-07-11 Starfall Arena" \
       --expected-architecture x86
   ```

4. **Convergence history visualization:** Collect multiple `convergence-analyze` runs with `--history` and render a trend graph showing byte-match percentage over time, section by section.

5. **Content-store integrity audit:** Before release, run `content-verify` on the entire artifact store to confirm zero-bit corruption:
   ```console
   $ x86decomp content-verify games/starfall-arena/project/artifacts/
   ```
