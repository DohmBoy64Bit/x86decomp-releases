"""Provide tests.test_project functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from pe_fixture import build_minimal_pe32
from x86decomp.project import initialize_project, verify_project


class ProjectTests(unittest.TestCase):
    """Implement the ProjectTests class using its declared base class contract.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def test_initialize_and_verify(self) -> None:
        """Verify initialize and verify.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            binary = build_minimal_pe32(root / "sample.exe")
            project_root = root / "project"
            project = initialize_project(binary, project_root)
            self.assertTrue((project_root / "project.json").is_file())
            self.assertTrue((project_root / "analysis" / "program.json").is_file())
            self.assertEqual(project["binary"]["source_kind"], "copied")
            result = verify_project(project_root)
            self.assertTrue(result["valid"], result["failures"])

    def test_detect_binary_tampering(self) -> None:
        """Verify detect binary tampering.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            binary = build_minimal_pe32(root / "sample.exe")
            project_root = root / "project"
            initialize_project(binary, project_root)
            stored = project_root / "original" / "sample.exe"
            stored.write_bytes(stored.read_bytes() + b"tamper")
            result = verify_project(project_root)
            self.assertFalse(result["valid"])
            self.assertTrue(any("SHA-256" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
