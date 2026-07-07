"""Integration fixture that echoes stdin in uppercase and writes result.txt."""
from pathlib import Path
import sys
value = sys.stdin.read().strip()
Path("result.txt").write_text(value.upper() + "\n", encoding="utf-8")
print(value.upper())
