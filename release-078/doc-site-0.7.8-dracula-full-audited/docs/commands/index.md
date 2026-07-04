---
title: Command Reference
description: Parser-derived x86decomp command coverage for v0.7.8.
---

# Command Reference

This reference is generated from the v0.7.8 command parser. It records parser surface, not inferred runtime success. A command's validation claim is limited to its report and inputs at runtime.

| Command | Usage | Canonical group |
| --- | --- | --- |
| [`x86decomp abi`](abi.md) | `usage: x86decomp abi [-h] [--project PROJECT] [--actor ACTOR] {compare,export,recover,shim,show,verify} ...` | yes |
| [`x86decomp abi-check`](abi-check.md) | `usage: x86decomp abi-check [-h] [--base BASE] [--report REPORT] code contract` | no |
| [`x86decomp angr-validate`](angr-validate.md) | `usage: x86decomp angr-validate [-h] [--architecture {x86,x86_64}] [--input-register INPUT_REGISTER] [--stack-argument-words STACK_ARGUMENT_WORDS] [--output-register OUTPUT_REGISTER] [--max-steps MAX_STEPS] [--max-paths MAX_PATHS] [--report REPORT] target candidate` | no |
| [`x86decomp artifact-import`](artifact-import.md) | `usage: x86decomp artifact-import [-h] project exported_dir` | no |
| [`x86decomp artifact-verify`](artifact-verify.md) | `usage: x86decomp artifact-verify [-h] artifact_dir` | no |
| [`x86decomp asm`](asm.md) | `usage: x86decomp asm [-h] [--project PROJECT] [--actor ACTOR] {annotate,batch,list,materialize,report,verify-roundtrip} ...` | yes |
| [`x86decomp asset`](asset.md) | `usage: x86decomp asset [-h] [--project PROJECT] [--actor ACTOR] {inventory} ...` | yes |
| [`x86decomp benchmark-run`](benchmark-run.md) | `usage: x86decomp benchmark-run [-h] [--report REPORT] manifest` | no |
| [`x86decomp boundary`](boundary.md) | `usage: x86decomp boundary [-h] [--project PROJECT] [--actor ACTOR] {audit,audit-project,export-ghidra-fixes,list,show} ...` | yes |
| [`x86decomp build`](build.md) | `usage: x86decomp build [-h] [--project PROJECT] [--actor ACTOR] {add-target,add-variant,compare-modes,create,generate,matrix,show,validate} ...` | yes |
| [`x86decomp campaign`](campaign.md) | `usage: x86decomp campaign [-h] [--project PROJECT] [--actor ACTOR] {branch,create,list,pause,plan,resume,snapshot,start,status,stop} ...` | yes |
| [`x86decomp candidate`](candidate.md) | `usage: x86decomp candidate [-h] [--project PROJECT] [--actor ACTOR] {add-file,compare,create,evaluate,list,promote,search,show,transition} ...` | yes |
| [`x86decomp capsule`](capsule.md) | `usage: x86decomp capsule [-h] [--project PROJECT] [--actor ACTOR] {create,inspect,reproduce,verify} ...` | yes |
| [`x86decomp changeset`](changeset.md) | `usage: x86decomp changeset [-h] [--project PROJECT] [--actor ACTOR] {add-operation,apply,conflicts,create,export,inspect,merge,rebase,show,verify} ...` | yes |
| [`x86decomp claim-attach`](claim-attach.md) | `usage: x86decomp claim-attach [-h] project claim_id evidence_id` | no |
| [`x86decomp claim-contradict`](claim-contradict.md) | `usage: x86decomp claim-contradict [-h] project claim_id evidence_id` | no |
| [`x86decomp claim-create`](claim-create.md) | `usage: x86decomp claim-create [-h] --subject SUBJECT --predicate PREDICATE --object OBJECT_VALUE [--evidence EVIDENCE] [--id ID] project` | no |
| [`x86decomp claim-verify`](claim-verify.md) | `usage: x86decomp claim-verify [-h] project claim_id` | no |
| [`x86decomp class`](class.md) | `usage: x86decomp class [-h] [--project PROJECT] [--actor ACTOR] {scaffold} ...` | yes |
| [`x86decomp coff-comdat-resolve`](coff-comdat-resolve.md) | `usage: x86decomp coff-comdat-resolve [-h] [--report REPORT] objects [objects ...]` | no |
| [`x86decomp coff-extract`](coff-extract.md) | `usage: x86decomp coff-extract [-h] [--size SIZE] object symbol output` | no |
| [`x86decomp coff-inspect`](coff-inspect.md) | `usage: x86decomp coff-inspect [-h] object` | no |
| [`x86decomp coff-synthesize`](coff-synthesize.md) | `usage: x86decomp coff-synthesize [-h] [--architecture {x86,x86_64}] [--relocations RELOCATIONS] code symbol output` | no |
| [`x86decomp commands`](commands.md) | `usage: x86decomp commands [-h] [--group {abi,asm,asset,boundary,build,campaign,candidate,capsule,changeset,class,compiler-rules,consensus,counterexample,decompiler,diff,family,function,game-pattern,ghidra-mcp,graph,headers,hybrid,hypothesis,image-text,library,llm,loop,match,mod,module,pattern,pe,playability,plugin,progress,project,proof,provenance,regression,release-policy,reloc,review,runtime,runtime-analysis,script-port,security,source,source-map,source-stage,staging,subsystem,tests,text-swap,toolchain,triage,type,vtable,windows,worker}] [--owner {governance,reconstruction,native,assembly}]` | no |
| [`x86decomp compile`](compile.md) | `usage: x86decomp compile [-h] [--report REPORT] [--extra-arg EXTRA_ARG] [--cache CACHE] profile source output` | no |
| [`x86decomp compile-worker`](compile-worker.md) | `usage: x86decomp compile-worker [-h] [--isolation {local_bounded,container}] [--container-image CONTAINER_IMAGE] [--cache CACHE] [--report REPORT] profile source output` | no |
| [`x86decomp compiler-lab`](compiler-lab.md) | `usage: x86decomp compiler-lab [-h] [--report REPORT] lab` | no |
| [`x86decomp compiler-rules`](compiler-rules.md) | `usage: x86decomp compiler-rules [-h] [--project PROJECT] [--actor ACTOR] {compare-flags,learn-rule,rule-report} ...` | yes |
| [`x86decomp consensus`](consensus.md) | `usage: x86decomp consensus [-h] [--project PROJECT] [--actor ACTOR] {conflicts,explain,record,resolve,scan} ...` | yes |
| [`x86decomp content-put`](content-put.md) | `usage: x86decomp content-put [-h] [--media-type MEDIA_TYPE] [--reference REFERENCE] [--kind KIND] [--owner OWNER] store file` | no |
| [`x86decomp content-verify`](content-verify.md) | `usage: x86decomp content-verify [-h] store` | no |
| [`x86decomp convergence-analyze`](convergence-analyze.md) | `usage: x86decomp convergence-analyze [-h] [--profile PROFILE] [--previous PREVIOUS] [--report REPORT] [--history HISTORY] reference candidate` | no |
| [`x86decomp corpus-build`](corpus-build.md) | `usage: x86decomp corpus-build [-h] [--report REPORT] manifest output_directory` | no |
| [`x86decomp corpus-compare`](corpus-compare.md) | `usage: x86decomp corpus-compare [-h] [--report REPORT] reports [reports ...]` | no |
| [`x86decomp corpus-create-manifest`](corpus-create-manifest.md) | `usage: x86decomp corpus-create-manifest [-h] repository output` | no |
| [`x86decomp corpus-generate`](corpus-generate.md) | `usage: x86decomp corpus-generate [-h] [--cases-per-family CASES_PER_FAMILY] [--seed SEED] [--c-only] [--cpp-only] [--report REPORT] output_directory` | no |
| [`x86decomp corpus-generated-verify`](corpus-generated-verify.md) | `usage: x86decomp corpus-generated-verify [-h] report` | no |
| [`x86decomp corpus-verify`](corpus-verify.md) | `usage: x86decomp corpus-verify [-h] report` | no |
| [`x86decomp counterexample`](counterexample.md) | `usage: x86decomp counterexample [-h] [--project PROJECT] [--actor ACTOR] {add,list,promote,show} ...` | yes |
| [`x86decomp cpp-recover`](cpp-recover.md) | `usage: x86decomp cpp-recover [-h] [--metadata-report METADATA_REPORT] [--object OBJECT] [--map MAP] [--report REPORT] pe` | no |
| [`x86decomp crosscheck-ghidra`](crosscheck-ghidra.md) | `usage: x86decomp crosscheck-ghidra [-h] --base BASE [--architecture {x86,x86_64}] [--report REPORT] instructions_jsonl code` | no |
| [`x86decomp db-constraint-accept`](db-constraint-accept.md) | `usage: x86decomp db-constraint-accept [-h] database constraint_id` | no |
| [`x86decomp db-constraint-add`](db-constraint-add.md) | `usage: x86decomp db-constraint-add [-h] [--evidence-id EVIDENCE_ID] [--confidence CONFIDENCE] database subject relation object_value provenance` | no |
| [`x86decomp db-constraint-conflicts`](db-constraint-conflicts.md) | `usage: x86decomp db-constraint-conflicts [-h] database subject relation` | no |
| [`x86decomp db-ingest`](db-ingest.md) | `usage: x86decomp db-ingest [-h] [--image-base IMAGE_BASE] database artifact` | no |
| [`x86decomp db-query`](db-query.md) | `usage: x86decomp db-query [-h] [--parameters-json PARAMETERS_JSON] database sql` | no |
| [`x86decomp decompiler`](decompiler.md) | `usage: x86decomp decompiler [-h] [--project PROJECT] [--actor ACTOR] {cleanup} ...` | yes |
| [`x86decomp decompme-pack`](decompme-pack.md) | `usage: x86decomp decompme-pack [-h] [--overwrite] artifact_dir output_dir` | no |
| [`x86decomp dependency-audit`](dependency-audit.md) | `usage: x86decomp dependency-audit [-h] [--executable EXECUTABLE] [--timeout TIMEOUT] [--report REPORT]` | no |
| [`x86decomp diff`](diff.md) | `usage: x86decomp diff [-h] [--project PROJECT] [--actor ACTOR] {explain} ...` | yes |
| [`x86decomp diff-bytes`](diff-bytes.md) | `usage: x86decomp diff-bytes [-h] [--report REPORT] [--max-mismatches MAX_MISMATCHES] target candidate` | no |
| [`x86decomp diff-function`](diff-function.md) | `usage: x86decomp diff-function [-h] [--report REPORT] pe rva size coff symbol` | no |
| [`x86decomp disassemble`](disassemble.md) | `usage: x86decomp disassemble [-h] [--base BASE] [--architecture {x86,x86_64}] [--report REPORT] code` | no |
| [`x86decomp drcov-parse`](drcov-parse.md) | `usage: x86decomp drcov-parse [-h] log` | no |
| [`x86decomp drcov-run`](drcov-run.md) | `usage: x86decomp drcov-run [-h] [--drrun DRRUN] [--program-arg PROGRAM_ARG] [--timeout TIMEOUT] [--report REPORT] executable output_directory` | no |
| [`x86decomp dynamic-validate`](dynamic-validate.md) | `usage: x86decomp dynamic-validate [-h] [--target-base TARGET_BASE] [--candidate-base CANDIDATE_BASE] [--report REPORT] target candidate harness` | no |
| [`x86decomp evidence-add`](evidence-add.md) | `usage: x86decomp evidence-add [-h] --kind {binary_bytes,static_analysis,dynamic_trace,compiler_output,debug_symbol,external_document,human_review} --source SOURCE --locator LOCATOR --assertion ASSERTION --independent-group INDEPENDENT_GROUP [--file FILE] [--id ID] project` | no |
| [`x86decomp family`](family.md) | `usage: x86decomp family [-h] [--project PROJECT] [--actor ACTOR] {add,correlate,create,report} ...` | yes |
| [`x86decomp function`](function.md) | `usage: x86decomp function [-h] [--project PROJECT] [--actor ACTOR] {classify,discover,reconcile,sort} ...` | yes |
| [`x86decomp game-pattern`](game-pattern.md) | `usage: x86decomp game-pattern [-h] [--project PROJECT] [--actor ACTOR] {state-machine} ...` | yes |
| [`x86decomp ghidra-export`](ghidra-export.md) | `usage: x86decomp ghidra-export [-h] [--scripts-dir SCRIPTS_DIR] [--ghidra-home GHIDRA_HOME] [--overwrite] [--selector SELECTOR] [--timeout TIMEOUT] [--report REPORT] [--print-command] binary ghidra_project_dir ghidra_project_name output_dir` | no |
| [`x86decomp ghidra-mcp`](ghidra-mcp.md) | `usage: x86decomp ghidra-mcp [-h] [--project PROJECT] [--actor ACTOR] {batch-decompile,decompile,functions,probe,sync-names} ...` | yes |
| [`x86decomp graph`](graph.md) | `usage: x86decomp graph [-h] [--project PROJECT] [--actor ACTOR] {edge,impact,node} ...` | yes |
| [`x86decomp harness-generate`](harness-generate.md) | `usage: x86decomp harness-generate [-h] [--pointer-parameters POINTER_PARAMETERS] [--no-observe-pointers] [--max-instructions MAX_INSTRUCTIONS] [--timeout-ms TIMEOUT_MS] abi_contract output` | no |
| [`x86decomp headers`](headers.md) | `usage: x86decomp headers [-h] [--project PROJECT] [--actor ACTOR] {create,cycles,declare,explain,include,synthesize,synthesize-project,validate} ...` | yes |
| [`x86decomp hybrid`](hybrid.md) | `usage: x86decomp hybrid [-h] [--project PROJECT] [--actor ACTOR] {compose,generate,verify} ...` | yes |
| [`x86decomp hybrid-generate`](hybrid-generate.md) | `usage: x86decomp hybrid-generate [-h] [--architecture {x86,x86_64}] [--asm-format {bytes,annotated,mnemonic}] [--image-base IMAGE_BASE] [--assembler-command-json ASSEMBLER_COMMAND_JSON] [--symbol-map SYMBOL_MAP] [--overwrite] project output` | no |
| [`x86decomp hypothesis`](hypothesis.md) | `usage: x86decomp hypothesis [-h] [--project PROJECT] [--actor ACTOR] {create,dependency,evidence,gate,list,show,transition} ...` | yes |
| [`x86decomp image-match`](image-match.md) | `usage: x86decomp image-match [-h] [--profile PROFILE] [--report REPORT] reference candidate` | no |
| [`x86decomp image-profile`](image-profile.md) | `usage: x86decomp image-profile [-h] reference output` | no |
| [`x86decomp image-text`](image-text.md) | `usage: x86decomp image-text [-h] [--project PROJECT] [--actor ACTOR] {compose} ...` | yes |
| [`x86decomp init`](init.md) | `usage: x86decomp init [-h] [--reference-binary] binary project` | no |
| [`x86decomp inspect-pe`](inspect-pe.md) | `usage: x86decomp inspect-pe [-h] binary` | no |
| [`x86decomp integration-run`](integration-run.md) | `usage: x86decomp integration-run [-h] [--allow-host-execution] [--report REPORT] manifest` | no |
| [`x86decomp layout-reconstruct`](layout-reconstruct.md) | `usage: x86decomp layout-reconstruct [-h] [--report REPORT] pe map [objects ...]` | no |
| [`x86decomp lib-inspect`](lib-inspect.md) | `usage: x86decomp lib-inspect [-h] library` | no |
| [`x86decomp library`](library.md) | `usage: x86decomp library [-h] [--project PROJECT] [--actor ACTOR] {accept,candidates,externalize,identify,reconstruct,reject} ...` | yes |
| [`x86decomp linker-plan`](linker-plan.md) | `usage: x86decomp linker-plan [-h] [--library LIBRARY] [--linker LINKER] [--output-image OUTPUT_IMAGE] [--report REPORT] [--write-relink-manifest WRITE_RELINK_MANIFEST] pe map objects [objects ...]` | no |
| [`x86decomp llm`](llm.md) | `usage: x86decomp llm [-h] [--project PROJECT] [--actor ACTOR] {batch-create,batch-match,cpp-generate,generate,job-create,job-from-range,match,probe,profile-create,profile-validate,prompt,providers,verify} ...` | yes |
| [`x86decomp loop`](loop.md) | `usage: x86decomp loop [-h] [--project PROJECT] [--actor ACTOR] {list,run,show} ...` | yes |
| [`x86decomp map-inspect`](map-inspect.md) | `usage: x86decomp map-inspect [-h] map` | no |
| [`x86decomp match`](match.md) | `usage: x86decomp match [-h] [--project PROJECT] [--actor ACTOR] {batch,compare,mismatches,report} ...` | yes |
| [`x86decomp mcp-commit`](mcp-commit.md) | `usage: x86decomp mcp-commit [-h] [--url URL] [--command-json COMMAND_JSON] --allow-tool ALLOW_TOOL project approval_hash` | no |
| [`x86decomp mcp-propose`](mcp-propose.md) | `usage: x86decomp mcp-propose [-h] [--url URL] [--command-json COMMAND_JSON] --allow-tool ALLOW_TOOL --rationale RATIONALE --evidence EVIDENCE project tool arguments` | no |
| [`x86decomp mcp-read`](mcp-read.md) | `usage: x86decomp mcp-read [-h] [--url URL] [--command-json COMMAND_JSON] project tool arguments` | no |
| [`x86decomp mcp-tools`](mcp-tools.md) | `usage: x86decomp mcp-tools [-h] [--url URL] [--command-json COMMAND_JSON]` | no |
| [`x86decomp memory-add`](memory-add.md) | `usage: x86decomp memory-add [-h] --actor ACTOR --category CATEGORY --summary SUMMARY [--details-json DETAILS_JSON] [--evidence EVIDENCE] project` | no |
| [`x86decomp memory-render`](memory-render.md) | `usage: x86decomp memory-render [-h] project` | no |
| [`x86decomp memory-verify`](memory-verify.md) | `usage: x86decomp memory-verify [-h] project` | no |
| [`x86decomp metadata-scan`](metadata-scan.md) | `usage: x86decomp metadata-scan [-h] [--object OBJECT] [--map MAP] [--report REPORT] pe` | no |
| [`x86decomp mod`](mod.md) | `usage: x86decomp mod [-h] [--project PROJECT] [--actor ACTOR] {branch-init} ...` | yes |
| [`x86decomp module`](module.md) | `usage: x86decomp module [-h] [--project PROJECT] [--actor ACTOR] {add-member,add-unit-member,assign,create,create-unit,list,show,show-unit,suggest} ...` | yes |
| [`x86decomp objdiff-run`](objdiff-run.md) | `usage: x86decomp objdiff-run [-h] [--report REPORT] manifest` | no |
| [`x86decomp patch-image`](patch-image.md) | `usage: x86decomp patch-image [-h] --rva RVA [--expected-original-sha256 EXPECTED_ORIGINAL_SHA256] [--expected-function-sha256 EXPECTED_FUNCTION_SHA256] [--report REPORT] original candidate output` | no |
| [`x86decomp pattern`](pattern.md) | `usage: x86decomp pattern [-h] [--project PROJECT] [--actor ACTOR] {catalog,generate,match,promote,scan} ...` | yes |
| [`x86decomp pdb-inspect`](pdb-inspect.md) | `usage: x86decomp pdb-inspect [-h] [--pe PE] pdb` | no |
| [`x86decomp pe`](pe.md) | `usage: x86decomp pe [-h] [--project PROJECT] [--actor ACTOR] {export-coff,export-sections,inventory,patch-apply,patch-plan,text-swap} ...` | yes |
| [`x86decomp pipeline-cancel`](pipeline-cancel.md) | `usage: x86decomp pipeline-cancel [-h] [--stage-id STAGE_ID] project pipeline_id` | no |
| [`x86decomp pipeline-create`](pipeline-create.md) | `usage: x86decomp pipeline-create [-h] [--without-ghidra] project output` | no |
| [`x86decomp pipeline-recover`](pipeline-recover.md) | `usage: x86decomp pipeline-recover [-h] [--pipeline-id PIPELINE_ID] [--stale-seconds STALE_SECONDS] project` | no |
| [`x86decomp pipeline-retry`](pipeline-retry.md) | `usage: x86decomp pipeline-retry [-h] [--cascade] project pipeline_id stage_id` | no |
| [`x86decomp pipeline-run`](pipeline-run.md) | `usage: x86decomp pipeline-run [-h] [--continue-on-failure] project manifest` | no |
| [`x86decomp pipeline-status`](pipeline-status.md) | `usage: x86decomp pipeline-status [-h] project pipeline_id` | no |
| [`x86decomp playability`](playability.md) | `usage: x86decomp playability [-h] [--project PROJECT] [--actor ACTOR] {smoke-plan} ...` | yes |
| [`x86decomp plugin`](plugin.md) | `usage: x86decomp plugin [-h] [--project PROJECT] [--actor ACTOR] {doctor,install,invoke,list,validate} ...` | yes |
| [`x86decomp progress`](progress.md) | `usage: x86decomp progress [-h] [--project PROJECT] [--actor ACTOR] {reconcile} ...` | yes |
| [`x86decomp project`](project.md) | `usage: x86decomp project [-h] [--project PROJECT] [--actor ACTOR] {check,doctor-paths,explain-boundaries,export,health,init,synthesize-layout} ...` | yes |
| [`x86decomp project-backup`](project-backup.md) | `usage: x86decomp project-backup [-h] project output` | no |
| [`x86decomp project-check`](project-check.md) | `usage: x86decomp project-check [-h] project` | no |
| [`x86decomp project-from-target`](project-from-target.md) | `usage: x86decomp project-from-target [-h] [--reference-binary] target_pack project` | no |
| [`x86decomp project-gc`](project-gc.md) | `usage: x86decomp project-gc [-h] [--apply] project` | no |
| [`x86decomp project-migrate`](project-migrate.md) | `usage: x86decomp project-migrate [-h] [--dry-run] [--backup BACKUP] project` | no |
| [`x86decomp project-repair`](project-repair.md) | `usage: x86decomp project-repair [-h] [--apply] project` | no |
| [`x86decomp project-restore`](project-restore.md) | `usage: x86decomp project-restore [-h] archive destination` | no |
| [`x86decomp proof`](proof.md) | `usage: x86decomp proof [-h] [--project PROJECT] [--actor ACTOR] {evaluate,export,inspect,obligation,result,verify} ...` | yes |
| [`x86decomp provenance`](provenance.md) | `usage: x86decomp provenance [-h] [--project PROJECT] [--actor ACTOR] {binary,export,record,source} ...` | yes |
| [`x86decomp regression`](regression.md) | `usage: x86decomp regression [-h] [--project PROJECT] [--actor ACTOR] {compare} ...` | yes |
| [`x86decomp release-gate`](release-gate.md) | `usage: x86decomp release-gate [-h] [--reproduction-manifest REPRODUCTION_MANIFEST] [--security-report SECURITY_REPORT] [--convergence-report CONVERGENCE_REPORT] [--require-workflows] [--require-verified-claims] [--require-succeeded-pipelines] [--report REPORT] project` | no |
| [`x86decomp release-manifest-verify`](release-manifest-verify.md) | `usage: x86decomp release-manifest-verify [-h] [--manifest MANIFEST] root` | no |
| [`x86decomp release-policy`](release-policy.md) | `usage: x86decomp release-policy [-h] [--project PROJECT] [--actor ACTOR] {moddable-source} ...` | yes |
| [`x86decomp relink`](relink.md) | `usage: x86decomp relink [-h] [--report REPORT] manifest` | no |
| [`x86decomp reloc`](reloc.md) | `usage: x86decomp reloc [-h] [--project PROJECT] [--actor ACTOR] {inspect,resolve,supported} ...` | yes |
| [`x86decomp reproduce-create`](reproduce-create.md) | `usage: x86decomp reproduce-create [-h] [--required-tool REQUIRED_TOOL] project output` | no |
| [`x86decomp reproduce-verify`](reproduce-verify.md) | `usage: x86decomp reproduce-verify [-h] project manifest` | no |
| [`x86decomp review`](review.md) | `usage: x86decomp review [-h] [--project PROJECT] [--actor ACTOR] {assign,create,decide,list,lock,show} ...` | yes |
| [`x86decomp runtime`](runtime.md) | `usage: x86decomp runtime [-h] [--project PROJECT] [--actor ACTOR] {launch,map-crash,validate-image} ...` | yes |
| [`x86decomp runtime-analysis`](runtime-analysis.md) | `usage: x86decomp runtime-analysis [-h] [--project PROJECT] [--actor ACTOR] {identify,match-library,quarantine} ...` | yes |
| [`x86decomp sbom-generate`](sbom-generate.md) | `usage: x86decomp sbom-generate [-h] output` | no |
| [`x86decomp script-port`](script-port.md) | `usage: x86decomp script-port [-h] [--project PROJECT] [--actor ACTOR] {audit} ...` | yes |
| [`x86decomp security`](security.md) | `usage: x86decomp security [-h] [--project PROJECT] [--actor ACTOR] {finding,policy,report,scan} ...` | yes |
| [`x86decomp security-audit`](security-audit.md) | `usage: x86decomp security-audit [-h] [--report REPORT] root` | no |
| [`x86decomp serve`](serve.md) | `usage: x86decomp serve [-h] [--host HOST] [--port PORT] project` | no |
| [`x86decomp snapshot-tools`](snapshot-tools.md) | `usage: x86decomp snapshot-tools [-h] [--output OUTPUT] [--ghidra-home GHIDRA_HOME]` | no |
| [`x86decomp source`](source.md) | `usage: x86decomp source [-h] [--project PROJECT] [--actor ACTOR] {impact,lock,reconcile,unlock} ...` | yes |
| [`x86decomp source-map`](source-map.md) | `usage: x86decomp source-map [-h] [--project PROJECT] [--actor ACTOR] {annotate,verify} ...` | yes |
| [`x86decomp source-stage`](source-stage.md) | `usage: x86decomp source-stage [-h] [--project PROJECT] [--actor ACTOR] {classify} ...` | yes |
| [`x86decomp staging`](staging.md) | `usage: x86decomp staging [-h] [--project PROJECT] [--actor ACTOR] {compile-check,generate-context,resolve,scan,unresolved} ...` | yes |
| [`x86decomp subsystem`](subsystem.md) | `usage: x86decomp subsystem [-h] [--project PROJECT] [--actor ACTOR] {detect} ...` | yes |
| [`x86decomp symbolic-memory-validate`](symbolic-memory-validate.md) | `usage: x86decomp symbolic-memory-validate [-h] [--report REPORT] target candidate harness` | no |
| [`x86decomp symbolic-validate`](symbolic-validate.md) | `usage: x86decomp symbolic-validate [-h] [--architecture {x86,x86_64}] [--input-register INPUT_REGISTER] [--stack-argument-words STACK_ARGUMENT_WORDS] [--output-register OUTPUT_REGISTER] [--max-steps MAX_STEPS] [--max-paths MAX_PATHS] [--report REPORT] target candidate` | no |
| [`x86decomp target-pack-infer`](target-pack-infer.md) | `usage: x86decomp target-pack-infer [-h] [--name NAME] [--pdb PDB] [--map MAP] [--object OBJECT] [--library LIBRARY] [--rebuilt-image REBUILT_IMAGE] [--decisions DECISIONS] [--reference-artifacts] primary_image output_directory` | no |
| [`x86decomp target-pack-verify`](target-pack-verify.md) | `usage: x86decomp target-pack-verify [-h] target_pack` | no |
| [`x86decomp template-derive`](template-derive.md) | `usage: x86decomp template-derive [-h] target_pack` | no |
| [`x86decomp template-materialize`](template-materialize.md) | `usage: x86decomp template-materialize [-h] project` | no |
| [`x86decomp test-bundle-create`](test-bundle-create.md) | `usage: x86decomp test-bundle-create [-h] --artifact ARTIFACT --authorization AUTHORIZATION [--name NAME] [--description DESCRIPTION] [--expected-architecture {x86,x86_64}] output` | no |
| [`x86decomp test-bundle-inspect`](test-bundle-inspect.md) | `usage: x86decomp test-bundle-inspect [-h] [--report REPORT] bundle` | no |
| [`x86decomp tests`](tests.md) | `usage: x86decomp tests [-h] [--project PROJECT] [--actor ACTOR] {add,explain,list,promote-counterexample,synthesize} ...` | yes |
| [`x86decomp text-swap`](text-swap.md) | `usage: x86decomp text-swap [-h] [--project PROJECT] [--actor ACTOR] {build,inject,plan,verify} ...` | yes |
| [`x86decomp toolchain`](toolchain.md) | `usage: x86decomp toolchain [-h] [--project PROJECT] [--actor ACTOR] {hash-tree,redact-package,verify-local} ...` | yes |
| [`x86decomp toolchain-register`](toolchain-register.md) | `usage: x86decomp toolchain-register [-h] --executable EXECUTABLE registry toolchain_id family version` | no |
| [`x86decomp toolchain-verify`](toolchain-verify.md) | `usage: x86decomp toolchain-verify [-h] registry toolchain_id` | no |
| [`x86decomp triage`](triage.md) | `usage: x86decomp triage [-h] [--project PROJECT] [--actor ACTOR] {next} ...` | yes |
| [`x86decomp type`](type.md) | `usage: x86decomp type [-h] [--project PROJECT] [--actor ACTOR] {propagate} ...` | yes |
| [`x86decomp verify-project`](verify-project.md) | `usage: x86decomp verify-project [-h] project` | no |
| [`x86decomp vtable`](vtable.md) | `usage: x86decomp vtable [-h] [--project PROJECT] [--actor ACTOR] {recover} ...` | yes |
| [`x86decomp windows`](windows.md) | `usage: x86decomp windows [-h] [--project PROJECT] [--actor ACTOR] {discover-ghidra,doctor,response-file} ...` | yes |
| [`x86decomp work-claim`](work-claim.md) | `usage: x86decomp work-claim [-h] database task_id assignee` | no |
| [`x86decomp work-create`](work-create.md) | `usage: x86decomp work-create [-h] --validator VALIDATOR [--priority PRIORITY] database function_id {matching,functional} kind instructions` | no |
| [`x86decomp work-next`](work-next.md) | `usage: x86decomp work-next [-h] [--mode {matching,functional}] database` | no |
| [`x86decomp work-propose`](work-propose.md) | `usage: x86decomp work-propose [-h] --evidence EVIDENCE database task_id proposal` | no |
| [`x86decomp work-validate`](work-validate.md) | `usage: x86decomp work-validate [-h] [--passed] database task_id validator report_path` | no |
| [`x86decomp worker`](worker.md) | `usage: x86decomp worker [-h] [--project PROJECT] [--actor ACTOR] {doctor,list,register,select,status} ...` | yes |
| [`x86decomp worker-capabilities`](worker-capabilities.md) | `usage: x86decomp worker-capabilities [-h]` | no |
| [`x86decomp workflow-init`](workflow-init.md) | `usage: x86decomp workflow-init [-h] [--mode {matching,functional}] project function_id` | no |
| [`x86decomp workflow-show`](workflow-show.md) | `usage: x86decomp workflow-show [-h] project function_id` | no |
| [`x86decomp workflow-update`](workflow-update.md) | `usage: x86decomp workflow-update [-h] [--source-stage {original_bytes,generated_assembly,decompiler_candidate,human_candidate,accepted_source}] [--matching-status {not_started,decompiled,compiles,abi_compatible,instruction_similar,byte_matched,image_integrated,full_relink_validated,blocked}] [--functional-status {not_started,decompiled,compiles,abi_compatible,differentially_validated,symbolically_bounded,integration_validated,blocked}] [--candidate CANDIDATE] [--compiler-profile COMPILER_PROFILE] [--report-kind REPORT_KIND] [--report-path REPORT_PATH] [--blocker BLOCKER] [--allow-regression] project function_id` | no |
