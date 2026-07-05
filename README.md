# Image Metadata Remover

A small Python script that strips **all** metadata from images — EXIF, GPS
location, camera info, XMP, ICC color profiles, and any other embedded
chunks — by rebuilding the image from raw pixel data only.

## Why

Photos from phones and cameras often carry EXIF metadata (including GPS
coordinates) that you may not want to share publicly. This tool produces a
clean copy with none of that.

## Install

```bash
pip install -r requirements.txt
```

## Usage

Clean a file or folder in place (overwrites the originals):

```bash
python remove_metadata.py photo.jpg
python remove_metadata.py ./photos
```

Clean a file or folder into a new location, preserving filenames and
subfolder structure:

```bash
python remove_metadata.py photo.jpg -o clean.jpg
python remove_metadata.py ./photos -o ./photos_clean
```

### Windows: drag-and-drop

No terminal needed — just drag an image or folder onto one of these:

- `clean_inplace.bat` — removes metadata in place
- `clean_to_new.bat` — saves a cleaned copy next to the original with a
  `_clean` suffix

## Supported formats

`.jpg` `.jpeg` `.png` `.webp` `.tiff` `.tif` `.bmp`

## License

MIT
