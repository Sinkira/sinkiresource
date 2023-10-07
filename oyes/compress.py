import os
from PIL import Image

compression_strength = 5


def compress_png_to_webp(png_path, webp_path, quality=80):
    img = Image.open(png_path).convert("RGBA")
    img.save(webp_path, "WEBP", quality=quality)
    return os.path.getsize(webp_path)

def compress_pngs_to_webps():
    for dirpath, dirnames, filenames in os.walk("."):
        png_files = [f for f in filenames if f.endswith(".png")]
        for png_file in png_files:
            png_path = os.path.join(dirpath, png_file)
            webp_file = png_file.replace(".png", ".webp")
            webp_path = os.path.join(dirpath, webp_file)
            if os.path.exists(webp_path):
                continue
            original_size = os.path.getsize(png_path)
            target_size = original_size // compression_strength
            quality = 80
            compressed_size = compress_png_to_webp(png_path, webp_path, quality)
            while compressed_size > target_size and quality > 0:
                quality -= 1
                compressed_size = compress_png_to_webp(png_path, webp_path, quality)

compress_pngs_to_webps()