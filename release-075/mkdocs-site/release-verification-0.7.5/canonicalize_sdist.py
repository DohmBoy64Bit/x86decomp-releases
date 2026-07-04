from __future__ import annotations

import argparse
import gzip
import io
import os
import tarfile
import tempfile
from pathlib import Path

EPOCH = 1704067200


def canonicalize(source: Path, output: Path) -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        with tarfile.open(source, "r:gz") as archive:
            archive.extractall(root, filter="data")
        tops = list(root.iterdir())
        if len(tops) != 1 or not tops[0].is_dir():
            raise RuntimeError("sdist must contain exactly one top-level directory")
        top = tops[0]
        buffer = io.BytesIO()
        with tarfile.open(fileobj=buffer, mode="w", format=tarfile.PAX_FORMAT) as out:
            paths = [top] + sorted(top.rglob("*"), key=lambda p: p.relative_to(root).as_posix())
            for path in paths:
                rel = path.relative_to(root).as_posix()
                info = tarfile.TarInfo(rel + ("/" if path.is_dir() else ""))
                info.mtime = EPOCH
                info.uid = 0
                info.gid = 0
                info.uname = "root"
                info.gname = "root"
                if path.is_dir():
                    info.type = tarfile.DIRTYPE
                    info.mode = 0o755
                    info.size = 0
                    out.addfile(info)
                elif path.is_symlink():
                    info.type = tarfile.SYMTYPE
                    info.mode = 0o777
                    info.linkname = os.readlink(path)
                    info.size = 0
                    out.addfile(info)
                elif path.is_file():
                    info.type = tarfile.REGTYPE
                    info.mode = 0o755 if os.access(path, os.X_OK) else 0o644
                    data = path.read_bytes()
                    info.size = len(data)
                    out.addfile(info, io.BytesIO(data))
                else:
                    raise RuntimeError(f"unsupported sdist member: {path}")
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("wb") as raw:
            with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=EPOCH, compresslevel=9) as zipped:
                zipped.write(buffer.getvalue())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    canonicalize(args.source, args.output)


if __name__ == "__main__":
    main()
