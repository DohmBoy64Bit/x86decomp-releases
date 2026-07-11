"""Verify the current toolkit behavior covered by `tests/test_artifacts.py`."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from x86decomp.artifacts import import_function_artifact, verify_function_artifact


class ArtifactTests(unittest.TestCase):
    """Group regression tests covering Artifact behavior."""
    def _export(self, root: Path) -> Path:
        """Export artifact tests."""
        exported = root / "exported"
        (exported / "ranges").mkdir(parents=True)
        (exported / "ranges" / "00.bin").write_bytes(b"\x90\xc3")
        (exported / "function.json").write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "id": "pe-rva:00001000",
                    "entry_rva": 0x1000,
                    "body_ranges": [
                        {"start_rva": 0x1000, "end_rva": 0x1002, "file": "ranges/00.bin"}
                    ],
                }
            ),
            encoding="utf-8",
        )
        return exported

    def test_import_and_verify(self) -> None:
        """Verify import and verify behavior."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            destination = import_function_artifact(root / "project", self._export(root))
            result = verify_function_artifact(destination)
            self.assertTrue(result["valid"], result["failures"])

    def test_integrity_path_escape_is_rejected(self) -> None:
        """Verify integrity path escape is rejected behavior."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            destination = import_function_artifact(root / "project", self._export(root))
            integrity_path = destination / "integrity.json"
            integrity = json.loads(integrity_path.read_text(encoding="utf-8"))
            integrity["files"].append({"path": "../outside", "size": 1, "sha256": "0" * 64})
            integrity_path.write_text(json.dumps(integrity), encoding="utf-8")
            result = verify_function_artifact(destination)
            self.assertFalse(result["valid"])
            self.assertTrue(any("escapes" in item for item in result["failures"]))


if __name__ == "__main__":
    unittest.main()
