---
title: Command Reference
description: Exact v0.7.8 parser-derived command reference.
---


# Command Reference

This section is regenerated from the live v0.7.8 toolkit parser and the v0.7.8 verification harness parser.

## Toolkit command pages

| Command page | Action count |
| --- | --- |
| [`x86decomp abi`](abi.md) | 6 |
| [`x86decomp abi-check`](abi-check.md) | 0 |
| [`x86decomp angr-validate`](angr-validate.md) | 0 |
| [`x86decomp artifact-import`](artifact-import.md) | 0 |
| [`x86decomp artifact-verify`](artifact-verify.md) | 0 |
| [`x86decomp asm`](asm.md) | 6 |
| [`x86decomp asset`](asset.md) | 1 |
| [`x86decomp benchmark-run`](benchmark-run.md) | 0 |
| [`x86decomp boundary`](boundary.md) | 5 |
| [`x86decomp build`](build.md) | 8 |
| [`x86decomp campaign`](campaign.md) | 10 |
| [`x86decomp candidate`](candidate.md) | 9 |
| [`x86decomp capsule`](capsule.md) | 4 |
| [`x86decomp changeset`](changeset.md) | 10 |
| [`x86decomp claim-attach`](claim-attach.md) | 0 |
| [`x86decomp claim-contradict`](claim-contradict.md) | 0 |
| [`x86decomp claim-create`](claim-create.md) | 0 |
| [`x86decomp claim-verify`](claim-verify.md) | 0 |
| [`x86decomp class`](class.md) | 1 |
| [`x86decomp coff-comdat-resolve`](coff-comdat-resolve.md) | 0 |
| [`x86decomp coff-extract`](coff-extract.md) | 0 |
| [`x86decomp coff-inspect`](coff-inspect.md) | 0 |
| [`x86decomp coff-synthesize`](coff-synthesize.md) | 0 |
| [`x86decomp commands`](commands.md) | 0 |
| [`x86decomp compile`](compile.md) | 0 |
| [`x86decomp compile-worker`](compile-worker.md) | 0 |
| [`x86decomp compiler-lab`](compiler-lab.md) | 0 |
| [`x86decomp compiler-rules`](compiler-rules.md) | 3 |
| [`x86decomp consensus`](consensus.md) | 5 |
| [`x86decomp content-put`](content-put.md) | 0 |
| [`x86decomp content-verify`](content-verify.md) | 0 |
| [`x86decomp convergence-analyze`](convergence-analyze.md) | 0 |
| [`x86decomp corpus-build`](corpus-build.md) | 0 |
| [`x86decomp corpus-compare`](corpus-compare.md) | 0 |
| [`x86decomp corpus-create-manifest`](corpus-create-manifest.md) | 0 |
| [`x86decomp corpus-generate`](corpus-generate.md) | 0 |
| [`x86decomp corpus-generated-verify`](corpus-generated-verify.md) | 0 |
| [`x86decomp corpus-verify`](corpus-verify.md) | 0 |
| [`x86decomp counterexample`](counterexample.md) | 4 |
| [`x86decomp cpp-recover`](cpp-recover.md) | 0 |
| [`x86decomp crosscheck-ghidra`](crosscheck-ghidra.md) | 0 |
| [`x86decomp db-constraint-accept`](db-constraint-accept.md) | 0 |
| [`x86decomp db-constraint-add`](db-constraint-add.md) | 0 |
| [`x86decomp db-constraint-conflicts`](db-constraint-conflicts.md) | 0 |
| [`x86decomp db-ingest`](db-ingest.md) | 0 |
| [`x86decomp db-query`](db-query.md) | 0 |
| [`x86decomp decompiler`](decompiler.md) | 1 |
| [`x86decomp decompme-pack`](decompme-pack.md) | 0 |
| [`x86decomp dependency-audit`](dependency-audit.md) | 0 |
| [`x86decomp diff`](diff.md) | 1 |
| [`x86decomp diff-bytes`](diff-bytes.md) | 0 |
| [`x86decomp diff-function`](diff-function.md) | 0 |
| [`x86decomp disassemble`](disassemble.md) | 0 |
| [`x86decomp drcov-parse`](drcov-parse.md) | 0 |
| [`x86decomp drcov-run`](drcov-run.md) | 0 |
| [`x86decomp dynamic-validate`](dynamic-validate.md) | 0 |
| [`x86decomp evidence-add`](evidence-add.md) | 0 |
| [`x86decomp family`](family.md) | 4 |
| [`x86decomp function`](function.md) | 4 |
| [`x86decomp game-pattern`](game-pattern.md) | 1 |
| [`x86decomp ghidra-export`](ghidra-export.md) | 0 |
| [`x86decomp ghidra-mcp`](ghidra-mcp.md) | 5 |
| [`x86decomp graph`](graph.md) | 3 |
| [`x86decomp harness-generate`](harness-generate.md) | 0 |
| [`x86decomp headers`](headers.md) | 8 |
| [`x86decomp hybrid`](hybrid.md) | 3 |
| [`x86decomp hybrid-generate`](hybrid-generate.md) | 0 |
| [`x86decomp hypothesis`](hypothesis.md) | 7 |
| [`x86decomp image-match`](image-match.md) | 0 |
| [`x86decomp image-profile`](image-profile.md) | 0 |
| [`x86decomp image-text`](image-text.md) | 1 |
| [`x86decomp init`](init.md) | 0 |
| [`x86decomp inspect-pe`](inspect-pe.md) | 0 |
| [`x86decomp integration-run`](integration-run.md) | 0 |
| [`x86decomp layout-reconstruct`](layout-reconstruct.md) | 0 |
| [`x86decomp lib-inspect`](lib-inspect.md) | 0 |
| [`x86decomp library`](library.md) | 6 |
| [`x86decomp linker-plan`](linker-plan.md) | 0 |
| [`x86decomp llm`](llm.md) | 13 |
| [`x86decomp loop`](loop.md) | 3 |
| [`x86decomp map-inspect`](map-inspect.md) | 0 |
| [`x86decomp match`](match.md) | 4 |
| [`x86decomp mcp-commit`](mcp-commit.md) | 0 |
| [`x86decomp mcp-propose`](mcp-propose.md) | 0 |
| [`x86decomp mcp-read`](mcp-read.md) | 0 |
| [`x86decomp mcp-tools`](mcp-tools.md) | 0 |
| [`x86decomp memory-add`](memory-add.md) | 0 |
| [`x86decomp memory-render`](memory-render.md) | 0 |
| [`x86decomp memory-verify`](memory-verify.md) | 0 |
| [`x86decomp metadata-scan`](metadata-scan.md) | 0 |
| [`x86decomp mod`](mod.md) | 1 |
| [`x86decomp module`](module.md) | 9 |
| [`x86decomp objdiff-run`](objdiff-run.md) | 0 |
| [`x86decomp patch-image`](patch-image.md) | 0 |
| [`x86decomp pattern`](pattern.md) | 5 |
| [`x86decomp pdb-inspect`](pdb-inspect.md) | 0 |
| [`x86decomp pe`](pe.md) | 6 |
| [`x86decomp pipeline-cancel`](pipeline-cancel.md) | 0 |
| [`x86decomp pipeline-create`](pipeline-create.md) | 0 |
| [`x86decomp pipeline-recover`](pipeline-recover.md) | 0 |
| [`x86decomp pipeline-retry`](pipeline-retry.md) | 0 |
| [`x86decomp pipeline-run`](pipeline-run.md) | 0 |
| [`x86decomp pipeline-status`](pipeline-status.md) | 0 |
| [`x86decomp playability`](playability.md) | 1 |
| [`x86decomp plugin`](plugin.md) | 5 |
| [`x86decomp progress`](progress.md) | 1 |
| [`x86decomp project`](project.md) | 7 |
| [`x86decomp project-backup`](project-backup.md) | 0 |
| [`x86decomp project-check`](project-check.md) | 0 |
| [`x86decomp project-from-target`](project-from-target.md) | 0 |
| [`x86decomp project-gc`](project-gc.md) | 0 |
| [`x86decomp project-migrate`](project-migrate.md) | 0 |
| [`x86decomp project-repair`](project-repair.md) | 0 |
| [`x86decomp project-restore`](project-restore.md) | 0 |
| [`x86decomp proof`](proof.md) | 6 |
| [`x86decomp provenance`](provenance.md) | 4 |
| [`x86decomp regression`](regression.md) | 1 |
| [`x86decomp release-gate`](release-gate.md) | 0 |
| [`x86decomp release-manifest-verify`](release-manifest-verify.md) | 0 |
| [`x86decomp release-policy`](release-policy.md) | 1 |
| [`x86decomp relink`](relink.md) | 0 |
| [`x86decomp reloc`](reloc.md) | 3 |
| [`x86decomp reproduce-create`](reproduce-create.md) | 0 |
| [`x86decomp reproduce-verify`](reproduce-verify.md) | 0 |
| [`x86decomp review`](review.md) | 6 |
| [`x86decomp runtime`](runtime.md) | 3 |
| [`x86decomp runtime-analysis`](runtime-analysis.md) | 3 |
| [`x86decomp sbom-generate`](sbom-generate.md) | 0 |
| [`x86decomp script-port`](script-port.md) | 1 |
| [`x86decomp security`](security.md) | 4 |
| [`x86decomp security-audit`](security-audit.md) | 0 |
| [`x86decomp serve`](serve.md) | 0 |
| [`x86decomp snapshot-tools`](snapshot-tools.md) | 0 |
| [`x86decomp source`](source.md) | 4 |
| [`x86decomp source-map`](source-map.md) | 2 |
| [`x86decomp source-stage`](source-stage.md) | 1 |
| [`x86decomp staging`](staging.md) | 5 |
| [`x86decomp subsystem`](subsystem.md) | 1 |
| [`x86decomp symbolic-memory-validate`](symbolic-memory-validate.md) | 0 |
| [`x86decomp symbolic-validate`](symbolic-validate.md) | 0 |
| [`x86decomp target-pack-infer`](target-pack-infer.md) | 0 |
| [`x86decomp target-pack-verify`](target-pack-verify.md) | 0 |
| [`x86decomp template-derive`](template-derive.md) | 0 |
| [`x86decomp template-materialize`](template-materialize.md) | 0 |
| [`x86decomp test-bundle-create`](test-bundle-create.md) | 0 |
| [`x86decomp test-bundle-inspect`](test-bundle-inspect.md) | 0 |
| [`x86decomp tests`](tests.md) | 5 |
| [`x86decomp text-swap`](text-swap.md) | 4 |
| [`x86decomp toolchain`](toolchain.md) | 3 |
| [`x86decomp toolchain-register`](toolchain-register.md) | 0 |
| [`x86decomp toolchain-verify`](toolchain-verify.md) | 0 |
| [`x86decomp triage`](triage.md) | 1 |
| [`x86decomp type`](type.md) | 1 |
| [`x86decomp verify-project`](verify-project.md) | 0 |
| [`x86decomp vtable`](vtable.md) | 1 |
| [`x86decomp windows`](windows.md) | 3 |
| [`x86decomp work-claim`](work-claim.md) | 0 |
| [`x86decomp work-create`](work-create.md) | 0 |
| [`x86decomp work-next`](work-next.md) | 0 |
| [`x86decomp work-propose`](work-propose.md) | 0 |
| [`x86decomp work-validate`](work-validate.md) | 0 |
| [`x86decomp worker`](worker.md) | 5 |
| [`x86decomp worker-capabilities`](worker-capabilities.md) | 0 |
| [`x86decomp workflow-init`](workflow-init.md) | 0 |
| [`x86decomp workflow-show`](workflow-show.md) | 0 |
| [`x86decomp workflow-update`](workflow-update.md) | 0 |

## Verification harness

- [`x86decomp-test`](x86decomp-test.md)

