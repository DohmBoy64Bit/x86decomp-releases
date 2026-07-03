# Changelog

## 0.7.5 — Unified current release

- Added the canonical `llm` capability group with provider discovery, profile creation and validation, endpoint probing, deterministic prompt materialization, one-shot generation, bounded exact-match loops, and report verification.
- Added local provider presets for LM Studio, Ollama, llama.cpp server, vLLM, LocalAI, and generic OpenAI-compatible endpoints.
- Added strict model-response and C-source contracts, loopback-only defaults, same-origin redirects, bounded HTTP I/O, environment-variable secrets, and remote-endpoint opt-in.
- Reused the deterministic compiler, COFF parser, relocation resolver, and raw byte comparator so model output cannot self-validate.
- Added four local-LLM schemas, three runnable examples, dedicated mock-server tests, and a real Clang-to-COFF exact-match retry test.
- Expanded the exact current interface to 34 canonical groups, 181 routes, 141 root commands, 97 schemas, and 36 adapter declarations.
- Consolidated every retained capability into the current feature-oriented packages: `governance`, `reconstruction`, `native`, and `assembly`.
- Made `x86decomp` the only toolkit executable and `x86decomp-test` the only verification executable.
- Removed version-specific executables, command bridges, deprecated executable shims, source-tree installers, embedded overlays, rollback payloads, and upgrade reports.
- Replaced release-numbered modules and tests with capability-oriented modules and one current contract.
- Rebuilt the recursive feature catalog around the complete current module, function, command, route, schema, adapter, and workflow inventories.
- Added hard checks that reject historical release references, versioned executable definitions, upgrade artifacts, stale catalog entries, placeholders, and missing current documentation.
- Preserved every prior capability while expanding the current interface to 34 groups and 181 routes; byte-form assembly remains the default.
- Synchronized the toolkit, test suite, schemas, examples, skill, architecture maps, package metadata, and verification documentation.

### Windows compatibility fixes
- Fixed `discover_assembler` to fall back to `C:\Program Files\LLVM\bin\clang.exe` on Windows when `shutil.which()` does not find clang.
- Fixed `StoredArtifact.to_dict()` to use `.as_posix()` for cross-platform forward-slash path rendering.
- Fixed `PluginRegistry.invoke()` and `run_dependency_vulnerability_audit()` to prepend `sys.executable` on Windows when the target script is not directly executable.

Earlier release history is retained in source-control tags and published release archives, not in the active 0.7.5 source tree.
