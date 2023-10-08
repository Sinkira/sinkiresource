import os
from PIL import Image

# Get all .webp files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.webp')]

for file in files:
    img = Image.open(file)
    # Get the dimensions of the image
    width, height = img.size
    # Resize the image to one-fifth of its original size
    img = img.resize((width//5, height//5))
    # Overwrite the original image with the resized image
    img.save(file)
