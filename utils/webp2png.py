from PIL import Image # Open a WebP image
def convert(webp_path):
    webp_image =Image.open(webp_path)
    name = webp_path.replace("webp","png")
    png_image = webp_image.convert("RGBA")
    png_image.save(name)
