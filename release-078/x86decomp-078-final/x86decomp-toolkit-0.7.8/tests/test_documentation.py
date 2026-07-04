from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_release_documents_and_maps_are_current() -> None:
    required = [
        ROOT / "README.md",
        ROOT / "FEATURE_PARITY.md",
        ROOT / "AGENTS.md",
        ROOT / "PROJECT_MEMORY.md",
        ROOT / "SECURITY.md",
        ROOT / "VERIFICATION.md",
        ROOT / "docs/ARCHITECTURE_MAP.md",
        ROOT / "docs/ARCHITECTURE_MAP_ASCII.txt",
        ROOT / "test-suite/README.md",
        ROOT / "test-suite/MAINTENANCE.md",
        ROOT / "test-suite/docs/ARCHITECTURE_MAP.md",
        ROOT / "test-suite/docs/ARCHITECTURE_MAP_ASCII.txt",
        ROOT / "skills/x86decomp/SKILL.md",
    ]
    for path in required:
        text = path.read_text(encoding="utf-8")
        assert "0.7.8" in text, path


def test_test_plan_counts_match_feature_catalog() -> None:
    catalog = json.loads(
        (ROOT / "test-suite/src/x86decomp_testkit/data/feature_catalog.json").read_text(encoding="utf-8")
    )
    plan = (ROOT / "test-suite/docs/TEST_PLAN.md").read_text(encoding="utf-8")
    expected = {
        "modules": len(catalog["modules"]),
        "functions": len(catalog["all_function_symbols"]),
        "commands": len(catalog["cli_commands"]),
        "groups": len(catalog["canonical_groups"]),
        "routes": len(catalog["canonical_routes"]),
        "schemas": len(catalog["schemas"]),
        "ghidra": len(catalog["ghidra_scripts"]),
        "adapters": len(catalog["adapters"]),
    }
    for name, value in expected.items():
        assert str(value) in plan, name


def test_four_architecture_artifacts_exist_and_cross_link() -> None:
    toolkit_mermaid = ROOT / "docs/ARCHITECTURE_MAP.md"
    toolkit_ascii = ROOT / "docs/ARCHITECTURE_MAP_ASCII.txt"
    suite_mermaid = ROOT / "test-suite/docs/ARCHITECTURE_MAP.md"
    suite_ascii = ROOT / "test-suite/docs/ARCHITECTURE_MAP_ASCII.txt"
    for path in (toolkit_mermaid, toolkit_ascii, suite_mermaid, suite_ascii):
        assert path.is_file()
        assert "0.7.8" in path.read_text(encoding="utf-8")
    assert "ARCHITECTURE_MAP_ASCII.txt" in toolkit_mermaid.read_text(encoding="utf-8")
    assert "ARCHITECTURE_MAP_ASCII.txt" in suite_mermaid.read_text(encoding="utf-8")
