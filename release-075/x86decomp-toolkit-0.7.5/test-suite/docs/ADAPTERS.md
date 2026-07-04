# Adapter detection, installation, and live-test contract

## Detection order

Every adapter is resolved before any prompt:

1. saved custom path;
2. adapter-specific environment variable;
3. system `PATH` or Python importability;
4. known platform locations;
5. interactive resolution only when still missing.

Detected tools produce no question. Only a missing adapter triggers:

```text
Is it already installed at a custom path? [y/N]
```

A custom executable, interpreter, virtual-environment root, or installation directory
is validated before persistence.

## Installation consent

Automatic installation requires `allow_install=true`. Network-backed installation also
requires `allow_network=true`. Commands and downloads are logged before execution.
Historical/proprietary MSVC is user-owned custom-path only.

## Adapter families

- Python/testing: Python, pytest, coverage, jsonschema, javalang, PyYAML, build.
- Analysis/validation: Capstone, Unicorn, Z3, angr, LIEF, FastAPI, Uvicorn.
- Native tools: Java, Ghidra, DynamoRIO, objdiff, Clang/Clang++, GCC/G++, LLD,
  LLVM librarian/readobj/objdump, CMake, Ninja.
- Production hardening: pip-audit and Docker/Podman container runtime.
- Local inference runtimes: LM Studio (`lms`), Ollama, llama.cpp server, vLLM, and LocalAI.
- Proprietary toolchain: operator-owned MSVC.

## Live probes

Existence is insufficient. Resolved adapters perform a real bounded operation:

- Python packages import and report versions.
- C/C++ compilers build fixtures; Clang emits Windows COFF.
- `lld-link` produces a minimal Windows PE.
- LLVM tools inspect or archive real objects.
- Ghidra imports a generated PE and runs maintained exporters.
- DynamoRIO runs `drcov` over a harmless suite-owned host fixture.
- objdiff executes the declared CLI path.
- pip-audit scans the selected environment and preserves its report.
- Docker/Podman executes a bounded capability/version probe; target workers still
  require an explicitly declared image and policy.
- Local inference runtimes execute bounded version/help probes only; model download, model loading,
  prompt execution, and network-backed installation remain explicit operator actions.

Unresolved tools become `BLOCKED`, never passed or silently skipped.

## Download safety

Downloaded archives are bounded by bytes/member count, hashed, and extracted through a
path-confined routine rejecting absolute paths, traversal, symlinks, hard links, and
special files. A logged hash establishes byte identity, not publisher authenticity;
release policy should pin vendor checksums/signatures where available.
