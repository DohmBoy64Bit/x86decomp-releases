#!/usr/bin/env sh
set -eu
if [ -z "${GHIDRA_HOME:-}" ]; then
  echo "GHIDRA_HOME is required" >&2
  exit 2
fi
if [ "$#" -ne 2 ]; then
  echo "usage: $0 <native-pe-binary> <work-dir>" >&2
  exit 2
fi
BINARY=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
WORK=$2
ROOT=$(cd "$(dirname "$0")/.." && pwd)
rm -rf "$WORK/project" "$WORK/export"
mkdir -p "$WORK/project" "$WORK/export"
"$GHIDRA_HOME/support/analyzeHeadless" "$WORK/project" x86decomp_verify \
  -import "$BINARY" -overwrite \
  -scriptPath "$ROOT/ghidra_scripts" \
  -postScript ExportProjectManifest.java "$WORK/export" \
  -postScript ExportFunctionArtifacts.java "$WORK/export" all
python3 - <<'PY' "$WORK/export"
import json, pathlib, sys
root = pathlib.Path(sys.argv[1])
for name in ("program.json", "sections.json", "metrics.json"):
    json.load((root / name).open(encoding="utf-8"))
for name in ("functions.jsonl", "symbols.jsonl", "types.jsonl"):
    with (root / name).open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if line.strip():
                json.loads(line)
count = 0
for directory in root.glob("functions/pe-rva_*"):
    count += 1
    manifest = json.load((directory / "function.json").open(encoding="utf-8"))
    assert manifest["schema_version"] == 2
    assert set(manifest["selected_modes"]) == {"matching", "functional"}
    for relative in manifest["artifacts"].values():
        assert (directory / relative).is_file(), (directory, relative)
    for record in manifest["body_ranges"]:
        assert record["start_rva"] < record["end_rva"]
        assert record["size"] == record["end_rva"] - record["start_rva"]
        assert (directory / record["file"]).is_file()
    for name in ("instructions.jsonl", "references.jsonl", "decompiler-tree.jsonl", "high-pcode.jsonl", "raw-pcode.jsonl"):
        with (directory / name).open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip(): json.loads(line)
assert count > 0, "no function artifacts were exported"
print(f"Ghidra export validation passed for {count} functions")
PY
