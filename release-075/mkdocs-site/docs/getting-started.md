---
title: From installation to a verified project
description: Source-checked installation and first-project workflow
original_path: getting-started.html
---

Section: Source-checked setup

# From installation to a verified project

These commands were parsed against the actual 0.7.5 toolkit and verification-harness parsers.

## <span class="doc-step-number">1</span> Install the packaged wheels { .doc-step }

```
python -m pip install .\x86decomp_toolkit-0.7.5-py3-none-any.whl
python -m pip install .\x86decomp_test_suite-0.7.5-py3-none-any.whl
```

The toolkit wheel declares no mandatory runtime dependencies. Optional extras are declared in `pyproject.toml` for disassembly, dynamic, symbolic, angr, service, PE, full, and development use.

## <span class="doc-step-number">2</span> Inspect the two installed interfaces { .doc-step }

```
x86decomp --help
x86decomp commands
x86decomp commands --owner governance
x86decomp-test --help
```

The only valid canonical owners are `governance`, `reconstruction`, `native`, and `assembly`.

## <span class="doc-step-number">3</span> Initialize the canonical project data plane { .doc-step }

```
x86decomp project --project .\work init
x86decomp project --project .\work check
```

## <span class="doc-step-number">4</span> Initialize and verify a native PE analysis project { .doc-step }

```
x86decomp init .\target.exe .\analysis-project
x86decomp verify-project .\analysis-project
```

## <span class="doc-step-number">5</span> Inspect a PE and disassemble an extracted byte range { .doc-step }

```
x86decomp inspect-pe .\target.exe
x86decomp disassemble .\function.bin --base 0x401000 --architecture x86
```

`disassemble` accepts a byte file plus `--base` and `--architecture`; it does not accept PE-specific `--rva` or `--size` options.

## <span class="doc-step-number">6</span> Configure and run the independent verification harness { .doc-step }

```
x86decomp-test init-config `
  --toolkit-root . `
  --output-root .\test-results `
  --install-root .\.x86decomp-test-tools `
  --config .\x86decomp-test.json

x86decomp-test run --config .\x86decomp-test.json --verbose
```

## <span class="doc-step-number">7</span> Verify an extracted source tree { .doc-step }

```
make verify-hashes
make verify
make test-suite
```

> **Safety boundary.** Analyze only binaries and systems you are authorized to inspect. Native execution and integration scenarios require an appropriate isolation decision and explicit consent.
