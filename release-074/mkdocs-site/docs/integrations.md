---
title: Integrations and adapters
description: Exact v0.7.4 adapter specifications
original_path: integrations.html
---

<a id="adapter-angr"></a>
<a id="adapter-build"></a>
<a id="adapter-capstone"></a>
<a id="adapter-clang"></a>
<a id="adapter-clangxx"></a>
<a id="adapter-cmake"></a>
<a id="adapter-container-runtime"></a>
<a id="adapter-coverage"></a>
<a id="adapter-dynamorio"></a>
<a id="adapter-fastapi"></a>
<a id="adapter-gcc"></a>
<a id="adapter-ghidra"></a>
<a id="adapter-gxx"></a>
<a id="adapter-java"></a>
<a id="adapter-javalang"></a>
<a id="adapter-jsonschema"></a>
<a id="adapter-lief"></a>
<a id="adapter-lld-link"></a>
<a id="adapter-llvm-lib"></a>
<a id="adapter-llvm-objdump"></a>
<a id="adapter-llvm-readobj"></a>
<a id="adapter-msvc"></a>
<a id="adapter-ninja"></a>
<a id="adapter-objdiff"></a>
<a id="adapter-pip-audit"></a>
<a id="adapter-pytest"></a>
<a id="adapter-python"></a>
<a id="adapter-pyyaml"></a>
<a id="adapter-unicorn"></a>
<a id="adapter-uvicorn"></a>
<a id="adapter-z3"></a>

Section: Exact adapter catalog

# Integrations and adapters

All 31 adapter specifications declared by `test-suite/src/x86decomp_testkit/adapters/catalog.py`.

> **Important:** The source catalog marks most adapters `optional=False` for the comprehensive harness. Missing adapters are reported as BLOCKED rather than silently skipped; the `msvc` adapter is explicitly optional and user-owned.

angr — angr

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `angr`, `symbolic-memory`

**Executable candidates:** none

**Python modules:** `angr`

**Environment variables:** none

**Pip requirement:** `angr>=9.2,<10`

build — Python build

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `packaging`

**Executable candidates:** none

**Python modules:** `build`

**Environment variables:** none

**Pip requirement:** `build>=1.2,<2`

capstone — Capstone Python bindings

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `disassembly`, `matching`, `symbolic`

**Executable candidates:** none

**Python modules:** `capstone`

**Environment variables:** none

**Pip requirement:** `capstone>=5.0.6,<6`

clang — Clang C compiler

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `compiler`, `corpus`, `coff`

**Executable candidates:** `clang`, `clang.exe`

**Python modules:** none

**Environment variables:** `CLANG`

Install LLVM/Clang or select the clang executable.

clangxx — Clang C++ compiler

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `compiler`, `corpus`, `cpp`

**Executable candidates:** `clang++`, `clang++.exe`

**Python modules:** none

**Environment variables:** `CLANGXX`

Install LLVM/Clang or select the clang++ executable.

cmake — CMake

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `native-build`

**Executable candidates:** `cmake`, `cmake.exe`

**Python modules:** none

**Environment variables:** none

Install CMake or select cmake.

container-runtime — Docker or Podman container runtime

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `isolated-workers`, `compiler-worker`

**Executable candidates:** `docker`, `podman`, `docker.exe`, `podman.exe`

**Python modules:** none

**Environment variables:** none

Install Docker or Podman, or select an existing runtime executable.

coverage — coverage.py

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `coverage`, `public-api`

**Executable candidates:** none

**Python modules:** `coverage`

**Environment variables:** none

**Pip requirement:** `coverage>=7,<8`

dynamorio — DynamoRIO

**Kind:** `directory` · **Optional flag:** `false`

**Verification suites:** `drcov-live`, `runtime-tracing`

**Executable candidates:** `drrun`, `drrun.exe`

**Python modules:** none

**Environment variables:** `DYNAMORIO_HOME`

Download a DynamoRIO release package and select its extracted root or drrun executable.

fastapi — FastAPI

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `service`

**Executable candidates:** none

**Python modules:** `fastapi`

**Environment variables:** none

**Pip requirement:** `fastapi>=0.128,<1`

gcc — GCC C compiler

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `compiler-regression`

**Executable candidates:** `gcc`, `gcc.exe`

**Python modules:** none

**Environment variables:** none

Install GCC or select gcc.

ghidra — Ghidra

**Kind:** `directory` · **Optional flag:** `false`

**Verification suites:** `ghidra-live`, `pcode`, `decompiler`

**Executable candidates:** `analyzeHeadless`, `analyzeHeadless.bat`

**Python modules:** none

**Environment variables:** `GHIDRA_HOME`

Download an official Ghidra release archive and extract it; select the extracted root directory.

gxx — GCC C++ compiler

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `compiler-regression`

**Executable candidates:** `g++`, `g++.exe`

**Python modules:** none

**Environment variables:** none

Install GCC or select g++.

java — Java runtime

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `ghidra`

**Executable candidates:** `java`

**Python modules:** none

**Environment variables:** `JAVA_HOME`

Install a Java version supported by the selected Ghidra release.

javalang — javalang

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `ghidra-static`

**Executable candidates:** none

**Python modules:** `javalang`

**Environment variables:** none

**Pip requirement:** `javalang>=0.13,<1`

jsonschema — jsonschema

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `contracts`

**Executable candidates:** none

**Python modules:** `jsonschema`

**Environment variables:** none

**Pip requirement:** `jsonschema>=4.23,<5`

lief — LIEF

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `independent-pe`

**Executable candidates:** none

**Python modules:** `lief`

**Environment variables:** none

**Pip requirement:** `lief>=0.17,<0.18`

lld-link — LLD COFF linker

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `relink`, `whole-image`

**Executable candidates:** `lld-link`, `lld-link.exe`

**Python modules:** none

**Environment variables:** `LLD_LINK`

Install LLVM/LLD or select lld-link.

llvm-lib — LLVM librarian

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `coff-archive`

**Executable candidates:** `llvm-lib`, `llvm-lib.exe`, `llvm-ar`

**Python modules:** none

**Environment variables:** none

Install LLVM tools or select llvm-lib/llvm-ar.

llvm-objdump — LLVM objdump

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `independent-disassembly`

**Executable candidates:** `llvm-objdump`, `llvm-objdump.exe`

**Python modules:** none

**Environment variables:** none

Install LLVM tools or select llvm-objdump.

llvm-readobj — LLVM object inspector

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `independent-coff`

**Executable candidates:** `llvm-readobj`, `llvm-readobj.exe`

**Python modules:** none

**Environment variables:** none

Install LLVM tools or select llvm-readobj.

msvc — User-owned Microsoft C/C++ toolchain

**Kind:** `toolchain` · **Optional flag:** `true`

**Verification suites:** `historical-msvc`, `matching`

**Executable candidates:** `cl.exe`, `link.exe`

**Python modules:** none

**Environment variables:** `VCINSTALLDIR`, `VSINSTALLDIR`

Select an authorized Visual C++ installation root or Developer Command Prompt environment. Historical proprietary compilers are never downloaded by this suite.

ninja — Ninja

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `native-build`

**Executable candidates:** `ninja`, `ninja.exe`

**Python modules:** none

**Environment variables:** none

Install Ninja or select ninja.

objdiff — objdiff CLI

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `objdiff`, `matching`

**Executable candidates:** `objdiff-cli`, `objdiff`

**Python modules:** none

**Environment variables:** `OBJDIFF`

Install the objdiff release CLI or select the objdiff executable.

pip-audit — pip-audit

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `dependency-security`, `release`

**Executable candidates:** none

**Python modules:** `pip_audit`

**Environment variables:** none

**Pip requirement:** `pip-audit>=2.7,<3`

Install pip-audit in the test-suite Python environment.

pytest — pytest

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `unit`, `integration`

**Executable candidates:** none

**Python modules:** `pytest`

**Environment variables:** none

**Pip requirement:** `pytest>=8,<10`

python — Python 3.11+

**Kind:** `executable` · **Optional flag:** `false`

**Verification suites:** `all`

**Executable candidates:** `python3`, `python`

**Python modules:** none

**Environment variables:** none

Install Python 3.11 or newer using your operating-system package manager or python.org.

pyyaml — PyYAML

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `skill-frontmatter`

**Executable candidates:** none

**Python modules:** `yaml`

**Environment variables:** none

**Pip requirement:** `PyYAML>=6,<7`

unicorn — Unicorn Python bindings

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `dynamic`, `functional`

**Executable candidates:** none

**Python modules:** `unicorn`

**Environment variables:** none

**Pip requirement:** `unicorn>=2.1.4,<3`

uvicorn — Uvicorn

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `service`

**Executable candidates:** none

**Python modules:** `uvicorn`

**Environment variables:** none

**Pip requirement:** `uvicorn>=0.48,<1`

z3 — Z3 Python bindings

**Kind:** `python` · **Optional flag:** `false`

**Verification suites:** `symbolic`, `functional`

**Executable candidates:** none

**Python modules:** `z3`

**Environment variables:** none

**Pip requirement:** `z3-solver>=4.13,<5`
