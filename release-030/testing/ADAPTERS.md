# Adapter detection and installation contract

## Non-prompting rule

For each adapter, detection always runs before any interactive question. An installed adapter is accepted and produces no prompt. Only unresolved adapters enter the custom-path/install flow.

## Detection sources

1. `adapter_paths` in the test configuration.
2. Adapter-specific environment variables.
3. Executables found on `PATH`.
4. Known Ghidra and Visual Studio locations where applicable.
5. Python module importability for Python adapters.

Executable aliases and symlink names are preserved. This matters for multi-call binaries such as `lld`, where invoking the `lld-link` alias selects COFF-linker behavior.

## Interactive missing-adapter flow

For a missing adapter the suite asks:

```text
Is it already installed at a custom path? [y/N]
```

When the answer is yes, it repeatedly validates a supplied executable or installation root until it succeeds or the user submits a blank value. A successful path is saved to the configuration.

When no valid custom path is provided, the suite may offer automatic installation. Installation does not happen unless `allow_install` is enabled. Network installers also require `allow_network`.

## Installation mechanisms

| Adapter type | Mechanism |
|---|---|
| Python packages | `python -m pip install <pinned range>` |
| Ghidra, DynamoRIO, objdiff | Official GitHub release asset, bounded download, SHA-256 log, safe extraction |
| Java, LLVM tools, GCC, CMake, Ninja | Supported operating-system package manager |
| Historical/proprietary MSVC | User-owned custom path only |

Downloaded archives reject absolute paths, `..` traversal, symbolic links, hard links, and excessive member counts. Downloads have a maximum byte limit and are hashed.

## Live probes

A resolved adapter is not considered tested merely because its executable exists:

- Python adapters are imported.
- C/C++ compilers compile a real source fixture.
- Clang emits Windows COFF objects.
- `lld-link` links a minimal Windows PE image.
- Ghidra imports a minimal PE and runs the toolkit exporters.
- DynamoRIO runs `drcov` against a harmless host executable.
- objdiff executes its CLI help path.
- Generic tools execute their version probe.

If a tool is absent, the corresponding live probe is `BLOCKED`; it is never reported as passed or omitted.

## CI/non-interactive mode

Use:

```json
{
  "interactive": false,
  "strict": true,
  "allow_install": false,
  "allow_network": false
}
```

Provide custom tool paths in `adapter_paths` or environment variables. Strict mode exits `2` when any adapter-backed test remains blocked.
