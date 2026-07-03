# x86decomp-toolkit 0.7.5 release verification

**Status: PASS**

## Release surface

- 141 root commands
- 34 canonical capability groups
- 181 canonical routes
- 113 toolkit modules
- 879 toolkit function/method bodies
- 97 JSON Schemas
- 36 adapters
- 6 local-model provider presets

## Tests and harness

- Distinct release tests: **223/223 passed** with zero failures, errors, or skips.
- Dedicated local-LLM tests: **8/8 passed**.
- Comprehensive harness: **191 PASS, 11 BLOCKED, 0 FAIL, 0 ERROR**.
- Function/method bodies executed: **879/879**.
- Statement coverage: **78.89%** against a 70% floor.
- Branch coverage: **51.73%** against a 50% floor.

Blocked external adapters: `container-runtime, dynamorio, ghidra, llama-server, llvm-readobj, lm-studio, localai, msvc, objdiff, ollama, vllm`.

## Packaging

- Root source manifest: **427/427**.
- Test-suite source manifest: **60/60**.
- Toolkit and test-suite wheels reproduced byte-for-byte.
- Setuptools sdist contents were identical but archive metadata varied; final sdists were canonicalized and reproduced byte-for-byte with fixed metadata.
- Both canonical sdists rebuilt into wheels successfully.
- Fresh wheel installation passed `pip check` and all installed CLI smoke tests.

## Documentation

- Material for MkDocs 9.7.6 / MkDocs 1.6.1.
- **366** source pages and **367** built HTML pages.
- **366/366** pages indexed by Material search.
- **20779** local links, fragments, and assets checked.
- **0** external runtime assets.
- Consecutive canonical builds reproduced byte-for-byte.

## Local-model claim boundary

The model proposes C only. It cannot verify or promote its own output. Exact matching is accepted only after deterministic compilation, symbol extraction, complete relocation resolution, equal length, and byte-for-byte identity with the declared contiguous target range. No live model-quality benchmark is claimed for the blocked inference runtimes.
