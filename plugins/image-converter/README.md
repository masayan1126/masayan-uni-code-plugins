# image-converter

Convert PNG/JPG/JPEG images to WebP, ICO, SVG formats.

## Installation

```bash
pip install Pillow
```

## Usage

### Slash Command

```
/convert-image
```

### Direct Script Usage

```bash
# Convert to WebP
python3 scripts/convert_image.py image.png --format webp

# Convert to ICO with custom sizes
python3 scripts/convert_image.py image.png --format ico --sizes 16,32,48,256

# Convert to SVG (embedded image)
python3 scripts/convert_image.py image.png --format svg
```

## Supported Formats

| Input | Output |
|-------|--------|
| PNG, JPG, JPEG | WebP |
| PNG, JPG, JPEG | ICO |
| PNG, JPG, JPEG | SVG (embedded) |

## License

MIT
