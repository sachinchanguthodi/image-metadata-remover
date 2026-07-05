import argparse
import sys
from pathlib import Path

from PIL import Image

SUPPORTED = {".jpg", ".jpeg", ".png", ".webp", ".tiff", ".tif", ".bmp"}


def strip_metadata(src: Path, dst: Path) -> None:
    with Image.open(src) as img:
        # Rebuilding the image from raw pixel data drops EXIF, XMP, ICC
        # profiles, and any other embedded metadata chunks.
        data = list(img.getdata())
        clean = Image.new(img.mode, img.size)
        clean.putdata(data)
        clean.save(dst)


def iter_targets(path: Path):
    if path.is_file():
        yield path
    else:
        for p in sorted(path.rglob("*")):
            if p.suffix.lower() in SUPPORTED:
                yield p


def main():
    parser = argparse.ArgumentParser(
        description="Strip all metadata (EXIF, XMP, ICC, GPS, etc.) from images."
    )
    parser.add_argument("input", help="Image file or directory")
    parser.add_argument(
        "-o", "--output",
        help="Output file or directory (default: overwrite in place)",
    )
    args = parser.parse_args()

    in_path = Path(args.input)
    if not in_path.exists():
        sys.exit(f"Input not found: {in_path}")

    out_path = Path(args.output) if args.output else None

    count = 0
    for src in iter_targets(in_path):
        if out_path is None:
            dst = src
        elif in_path.is_dir():
            dst = out_path / src.relative_to(in_path)
            dst.parent.mkdir(parents=True, exist_ok=True)
        else:
            dst = out_path

        strip_metadata(src, dst)
        print(f"Cleaned: {src} -> {dst}")
        count += 1

    if count == 0:
        print(f"No supported images found in {in_path}")


if __name__ == "__main__":
    main()
