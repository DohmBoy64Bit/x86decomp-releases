# Worker Commands

Local worker capability reporting and bounded compilation worker execution.

## `worker-capabilities`

Report local worker and tool capabilities.

```bash
x86decomp worker-capabilities
```

No arguments. Discovers and reports the local environment's worker capabilities: installed compilers, toolchains, Ghidra availability, Python version, platform details, and available validation backends.

### Example

```bash
x86decomp worker-capabilities
```

```json
{
  "platform": "win32",
  "python_version": "3.11.4",
  "available_toolchains": ["msvc-2019-x86", "msvc-2019-x86_64"],
  "ghidra_available": true,
  "angr_available": false,
  "dynamorio_available": true
}
```

---

## `compile-worker`

Run a bounded local or containerized compilation worker.

```bash
x86decomp compile-worker PROFILE SOURCE OUTPUT \
  --isolation {local_bounded,container} \
  --container-image IMAGE \
  --cache PATH \
  --report PATH
```

| Argument | Required | Description |
|---|---|---|
| `PROFILE` | yes | Path to the compiler profile |
| `SOURCE` | yes | Path to the source file to compile |
| `OUTPUT` | yes | Path for the compiled output |
| `--isolation` | no | Isolation mode: `local_bounded` (default) or `container` |
| `--container-image` | no | Container image name (required when `--isolation container`) |
| `--cache` | no | Cache directory for compiler artifacts |
| `--report` | no | Path for the compilation report |

!!! note "Cross-reference"
    Related: [`compile`](../compilation/compile.md) — compile one source file under a declared compiler profile (non-worker variant).

### Examples

```bash
# Local bounded compilation
x86decomp compile-worker ./profiles/msvc-2019-x86.json \
  ./src/00401000.c ./build/00401000.obj \
  --cache ./build/cache \
  --report ./reports/compile-401000.json

# Containerized compilation
x86decomp compile-worker ./profiles/msvc-2019-x86.json \
  ./src/00401000.c ./build/00401000.obj \
  --isolation container \
  --container-image msvc-2019:latest
```
