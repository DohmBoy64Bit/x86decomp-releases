---
title: tests/test_local_llm.py
description: Source-derived reference for 8 collected test nodes.
---

# `tests/test_local_llm.py`

**Collected nodes:** 8  
**Source SHA-256:** `6e876be44e16786200b013fb530103cf7ad7e3c145af0582cee5cb00cbcd5b98`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_provider_profiles_and_loopback_policy`

No test docstring is declared.

**Direct call names in source:** `create_profile`, `load_profile`, `provider_catalog`, `pytest.raises`, `validate_profile`  
**Node ID:** `tests/test_local_llm.py::test_provider_profiles_and_loopback_policy`  
**Area:** Toolkit behavior  
**Source line:** 145

## `test_prompt_is_deterministic_and_marks_injected_evidence_untrusted`

No test docstring is declared.

**Direct call names in source:** `_write_job`, `build_messages`, `first['trust_boundary'].startswith`, `load_job`, `messages[0]['content'].lower`, `prompt_record`  
**Node ID:** `tests/test_local_llm.py::test_prompt_is_deterministic_and_marks_injected_evidence_untrusted`  
**Area:** Toolkit behavior  
**Source line:** 160

## `test_openai_generation_and_structured_output_fallback`

No test docstring is declared.

**Direct call names in source:** `_candidate_payload`, `_good_source`, `_server`, `_write_job`, `create_profile`, `generate_candidate`, `json.dumps`, `output.read_text`, `pytest.raises`  
**Node ID:** `tests/test_local_llm.py::test_openai_generation_and_structured_output_fallback`  
**Area:** Toolkit behavior  
**Source line:** 172

## `test_ollama_probe_accepts_latest_tag_only_for_ollama`

No test docstring is declared.

**Direct call names in source:** `_server`, `create_profile`, `load_profile`, `probe_profile`  
**Node ID:** `tests/test_local_llm.py::test_ollama_probe_accepts_latest_tag_only_for_ollama`  
**Area:** Toolkit behavior  
**Source line:** 198

## `test_same_origin_redirect_rejects_cross_origin`

No test docstring is declared.

**Direct call names in source:** `_server`, `create_profile`, `load_profile`, `probe_profile`, `pytest.raises`  
**Node ID:** `tests/test_local_llm.py::test_same_origin_redirect_rejects_cross_origin`  
**Area:** Toolkit behavior  
**Source line:** 211

## `test_exact_byte_match_loop_and_tamper_detection`

No test docstring is declared.

**Direct call names in source:** `(output / 'accepted.c').write_text`, `_candidate_payload`, `_clang_profile`, `_good_source`, `_server`, `_write_job`, `create_profile`, `extract_symbol`, `good_source_path.write_text`, `json.dumps`, `parse_coff`, `pytest.raises`, `run_compiler_profile`, `run_match_loop`, `verify_match_report`  
**Node ID:** `tests/test_local_llm.py::test_exact_byte_match_loop_and_tamper_detection`  
**Area:** Toolkit behavior  
**Source line:** 222

## `test_candidate_contract_rejects_inline_assembly_and_multiple_functions`

No test docstring is declared.

**Direct call names in source:** `_candidate_payload`, `_parse_candidate`, `json.dumps`, `pytest.raises`  
**Node ID:** `tests/test_local_llm.py::test_candidate_contract_rejects_inline_assembly_and_multiple_functions`  
**Area:** Toolkit behavior  
**Source line:** 254

## `test_local_llm_helper_bodies_are_exercised`

Exercise bounded helper paths required by the all-function coverage gate.

**Direct call names in source:** `_feedback_from_diff`, `_ollama_body`, `load_job`, `mnemonic_path.write_text`, `resolved_addresses_are_loopback`, `write_json`  
**Node ID:** `tests/test_local_llm.py::test_local_llm_helper_bodies_are_exercised`  
**Area:** Toolkit behavior  
**Source line:** 269
