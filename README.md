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

Clean a single image (overwrites in place):

```bash
python remove_metadata.py photo.jpg
```

Clean a single image into a new file:

```bash
python remove_metadata.py photo.jpg -o clean.jpg
```

Clean every image in a folder (recursively) into an output folder,
preserving filenames and subfolder structure:

```bash
python remove_metadata.py ./photos -o ./photos_clean
```

## Supported formats

`.jpg` `.jpeg` `.png` `.webp` `.tiff` `.tif` `.bmp`

## License

MIT
