from __future__ import annotations

import json
import sys
from pathlib import Path

from x86decomp.decompme import create_decompme_packet
from x86decomp.objdiff_adapter import run_objdiff_manifest


def test_create_local_decompme_packet(tmp_path: Path) -> None:
    artifact = tmp_path / "artifact"
    artifact.mkdir()
    (artifact / "function.json").write_text(
        json.dumps(
            {
                "schema_version": 2,
                "id": "pe-rva:00001000",
                "name": "FUN_00401000",
                "body_ranges": [{"start_rva": 0x1000, "end_rva": 0x1003}],
            }
        ),
        encoding="utf-8",
    )
    for name, text in {
        "listing.asm": "xor eax,eax\nret\n",
        "decompiler.c": "int f(void) { return 0; }\n",
        "context.h": "typedef unsigned int uint;\n",
        "references.jsonl": "",
    }.items():
        (artifact / name).write_text(text, encoding="utf-8")
    output = tmp_path / "packet"
    report = create_decompme_packet(artifact, output)
    assert report["function_id"] == "pe-rva:00001000"
    assert report["uploaded"] is False
    assert (output / "packet.json").is_file()
    assert (output / "target_asm_ghidra.txt").read_text() == (artifact / "listing.asm").read_text()


def test_manifest_driven_objdiff_adapter(tmp_path: Path) -> None:
    target = tmp_path / "target.o"
    candidate = tmp_path / "candidate.o"
    target.write_bytes(b"same")
    candidate.write_bytes(b"same")
    script = tmp_path / "fake_objdiff.py"
    script.write_text(
        "import hashlib,json,sys\n"
        "target,candidate,output=sys.argv[1:4]\n"
        "a=open(target,'rb').read(); b=open(candidate,'rb').read()\n"
        "json.dump({'equal':a==b,'target_sha256':hashlib.sha256(a).hexdigest()},open(output,'w'))\n",
        encoding="utf-8",
    )
    manifest = tmp_path / "objdiff.json"
    manifest.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "executable": sys.executable,
                "target": "target.o",
                "candidate": "candidate.o",
                "arguments": [str(script), "{target}", "{candidate}", "{output}"],
                "output": "result.json",
                "output_format": "json",
                "require_output": True,
                "success_exit_codes": [0],
            }
        ),
        encoding="utf-8",
    )
    report = run_objdiff_manifest(manifest)
    assert report["success"]
    assert report["parsed_output"]["equal"] is True
