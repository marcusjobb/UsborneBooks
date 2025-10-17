#!/usr/bin/env python3
"""Convert each page of a PDF into numbered PNG images using PyMuPDF.

Usage:
    python pdf_to_png.py path/to/file.pdf [--dpi 300]

Creates a directory named after the PDF (without extension) alongside the file
and writes images as ``<stem>_0000.png`` etc. Requires ``PyMuPDF`` (`pip install
pymupdf`).
"""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyMuPDF is required. Install it with `pip install pymupdf`."
    ) from exc


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "pdf",
        type=Path,
        help="Path to the PDF file to convert",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="Output resolution in DPI (default: 300)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    pdf_path: Path = args.pdf

    if not pdf_path.exists():
        print(f"Error: {pdf_path} does not exist", file=sys.stderr)
        return 1
    if not pdf_path.is_file():
        print(f"Error: {pdf_path} is not a file", file=sys.stderr)
        return 1

    output_dir = pdf_path.with_suffix("")
    output_dir.mkdir(parents=True, exist_ok=True)

    zoom = args.dpi / 72  # 72 DPI is the default resolution
    matrix = fitz.Matrix(zoom, zoom)

    try:
        with fitz.open(pdf_path) as doc:
            total = doc.page_count
            digits = max(4, int(math.log10(total)) + 1 if total else 4)
            stem = pdf_path.stem
            for index, page in enumerate(doc):
                pix = page.get_pixmap(matrix=matrix)
                filename = f"{stem}_{index:0{digits}d}.png"
                target = output_dir / filename
                pix.save(target)
                print(f"Saved {target}")
    except Exception as exc:  # pragma: no cover
        print(f"Failed to convert {pdf_path}: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
