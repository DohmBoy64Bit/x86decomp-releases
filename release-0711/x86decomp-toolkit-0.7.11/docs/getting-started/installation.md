# Installation

## Prerequisites

| Requirement | Minimum | Notes |
|---|---|---|
| **Python** | 3.11+ | Check with `python --version`. Python 3.11, 3.12, and 3.13 are supported. |
| **pip** | Bundled with Python 3.11+ | Use `python -m pip` to guarantee the correct pip is invoked. |
| **Operating system** | Windows, Linux, macOS | The toolkit is pure Python with optional native-external tool adapters. |

### Optional external tools

x86decomp integrates with external tools for specific capability groups. None are required for
basic PE parsing, project initialization, or evidence tracking.

| Tool | Purpose | Required for |
|---|---|---|
| **Ghidra** (11.x+) | Headless decompilation, disassembly, type recovery | `ghidra-export`, MCP integration, `crosscheck-ghidra` |
| **DynamoRIO** | Runtime coverage tracing | `drcov-run`, `drcov-parse` |
| **Capstone** (5.0.6+) | Native disassembly | `disassemble`, `symbolic-validate`, `crosscheck-ghidra` |
| **Unicorn** (2.1.4+) | Emulation-based dynamic validation | `dynamic-validate` |
| **Z3** (4.15+) | Symbolic equivalence checking | `symbolic-validate` |
| **angr** (9.2+) | Advanced symbolic analysis with memory aliasing | `angr-validate`, `symbolic-memory-validate` |
| **LIEF** (0.17+) | Extended PE manipulation | PE patching, section manipulation |
| **objdiff-cli** | objdiff-compatible comparison | `objdiff-run` |

!!! tip "Install extras selectively"
    Use pip extras to pull in tool-specific dependencies. See [Optional extras](#optional-extras) below.

---

## Installation

### From the wheel

```console
$ python -m pip install x86decomp_toolkit-0.7.11-py3-none-any.whl
```

### From source

```console
$ git clone <repository-url> x86decomp-toolkit
$ cd x86decomp-toolkit
$ python -m pip install .
```

### Optional extras

Install extras to pull in tool-specific Python dependencies:

```console
$ python -m pip install 'x86decomp-toolkit[disassembly]'     # Capstone
$ python -m pip install 'x86decomp-toolkit[dynamic]'          # Unicorn
$ python -m pip install 'x86decomp-toolkit[symbolic]'         # Capstone + Z3
$ python -m pip install 'x86decomp-toolkit[angr]'             # angr
$ python -m pip install 'x86decomp-toolkit[service]'          # FastAPI + uvicorn
$ python -m pip install 'x86decomp-toolkit[pe]'               # LIEF
```

Combine multiple extras:

```console
$ python -m pip install 'x86decomp-toolkit[disassembly,dynamic,symbolic]'
```

Install everything:

```console
$ python -m pip install 'x86decomp-toolkit[full,pe]'
```

Install the development stack:

```console
$ python -m pip install 'x86decomp-toolkit[dev]'
```

The `[dev]` extra includes pytest, jsonschema, PyYAML, build, pyflakes, ruff, pyright, and
the MkDocs Material stack for documentation.

| Extra | Packages pulled in |
|---|---|
| `[disassembly]` | `capstone>=5.0.6,<6` |
| `[dynamic]` | `unicorn>=2.1.4,<3` |
| `[symbolic]` | `capstone>=5.0.6,<6`, `z3-solver>=4.15,<5` |
| `[angr]` | `angr>=9.2,<10` |
| `[service]` | `fastapi>=0.128,<1`, `uvicorn>=0.48,<1` |
| `[pe]` | `lief>=0.17,<0.18` |
| `[full]` | All of `disassembly`, `dynamic`, `symbolic`, `service`, `angr` |
| `[dev]` | `pytest`, `jsonschema`, `javalang`, `PyYAML`, `build`, `pyflakes`, `ruff`, `pyright`, `mkdocs`, `mkdocs-material` |
| `[docs]` | `mkdocs>=1.6,<2`, `mkdocs-material>=9.6,<10` |

---

## Verify installation

```console
$ x86decomp --version
x86decomp 0.7.11
```

If the command is not found, ensure your Python `Scripts` or `bin` directory is on `PATH`:

```console
$ python -m x86decomp --version
x86decomp 0.7.11
```

---

## Environment setup

### Ghidra

Set the `GHIDRA_HOME` environment variable to the Ghidra installation root, or pass
`--ghidra-home` to commands that need it:

```console
$ export GHIDRA_HOME=/opt/ghidra_11.2_PUBLIC
```

On Windows (PowerShell):

```powershell
$ $env:GHIDRA_HOME = "C:\Tools\ghidra_11.2_PUBLIC"
```

The toolkit locates the `analyzeHeadless` launcher under `$GHIDRA_HOME/support/`. It prefers
`analyzeHeadless.bat` on Windows and `analyzeHeadless` on Linux/macOS.

### DynamoRIO

For coverage tracing (`drcov-run`), pass the `--drrun` path to the DynamoRIO `drrun` executable,
or ensure it is on `PATH`.

### Compiler toolchains

Compiler laboratory commands (`compile`, `compiler-lab`) locate `gcc`, `clang`, and other
compilers via `PATH`. Use `toolchain-register` to record toolchain versions and executables
in a versioned registry for reproducible builds:

```console
$ x86decomp toolchain-register registry.json msvc-19.40 msvc 19.40 \
    --executable "cc=cl.exe" --executable "link=link.exe"
```

---

## Snapshot tools

Run `snapshot-tools` to probe and record the availability and versions of external tools:

```console
$ x86decomp snapshot-tools --output tools.json --ghidra-home /opt/ghidra_11.2_PUBLIC
```

Output:

```json
{
  "schema_version": 1,
  "captured_at": "2026-07-11T14:22:31.123456Z",
  "tools": {
    "python": {
      "available": true,
      "path": "/usr/bin/python3",
      "version": "Python 3.12.4",
      "return_code": 0
    },
    "gcc": {
      "available": true,
      "path": "/usr/bin/gcc",
      "version": "gcc (GCC) 13.2.0",
      "return_code": 0
    },
    "clang": {
      "available": true,
      "path": "/usr/bin/clang",
      "version": "clang version 18.1.8",
      "return_code": 0
    },
    "objdiff-cli": {
      "available": true,
      "path": "/usr/local/bin/objdiff-cli",
      "version": "objdiff-cli 2.6.0",
      "return_code": 0
    },
    "java": {
      "available": true,
      "path": "/usr/bin/java",
      "version": "openjdk version \"21.0.3\" 2024-04-16 LTS",
      "return_code": 0
    },
    "ghidra-analyzeHeadless": {
      "available": true,
      "path": "/opt/ghidra_11.2_PUBLIC/support/analyzeHeadless"
    }
  }
}
```

!!! note
    Missing tools appear with `"available": false`. The `snapshot-tools` command does not fail
    on missing tools; it records the current environment state for later reproducibility checks.

---

## Next steps

- [Create your first project](first-project.md)
- [Understand verification](verification.md)
- [Browse command reference](../commands/index.md)
