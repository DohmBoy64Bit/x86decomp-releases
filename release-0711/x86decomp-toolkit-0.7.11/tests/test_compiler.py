"""Verify the current toolkit behavior covered by `tests/test_compiler.py`."""
from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from x86decomp.compiler import run_compiler_profile


class CompilerTests(unittest.TestCase):
    """Group regression tests covering Compiler behavior."""
    @unittest.skipUnless(shutil.which("gcc"), "gcc is unavailable")
    def test_compile_i386_object(self) -> None:
        """Verify compile i386 object behavior."""
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
