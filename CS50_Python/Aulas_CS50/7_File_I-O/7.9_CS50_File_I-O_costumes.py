import sys

from PIL import Image

images = []

for arg in sys.argv:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all =True, append_images=[images[1]], duration=200, loop=0
)

# Input: A list of images
# Output: A GIF file named "costumes.gif" 
# containing all the images in the list, with