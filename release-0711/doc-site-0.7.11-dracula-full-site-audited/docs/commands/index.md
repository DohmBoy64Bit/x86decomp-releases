---
title: Commands
description: Parser-derived root command index for x86decomp 0.7.11.
---

# Commands

This index is regenerated from the `0.7.11` parser and canonical route registry.

- Root commands: **166**
- Canonical groups: **59**
- Canonical routes: **239**

| Command | Canonical group | Route actions |
| --- | --- | --- |
| [`abi`](abi.md) | yes | compare, export, recover, shim, show, verify |
| [`abi-check`](abi-check.md) | no | Root command or compatibility entry point |
| [`angr-validate`](angr-validate.md) | no | Root command or compatibility entry point |
| [`artifact-import`](artifact-import.md) | no | Root command or compatibility entry point |
| [`artifact-verify`](artifact-verify.md) | no | Root command or compatibility entry point |
| [`asm`](asm.md) | yes | annotate, batch, list, materialize, report, verify-roundtrip |
| [`asset`](asset.md) | yes | inventory |
| [`benchmark-run`](benchmark-run.md) | no | Root command or compatibility entry point |
| [`boundary`](boundary.md) | yes | audit, audit-project, export-ghidra-fixes, list, show |
| [`build`](build.md) | yes | add-target, add-variant, compare-modes, create, generate, matrix, show, validate |
| [`campaign`](campaign.md) | yes | branch, create, list, pause, plan, resume, snapshot, start, status, stop |
| [`candidate`](candidate.md) | yes | add-file, compare, create, evaluate, list, promote, search, show, transition |
| [`capsule`](capsule.md) | yes | create, inspect, reproduce, verify |
| [`changeset`](changeset.md) | yes | add-operation, apply, conflicts, create, export, inspect, merge, rebase, show, verify |
| [`claim-attach`](claim-attach.md) | no | Root command or compatibility entry point |
| [`claim-contradict`](claim-contradict.md) | no | Root command or compatibility entry point |
| [`claim-create`](claim-create.md) | no | Root command or compatibility entry point |
| [`claim-verify`](claim-verify.md) | no | Root command or compatibility entry point |
| [`class`](class.md) | yes | scaffold |
| [`coff-comdat-resolve`](coff-comdat-resolve.md) | no | Root command or compatibility entry point |
| [`coff-extract`](coff-extract.md) | no | Root command or compatibility entry point |
| [`coff-inspect`](coff-inspect.md) | no | Root command or compatibility entry point |
| [`coff-synthesize`](coff-synthesize.md) | no | Root command or compatibility entry point |
| [`commands`](commands.md) | no | Root command or compatibility entry point |
| [`compile`](compile.md) | no | Root command or compatibility entry point |
| [`compile-worker`](compile-worker.md) | no | Root command or compatibility entry point |
| [`compiler-lab`](compiler-lab.md) | no | Root command or compatibility entry point |
| [`compiler-rules`](compiler-rules.md) | yes | compare-flags, learn-rule, rule-report |
| [`consensus`](consensus.md) | yes | conflicts, explain, record, resolve, scan |
| [`content-put`](content-put.md) | no | Root command or compatibility entry point |
| [`content-verify`](content-verify.md) | no | Root command or compatibility entry point |
| [`convergence-analyze`](convergence-analyze.md) | no | Root command or compatibility entry point |
| [`corpus-build`](corpus-build.md) | no | Root command or compatibility entry point |
| [`corpus-compare`](corpus-compare.md) | no | Root command or compatibility entry point |
| [`corpus-create-manifest`](corpus-create-manifest.md) | no | Root command or compatibility entry point |
| [`corpus-generate`](corpus-generate.md) | no | Root command or compatibility entry point |
| [`corpus-generated-verify`](corpus-generated-verify.md) | no | Root command or compatibility entry point |
| [`corpus-verify`](corpus-verify.md) | no | Root command or compatibility entry point |
| [`counterexample`](counterexample.md) | yes | add, list, promote, show |
| [`cpp-recover`](cpp-recover.md) | no | Root command or compatibility entry point |
| [`crosscheck-ghidra`](crosscheck-ghidra.md) | no | Root command or compatibility entry point |
| [`db-constraint-accept`](db-constraint-accept.md) | no | Root command or compatibility entry point |
| [`db-constraint-add`](db-constraint-add.md) | no | Root command or compatibility entry point |
| [`db-constraint-conflicts`](db-constraint-conflicts.md) | no | Root command or compatibility entry point |
| [`db-ingest`](db-ingest.md) | no | Root command or compatibility entry point |
| [`db-query`](db-query.md) | no | Root command or compatibility entry point |
| [`decompiler`](decompiler.md) | yes | cleanup |
| [`decompme-pack`](decompme-pack.md) | no | Root command or compatibility entry point |
| [`dependency-audit`](dependency-audit.md) | no | Root command or compatibility entry point |
| [`diff`](diff.md) | yes | explain |
| [`diff-bytes`](diff-bytes.md) | no | Root command or compatibility entry point |
| [`diff-function`](diff-function.md) | no | Root command or compatibility entry point |
| [`disassemble`](disassemble.md) | no | Root command or compatibility entry point |
| [`drcov-parse`](drcov-parse.md) | no | Root command or compatibility entry point |
| [`drcov-run`](drcov-run.md) | no | Root command or compatibility entry point |
| [`dynamic-validate`](dynamic-validate.md) | no | Root command or compatibility entry point |
| [`evidence-add`](evidence-add.md) | no | Root command or compatibility entry point |
| [`family`](family.md) | yes | add, correlate, create, report |
| [`function`](function.md) | yes | classify, discover, reconcile, sort |
| [`game-pattern`](game-pattern.md) | yes | state-machine |
| [`ghidra-export`](ghidra-export.md) | no | Root command or compatibility entry point |
| [`ghidra-mcp`](ghidra-mcp.md) | yes | batch-decompile, decompile, functions, probe, sync-names |
| [`graph`](graph.md) | yes | edge, impact, node |
| [`harness-generate`](harness-generate.md) | no | Root command or compatibility entry point |
| [`headers`](headers.md) | yes | create, cycles, declare, explain, include, synthesize, synthesize-project, validate |
| [`hybrid`](hybrid.md) | yes | compose, generate, verify |
| [`hybrid-generate`](hybrid-generate.md) | no | Root command or compatibility entry point |
| [`hypothesis`](hypothesis.md) | yes | create, dependency, evidence, gate, list, show, transition |
| [`image-match`](image-match.md) | no | Root command or compatibility entry point |
| [`image-profile`](image-profile.md) | no | Root command or compatibility entry point |
| [`image-text`](image-text.md) | yes | compose |
| [`init`](init.md) | no | Root command or compatibility entry point |
| [`inspect-pe`](inspect-pe.md) | no | Root command or compatibility entry point |
| [`integration-run`](integration-run.md) | no | Root command or compatibility entry point |
| [`layout-reconstruct`](layout-reconstruct.md) | no | Root command or compatibility entry point |
| [`lib-inspect`](lib-inspect.md) | no | Root command or compatibility entry point |
| [`library`](library.md) | yes | accept, candidates, externalize, identify, reconstruct, reject |
| [`linker-plan`](linker-plan.md) | no | Root command or compatibility entry point |
| [`llm`](llm.md) | yes | batch-create, batch-match, cpp-generate, generate, job-create, job-from-range, match, probe, profile-create, profile-validate, prompt, providers, verify |
| [`loop`](loop.md) | yes | list, run, show |
| [`map-inspect`](map-inspect.md) | no | Root command or compatibility entry point |
| [`match`](match.md) | yes | batch, compare, mismatches, report |
| [`mcp-commit`](mcp-commit.md) | no | Root command or compatibility entry point |
| [`mcp-propose`](mcp-propose.md) | no | Root command or compatibility entry point |
| [`mcp-read`](mcp-read.md) | no | Root command or compatibility entry point |
| [`mcp-tools`](mcp-tools.md) | no | Root command or compatibility entry point |
| [`memory-add`](memory-add.md) | no | Root command or compatibility entry point |
| [`memory-render`](memory-render.md) | no | Root command or compatibility entry point |
| [`memory-verify`](memory-verify.md) | no | Root command or compatibility entry point |
| [`metadata-scan`](metadata-scan.md) | no | Root command or compatibility entry point |
| [`mod`](mod.md) | yes | branch-init |
| [`module`](module.md) | yes | add-member, add-unit-member, assign, create, create-unit, list, show, show-unit, suggest |
| [`objdiff-run`](objdiff-run.md) | no | Root command or compatibility entry point |
| [`patch-image`](patch-image.md) | no | Root command or compatibility entry point |
| [`pattern`](pattern.md) | yes | catalog, generate, match, promote, scan |
| [`pdb-inspect`](pdb-inspect.md) | no | Root command or compatibility entry point |
| [`pe`](pe.md) | yes | export-coff, export-sections, inventory, patch-apply, patch-plan, text-swap |
| [`pipeline-cancel`](pipeline-cancel.md) | no | Root command or compatibility entry point |
| [`pipeline-create`](pipeline-create.md) | no | Root command or compatibility entry point |
| [`pipeline-recover`](pipeline-recover.md) | no | Root command or compatibility entry point |
| [`pipeline-retry`](pipeline-retry.md) | no | Root command or compatibility entry point |
| [`pipeline-run`](pipeline-run.md) | no | Root command or compatibility entry point |
| [`pipeline-status`](pipeline-status.md) | no | Root command or compatibility entry point |
| [`playability`](playability.md) | yes | smoke-plan |
| [`plugin`](plugin.md) | yes | doctor, install, invoke, list, validate |
| [`progress`](progress.md) | yes | reconcile |
| [`project`](project.md) | yes | check, doctor-paths, explain-boundaries, export, health, init, synthesize-layout |
| [`project-backup`](project-backup.md) | no | Root command or compatibility entry point |
| [`project-check`](project-check.md) | no | Root command or compatibility entry point |
| [`project-from-target`](project-from-target.md) | no | Root command or compatibility entry point |
| [`project-gc`](project-gc.md) | no | Root command or compatibility entry point |
| [`project-migrate`](project-migrate.md) | no | Root command or compatibility entry point |
| [`project-repair`](project-repair.md) | no | Root command or compatibility entry point |
| [`project-restore`](project-restore.md) | no | Root command or compatibility entry point |
| [`proof`](proof.md) | yes | evaluate, export, inspect, obligation, result, verify |
| [`provenance`](provenance.md) | yes | binary, export, record, source |
| [`regression`](regression.md) | yes | compare |
| [`release-gate`](release-gate.md) | no | Root command or compatibility entry point |
| [`release-manifest-verify`](release-manifest-verify.md) | no | Root command or compatibility entry point |
| [`release-policy`](release-policy.md) | yes | moddable-source |
| [`relink`](relink.md) | no | Root command or compatibility entry point |
| [`reloc`](reloc.md) | yes | inspect, resolve, supported |
| [`reproduce-create`](reproduce-create.md) | no | Root command or compatibility entry point |
| [`reproduce-verify`](reproduce-verify.md) | no | Root command or compatibility entry point |
| [`review`](review.md) | yes | assign, create, decide, list, lock, show |
| [`runtime`](runtime.md) | yes | launch, map-crash, validate-image |
| [`runtime-analysis`](runtime-analysis.md) | yes | identify, match-library, quarantine |
| [`sbom-generate`](sbom-generate.md) | no | Root command or compatibility entry point |
| [`script-port`](script-port.md) | yes | audit |
| [`security`](security.md) | yes | finding, policy, report, scan |
| [`security-audit`](security-audit.md) | no | Root command or compatibility entry point |
| [`serve`](serve.md) | no | Root command or compatibility entry point |
| [`snapshot-tools`](snapshot-tools.md) | no | Root command or compatibility entry point |
| [`source`](source.md) | yes | impact, lock, reconcile, unlock |
| [`source-map`](source-map.md) | yes | annotate, verify |
| [`source-stage`](source-stage.md) | yes | classify |
| [`staging`](staging.md) | yes | compile-check, generate-context, resolve, scan, unresolved |
| [`subsystem`](subsystem.md) | yes | detect |
| [`symbolic-memory-validate`](symbolic-memory-validate.md) | no | Root command or compatibility entry point |
| [`symbolic-validate`](symbolic-validate.md) | no | Root command or compatibility entry point |
| [`target-pack-infer`](target-pack-infer.md) | no | Root command or compatibility entry point |
| [`target-pack-verify`](target-pack-verify.md) | no | Root command or compatibility entry point |
| [`template-derive`](template-derive.md) | no | Root command or compatibility entry point |
| [`template-materialize`](template-materialize.md) | no | Root command or compatibility entry point |
| [`test-bundle-create`](test-bundle-create.md) | no | Root command or compatibility entry point |
| [`test-bundle-inspect`](test-bundle-inspect.md) | no | Root command or compatibility entry point |
| [`tests`](tests.md) | yes | add, explain, list, promote-counterexample, synthesize |
| [`text-swap`](text-swap.md) | yes | build, inject, plan, verify |
| [`toolchain`](toolchain.md) | yes | hash-tree, redact-package, verify-local |
| [`toolchain-register`](toolchain-register.md) | no | Root command or compatibility entry point |
| [`toolchain-verify`](toolchain-verify.md) | no | Root command or compatibility entry point |
| [`triage`](triage.md) | yes | next |
| [`type`](type.md) | yes | propagate |
| [`verify-project`](verify-project.md) | no | Root command or compatibility entry point |
| [`vtable`](vtable.md) | yes | recover |
| [`windows`](windows.md) | yes | discover-ghidra, doctor, response-file |
| [`work-claim`](work-claim.md) | no | Root command or compatibility entry point |
| [`work-create`](work-create.md) | no | Root command or compatibility entry point |
| [`work-next`](work-next.md) | no | Root command or compatibility entry point |
| [`work-propose`](work-propose.md) | no | Root command or compatibility entry point |
| [`work-validate`](work-validate.md) | no | Root command or compatibility entry point |
| [`worker`](worker.md) | yes | doctor, list, register, select, status |
| [`worker-capabilities`](worker-capabilities.md) | no | Root command or compatibility entry point |
| [`workflow-init`](workflow-init.md) | no | Root command or compatibility entry point |
| [`workflow-show`](workflow-show.md) | no | Root command or compatibility entry point |
| [`workflow-update`](workflow-update.md) | no | Root command or compatibility entry point |
