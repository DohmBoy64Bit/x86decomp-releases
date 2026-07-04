from __future__ import annotations

import json
import shutil
import struct
import subprocess
from pathlib import Path

import pytest

from pe_fixture import build_minimal_pe32
from x86decomp.angr_backend import angr_memory_alias_compare
from x86decomp.coff import (
    IMAGE_COMDAT_SELECT_ANY,
    IMAGE_COMDAT_SELECT_EXACT_MATCH,
    IMAGE_COMDAT_SELECT_LARGEST,
    IMAGE_FILE_MACHINE_I386,
    build_comdat_coff,
    parse_coff_bytes,
    resolve_comdats,
)
from x86decomp.ground_truth import build_ground_truth_corpus, verify_ground_truth_corpus
from x86decomp.image_match import compare_whole_images, derive_layout_profile
from x86decomp.linker_layout import parse_msvc_map_text, reconstruct_linker_layout
from x86decomp.msvc_metadata import analyze_msvc_metadata, scan_coff_tls, scan_static_initializers


def _minimal_bigobj() -> bytes:
    header_size = 56
    section_size = 40
    code = b"\xc3"
    raw_pointer = header_size + section_size
    symbol_pointer = raw_pointer + len(code)
    class_id = bytes.fromhex("C7A1BAD1EEBAA94Baf20FAF66AA4DCB8")
    header = struct.pack(
        "<HHHHI16sIIIIIII",
        0,
        0xFFFF,
        2,
        IMAGE_FILE_MACHINE_I386,
        0,
        class_id,
        0,
        0,
        0,
        0,
        1,
        symbol_pointer,
        1,
    )
    section = b".text\x00\x00\x00" + struct.pack(
        "<IIIIIIHHI", 0, 0, len(code), raw_pointer, 0, 0, 0, 0, 0x60000020
    )
    symbol = b"f\x00\x00\x00\x00\x00\x00\x00" + struct.pack("<IiHBB", 0, 1, 0x20, 2, 0)
    return header + section + code + symbol + struct.pack("<I", 4)


def test_bigobj_and_comdat_resolution() -> None:
    big = parse_coff_bytes(_minimal_bigobj())
    assert big.format_variant == "bigobj"
    assert big.symbols[0].name == "f"

    any_a = parse_coff_bytes(build_comdat_coff(data=b"a", symbol_name="same", selection=IMAGE_COMDAT_SELECT_ANY))
    any_b = parse_coff_bytes(build_comdat_coff(data=b"bb", symbol_name="same", selection=IMAGE_COMDAT_SELECT_ANY))
    resolution = resolve_comdats([any_a, any_b])
    assert resolution.valid
    assert resolution.winners[0].object_index == 0

    large_a = parse_coff_bytes(build_comdat_coff(data=b"a", symbol_name="large", selection=IMAGE_COMDAT_SELECT_LARGEST))
    large_b = parse_coff_bytes(build_comdat_coff(data=b"bbbb", symbol_name="large", selection=IMAGE_COMDAT_SELECT_LARGEST))
    resolution = resolve_comdats([large_a, large_b])
    assert resolution.valid
    assert resolution.winners[0].size == 4

    exact_a = parse_coff_bytes(build_comdat_coff(data=b"a", symbol_name="exact", selection=IMAGE_COMDAT_SELECT_EXACT_MATCH))
    exact_b = parse_coff_bytes(build_comdat_coff(data=b"b", symbol_name="exact", selection=IMAGE_COMDAT_SELECT_EXACT_MATCH))
    resolution = resolve_comdats([exact_a, exact_b])
    assert not resolution.valid
    assert resolution.conflicts[0]["reason"] == "exact_match_violation"


def test_map_parser_and_layout_reconstruction(tmp_path: Path) -> None:
    binary = build_minimal_pe32(tmp_path / "target.exe")
    map_text = """
target
 Timestamp is 12345678
 Preferred load address is 00400000

 Start         Length     Name                   Class
 0001:00000000 00000003H .text                  CODE

 Address         Publics by Value              Rva+Base       Lib:Object
 0001:00000000       _entry                     00401000 f   entry.obj

 entry point at        0001:00000000
"""
    parsed = parse_msvc_map_text(map_text)
    assert parsed.preferred_load_address == 0x400000
    assert parsed.publics[0].name == "_entry"
    map_path = tmp_path / "target.map"
    map_path.write_text(map_text)
    report = reconstruct_linker_layout(binary, map_path)
    assert report["map"]["entry"] == {"segment": 1, "offset": 0}
    assert report["object_order_evidenced"] is True
    assert report["byte_accurate_contributions_evidenced"] is False
    assert report["object_order"] == ["entry.obj"]


def test_target_specific_image_normalization(tmp_path: Path) -> None:
    reference = build_minimal_pe32(tmp_path / "reference.exe")
    candidate = tmp_path / "candidate.exe"
    data = bytearray(reference.read_bytes())
    pe_offset = struct.unpack_from("<I", data, 0x3C)[0]
    checksum_offset = pe_offset + 24 + 64
    struct.pack_into("<I", data, checksum_offset, 0x12345678)
    candidate.write_bytes(data)
    profile_path = tmp_path / "profile.json"
    derive_layout_profile(reference, output=profile_path)
    report = compare_whole_images(reference, candidate, profile_path=profile_path)
    assert not report["raw_exact_match"]
    assert report["normalized_match"]
    assert report["classification"] == "profile_normalized_match"


@pytest.mark.skipif(shutil.which("clang++") is None or shutil.which("lld-link") is None, reason="LLVM tools unavailable")
def test_msvc_rtti_unwind_and_static_initializer_recovery(tmp_path: Path) -> None:
    source = tmp_path / "rtti.cpp"
    source.write_text(
        """
struct Base { virtual int f(){return 1;} virtual ~Base(){} };
struct Derived: Base { int f() override {return 2;} };
Derived global_object;
extern "C" int atexit(void(*)(void)){return 0;}
extern "C" int entry(){return global_object.f();}
"""
    )
    obj = tmp_path / "rtti.obj"
    image = tmp_path / "rtti.exe"
    subprocess.run(
        ["clang++", "-target", "x86_64-pc-windows-msvc", "-c", str(source), "-O0", "-frtti", "-fexceptions", "-o", str(obj)],
        check=True,
        capture_output=True,
        text=True,
    )
    completed = subprocess.run(
        ["lld-link", "/nologo", "/machine:x64", "/entry:entry", "/subsystem:console", "/nodefaultlib", "/force:unresolved", f"/out:{image}", str(obj)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
    report = analyze_msvc_metadata(image, object_paths=[obj])
    assert len(report["rtti"]["type_descriptors"]) >= 2
    assert len(report["rtti"]["complete_object_locators"]) >= 1
    assert len(report["rtti"]["vtables"]) >= 1
    assert len(report["exceptions"]["x64_unwind"]) >= 1
    initializers = scan_static_initializers(object_paths=[obj])
    assert any(item["section"].upper().startswith(".CRT$X") for item in initializers["objects"])


@pytest.mark.skipif(shutil.which("clang") is None, reason="clang unavailable")
def test_compiler_ground_truth_corpus(tmp_path: Path) -> None:
    source = tmp_path / "case.c"
    source.write_text("int corpus_case(int x){return x * 3 + 1;}\n")
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps({
        "schema_version": 1,
        "compilers": [{
            "id": "clang-x86", "executable": "clang",
            "base_args": ["-target", "i686-pc-windows-msvc", "-c"]
        }],
        "flag_matrix": {"optimization": [
            {"id": "O0", "args": ["-O0"]}, {"id": "O2", "args": ["-O2"]}
        ]},
        "cases": [{"id": "case", "source": "case.c", "compilers": ["clang-x86"]}]
    }))
    output = tmp_path / "corpus"
    report = build_ground_truth_corpus(manifest, output)
    assert report["summary"] == {"total": 2, "succeeded": 2, "failed": 0}
    assert all(build.get("coff", {}).get("format") == "COFF" for build in report["builds"])
    assert verify_ground_truth_corpus(output / "corpus.json")["valid"]


@pytest.mark.skipif(shutil.which("python") is None, reason="python unavailable")
def test_symbolic_memory_alias_model() -> None:
    pytest.importorskip("angr")
    target = bytes.fromhex("c701010000008b02c3")
    candidate = bytes.fromhex("8b02c70101000000c3")
    harness = {
        "architecture": "x86",
        "regions": [
            {"name": "left", "pointer_register": "ecx", "size": 4, "alignment": 4, "initial": "symbolic"},
            {"name": "right", "pointer_register": "edx", "size": 4, "alignment": 4, "initial": "symbolic"},
        ],
        "alias_constraints": [{"left": "left", "right": "right", "relation": "may_alias"}],
        "observe_memory": [{"region": "left", "size": 4}, {"region": "right", "size": 4}],
        "output_registers": ["eax"],
        "alias_slots": 2,
        "max_steps": 32,
        "max_paths": 16,
    }
    report = angr_memory_alias_compare(target, candidate, harness)
    assert not report["equivalent_within_completed_model"]
    assert report["counterexample_target_to_candidate"] is not None


@pytest.mark.skipif(shutil.which("clang") is None, reason="clang unavailable")
def test_real_clang_weak_external_and_tls_coff(tmp_path: Path) -> None:
    weak_source = tmp_path / "weak.c"
    weak_source.write_text(
        "__attribute__((weak)) int weakfn(void){return 1;}\n"
        "int call(void){return weakfn();}\n"
    )
    weak_object = tmp_path / "weak.obj"
    subprocess.run(
        ["clang", "-target", "i686-pc-windows-gnu", "-c", str(weak_source), "-O0", "-o", str(weak_object)],
        check=True, capture_output=True, text=True,
    )
    weak = __import__("x86decomp.coff", fromlist=["parse_coff"]).parse_coff(weak_object)
    weak_symbol = next(symbol for symbol in weak.symbols if symbol.name == "_weakfn")
    assert weak_symbol.weak_external is not None
    assert weak_symbol.weak_external.to_dict()["characteristics_name"] == "alias"

    tls_source = tmp_path / "tls.cpp"
    tls_source.write_text(
        "__declspec(thread) int tls_value = 7;\n"
        "extern \"C\" int entry(){return tls_value;}\n"
    )
    tls_object = tmp_path / "tls.obj"
    subprocess.run(
        ["clang++", "-target", "x86_64-pc-windows-msvc", "-c", str(tls_source), "-O0", "-o", str(tls_object)],
        check=True, capture_output=True, text=True,
    )
    tls = scan_coff_tls(object_paths=[tls_object])
    assert any(item["section"].upper().startswith(".TLS$") for item in tls["object_sections"])
    assert any(item["raw_hex"] == "07000000" for item in tls["object_sections"])

@pytest.mark.skipif(shutil.which("clang") is None or shutil.which("clang++") is None, reason="clang unavailable")
def test_builtin_corpus_manifest_is_expanded_and_sources_compile(tmp_path: Path) -> None:
    from x86decomp.ground_truth import create_builtin_manifest

    repository = Path(__file__).resolve().parents[1]
    manifest_path = tmp_path / "builtin.json"
    manifest = create_builtin_manifest(repository, output=manifest_path)
    assert len(manifest["cases"]) >= 24
    assert {"optimization", "frame_pointer"} <= set(manifest["flag_matrix"])
    for case in manifest["cases"]:
        assert (manifest_path.parent / case["source"]).resolve().is_file()


def test_ground_truth_cross_report_comparison(tmp_path: Path) -> None:
    from x86decomp.ground_truth import compare_ground_truth_corpora

    reports = []
    for index, output_hash in enumerate(("a" * 64, "b" * 64)):
        path = tmp_path / f"corpus-{index}.json"
        path.write_text(json.dumps({
            "kind": "compiler_ground_truth_corpus",
            "compilers": [{"id": f"compiler-{index}", "version": str(index)}],
            "builds": [{
                "success": True,
                "build_id": f"build-{index}",
                "case_id": "arithmetic",
                "variant_id": "O2",
                "compiler_id": f"compiler-{index}",
                "compiler_sha256": str(index) * 64,
                "output_sha256": output_hash,
                "coff": {"architecture": "x86", "sections": [], "symbols": []},
            }],
        }))
        reports.append(path)
    result = compare_ground_truth_corpora(reports)
    assert result["summary"]["aligned_case_variants"] == 1
    assert not result["comparisons"][0]["all_object_bytes_identical"]
    assert result["semantic_equivalence_claimed"] is False

@pytest.mark.skipif(shutil.which("clang++") is None or shutil.which("lld-link") is None, reason="LLVM tools unavailable")
def test_image_profile_can_explicitly_normalize_debug_records(tmp_path: Path) -> None:
    source = tmp_path / "debug.cpp"
    source.write_text('extern "C" int entry(){return 1;}\n')
    obj = tmp_path / "debug.obj"
    reference = tmp_path / "debug.exe"
    pdb = tmp_path / "debug.pdb"
    subprocess.run(
        ["clang++", "-target", "x86_64-pc-windows-msvc", "-c", str(source), "-gcodeview", "-o", str(obj)],
        check=True, capture_output=True, text=True,
    )
    subprocess.run(
        ["lld-link", "/nologo", "/machine:x64", "/entry:entry", "/subsystem:console", "/nodefaultlib", "/debug", f"/pdb:{pdb}", f"/out:{reference}", str(obj)],
        check=True, capture_output=True, text=True,
    )
    from x86decomp.pe import parse_pe
    image = parse_pe(reference)
    assert image.debug_records
    candidate = tmp_path / "candidate.exe"
    data = bytearray(reference.read_bytes())
    record = image.debug_records[0]
    data[record.raw_data_offset + 24] ^= 0x01
    candidate.write_bytes(data)
    profile_path = tmp_path / "profile.json"
    profile = derive_layout_profile(reference)
    profile["normalization"]["debug_directory_records"] = True
    profile_path.write_text(json.dumps(profile))
    report = compare_whole_images(reference, candidate, profile_path=profile_path)
    assert report["normalized_match"]
    assert any(item["reason"].startswith("debug_payload") for item in report["normalization_ranges"])
