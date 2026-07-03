from __future__ import annotations

import argparse
import gzip
from pathlib import Path

EPOCH = 1704067200


def main() -> None:
    parser = argparse.ArgumentParser(description="Canonicalize generated gzip assets for deterministic site builds.")
    parser.add_argument("site", type=Path, nargs="?", default=Path("site"))
    args = parser.parse_args()
    site = args.site.resolve()
    sitemap = site / "sitemap.xml"
    compressed = site / "sitemap.xml.gz"
    if not sitemap.is_file():
        raise SystemExit(f"missing generated sitemap: {sitemap}")
    with compressed.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=EPOCH, compresslevel=9) as stream:
            stream.write(sitemap.read_bytes())


if __name__ == "__main__":
    main()
