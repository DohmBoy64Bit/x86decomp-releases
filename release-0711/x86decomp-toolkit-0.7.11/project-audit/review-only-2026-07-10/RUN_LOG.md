# Run log

Commands were executed against the extracted baseline or disposable byte-identical clones. Exit status is reported only when observed. Long outputs are stored under `evidence/`.

| Command / operation | Purpose | Exit/result | Conclusive? | Side effects / notes |
|---|---|---:|---|---|
| SHA-256 of uploaded ZIP | Bind input archive | `ec222b…7468a` | Yes | Read-only |
| Recursive byte inventory and UTF-8 decode | Discover/read every baseline file | 543 files; 540 text; 3 binary | Yes for inventory/read status | Read-only; `evidence/baseline_all_files.json` |
| `python scripts/source_hashes.py verify` on pristine clone | Verify root/suite/all-file manifests | 0; 540/540, 63/63, 542/542 | Yes | Read-only relative to tracked inventory |
| Python AST parse of all `.py` files | Syntax/symbol/import/risk/docstring analysis | All parsed; no syntax failures | Yes for parseability | Read-only |
| JSON parse of all `.json` files | Validate JSON syntax | All parsed | Yes for syntax | Read-only |
| Markdown local-link resolver | Check local target existence | 0 broken local targets | Yes for local paths | External URLs not dereferenced |
| CLI root/help/commands probes | Inventory live command system | 166 root; 405 parser nodes; exit 0 | Yes | Read-only |
| CLI invalid/missing/version probes | Check error/version behavior | invalid 2; missing 2; version 2 | Yes for executed paths | Read-only |
| `scripts/audit-docstrings.py` with redirected outputs | Exercise gate without source writes | 0/PASS | Yes for shipped checks | Outputs under disposable/audit paths |
| Default `scripts/audit-docstrings.py` then hash verify in disposable clone | Test documented sequence | docstring 0; hash verify 2 | Yes | Changed only disposable clone reports; evidence preserves before/after hashes |
| Expanded AST docstring scan | Detect generic quality patterns | 364/1,853 symbols across 128 files | Yes for defined patterns | Pattern policy is documented in JSON evidence |
| Parser malformed-input smoke | Exercise COFF/archive/PDB/PE rejection | 7,000 expected typed rejections; 0 unexpected | Yes for generated cases | Deterministic random seed; not exhaustive fuzzing |
| Exact pytest collection | Establish intended inventory | 258 tests, 86 partitions | Yes | Cache disabled |
| Resumable exact pytest partition replay | Execute intended inventory | 258 passed; 0 failed/errors/skips | Yes | Disposable clone; every partition has JSON/log/JUnit evidence |
| Packaged self-test replay | Exercise duplicated packaged tests | 21 passed | Yes | Disposable clone; cache disabled |
| Corpus synchronization check | Compare 24 source/package copies | 0/PASS | Yes | Read-only |
| `bash -n scripts/verify.sh` and `bash -n scripts/verify-ghidra.sh` | Shell syntax | 0 | Yes for syntax only | Scripts not fully executed |
| Contract validation | Validate schemas/Java contracts | Blocked: `javalang` absent | No | Dependency not installed under review-only rule |
| Strict MkDocs build | Validate site | Blocked: `mkdocs` absent | No | Dependency not installed |
| Pyflakes | Static undefined/unused check | Blocked: `pyflakes` absent | No | Dependency not installed |
| Expanded trailing-whitespace scan | Format hygiene | 45 lines / 17 files | Yes | Read-only; intentional Markdown hard breaks distinguished in recommendations |
| Final original-file SHA reconciliation | Prove no baseline modification | Generated after all reports | Yes | See `ORIGINAL_FILE_HASH_RECONCILIATION.json` |

## Interpretation

Passing tests verify the executed behavior only. Blocked gates are not described as passes. Historical reports in the input repository are treated as corroboration, not substituted for current execution. No optional external integration or suspicious binary was executed.
