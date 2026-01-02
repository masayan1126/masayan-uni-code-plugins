#!/usr/bin/env python3
"""
Image Converter - Convert PNG/JPG/JPEG to WebP, ICO, SVG formats.
"""

import argparse
import base64
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow is required. Install with: pip install Pillow", file=sys.stderr)
    sys.exit(1)


def convert_to_webp(img: Image.Image, output_path: Path, quality: int = 85) -> None:
    """Convert image to WebP format."""
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        img = img.convert('RGBA')
    else:
        img = img.convert('RGB')
    img.save(output_path, 'WEBP', quality=quality)
    print(f"Created: {output_path}")


def convert_to_ico(img: Image.Image, output_path: Path, sizes: list[int]) -> None:
    """Convert image to ICO format with multiple sizes."""
    ico_sizes = [(s, s) for s in sizes]
    img.save(output_path, 'ICO', sizes=ico_sizes)
    print(f"Created: {output_path} (sizes: {sizes})")


def convert_to_svg(img: Image.Image, output_path: Path, input_path: Path) -> None:
    """Convert image to SVG format (embedded base64)."""
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # Get original format
    suffix = input_path.suffix.lower()
    mime_type = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
    }.get(suffix, 'image/png')

    # Read original file and encode
    with open(input_path, 'rb') as f:
        img_data = base64.b64encode(f.read()).decode('utf-8')

    width, height = img.size
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <image width="{width}" height="{height}"
         xlink:href="data:{mime_type};base64,{img_data}"/>
</svg>'''

    output_path.write_text(svg_content)
    print(f"Created: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert PNG/JPG/JPEG images to WebP, ICO, or SVG format.'
    )
    parser.add_argument('input', type=Path, help='Input image file (PNG, JPG, JPEG)')
    parser.add_argument(
        '--format', '-f',
        choices=['webp', 'ico', 'svg'],
        required=True,
        help='Output format'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        help='Output file path (default: input name with new extension)'
    )
    parser.add_argument(
        '--quality', '-q',
        type=int,
        default=85,
        help='Quality for WebP (1-100, default: 85)'
    )
    parser.add_argument(
        '--sizes', '-s',
        type=str,
        default='16,32,48,256',
        help='Comma-separated sizes for ICO (default: 16,32,48,256)'
    )

    args = parser.parse_args()

    # Validate input
    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    if args.input.suffix.lower() not in ('.png', '.jpg', '.jpeg'):
        print(f"Error: Unsupported input format: {args.input.suffix}", file=sys.stderr)
        sys.exit(1)

    # Determine output path
    output_path = args.output or args.input.with_suffix(f'.{args.format}')

    # Load image
    try:
        img = Image.open(args.input)
    except Exception as e:
        print(f"Error: Failed to open image: {e}", file=sys.stderr)
        sys.exit(1)

    # Convert
    if args.format == 'webp':
        convert_to_webp(img, output_path, args.quality)
    elif args.format == 'ico':
        sizes = [int(s.strip()) for s in args.sizes.split(',')]
        convert_to_ico(img, output_path, sizes)
    elif args.format == 'svg':
        convert_to_svg(img, output_path, args.input)

    img.close()


if __name__ == '__main__':
    main()
