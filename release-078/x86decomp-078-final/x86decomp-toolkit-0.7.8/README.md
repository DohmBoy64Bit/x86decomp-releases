# x86decomp-toolkit 0.7.8

x86decomp-toolkit is an evidence-governed toolkit for authorized x86 and x86-64 Windows binary analysis, reconstruction, validation, and reproducible release work.

## Unified interface

The toolkit exposes one executable:

```bash
x86decomp --help
x86decomp commands
x86decomp <group> <action> [options]
```

The current interface contains 34 capability groups and 181 canonical routes. There are no version-specific executables, command bridges, source-tree installers, embedded release overlays, or upgrade reports.

The separately packaged verification harness exposes one executable:

```bash
x86decomp-test --help
```

## Install

```bash
python -m pip install x86decomp_toolkit-0.7.8-py3-none-any.whl
```

Install the complete optional analysis and development stack when needed:

```bash
python -m pip install 'x86decomp-toolkit[full,pe,dev]'
```

## First project

Inspect the available current commands:

```bash
x86decomp commands
x86decomp commands --owner governance
x86decomp project --help
```

Initialize the project data plane used by the unified capability commands:

```bash
x86decomp project --project ./work init
x86decomp project --project ./work check
```

Initialize a binary-analysis project through the core command plane:

```bash
x86decomp init ./target.exe ./analysis-project
x86decomp verify-project ./analysis-project
```

## Local LLM proposal and byte-match loop

The `llm` capability group supports LM Studio, Ollama, llama.cpp server, vLLM, LocalAI, and generic OpenAI-compatible local endpoints. Model output remains an untrusted proposal until the deterministic compiler, COFF, relocation, and raw byte-identity gates pass.

```bash
x86decomp llm providers
x86decomp llm profile-create ollama ./ollama.json --model qwen2.5-coder
x86decomp llm prompt ./job.json ./prompt.json
x86decomp llm match ./ollama.json ./compiler-profile.json ./job.json ./llm-output
x86decomp llm verify ./llm-output/report.json
```

Endpoints are loopback-only by default, secrets are referenced through environment variables, redirects cannot cross origins, and accepted reports require zero unresolved relocations. See `docs/local-llm.md`.

## Assembly output

Byte-form assembly is the exact, conservative default. Annotated and mnemonic modes are explicit alternatives. Unsupported or non-reproducible encodings fall back to bytes rather than claiming an exact round trip.

```bash
x86decomp asm --project ./work materialize --help
```

## Verification

From an extracted source tree, verify the pinned source hashes and run the complete current contract:

```bash
make verify
```

Regenerate the deterministic source manifests only after an intentional reviewed source change:

```bash
make hashes
make verify-hashes
```

Run the comprehensive adapter-aware harness:

```bash
x86decomp-test init-config \
  --toolkit-root . \
  --output-root ./test-results \
  --install-root ./.x86decomp-test-tools \
  --config ./x86decomp-test.json
x86decomp-test run --config ./x86decomp-test.json --verbose
```

The run command creates the configured output directory and a unique run subdirectory containing logs and reports.

## Operating principles

- Observations, derivations, hypotheses, decisions, and verified claims remain distinct.
- Unknowns and blocked external integrations are reported explicitly.
- Native execution requires explicit authorization and isolation.
- No placeholder implementation, fake adapter, silent skip, or fabricated success is permitted.
- A capability may be removed only after a complete tested successor supersedes it.
- The current source tree represents one release only: 0.7.8.

See `docs/architecture.md`, `docs/supported-scope.md`, `docs/build-and-verification.md`, and `SECURITY.md` for the current operating contract.


## 0.7.8 adapter-capability note

The test harness now records protocol capabilities separately from product adapter identities. `lm-studio-http` can satisfy OpenAI-compatible local-LLM coverage through a loopback `/v1/models` probe without marking `ollama`, `llama-server`, `localai`, or `vllm` as installed.
