# Supported scope

The toolkit supports authorized analysis and reconstruction of native Windows x86 and x86-64
PE artifacts, related COFF objects and libraries, MAP and PDB evidence, and bounded comparison
workflows.

## What is in scope

| Category | Details |
|---|---|
| **PE artifacts** | PE32 and PE32+ (native Windows x86 and x86-64) |
| **COFF** | Objects and libraries |
| **Evidence** | MAP files, PDB streams |
| **Comparison** | Bounded comparison workflows (byte, function, instruction, ABI, dynamic, symbolic, integration) |

## What is explicitly NOT claimed

!!! warning
    The toolkit does **not** claim recovery of original source text, comments, names, macros,
    build environments, or universal semantic equivalence without authenticated evidence.

* Dynamic execution is optional and requires explicit authorization.
* External tool support depends on detected adapters and is reported honestly.
* No claim is made about recovering build systems, makefiles, or project structures.
