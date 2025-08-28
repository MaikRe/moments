import os
import random
from PIL import Image, ImageDraw, ImageFont

# Parameters
num_images = 100
output_dir = "generated_images"

formats = {
    'PNG': '.png',
    'JPEG': '.jpg',
    'WEBP': '.webp'
}

aspect_ratios = {
    '16:9': [(1920, 1080), (1280, 720), (854, 480)],
    '4:3': [(1024, 768), (800, 600), (640, 480)],
    '1:1': [(1000, 1000), (512, 512)],
}

os.makedirs(output_dir, exist_ok=True)

def random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

# Load a scalable font or raise error
def load_font(size):
    possible_fonts = [
        "/usr/share/fonts/TTF/DejaVuSerif-Bold.ttf",  # Linux
    ]
    for path in possible_fonts:
        if os.path.isfile(path):
            return ImageFont.truetype(path, size)
    raise RuntimeError("No suitable TTF font found. Please install DejaVuSans or Arial.")

for i in range(1, num_images + 1):
    fmt = random.choice(list(formats.keys()))
    ext = formats[fmt]
    ratio = random.choice(list(aspect_ratios.keys()))
    width, height = random.choice(aspect_ratios[ratio])
    color = random_color()
    img = Image.new("RGB", (width, height), color)

    draw = ImageDraw.Draw(img)

    # Set font size based on image dimensions
    font_size = int(min(width, height) * 0.4)
    font = load_font(font_size)

    text = str(i)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_position = ((width - text_width) // 2, (height - text_height) // 2)

    draw.text(text_position, text, fill="white", font=font)

    filename = f"image_{i}{ext}"
    img.save(os.path.join(output_dir, filename), format=fmt)

print(f"{num_images} large-numbered images generated in '{output_dir}'")
