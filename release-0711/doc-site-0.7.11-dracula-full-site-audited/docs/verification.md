---
title: Verification
description: Verification summary for x86decomp 0.7.11.
---

# Verification

Summary from `RELEASE_VERIFICATION.json` and `SECOND_AUDIT_FIX_VERIFICATION_0.7.11.json`.

## Release summary

- Release: **0.7.11**
- Summary: Second-audit fix release for the current unified toolkit surface.
- Root commands: **166**
- Canonical groups/routes: **59 / 239**
- Schemas: **97**
- Adapters: **37**

## Completed checks

| Check | Result |
| --- | --- |
| clean_wheel_install_and_pip_check | PASS |
| compileall | PASS |
| documentation_architecture_tests | 7 passed |
| final_compileall_before_packaging | PASS |
| final_extracted_zip_compileall_pyflakes_validate_contracts | PASS |
| final_extracted_zip_source_manifest_verify | PASS: root 449/449, test-suite 63/63 |
| final_pyflakes_before_packaging | PASS |
| final_validate_contracts_before_packaging | PASS |
| pyflakes_src_scripts_testsuite_src | PASS |
| release_contract_tests | 9 passed |
| targeted_second_audit_tests | 7 passed |
| validate_contracts | PASS |
| wheels_sdists_built | PASS |

## Not claimed

- single monolithic pytest tests completion
- live external local-model runtime availability or model quality
- single monolithic pytest tests completion
- live external local-LLM runtime quality/availability
