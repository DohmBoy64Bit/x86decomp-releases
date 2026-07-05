"""Provide tests.test_compiler functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from x86decomp.compiler import run_compiler_profile


class CompilerTests(unittest.TestCase):
    """Implement the CompilerTests class using its declared base class contract.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    @unittest.skipUnless(shutil.which("gcc"), "gcc is unavailable")
    def test_compile_i386_object(self) -> None:
        """Verify compile i386 object.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        repository = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "add.o"
            report = run_compiler_profile(
                repository / "examples" / "compiler-profiles" / "gcc-i686-object.json",
                repository / "examples" / "sample_source" / "add.c",
                output,
            )
            self.assertTrue(report["success"])
            self.assertTrue(output.is_file())


if __name__ == "__main__":
    unittest.main()
