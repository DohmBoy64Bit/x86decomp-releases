from __future__ import annotations

from pathlib import Path


REQUIRED_MAPS = (
    "docs/ARCHITECTURE_MAP.md",
    "docs/ARCHITECTURE_MAP_ASCII.txt",
    "test-suite/docs/ARCHITECTURE_MAP.md",
    "test-suite/docs/ARCHITECTURE_MAP_ASCII.txt",
)


def _repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _normalized(text: str) -> str:
    return " ".join(text.lower().replace("-", " ").split())


def test_all_architecture_map_artifacts_exist_and_are_versioned() -> None:
    root = _repository_root()
    for relative in REQUIRED_MAPS:
        path = root / relative
        assert path.is_file(), f"missing architecture artifact: {relative}"
        text = path.read_text(encoding="utf-8")
        assert "0.4.0" in text, f"architecture version missing from {relative}"


def test_toolkit_mermaid_and_ascii_maps_cover_same_major_planes_and_states() -> None:
    root = _repository_root()
    mermaid = (root / "docs/ARCHITECTURE_MAP.md").read_text(encoding="utf-8")
    ascii_map = (root / "docs/ARCHITECTURE_MAP_ASCII.txt").read_text(encoding="utf-8")

    for token in (
        "Immutable ingestion",
        "Static-analysis plane",
        "Project control plane",
        "Candidate-generation plane",
        "Compiler and linker plane",
        "Matching-decompilation lane",
        "Functional-decompilation lane",
        "Acceptance, evidence, and feedback",
        "not_started",
        "instruction_similar",
        "full_relink_validated",
        "differentially_validated",
        "symbolically_bounded",
        "integration_validated",
    ):
        expected = _normalized(token)
        assert expected in _normalized(mermaid), f"Mermaid toolkit map missing {token}"
        assert expected in _normalized(ascii_map), f"ASCII toolkit map missing {token}"


def test_test_suite_mermaid_and_ascii_maps_cover_same_resolution_and_gate_contract() -> None:
    root = _repository_root()
    mermaid = (root / "test-suite/docs/ARCHITECTURE_MAP.md").read_text(encoding="utf-8")
    ascii_map = (root / "test-suite/docs/ARCHITECTURE_MAP_ASCII.txt").read_text(encoding="utf-8")

    for token in (
        "Adapter resolution",
        "custom path",
        "consent-gated",
        "BLOCKED",
        "Pinned surface",
        "catalog drift",
        "Built-in verification",
        "Safe process execution",
        "Unified result",
        "Strict release gate",
        "PASS",
        "FAIL",
        "ERROR",
    ):
        expected = _normalized(token)
        assert expected in _normalized(mermaid), f"Mermaid test-suite map missing {token}"
        assert expected in _normalized(ascii_map), f"ASCII test-suite map missing {token}"


def test_architecture_map_cross_links_and_ascii_format_contract() -> None:
    root = _repository_root()
    toolkit_mermaid = (root / "docs/ARCHITECTURE_MAP.md").read_text(encoding="utf-8")
    suite_mermaid = (root / "test-suite/docs/ARCHITECTURE_MAP.md").read_text(encoding="utf-8")

    assert "docs/ARCHITECTURE_MAP_ASCII.txt" in toolkit_mermaid
    assert "test-suite/docs/ARCHITECTURE_MAP_ASCII.txt" in toolkit_mermaid
    assert "docs/ARCHITECTURE_MAP.md" in suite_mermaid
    assert "test-suite/docs/ARCHITECTURE_MAP_ASCII.txt" in suite_mermaid

    for relative in (
        "docs/ARCHITECTURE_MAP_ASCII.txt",
        "test-suite/docs/ARCHITECTURE_MAP_ASCII.txt",
    ):
        text = (root / relative).read_text(encoding="utf-8")
        assert "```" not in text, f"ASCII map must remain plain text: {relative}"
        assert "┌" in text and "└" in text and "│" in text
