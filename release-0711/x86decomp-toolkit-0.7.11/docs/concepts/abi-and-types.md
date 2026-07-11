# ABI and Types

ABI contracts capture calling conventions, register usage, and stack behavior. The type
system records constraints in the analysis database. Together they feed the validation
pipeline: `abi-check` verifies that compiled code matches the original's interface, and
`cpp-recover` reconstructs C++ class relationships.

## ABI Contracts

An ABI contract declares how a function interacts with its callers:

```json
{
  "architecture": "x86",
  "convention": "stdcall",
  "stack_argument_bytes": 12,
  "callee_stack_cleanup": 12,
  "variadic": false,
  "this_register": null,
  "register_arguments": [],
  "return_registers": ["eax"],
  "structure_return": false,
  "floating_point": "none"
}
```

### Contract Fields

| Field | Type | Description |
|---|---|---|
| `architecture` | `"x86"` or `"x86_64"` | Target architecture |
| `convention` | Enum | `cdecl`, `stdcall`, `thiscall`, `fastcall`, `vectorcall`, `unknown` |
| `stack_argument_bytes` | int or null | Bytes of stack arguments (excluding return address) |
| `callee_stack_cleanup` | int or null | Bytes popped by `ret N` in the callee |
| `variadic` | bool | True for `...` functions |
| `this_register` | str or null | Register holding `this` pointer (`ecx` for MSVC thiscall) |
| `register_arguments` | str[] | Registers used for parameter passing |
| `return_registers` | str[] | Registers holding return value (default `eax`/`rax`) |
| `structure_return` | bool | True if the function returns a struct by hidden pointer |
| `floating_point` | Enum | `x87`, `sse`, `mixed`, `none`, `unknown` |

### Calling Convention Mapping

| Convention | x86 Stack Cleanup | x86 Arg Registers | x86 This Register |
|---|---|---|---|
| `cdecl` | Caller | None | N/A |
| `stdcall` | Callee (`ret N`) | None | N/A |
| `thiscall` | Callee | None | `ecx` |
| `fastcall` | Callee | `ecx`, `edx` | N/A |
| `vectorcall` | Callee | `ecx`, `edx`, `xmm0`–`xmm3` | `ecx` |
| `unknown` | — | — | — |

## Creating ABI Contracts

Contracts are JSON files stored in the project. Create them manually or generate them
from analysis:

```json
{
  "architecture": "x86",
  "convention": "fastcall",
  "stack_argument_bytes": 8,
  "callee_stack_cleanup": 8,
  "variadic": false,
  "this_register": null,
  "register_arguments": ["ecx", "edx"],
  "return_registers": ["eax"],
  "structure_return": false,
  "floating_point": "none"
}
```

## ABI Analysis

The `analyze_abi` function inspects disassembled code to infer ABI properties:

```bash
x86decomp disassemble --code <hex_bytes> --base-address 0x401000 --architecture x86
```

But the analysis is also available programmatically. It checks:

- **Ret immediates**: `ret 0C` implies 12 bytes of callee stack cleanup (stdcall/fastcall).
- **Register usage**: References to `ecx`/`edx` suggest fastcall or thiscall.
- **Floating-point**: `f`-prefixed instructions indicate x87; `xmm`/`ymm` indicate SSE.
- **Frame pointers**: `push ebp; mov ebp, esp` patterns.
- **Stack adjustments**: `add esp, N` or `sub esp, N` instructions.

```json
{
  "architecture": "x86",
  "instruction_count": 42,
  "return_instruction_count": 1,
  "ret_immediates": [12],
  "inferred_callee_stack_cleanup": 12,
  "uses_ecx_or_rcx": true,
  "uses_edx_or_rdx": false,
  "frame_pointer_pattern_observed": true,
  "stack_adjustments": ["sub esp, 20h"],
  "floating_point_observed": "none",
  "convention_candidates": ["thiscall", "stdcall"],
  "limitations": [
    "Register occurrence is not proof of parameter passing.",
    "Optimized leaf functions may omit standard prologues and epilogues.",
    "Caller-side evidence is required to establish a convention reliably."
  ]
}
```

!!! warning "Analysis is bounded"
    The static ABI analyzer observes patterns, not semantics. Register *occurrence* is not
    register *parameter passing*. A function might use `ecx` internally without it being
    a `this` pointer. Caller-side evidence is needed for reliable convention determination.

## ABI Validation

`abi-check` validates that compiled code matches an ABI contract:

```bash
x86decomp abi-check \
  --code <hex_bytes> \
  --contract config/abi/function-401000.json \
  --base-address 0x401000 \
  --report abi-report.json
```

The validator runs a series of bounded checks:

| Check | Strength | What It Verifies |
|---|---|---|
| `callee_stack_cleanup` | `direct_epilogue_observation` | `ret N` matches expected cleanup |
| `variadic_caller_cleanup` | `necessary_not_sufficient` | Variadic functions don't pop args |
| `this_register_observed` | `weak_static_signal` | `ecx`/`rcx` is referenced in code |
| `floating_point_mode` | `instruction_family_observation` | FP instruction families match |
| `cdecl_no_callee_argument_pop` | `necessary_not_sufficient` | CDECL has no `ret N` |
| `callee_pop_matches_stack_arguments` | `direct_epilogue_observation` | STDCALL/FASTCALL `ret N` matches args |

```json
{
  "kind": "bounded_static_abi_validation",
  "contract": {
    "architecture": "x86",
    "convention": "stdcall",
    "stack_argument_bytes": 12,
    "callee_stack_cleanup": 12
  },
  "analysis": {
    "inferred_callee_stack_cleanup": 12
  },
  "checks": [
    {
      "name": "callee_stack_cleanup",
      "passed": true,
      "expected": 12,
      "observed": 12,
      "strength": "direct_epilogue_observation"
    }
  ],
  "compatible_with_observed_code": true,
  "semantic_or_full_abi_equivalence_claimed": false
}
```

!!! note "Not semantic equivalence"
    `compatible_with_observed_code: true` means the code does not contradict the contract.
    It is NOT a claim of full semantic ABI equivalence. The limitations section makes this
    explicit.

## Type Constraints in the Analysis Database

The analysis database (`analysis/database/`) stores type constraints as provenance-bearing
records:

```bash
x86decomp db-constraint-add --project . \
  --subject pe-rva:00401000 \
  --relation has_argument_type \
  --object "int, const char*, size_t" \
  --evidence ev-abc123 \
  --evidence ev-def456 \
  --provenance "pdb-type-recovery"
```

### Constraint Operations

```bash
# List constraints for a function
x86decomp db-query --project . \
  --sql "SELECT * FROM constraints WHERE subject = 'pe-rva:00401000'"

# Check for conflicts
x86decomp db-constraint-conflicts --project . \
  --subject pe-rva:00401000 --relation has_argument_type

# Accept a specific constraint resolution
x86decomp db-constraint-accept --project . \
  --constraint-id const-0011223344
```

## C++ Recovery

`cpp-recover` reconstructs C++ class metadata from PE artifacts:

```bash
x86decomp cpp-recover \
  --pe original/game.exe \
  --output cpp-model.json
```

### What It Recovers

- **VTables**: Virtual function tables and their layouts.
- **RTTI data**: `RTTICompleteObjectLocator`, `RTTIClassHierarchyDescriptor`,
  `RTTIBaseClassDescriptor` structures.
- **Class hierarchies**: Base class relationships from RTTI chains.
- **Constructor/destructor patterns**: Identified via vtable initialization patterns.
- **Member function groupings**: Functions sharing the same vtable.

### Example Output

```json
{
  "classes": [
    {
      "name": "UnknownClass_0041A000",
      "mangled_name": ".?AVUnknownClass_0041A000@@",
      "vtable_rva": "0x41A000",
      "vtable_size": 20,
      "virtual_functions": [
        {"rva": "0x401000", "index": 0},
        {"rva": "0x401050", "index": 1},
        {"rva": "0x4010A0", "index": 2},
        {"rva": "0x4010F0", "index": 3},
        {"rva": "0x401140", "index": 4}
      ],
      "base_classes": [],
      "rtti_locator_rva": "0x41A100"
    }
  ],
  "class_hierarchies": [
    {
      "derived": "UnknownClass_0041A200",
      "bases": ["UnknownClass_0041A000"],
      "evidence": "rtti_base_class_array"
    }
  ]
}
```

### C++ Scaffolding

The output model can be used to generate header scaffolding:

- VTable declarations as C `struct` with function pointer members.
- Class `struct` definitions with vtable pointer as first member.
- Constructor/destructor stubs with vtable initialization.
- Base class embedding for single-inheritance hierarchies.

!!! tip "Manual refinement required"
    `cpp-recover` recovers layout, not names. Class names like `UnknownClass_0041A000` are
    placeholder labels derived from the vtable RVA. Rename them after recovery using
    PDB symbols or manual analysis.

## Integration with ABI Validation

For C++ member functions:

1. Recover the class structure with `cpp-recover`.
2. Identify member functions by their `this` pointer usage.
3. Create ABI contracts with `convention: thiscall` and `this_register: ecx`.
4. Validate with `abi-check`.

```bash
x86decomp abi-check \
  --code <member_function_bytes> \
  --contract config/abi/class-method-401000.json
```

The validator checks for `ecx` register usage to confirm the `thiscall` convention.
