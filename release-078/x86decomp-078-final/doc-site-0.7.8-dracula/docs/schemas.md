---
title: JSON Schemas
description: Complete source-derived JSON Schema inventory.
---

# All 97 JSON Schemas

Each entry is read from the current schema file. Missing titles or descriptions are identified rather than inferred.

<a id="schema-abi-contract-schema-json"></a>

## `abi-contract.schema.json`

x86decomp ABI contract

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:abi-contract:1`
- **Top-level type:** `object`
- **Required fields:** `architecture`, `convention`
- **Top-level properties:** `architecture`, `callee_stack_cleanup`, `convention`, `floating_point`, `register_arguments`, `return_registers`, `stack_argument_bytes`, `structure_return`, `this_register`, `variadic`

SHA-256: `536e89f5ab760329f3799138b17c8a321170fc1fc729528d97b7f75d4af96c76`

<a id="schema-assembly-asm-function-schema-json"></a>

## `assembly/asm-function.schema.json`

v0.7.8 function assembly result

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.local/schemas/assembly/asm-function.schema.json`
- **Top-level type:** `object`
- **Required fields:** `function_id`, `symbol`, `rva`, `format`, `classification`, `exact_match`, `input_sha256`, `source_sha256`
- **Top-level properties:** `byte_escape_count`, `classification`, `exact_match`, `format`, `function_id`, `input_sha256`, `instruction_count`, `mnemonic_count`, `relocation_count`, `resolved_relocation_count`, `rva`, `source_sha256`, `symbol`, `unresolved_relocation_count`

SHA-256: `309919f4585a49208b88562ed6a97ca7a47ede3ca0a26cdb8a7d4d454eac1478`

<a id="schema-assembly-asm-run-schema-json"></a>

## `assembly/asm-run.schema.json`

v0.7.8 assembly run

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.local/schemas/assembly/asm-run.schema.json`
- **Top-level type:** `object`
- **Required fields:** `run_id`, `asm_format`, `architecture`, `status`, `summary`
- **Top-level properties:** `architecture`, `asm_format`, `run_id`, `status`, `summary`

SHA-256: `6c728e9e657571a4aa03d77f1974a2d6d79d8a03e903dda4571f46979f898526`

<a id="schema-assembly-relocation-resolution-schema-json"></a>

## `assembly/relocation-resolution.schema.json`

v0.7.8 COFF relocation resolution

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.local/schemas/assembly/relocation-resolution.schema.json`
- **Top-level type:** `object`
- **Required fields:** `object`, `symbol`, `architecture`, `base_rva`, `resolved_count`, `unresolved_count`, `relocations`, `exact_match`
- **Top-level properties:** `architecture`, `base_rva`, `exact_match`, `object`, `relocations`, `resolved_count`, `symbol`, `unresolved_count`

SHA-256: `c60fc6b40f9568eea179ae35dd115364518a4d430142560f03caccaf6e05fc49`

<a id="schema-assembly-roundtrip-report-schema-json"></a>

## `assembly/roundtrip-report.schema.json`

v0.7.8 mnemonic round-trip report

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.local/schemas/assembly/roundtrip-report.schema.json`
- **Top-level type:** `object`
- **Required fields:** `source`, `object`, `symbol`, `rva`, `architecture`, `input_sha256`, `resolved_sha256`, `exact_match`, `classification`
- **Top-level properties:** `architecture`, `classification`, `exact_match`, `input_sha256`, `object`, `resolved_sha256`, `rva`, `semantic_equivalence_claimed`, `source`, `symbol`

SHA-256: `3812e340bb6233778c279ae0ff0b4c038bb68c24ede68ca6c5a07e64c49119bc`

<a id="schema-assembly-symbol-map-schema-json"></a>

## `assembly/symbol-map.schema.json`

v0.7.8 original-RVA symbol map

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.local/schemas/assembly/symbol-map.schema.json`
- **Top-level type:** `object`
- **Required fields:** none declared
- **Top-level properties:** none declared

SHA-256: `8e5478b2606ae106f5f72b828134a9b6b91b8df9602eae94bda00cef23264337`

<a id="schema-benchmark-corpus-schema-json"></a>

## `benchmark-corpus.schema.json`

Ground-truth benchmark corpus

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:benchmark-corpus:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `name`, `cases`
- **Top-level properties:** `cases`, `name`, `schema_version`

SHA-256: `0081dd4d038287641f14ccd228dd0e824bff8bd3745f8251aaa0a94c1c61e36c`

<a id="schema-claim-schema-json"></a>

## `claim.schema.json`

x86decomp claim

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:claim:1`
- **Top-level type:** `object`
- **Required fields:** `id`, `subject`, `predicate`, `object`, `state`, `evidence_ids`, `contradiction_ids`, `notes`, `created_at`, `updated_at`
- **Top-level properties:** `contradiction_ids`, `created_at`, `evidence_ids`, `id`, `notes`, `object`, `predicate`, `state`, `subject`, `updated_at`

SHA-256: `362341adcb81640a7839c77d37d7203b911e7e79655be6c0ab4115f460609532`

<a id="schema-coff-archive-schema-json"></a>

## `coff-archive.schema.json`

x86decomp COFF Archive Inspection

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:coff-archive:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `format`, `source_path`, `source_sha256`, `member_count`, `members`, `linker_symbols`
- **Top-level properties:** `format`, `linker_symbols`, `member_count`, `members`, `schema_version`, `source_path`, `source_sha256`

SHA-256: `5f5a43f1ce6ae1221df24107f7b9db057156731736ff4aad5c81c93a73abaab3`

<a id="schema-comdat-resolution-schema-json"></a>

## `comdat-resolution.schema.json`

COFF COMDAT resolution report

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:comdat-resolution:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `valid`, `winners`, `discarded`, `conflicts`
- **Top-level properties:** `conflicts`, `discarded`, `schema_version`, `valid`, `winners`

SHA-256: `01fd177dfa983202ca8770e7985aa623e166fd22c20fdecc1d3d37f9cbfe0aae`

<a id="schema-compiler-ground-truth-comparison-schema-json"></a>

## `compiler-ground-truth-comparison.schema.json`

Compiler/version ground-truth corpus comparison

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:compiler-ground-truth-comparison:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `reports`, `comparisons`, `summary`, `semantic_equivalence_claimed`
- **Top-level properties:** `comparisons`, `kind`, `reports`, `schema_version`, `semantic_equivalence_claimed`, `summary`

SHA-256: `1ea55d940c62d4e60487f74ac4d9756e4ff4c7cb2c39c9dd629b1d4150646dfb`

<a id="schema-compiler-ground-truth-schema-json"></a>

## `compiler-ground-truth.schema.json`

Compiler ground-truth corpus manifest

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:compiler-ground-truth:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `compilers`, `cases`
- **Top-level properties:** `cases`, `compilers`, `flag_matrix`, `schema_version`, `timeout_seconds`

SHA-256: `1f8d15358ce71168a0f7c4d61ba7ad9db1ef12b534b27444bdda1f77f96392a2`

<a id="schema-compiler-lab-schema-json"></a>

## `compiler-lab.schema.json`

Compiler experiment matrix

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:compiler-lab:1`
- **Top-level type:** `object`
- **Required fields:** `source`, `profiles`
- **Top-level properties:** `cache_root`, `matrix`, `max_experiments`, `output_name`, `output_root`, `profiles`, `source`, `target`

SHA-256: `37bc55f945daffc31844a78c2b4788191f501589303826a6cee207c5c4717506`

<a id="schema-compiler-profile-schema-json"></a>

## `compiler-profile.schema.json`

x86decomp compiler profile

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:compiler-profile:2`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `id`, `description`, `executable`, `language`, `output_kind`, `timeout_seconds`, `arguments`, `environment`
- **Top-level properties:** `arguments`, `command_prefix`, `description`, `environment`, `executable`, `family`, `id`, `inherit_environment`, `language`, `output_kind`, `schema_version`, `timeout_seconds`, `version`, `version_arguments`

SHA-256: `6903f160acf5cfb8329567efbdd2da82b9f171705971e9842afcae21a4a4f844`

<a id="schema-convergence-report-schema-json"></a>

## `convergence-report.schema.json`

No schema title is declared.

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:convergence-report:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `reference_sha256`, `candidate_sha256`, `image_match`, `totals`, `sections`, `next_actions`, `complete`, `normalized_complete`
- **Top-level properties:** `candidate_sha256`, `complete`, `created_at`, `delta_from_previous`, `image_match`, `kind`, `limitations`, `next_actions`, `normalized_complete`, `reference_sha256`, `root_cause_claimed`, `schema_version`, `sections`, `totals`

SHA-256: `ace195921a16f72366e2920e6e2ce4e464b51f665d4d12ff5117dbea49119185`

<a id="schema-cpp-recovery-schema-json"></a>

## `cpp-recovery.schema.json`

No schema title is declared.

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:cpp-recovery:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `classes`, `vtable_groups`, `adjustor_thunk_candidates`, `counts`, `claims`, `limitations`
- **Top-level properties:** `adjustor_thunk_candidates`, `claims`, `classes`, `counts`, `created_at`, `image`, `kind`, `limitations`, `metadata_source`, `schema_version`, `static_initializer_order_evidence`, `vtable_groups`

SHA-256: `9eda5eb04cdd6404ed82077dab0b1f2668f3682b33f864fec3c7348439515d8a`

<a id="schema-decompme-packet-schema-json"></a>

## `decompme-packet.schema.json`

Local decomp.me-style function packet

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:decompme-packet:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `created_at`, `kind`, `function_id`, `source_artifact`, `output_directory`, `files`, `uploaded`, `limitations`
- **Top-level properties:** `created_at`, `files`, `function_id`, `kind`, `limitations`, `output_directory`, `schema_version`, `source_artifact`, `uploaded`

SHA-256: `65cd0a5d3197e6de85ec46c8eb372a387102192d9341ee252a7f40ca83b91704`

<a id="schema-dependency-audit-schema-json"></a>

## `dependency-audit.schema.json`

x86decomp dependency vulnerability audit

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:dependency-audit:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `created_at`, `tool`, `tool_sha256`, `return_code`, `dependency_count`, `vulnerability_count`, `vulnerabilities`, `passed`, `raw_report`
- **Top-level properties:** `created_at`, `dependency_count`, `kind`, `passed`, `raw_report`, `return_code`, `schema_version`, `stderr`, `tool`, `tool_sha256`, `vulnerabilities`, `vulnerability_count`

SHA-256: `2eef4097789050d846536b406ccd7b9e8e639467bdf1ca530045fcc6050c8ee2`

<a id="schema-drcov-trace-schema-json"></a>

## `drcov-trace.schema.json`

Normalized DynamoRIO drcov text trace

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:drcov-trace:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `source`, `source_sha256`, `drcov_version`, `modules`, `basic_blocks`, `unique_basic_blocks`
- **Top-level properties:** `basic_blocks`, `drcov_flavor`, `drcov_version`, `kind`, `module_table_version`, `modules`, `schema_version`, `source`, `source_sha256`, `unique_basic_blocks`

SHA-256: `aedc8ab92612b4b325552d3de98da9d04e2e4c3aa2bb2ab319e20f85616cfe7f`

<a id="schema-dynamic-report-schema-json"></a>

## `dynamic-report.schema.json`

Bounded Unicorn differential report

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:dynamic-report:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `equivalent_for_harness`, `target`, `candidate`, `scope_statement`
- **Top-level properties:** `candidate`, `equivalent_for_harness`, `schema_version`, `scope_statement`, `target`

SHA-256: `1af7c179c9d4fedbf542c098eab126d556fc8345a464176d211640f391effce0`

<a id="schema-evidence-schema-json"></a>

## `evidence.schema.json`

x86decomp evidence item

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:evidence:1`
- **Top-level type:** `object`
- **Required fields:** `id`, `kind`, `source`, `locator`, `assertion`, `independent_group`, `digest_sha256`, `observed_at`, `metadata`
- **Top-level properties:** `assertion`, `digest_sha256`, `id`, `independent_group`, `kind`, `locator`, `metadata`, `observed_at`, `source`

SHA-256: `5c5199ae9f480dbbb28eb3ebd889a53a46c08535cabf346d3a0bf04f4a4aa7bd`

<a id="schema-exe-diff-report-schema-json"></a>

## `exe-diff-report.schema.json`

PE function to COFF symbol comparison

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:exe-diff-report:2`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `classification`, `pe`, `coff`, `normalization_masks`, `raw_byte_comparison`, `normalized_byte_comparison`, `semantic_equivalence_claimed`
- **Top-level properties:** `architecture`, `classification`, `coff`, `created_at`, `instruction_comparison`, `instruction_comparison_error`, `kind`, `limitations`, `normalization_masks`, `normalized_byte_comparison`, `pe`, `raw_byte_comparison`, `schema_version`, `semantic_equivalence_claimed`

SHA-256: `3bfb70b7158750523074f638ff5955cc519097a37543f9f097909f4576373b50`

<a id="schema-execution-harness-generated-schema-json"></a>

## `execution-harness-generated.schema.json`

No schema title is declared.

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:execution-harness-generated:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `architecture`, `code_base`, `stack_base`, `stack_size`, `sentinel_address`, `max_instructions`, `timeout_ms`, `registers`, `stack_arguments_hex`, `memory`, `observe_registers`, `observe_memory`, `stubs`, `generation`, `limitations`
- **Top-level properties:** `architecture`, `code_base`, `created_at`, `generation`, `limitations`, `max_instructions`, `memory`, `observe_memory`, `observe_registers`, `registers`, `schema_version`, `sentinel_address`, `stack_arguments_hex`, `stack_base`, `stack_size`, `stubs`, `timeout_ms`

SHA-256: `7ba43bfcb6b5b8736d784112af5531e1a890630e379eb2c345f15442c18a2c6d`

<a id="schema-execution-harness-schema-json"></a>

## `execution-harness.schema.json`

Bounded Unicorn execution harness

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:execution-harness:1`
- **Top-level type:** `object`
- **Required fields:** `architecture`
- **Top-level properties:** `architecture`, `code_base`, `max_instructions`, `memory`, `observe_memory`, `observe_registers`, `registers`, `sentinel_address`, `stack_arguments_hex`, `stack_base`, `stack_size`, `stubs`, `timeout_ms`

SHA-256: `2ec27dc202dcf7ab923c646c71e30769b0c18527aaf2e6ba44e70536574e4f68`

<a id="schema-function-workflow-schema-json"></a>

## `function-workflow.schema.json`

x86decomp per-function workflow

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:function-workflow:2`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `function_id`, `selected_modes`, `source_stage`, `matching_status`, `functional_status`, `reports`, `blockers`, `updated_at`
- **Top-level properties:** `active_candidate`, `blockers`, `compiler_profile`, `function_id`, `functional_status`, `matching_status`, `reports`, `schema_version`, `selected_modes`, `source_stage`, `updated_at`

SHA-256: `972f7c4fef555a4653a57cad04f1dedb186cc70a6c59de7e674645b30c240351`

<a id="schema-function-schema-json"></a>

## `function.schema.json`

x86decomp Ghidra function artifact (schema versions 1 and 2)

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:function:2`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `id`, `entry`, `entry_rva`, `name`, `name_source`, `calling_convention`, `signature`, `return_type`, `body_ranges`, `parameters`
- **Top-level properties:** `artifacts`, `body_ranges`, `calling_convention`, `decompile_completed`, `decompile_error`, `entry`, `entry_rva`, `functional_status`, `id`, `is_thunk`, `matching_status`, `name`, `name_source`, `parameters`, `qualified_name`, `return_type`, `schema_version`, `selected_modes`, `signature`

SHA-256: `00c65be77cc237df28a9112019c07019f88f38072ceb329907adc88bcfc34704`

<a id="schema-governance-campaign-schema-json"></a>

## `governance/campaign.schema.json`

campaign

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `not declared`
- **Top-level type:** `object`
- **Required fields:** `goal`, `status`, `budget`, `used`
- **Top-level properties:** `budget`, `goal`, `policy`, `status`, `used`

SHA-256: `df027ea63ef0017b5a9ecae133a21ab7fa13f68e00545529e8606b5f39d1f854`

<a id="schema-governance-candidate-schema-json"></a>

## `governance/candidate.schema.json`

candidate

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `not declared`
- **Top-level type:** `object`
- **Required fields:** `branch_name`, `state`, `objective`
- **Top-level properties:** `branch_name`, `evaluations`, `files`, `objective`, `state`

SHA-256: `db23f94af8b37ebdfff2798c271a0ef02ea9d77aae83fa8c8ebdab3d2f55ad67`

<a id="schema-governance-changeset-schema-json"></a>

## `governance/changeset.schema.json`

changeset manifest

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `not declared`
- **Top-level type:** `object`
- **Required fields:** `format`, `changeset_id`, `base_event_hash`, `tip_event_hash`, `event_count`
- **Top-level properties:** `base_event_hash`, `changeset_id`, `created_at`, `event_count`, `format`, `tip_event_hash`

SHA-256: `6788b90056dbf46cdaaaab292bdc6c3102e20ff47c790f131b47c15d08f5cbd3`

<a id="schema-governance-consensus-schema-json"></a>

## `governance/consensus.schema.json`

consensus observation

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `not declared`
- **Top-level type:** `object`
- **Required fields:** `subject_kind`, `subject_id`, `property_name`, `value`, `adapter_name`, `adapter_version`, `evidence_id`, `independence_group`, `confidence`
- **Top-level properties:** `adapter_name`, `adapter_version`, `confidence`, `evidence_id`, `independence_group`, `property_name`, `subject_id`, `subject_kind`, `value`

SHA-256: `f3edcf4a5962701cde7a0f4f483a19d49e9f5beea5e6a4dc3c643c9970ee9c43`

<a id="schema-governance-counterexample-schema-json"></a>

## `governance/counterexample.schema.json`

counterexample

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `not declared`
- **Top-level type:** `object`
- **Required fields:** `scope_kind`, `scope_id`, `current_sha256`, `size_bytes`, `state`, `predicate`
- **Top-level properties:** `current_sha256`, `predicate`, `provenance`, `scope_id`, `scope_kind`, `size_bytes`, `state`

SHA-256: `0e2b706ed1bf89e6c07a483dd171dbb23fbac4f67c87ef1df16be6c2fe50d19c`

<a id="schema-governance-family-schema-json"></a>

## `governance/family.schema.json`

binary family report

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `not declared`
- **Top-level type:** `object`
- **Required fields:** `family_id`, `name`, `members`, `correlations`, `non_claims`
- **Top-level properties:** `correlations`, `family_id`, `members`, `name`, `non_claims`

SHA-256: `cd02347eefe68396b21d7ec5af6ef9c1554dd4715e962e302ece657cb0b851ed`

<a id="schema-governance-hypothesis-schema-json"></a>

## `governance/hypothesis.schema.json`

hypothesis

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `not declared`
- **Top-level type:** `object`
- **Required fields:** `statement`, `scope_kind`, `scope_id`, `state`, `confidence`, `origin`
- **Top-level properties:** `confidence`, `locked`, `origin`, `scope_id`, `scope_kind`, `state`, `statement`

SHA-256: `1013bee5c093d4cf0e619dbcdc52a2b2ff79c0b768da9c699ad0483bfc283a83`

<a id="schema-governance-knowledge-graph-schema-json"></a>

## `governance/knowledge-graph.schema.json`

knowledge graph impact

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `not declared`
- **Top-level type:** `object`
- **Required fields:** `root`, `direction`, `max_depth`, `nodes`, `edges`
- **Top-level properties:** `direction`, `edges`, `max_depth`, `nodes`, `root`

SHA-256: `d1bc76932c0264e763eb4cdb47d46397ddf00bb57e1c240371ef42049631db28`

<a id="schema-governance-plugin-schema-json"></a>

## `governance/plugin.schema.json`

plugin manifest

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `not declared`
- **Top-level type:** `object`
- **Required fields:** `name`, `version`, `api_version`, `executable`, `capabilities`
- **Top-level properties:** `api_version`, `capabilities`, `executable`, `name`, `version`

SHA-256: `1fb5e12f5c8eb5408dea6372c5442273b1694559dc9c09784bbca4309dbf5fd2`

<a id="schema-governance-proof-bundle-schema-json"></a>

## `governance/proof-bundle.schema.json`

proof bundle manifest

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `not declared`
- **Top-level type:** `object`
- **Required fields:** `format`, `release`, `files`
- **Top-level properties:** `audit_tip`, `files`, `format`, `release`

SHA-256: `36ab796b4f987ec253c7a5110479fd3261ac313b29ae4b90a73b72a824654b43`

<a id="schema-governance-review-schema-json"></a>

## `governance/review.schema.json`

review item

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `not declared`
- **Top-level type:** `object`
- **Required fields:** `kind`, `subject_id`, `priority`, `status`, `summary`
- **Top-level properties:** `details`, `kind`, `locked`, `priority`, `status`, `subject_id`, `summary`

SHA-256: `280cfe7963adcdcbbb3a1fde01b921cad82751d2240a4fcdaa9b9543db071bc2`

<a id="schema-governance-worker-schema-json"></a>

## `governance/worker.schema.json`

worker profile

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `not declared`
- **Top-level type:** `object`
- **Required fields:** `name`, `status`, `capabilities`
- **Top-level properties:** `capabilities`, `endpoint`, `environment_sha256`, `name`, `status`

SHA-256: `ca8f6768a4c7dfe89e80f2107c4bb43badde4d01d3ec6947ff001c9b207b403c`

<a id="schema-hybrid-project-schema-json"></a>

## `hybrid-project.schema.json`

Continuously buildable hybrid project

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:hybrid-project:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `created_at`, `project_root`, `architecture`, `functions`, `build`
- **Top-level properties:** `architecture`, `build`, `created_at`, `functions`, `project_root`, `schema_version`

SHA-256: `c72692b4469f7ba92b2945968974d495371e2c0f03ad438c970418c3ce31d9b0`

<a id="schema-image-match-report-schema-json"></a>

## `image-match-report.schema.json`

Target-specific whole-image match report

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:image-match-report:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `reference`, `candidate`, `profile`, `raw_exact_match`, `normalized_match`, `sections`, `classification`, `universal_equivalence_claimed`
- **Top-level properties:** `candidate`, `classification`, `kind`, `normalized_match`, `normalized_mismatch_count`, `profile`, `raw_exact_match`, `raw_mismatch_count`, `reference`, `schema_version`, `sections`, `universal_equivalence_claimed`

SHA-256: `f81f81c2581b2941b9a3850aa2d296957e1d14de2ad3d8ee92839b34ccfadc23`

<a id="schema-image-profile-schema-json"></a>

## `image-profile.schema.json`

Target-specific PE image layout profile

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:image-profile:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `reference_sha256`, `architecture`, `section_order`, `normalization`
- **Top-level properties:** `architecture`, `entry_rva`, `image_base`, `kind`, `normalization`, `reference_sha256`, `schema_version`, `section_order`, `sections`

SHA-256: `5916e3589fb77876a26861ccfea7dfbfbf4b9c55e92243ed66dae4270dad70d7`

<a id="schema-integration-report-schema-json"></a>

## `integration-report.schema.json`

Bounded integration comparison report

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:integration-report:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `created_at`, `kind`, `execution`, `scenario_count`, `passed_count`, `failed_count`, `all_scenarios_equivalent`, `scenarios`, `limitations`
- **Top-level properties:** `all_scenarios_equivalent`, `failed_count`, `kind`, `limitations`, `passed_count`, `scenario_count`, `scenarios`, `schema_version`

SHA-256: `4732a3a8f4038739f46c7b7b74b20999c68d9f637bac783a53b03eee91e91d1a`

<a id="schema-integration-scenarios-schema-json"></a>

## `integration-scenarios.schema.json`

Integration scenario manifest

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:integration-scenarios:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `name`, `execution`, `scenarios`
- **Top-level properties:** `captured_output_limit`, `execution`, `name`, `scenarios`, `schema_version`

SHA-256: `60799068b8df90e7d457415f6e08fa236a0620630ddab2641dec2ff8bac6e43e`

<a id="schema-linker-layout-schema-json"></a>

## `linker-layout.schema.json`

Linker layout reconstruction report

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:linker-layout:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `image`, `map`, `contributions`, `unresolved`
- **Top-level properties:** `comdat_resolution`, `complete_original_layout_claimed`, `contributions`, `image`, `kind`, `map`, `object_order_evidenced`, `schema_version`, `unresolved`

SHA-256: `a8faf6022c8b70e04c3375d47a480b9a811e72edd55ea7e0ec4e80a77a8ca934`

<a id="schema-linker-reconstruction-plan-schema-json"></a>

## `linker-reconstruction-plan.schema.json`

No schema title is declared.

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:linker-reconstruction-plan:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `reference_image`, `map`, `objects`, `sections`, `placements`, `comdat_resolution`, `relink_manifest`, `unresolved`, `ready_for_relink`
- **Top-level properties:** `archives`, `comdat_resolution`, `complete_original_link_command_claimed`, `created_at`, `kind`, `libraries`, `limitations`, `linker`, `map`, `objects`, `placements`, `ready_for_relink`, `reference_image`, `relink_manifest`, `schema_version`, `sections`, `unresolved`

SHA-256: `1d6fadf9737abed4d02cc90d3859898785edf62d3909c39fe893c8841c57f504`

<a id="schema-local-llm-candidate-schema-json"></a>

## `local-llm/candidate.schema.json`

Local LLM C proposal response

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.local/schemas/local-llm/candidate.schema.json`
- **Top-level type:** `object`
- **Required fields:** `status`, `c_source`, `assumptions`, `rationale`
- **Top-level properties:** `assumptions`, `c_source`, `rationale`, `status`

SHA-256: `cadff624248794b1841a55fd49f2f980658a442d046530c183ec0c89d44d99ab`

<a id="schema-local-llm-job-schema-json"></a>

## `local-llm/job.schema.json`

Local LLM C generation and byte-match job

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.local/schemas/local-llm/job.schema.json`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `id`, `function_name`, `architecture`
- **Top-level properties:** `abi`, `architecture`, `base_rva`, `evidence`, `function_name`, `id`, `image_base`, `max_attempts`, `mnemonics`, `mnemonics_file`, `schema_version`, `section_placements`, `symbol`, `symbol_map`, `target_bytes_file`, `target_bytes_hex`

SHA-256: `6ac68b5f4f22855154f8ec09e599c7caa3ce12d117fb125a0bae8e4dce0197a8`

<a id="schema-local-llm-profile-schema-json"></a>

## `local-llm/profile.schema.json`

Local LLM provider profile

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.local/schemas/local-llm/profile.schema.json`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `id`, `provider`, `protocol`, `base_url`, `models_path`, `chat_path`, `structured_output`, `model`, `temperature`, `max_tokens`, `timeout_seconds`, `max_response_bytes`, `verify_tls`, `allow_remote`, `api_key_env`, `headers`
- **Top-level properties:** `allow_remote`, `api_key_env`, `base_url`, `chat_path`, `headers`, `id`, `max_response_bytes`, `max_tokens`, `model`, `models_path`, `protocol`, `provider`, `schema_version`, `structured_output`, `temperature`, `timeout_seconds`, `verify_tls`

SHA-256: `dc3ed501bada8be1896567c329fd550ad843059786ed07bbae6ef3063fdfe3ee`

<a id="schema-local-llm-report-schema-json"></a>

## `local-llm/report.schema.json`

Local LLM exact byte-match report

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.local/schemas/local-llm/report.schema.json`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `created_at`, `status`, `profile`, `compiler_profile`, `job`, `attempt_limit`, `attempt_count`, `attempts`, `accepted`, `claim`, `limitations`
- **Top-level properties:** `accepted`, `attempt_count`, `attempt_limit`, `attempts`, `claim`, `compiler_profile`, `created_at`, `job`, `kind`, `limitations`, `profile`, `schema_version`, `status`

SHA-256: `d61c0308354431848f281d3c62cd32b39c9d61277492bee480a02276e5ad6ac0`

<a id="schema-mcp-mutation-schema-json"></a>

## `mcp-mutation.schema.json`

Evidence-gated MCP mutation

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:mcp-mutation:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `created_at`, `tool`, `arguments`, `rationale`, `evidence_ids`, `status`, `approval_hash`
- **Top-level properties:** `approval_hash`, `arguments`, `committed_at`, `created_at`, `evidence_ids`, `rationale`, `result`, `schema_version`, `status`, `tool`

SHA-256: `64335798160269133e880d823f14de7f0cb4f2dafbf0c47526e24fb9fb16ea29`

<a id="schema-memory-event-schema-json"></a>

## `memory-event.schema.json`

x86decomp project memory event

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:memory-event:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `id`, `sequence`, `timestamp`, `actor`, `category`, `summary`, `details`, `evidence_ids`, `previous_hash`, `event_hash`
- **Top-level properties:** `actor`, `category`, `details`, `event_hash`, `evidence_ids`, `id`, `previous_hash`, `schema_version`, `sequence`, `summary`, `timestamp`

SHA-256: `d2f38971ac7dda92dda0564bb77bb4858160b5a342476d36fe52238eb5289e74`

<a id="schema-msvc-metadata-schema-json"></a>

## `msvc-metadata.schema.json`

Bounded MSVC metadata analysis report

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:msvc-metadata:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `image`, `rtti`, `exceptions`, `tls`, `static_initializers`, `source_level_recovery_claimed`
- **Top-level properties:** `exceptions`, `image`, `kind`, `rtti`, `schema_version`, `source_level_recovery_claimed`, `static_initializers`, `tls`

SHA-256: `84d0b6bc880ab47954f951a4eed4db317c14ee33ed5cdbe0ee098ce61c1d6273`

<a id="schema-native-boundary-finding-schema-json"></a>

## `native/boundary-finding.schema.json`

x86decomp boundary-finding

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.invalid/schemas/native/boundary-finding.schema.json`
- **Top-level type:** `object`
- **Required fields:** `function_id`, `finding_kind`, `severity`
- **Top-level properties:** `finding_kind`, `function_id`, `severity`

SHA-256: `58d723eee6c5c374f78dcac68a23be5d0b60c6f002c3e8285d307eef496e74fc`

<a id="schema-native-candidate-manifest-schema-json"></a>

## `native/candidate-manifest.schema.json`

x86decomp candidate-manifest

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.invalid/schemas/native/candidate-manifest.schema.json`
- **Top-level type:** `object`
- **Required fields:** `function_id`, `rva`, `slot_size`, `candidate_path`
- **Top-level properties:** `candidate_path`, `function_id`, `rva`, `slot_size`, `symbol`

SHA-256: `d3bad2e693b4b7d6e1c230d9e03ff775298273523c8b562d3b78400c13313029`

<a id="schema-native-function-match-schema-json"></a>

## `native/function-match.schema.json`

x86decomp function-match

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.invalid/schemas/native/function-match.schema.json`
- **Top-level type:** `object`
- **Required fields:** `function_id`, `rva`, `slot_size`, `classification`, `replacement_safe`
- **Top-level properties:** `classification`, `function_id`, `replacement_safe`, `rva`, `slot_size`

SHA-256: `e598ca859f33c96b62fe8dac7fcf78ec77b53e4b8f178b9f19e1f288e2725cd1`

<a id="schema-native-function-slot-schema-json"></a>

## `native/function-slot.schema.json`

x86decomp function-slot

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.invalid/schemas/native/function-slot.schema.json`
- **Top-level type:** `object`
- **Required fields:** `function_id`, `rva`, `body_size`, `slot_size`, `classification`
- **Top-level properties:** `body_size`, `classification`, `function_id`, `rva`, `slot_size`

SHA-256: `61bb10550455068b1c58073dfb30939aea8095cefbd775abab4d044efe9a2914`

<a id="schema-native-hybrid-composition-schema-json"></a>

## `native/hybrid-composition.schema.json`

x86decomp hybrid-composition

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.invalid/schemas/native/hybrid-composition.schema.json`
- **Top-level type:** `object`
- **Required fields:** `run_id`, `output`, `promoted_count`, `fallback_count`
- **Top-level properties:** `fallback_count`, `output`, `promoted_count`, `run_id`

SHA-256: `feb6682c1aa1ed0a3bc3c06230ce27f006641d96238050151ad22584eb02cb9d`

<a id="schema-native-loop-run-schema-json"></a>

## `native/loop-run.schema.json`

x86decomp loop-run

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.invalid/schemas/native/loop-run.schema.json`
- **Top-level type:** `object`
- **Required fields:** `function_id`, `source_path`, `compile_command`, `candidate_path`
- **Top-level properties:** `candidate_path`, `compile_command`, `function_id`, `source_path`

SHA-256: `de5d1a277444c3ea53ae0c4860d1a7978b478893fb893cf4c1ba1fca4a11b038`

<a id="schema-native-match-run-schema-json"></a>

## `native/match-run.schema.json`

x86decomp match-run

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.invalid/schemas/native/match-run.schema.json`
- **Top-level type:** `object`
- **Required fields:** `original_path`, `comparison_policy`
- **Top-level properties:** `comparison_policy`, `original_path`

SHA-256: `7afbfb42c5995ff375a050c93bb119ce50f2a761220c610f2c1622f082c23fb5`

<a id="schema-native-patch-plan-schema-json"></a>

## `native/patch-plan.schema.json`

x86decomp patch-plan

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.invalid/schemas/native/patch-plan.schema.json`
- **Top-level type:** `object`
- **Required fields:** `original_path`, `output_path`, `operations`
- **Top-level properties:** `operations`, `original_path`, `output_path`

SHA-256: `90a1f06eaa3f6a3d6b235cc0439c57fec0187006ccc4c01b8fbb76571bb31958`

<a id="schema-native-runtime-validation-schema-json"></a>

## `native/runtime-validation.schema.json`

x86decomp runtime-validation

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.invalid/schemas/native/runtime-validation.schema.json`
- **Top-level type:** `object`
- **Required fields:** `image_path`, `validation_kind`, `status`, `checks`
- **Top-level properties:** `checks`, `image_path`, `status`, `validation_kind`

SHA-256: `f314d1ae2b72314a6ebf6c6d2905a8eb2f314498f256f567e01ae08622da90f3`

<a id="schema-native-section-export-schema-json"></a>

## `native/section-export.schema.json`

x86decomp section-export

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.invalid/schemas/native/section-export.schema.json`
- **Top-level type:** `object`
- **Required fields:** `source`, `sections`
- **Top-level properties:** `sections`, `source`

SHA-256: `121ed87fe1b51a248b230acafd9780b96e74e01c72e9cba7fcd20fbb466eb317`

<a id="schema-native-staging-symbol-schema-json"></a>

## `native/staging-symbol.schema.json`

x86decomp staging-symbol

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.invalid/schemas/native/staging-symbol.schema.json`
- **Top-level type:** `object`
- **Required fields:** `symbol_name`, `symbol_kind`, `declaration`, `status`
- **Top-level properties:** `declaration`, `status`, `symbol_kind`, `symbol_name`

SHA-256: `44b3ce02db0758435f6a230a9ad37bd00c3a6308bf71761836050e5c90c6c4d0`

<a id="schema-native-windows-tool-schema-json"></a>

## `native/windows-tool.schema.json`

x86decomp windows-tool

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.invalid/schemas/native/windows-tool.schema.json`
- **Top-level type:** `object`
- **Required fields:** `tool_name`, `available`
- **Top-level properties:** `available`, `path`, `tool_name`

SHA-256: `22af6f0e3266250f1c741e95e231c4ee3d62fd3944e0000e6ab6e652089906e0`

<a id="schema-objdiff-manifest-schema-json"></a>

## `objdiff-manifest.schema.json`

objdiff external invocation manifest

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:objdiff-manifest:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `target`, `candidate`, `arguments`
- **Top-level properties:** `arguments`, `candidate`, `environment`, `executable`, `inherit_environment`, `output`, `output_format`, `require_output`, `schema_version`, `success_exit_codes`, `target`, `timeout_seconds`

SHA-256: `2fe8f65399749687b2890cc643f474c0b8de221e90f6ae5013ce0d8b46590360`

<a id="schema-pdb-schema-json"></a>

## `pdb.schema.json`

x86decomp bounded PDB/MSF inventory

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:pdb:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `format`, `source_path`, `source_sha256`, `superblock`, `stream_count`, `streams`, `pdb_info`, `tpi`, `ipi`, `dbi`, `pe_match`, `scope`
- **Top-level properties:** `dbi`, `format`, `ipi`, `pdb_info`, `pe_match`, `schema_version`, `scope`, `source_path`, `source_sha256`, `stream_count`, `streams`, `superblock`, `tpi`

SHA-256: `850bbf885fa040ac4601dc4d93c2fb4b3afda1dd86612a0d8866a34bacf07008`

<a id="schema-pipeline-schema-json"></a>

## `pipeline.schema.json`

No schema title is declared.

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:pipeline:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `pipeline_id`, `project_root`, `stages`
- **Top-level properties:** `created_at`, `pipeline_id`, `project_root`, `schema_version`, `stages`

SHA-256: `a9b7b790fb6c877370a4c61ecbdf0f92eac13d9aba389cc0ab8d8723aee92ca6`

<a id="schema-project-template-schema-json"></a>

## `project-template.schema.json`

Grounded x86decomp project-template contract

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:project-template:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `created_at`, `target_id`, `architecture`, `image_kind`, `selected_modes`, `matching`, `functional`, `artifact_roles`, `blockers`, `truth_policy`
- **Top-level properties:** `architecture`, `artifact_roles`, `blockers`, `created_at`, `functional`, `image_kind`, `matching`, `schema_version`, `selected_modes`, `source_language_candidates`, `source_language_decision`, `target_id`, `truth_policy`

SHA-256: `1bf881ea328d3a6c00d727c0cbe1e47763726e70362a085354178add994458ce`

<a id="schema-project-schema-json"></a>

## `project.schema.json`

x86decomp project (schema versions 1, 2, and 3)

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:project:3`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `project_id`, `created_at`, `supported_scope`, `binary`, `program_manifest`, `memory_ledger`, `function_root`, `evidence_root`, `status`
- **Top-level properties:** `analysis_database`, `architecture`, `binary`, `content_store`, `created_at`, `default_modes`, `evidence_root`, `function_root`, `memory_ledger`, `orchestration_root`, `program_manifest`, `project_id`, `project_state_database`, `schema_version`, `status`, `supported_scope`, `target_id`, `target_pack`, `template_kind`, `toolkit_release`, `work_queue`

SHA-256: `4ab19d9064e8d249fdd545d1fa183920902d6afbe647d004ddd571a208295b0b`

<a id="schema-reconstruction-abi-contract-schema-json"></a>

## `reconstruction/abi-contract.schema.json`

ABI contract

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.dev/schemas/reconstruction/abi-contract.schema.json`
- **Top-level type:** `object`
- **Required fields:** `contract_id`, `subject_kind`, `subject_id`, `architecture`, `contract`, `evidence`
- **Top-level properties:** `architecture`, `contract`, `contract_id`, `evidence`, `subject_id`, `subject_kind`

SHA-256: `d2286943caed629e873a4107fcceb21f18b0759cfebd17b71f761af14e68e016`

<a id="schema-reconstruction-build-schema-json"></a>

## `reconstruction/build.schema.json`

Build reconstruction contract

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.dev/schemas/reconstruction/build.schema.json`
- **Top-level type:** `object`
- **Required fields:** `build_id`, `mode`, `generator`, `targets`
- **Top-level properties:** `build_id`, `generator`, `mode`, `targets`

SHA-256: `647d938812825abaa84206de119ebc4a18d8fad70a4f50121f990a4af2571dd0`

<a id="schema-reconstruction-capsule-schema-json"></a>

## `reconstruction/capsule.schema.json`

Reconstruction capsule manifest

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.dev/schemas/reconstruction/capsule.schema.json`
- **Top-level type:** `object`
- **Required fields:** `schema`, `toolkit_version`, `members`, `external_requirements`
- **Top-level properties:** `external_requirements`, `members`, `schema`, `toolkit_version`

SHA-256: `e033933bf2fe696c221bfce86fda56998c55b3d17496114a66bc6b6ff326d538`

<a id="schema-reconstruction-compatibility-shim-schema-json"></a>

## `reconstruction/compatibility-shim.schema.json`

Explicit compatibility shim

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.dev/schemas/reconstruction/compatibility-shim.schema.json`
- **Top-level type:** `object`
- **Required fields:** `shim_id`, `subject_id`, `shim_kind`, `source_path`, `contract`, `status`
- **Top-level properties:** `contract`, `shim_id`, `shim_kind`, `source_path`, `status`, `subject_id`

SHA-256: `714bcc499ffc2db676e163a5886ce9ca4fca7df0b2382a94488c6dfc5a782926`

<a id="schema-reconstruction-generated-test-schema-json"></a>

## `reconstruction/generated-test.schema.json`

Generated regression test

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.dev/schemas/reconstruction/generated-test.schema.json`
- **Top-level type:** `object`
- **Required fields:** `generated_test_id`, `name`, `scope_kind`, `scope_id`, `test_kind`, `relative_path`, `content_sha256`
- **Top-level properties:** `content_sha256`, `generated_test_id`, `name`, `relative_path`, `scope_id`, `scope_kind`, `test_kind`

SHA-256: `8e99342ae82922d0c5c17c41e857074a5a2cec9b1269e23572aea09b5715a7b5`

<a id="schema-reconstruction-header-schema-json"></a>

## `reconstruction/header.schema.json`

Recovered header contract

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.dev/schemas/reconstruction/header.schema.json`
- **Top-level type:** `object`
- **Required fields:** `header_id`, `path`, `visibility`, `declarations`
- **Top-level properties:** `declarations`, `header_id`, `path`, `visibility`

SHA-256: `c878f851e64b11db9e0dad34785d5ef3ba3baa753e380af72f554fe44529a850`

<a id="schema-reconstruction-library-match-schema-json"></a>

## `reconstruction/library-match.schema.json`

Static library recognition candidate

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.dev/schemas/reconstruction/library-match.schema.json`
- **Top-level type:** `object`
- **Required fields:** `match_id`, `subject_id`, `library_name`, `confidence`, `evidence`, `disposition`
- **Top-level properties:** `confidence`, `disposition`, `evidence`, `library_name`, `match_id`, `subject_id`, `version_range`

SHA-256: `cdf8967118c99e0f1d224829f1e3067a2b9db50f31ca945db68a3cec61b0f36e`

<a id="schema-reconstruction-module-schema-json"></a>

## `reconstruction/module.schema.json`

Recovered module hypothesis

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.dev/schemas/reconstruction/module.schema.json`
- **Top-level type:** `object`
- **Required fields:** `module_id`, `name`, `kind`, `confidence`, `evidence`
- **Top-level properties:** `confidence`, `evidence`, `kind`, `module_id`, `name`, `source_path`

SHA-256: `4aa87665cf31d30d9395bff7fb9388c9bd55257718808572669a874922436a4f`

<a id="schema-reconstruction-security-finding-schema-json"></a>

## `reconstruction/security-finding.schema.json`

Security finding

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.dev/schemas/reconstruction/security-finding.schema.json`
- **Top-level type:** `object`
- **Required fields:** `finding_id`, `rule_id`, `severity`, `subject_id`, `summary`, `evidence`, `status`
- **Top-level properties:** `evidence`, `finding_id`, `rule_id`, `severity`, `status`, `subject_id`, `summary`

SHA-256: `9a4f8a220e2e2d1d7dbc8116968bf2752d57a5725e18673faf59a192ace1826e`

<a id="schema-reconstruction-semantic-changeset-schema-json"></a>

## `reconstruction/semantic-changeset.schema.json`

Semantic changeset

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.dev/schemas/reconstruction/semantic-changeset.schema.json`
- **Top-level type:** `object`
- **Required fields:** `changeset_id`, `name`, `operations`, `status`
- **Top-level properties:** `base_audit_hash`, `changeset_id`, `name`, `operations`, `status`

SHA-256: `2cc66c0075ba39a54d86a20ca3705d4656ce90e922ce5a8c0b9357db1bc27b28`

<a id="schema-reconstruction-source-provenance-schema-json"></a>

## `reconstruction/source-provenance.schema.json`

Source provenance record

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.dev/schemas/reconstruction/source-provenance.schema.json`
- **Top-level type:** `object`
- **Required fields:** `provenance_id`, `source_path`, `line_start`, `line_end`, `binary_id`, `address_start`, `address_end`, `evidence`, `confidence`
- **Top-level properties:** `address_end`, `address_start`, `binary_id`, `confidence`, `evidence`, `line_end`, `line_start`, `provenance_id`, `source_path`

SHA-256: `d80a00434549c01f14f1afa7c43cb65b9eb653808b42fb5fa10f25b1d7ac1b0c`

<a id="schema-reconstruction-translation-unit-schema-json"></a>

## `reconstruction/translation-unit.schema.json`

Translation unit hypothesis

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `https://x86decomp.dev/schemas/reconstruction/translation-unit.schema.json`
- **Top-level type:** `object`
- **Required fields:** `unit_id`, `source_path`, `language`, `confidence`, `evidence`
- **Top-level properties:** `confidence`, `evidence`, `language`, `source_path`, `unit_id`

SHA-256: `ea17fb7bfec69c8e9e3eb5d14179194acece94ba90d5e0ad76c5f3e653dca642`

<a id="schema-release-gate-schema-json"></a>

## `release-gate.schema.json`

No schema title is declared.

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:release-gate:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `created_at`, `project_root`, `checks`, `requirements`, `failures`, `passed`, `truth_statement`
- **Top-level properties:** `checks`, `created_at`, `failures`, `kind`, `passed`, `project_root`, `requirements`, `schema_version`, `truth_statement`

SHA-256: `50e1f5a6cb46b67f833c881a7f025be5c7c047c1f23c3607608488afe17256cd`

<a id="schema-relink-manifest-schema-json"></a>

## `relink-manifest.schema.json`

Manifest-driven full relink

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:relink-manifest:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `linker`, `objects`, `output`, `arguments`, `environment`, `timeout_seconds`
- **Top-level properties:** `arguments`, `environment`, `inherit_environment`, `linker`, `objects`, `output`, `reference_image`, `schema_version`, `timeout_seconds`

SHA-256: `ca2b77b7be6b562589e841753a9afa8c6baf1fc7cf8c703409c90fc56507e890`

<a id="schema-reproduction-schema-json"></a>

## `reproduction.schema.json`

No schema title is declared.

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:reproduction:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `project_id`, `project_schema_version`, `binary`, `critical_files`, `tools`
- **Top-level properties:** `binary`, `content_store`, `created_at`, `critical_files`, `host`, `limitations`, `project_check`, `project_id`, `project_schema_version`, `schema_version`, `target_pack_check`, `toolkit_release`, `tools`

SHA-256: `aea350be271c7795406a2dd55096775e9d0b531215e05f43b75a9c6b5bd98281`

<a id="schema-security-audit-schema-json"></a>

## `security-audit.schema.json`

No schema title is declared.

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:security-audit:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `root`, `file_count`, `findings`, `severity_counts`, `passed`, `vulnerability_database_checked`
- **Top-level properties:** `created_at`, `file_count`, `findings`, `kind`, `limitations`, `passed`, `root`, `schema_version`, `severity_counts`, `total_bytes`, `vulnerability_database_checked`

SHA-256: `d62a14bd5c6d796dd52aee929ccfdf8e1265f825167070c8ffd680321a00b637`

<a id="schema-symbolic-memory-harness-schema-json"></a>

## `symbolic-memory-harness.schema.json`

Bounded symbolic memory and alias harness

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:symbolic-memory-harness:1`
- **Top-level type:** `object`
- **Required fields:** `architecture`, `regions`
- **Top-level properties:** `alias_constraints`, `alias_slots`, `architecture`, `input_registers`, `max_paths`, `max_steps`, `observe_memory`, `output_registers`, `regions`, `slot_stride`, `stack_argument_words`

SHA-256: `e7ce53b843c172758fc086503e040cd1c60a3836f528b2c8396a7e77ab7c200a`

<a id="schema-symbolic-memory-report-schema-json"></a>

## `symbolic-memory-report.schema.json`

Bounded angr symbolic memory-alias comparison

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:symbolic-memory-report:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `architecture`, `harness`, `target_execution`, `candidate_execution`, `equivalent_within_completed_model`, `scope_statement`, `universal_equivalence_claimed`
- **Top-level properties:** `architecture`, `candidate_execution`, `candidate_sha256`, `equivalent_within_completed_model`, `harness`, `kind`, `schema_version`, `scope_statement`, `target_execution`, `target_sha256`, `universal_equivalence_claimed`

SHA-256: `5e17dedb1bedf6581662f4cced118e40b8075957a161daea2abfab778d0298ba`

<a id="schema-symbolic-report-schema-json"></a>

## `symbolic-report.schema.json`

Bounded symbolic comparison report

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:symbolic-report:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `equivalent_within_model`, `scope_statement`
- **Top-level properties:** `equivalent_within_model`, `schema_version`, `scope_statement`

SHA-256: `cc596ec7c42bc74e7810dbf52bf50cba2d17375e9438f0a3fcbb3dae67a88e29`

<a id="schema-synthetic-corpus-schema-json"></a>

## `synthetic-corpus.schema.json`

Deterministic synthetic source corpus

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:synthetic-corpus:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `created_at`, `seed`, `cases_per_family`, `families`, `case_count`, `cases`, `truth_scope`
- **Top-level properties:** `case_count`, `cases`, `cases_per_family`, `created_at`, `families`, `kind`, `schema_version`, `seed`, `truth_scope`

SHA-256: `3c05d2c0a766021805afdd306d6a08068af6a24cdb0adb82fb3eca4d0f1d7c7d`

<a id="schema-target-decisions-schema-json"></a>

## `target-decisions.schema.json`

Operator-confirmed target decisions

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:target-decisions:1`
- **Top-level type:** `object`
- **Required fields:** `preferred_mode`, `compiler_family`, `compiler_version`, `linker_family`, `source_language`, `allow_host_execution`, `target_description`
- **Top-level properties:** `allow_host_execution`, `compiler_family`, `compiler_version`, `linker_family`, `preferred_mode`, `source_language`, `target_description`

SHA-256: `647192549c5e079a02e597648a0d3d2ade5078866f869b7e0da34324b5976ed6`

<a id="schema-target-pack-schema-json"></a>

## `target-pack.schema.json`

No schema title is declared.

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:target-pack:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `target_id`, `name`, `created_at`, `architecture`, `image_kind`, `primary_image`, `primary_sha256`, `default_modes`, `scope`, `decisions`, `artifacts`
- **Top-level properties:** `architecture`, `artifacts`, `created_at`, `decisions`, `default_modes`, `image_kind`, `name`, `primary_image`, `primary_sha256`, `schema_version`, `scope`, `target_id`

SHA-256: `867b89f3738ff1310340d078c5ae530f0087277e96cd00106fa1275cd0bcc954`

<a id="schema-test-bundle-report-schema-json"></a>

## `test-bundle-report.schema.json`

x86decomp Static Test Bundle Report

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:test-bundle-report:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `kind`, `archive`, `bundle`, `artifacts`, `analyses`, `errors`, `static_analysis_only`, `supplied_code_executed`, `passed`
- **Top-level properties:** `analyses`, `archive`, `artifacts`, `bundle`, `created_at`, `errors`, `kind`, `limitations`, `passed`, `schema_version`, `static_analysis_only`, `supplied_code_executed`

SHA-256: `482f5b618cd46eb5e815392f2655bb9fe4f3683e1f5122b8f7ab0ea69f8a2820`

<a id="schema-test-bundle-schema-json"></a>

## `test-bundle.schema.json`

x86decomp Authorized Static Test Bundle

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:test-bundle:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `authorization`, `artifacts`
- **Top-level properties:** `artifacts`, `authorization`, `description`, `expected_architecture`, `name`, `schema_version`

SHA-256: `398d162a3ccc9e3bd1e984af67efbfaf12a840f4013b406c0cf8d150f490deab`

<a id="schema-type-constraint-schema-json"></a>

## `type-constraint.schema.json`

Type/ABI constraint record

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:type-constraint:1`
- **Top-level type:** `object`
- **Required fields:** `subject_entity`, `relation`, `object_value`, `provenance`, `status`
- **Top-level properties:** `confidence`, `constraint_id`, `evidence_id`, `object_value`, `provenance`, `relation`, `status`, `subject_entity`

SHA-256: `f98328b457deccc685ea8be764507320d5ff94deddb366e47c5018a678baa59d`

<a id="schema-verification-schema-json"></a>

## `verification.schema.json`

x86decomp byte verification report

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:verification:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `created_at`, `equal`, `target_size`, `candidate_size`, `target_sha256`, `candidate_sha256`, `matching_prefix_bytes`, `matching_suffix_bytes`, `sequence_similarity`, `reported_mismatches`, `mismatch_report_truncated`, `semantic_equivalence_claimed`
- **Top-level properties:** `candidate_sha256`, `candidate_size`, `created_at`, `equal`, `matching_prefix_bytes`, `matching_suffix_bytes`, `mismatch_report_truncated`, `reported_mismatches`, `schema_version`, `semantic_equivalence_claimed`, `sequence_similarity`, `target_sha256`, `target_size`

SHA-256: `a70e3422e6b0bec967695257c7b66d44f17a0cfe3f15d99799eb1c038ccb7fa0`

<a id="schema-work-task-schema-json"></a>

## `work-task.schema.json`

Validator-gated work item

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:work-task:1`
- **Top-level type:** `object`
- **Required fields:** `id`, `function_id`, `mode`, `kind`, `status`, `priority`, `instructions`, `required_validators`, `validator_results`, `evidence_ids`, `created_at`, `updated_at`
- **Top-level properties:** `assignee`, `created_at`, `evidence_ids`, `function_id`, `id`, `instructions`, `kind`, `mode`, `priority`, `proposal`, `required_validators`, `status`, `updated_at`, `validator_results`

SHA-256: `36794b2e24e785918a28d8bd7f5fedd100c090ed64030c71eefa0a8c933b92c9`

<a id="schema-worker-report-schema-json"></a>

## `worker-report.schema.json`

No schema title is declared.

- **Meta-schema:** `https://json-schema.org/draft/2020-12/schema`
- **$id:** `urn:x86decomp:schema:worker-report:1`
- **Top-level type:** `object`
- **Required fields:** `schema_version`, `status`, `command`, `isolation`, `isolation_strength`, `input_hashes`, `output_hashes`
- **Top-level properties:** `command`, `duration_seconds`, `error`, `input_hashes`, `isolation`, `isolation_strength`, `output_hashes`, `returncode`, `schema_version`, `started_at`, `status`, `stderr_path`, `stderr_truncated`, `stdout_path`, `stdout_truncated`

SHA-256: `f4fee8d629c5e963519a4f5ab25c4bb0856592421ee218fe7d047b5ebe089b3c`
