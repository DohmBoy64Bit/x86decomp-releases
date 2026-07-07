"""Verify the current toolkit behavior covered by `tests/test_ghidra.py`."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from x86decomp.ghidra import build_export_command


class GhidraCommandTests(unittest.TestCase):
    """Coordinate ghidra command tests behavior for the current toolkit workflow."""
    def test_build_export_command_is_argument_array(self) -> None:
        """Verify build export command is argument array behavior."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            home = root / "ghidra"
            analyze = home / "support" / "analyzeHeadless"
            analyze.parent.mkdir(parents=True)
            analyze.write_text("#!/bin/sh\n", encoding="utf-8")
            binary = root / "sample.exe"
            binary.write_bytes(b"MZ")
            scripts = root / "scripts"
            scripts.mkdir()
            for name in ("ExportProjectManifest.java", "ExportFunctionArtifacts.java"):
                (scripts / name).write_text("// test\n", encoding="utf-8")
            command = build_export_command(
                binary=binary,
                ghidra_project_dir=root / "project",
                ghidra_project_name="sample",
                scripts_dir=scripts,
                output_dir=root / "output",
                ghidra_home=home,
                overwrite=True,
            )
            self.assertIsInstance(command, list)
            self.assertEqual(command[0], str(analyze.resolve()))
            self.assertIn("ExportProjectManifest.java", command)
            self.assertIn("ExportFunctionArtifacts.java", command)
            self.assertNotIn("sh", command)


if __name__ == "__main__":
    unittest.main()
