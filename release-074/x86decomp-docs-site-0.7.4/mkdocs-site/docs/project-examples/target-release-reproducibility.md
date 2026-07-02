---
title: 'Example: target release and reproducibility project'
description: Hash the project and required tools, verify reproducibility inputs, audit
  source and dependencies, and evaluate an explicit target release contract without
  overclaiming correctness.
original_path: project-examples/target-release-reproducibility.html
---

<a id="model"></a>
<a id="target-release-reproducibility-flow-title"></a>
<a id="target-release-reproducibility-flow-desc"></a>
<a id="arrow-target-release-reproducibility"></a>
<a id="target-release-reproducibility-flow-caption"></a>
<a id="check"></a>
<a id="reproduce"></a>
<a id="security"></a>
<a id="claims"></a>
<a id="gate"></a>
<a id="archive"></a>
<a id="limits"></a>
<a id="source-basis"></a>

Section: Project examples

# Example: target release and reproducibility project

Hash the project and required tools, verify reproducibility inputs, audit source and dependencies, and evaluate an explicit target release contract without overclaiming correctness.

> **Example notation.** Paths and function identifiers are representative local names. Commands and options are exact v0.7.4 parser forms; target-specific hashes, addresses, profiles, reports, and passing outcomes must come from the actual project.

> **Classification.** This is a release-acceptance workflow. It evaluates declared project contracts; it is separate from the sealed toolkit release process.

**On this page**

1. [Release model](#model)
2. [Check project state](#check)
3. [Create reproducibility manifest](#reproduce)
4. [Run audits](#security)
5. [Verify claims and pipelines](#claims)
6. [Evaluate release gate](#gate)
7. [Archive evidence](#archive)
8. [Truth boundary](#limits)
9. [Source basis](#source-basis)

## Release model

The gate combines explicit inputs and reports; it does not infer success from missing evidence.Project check → Workflow records → Verified claims → Pipeline results → Reproduction → Security → Release gate

Project checkWorkflow recordsVerified claimsPipeline resultsReproductionSecurityRelease gate

The gate combines explicit inputs and reports; it does not infer success from missing evidence.

```ascii-fallback
Project check → Workflow records → Verified claims → Pipeline results → Reproduction → Security → Release gate
```

1

## Verify project integrity and current workflows

```
x86decomp project-check project
x86decomp memory-verify project
x86decomp content-verify project/artifacts
x86decomp workflow-show project pe-rva:00401230
```

Resolve corrupt state, unresolved required blockers, or missing referenced reports before evaluating a gate.

2

## Create and verify a reproduction manifest

```
x86decomp reproduce-create project reports/reproducibility/manifest.json --required-tool gcc --required-tool lld-link
x86decomp reproduce-verify project reports/reproducibility/manifest.json
```

The manifest records project inputs, selected configuration identities, and requested tool identities. Verification reports exact drift; it does not rebuild the target automatically.

3

## Run source, dependency, SBOM, and manifest checks

```
x86decomp security-audit project --report reports/security/source-audit.json
x86decomp dependency-audit --executable pip-audit --timeout 300 --report reports/security/dependencies.json
x86decomp sbom-generate reports/security/sbom.json
x86decomp release-manifest-verify project --manifest MANIFEST.sha256
```

The source audit’s pass condition is the absence of critical/high findings under its implemented rules. Dependency audit preserves the installed adapter’s findings. Neither report certifies the target as safe or vulnerability-free.

4

## Require provenance and completed orchestration where policy demands it

```
x86decomp claim-verify project claim-entry-00401230
x86decomp pipeline-status project PIPELINE_ID
```

Every claim file present in the project is passed through the strict evidence verifier and a non-verified claim fails the gate. `--require-verified-claims` additionally requires at least one claim. Pipeline failures affect the release gate only when `--require-succeeded-pipelines` is supplied, and that flag also requires at least one durable pipeline.

5

## Evaluate the explicit target release gate

```
x86decomp release-gate project --reproduction-manifest reports/reproducibility/manifest.json --security-report reports/security/source-audit.json --convergence-report reports/convergence/latest.json --require-workflows --require-verified-claims --require-succeeded-pipelines --report reports/release-gate.json
```

Inspect every gate check and the truth statement in the report. **v0.7.4 workflow compatibility limit:** the release gate reads a legacy per-function `modes` object, while the public `workflow-init`/`workflow-update` path writes schema-v2 fields named `selected_modes`, `matching_status`, and `functional_status`. Therefore `--require-workflows` can require that at least one workflow file exists, but this gate does not enforce the public schema-v2 status minima. Inspect those states separately with `workflow-show` and do not claim that v0.7.4 release-gate validated them. Subject to that limitation, a pass means the other recorded checks satisfied the supplied gate contract at that point in time.

6

## Create a deterministic project backup

```
x86decomp project-backup project releases/project-release-backup.tar.gz
```

Store the backup together with the gate, reproduction, security, convergence, workflow, compiler, linker, and validation reports. The project backup rejects symlinks and is designed to be deterministic for the same project content.

## Required release wording

> **Supported statement.** “This target project passed the checks recorded in `reports/release-gate.json`; public schema-v2 workflow minima were reviewed separately because v0.7.4 release-gate does not consume those status fields.”

> **Unsupported statement.** Do not translate that into “original source recovered,” “universally equivalent,” “safe,” or “historically identical” unless separate evidence actually establishes those claims.

## v0.7.4 source basis

> **Triple-check model.** Each example was checked against the CLI parser, implementation behavior, and an independent test, schema, or contract document. Full hashes and search anchors are in [the source audit](source-audit.md).

| Evidence class | File | Lines | SHA-256 |
| --- | --- | --- | --- |
| parser | `src/x86decomp/cli.py` | L232–L235 | `21e0654ced2f` |
| implementation | `src/x86decomp/release_gate.py` | L41–L44 | `8e79be8c5af6` |
| implementation | `src/x86decomp/release_gate.py` | L92–L95 | `8e79be8c5af6` |
| implementation | `src/x86decomp/reproducibility.py` | L52–L55 | `bcc5e2a773d7` |
| implementation | `src/x86decomp/security_audit.py` | L78–L81 | `274c689b0141` |
| implementation | `src/x86decomp/workflow.py` | L82–L85 | `cae8a093f08f` |
| test | `tests/test_production.py` | L261–L264 | `da0d4bd57f7f` |
| test | `tests/test_production.py` | L486–L489 | `da0d4bd57f7f` |

## Related examples

[Matching project

Open the source-verified workflow.](matching-project.md)[Functional project

Open the source-verified workflow.](functional-project.md)[Hybrid composition

Open the source-verified workflow.](hybrid-project.md)
