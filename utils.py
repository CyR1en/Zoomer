from PIL import Image, ImageDraw
import os


def create_image():
    # Generate an image and draw a pattern
    resource_dir = os.path.join(os.getcwd(), 'resources')
    image = Image.open(os.path.join(resource_dir, 'icon.png'))
    return image
