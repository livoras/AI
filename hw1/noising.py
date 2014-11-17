import random
from PIL import Image

img = Image.open("original.png")
width, height = img.size

for x in xrange(width):
    for y in xrange(height):
        val = img.getpixel((x, y))
        if random.random() * 100 < 90:
            continue
        if (val == 255):
            img.putpixel((x, y), 0)
        else:
            img.putpixel((x, y), 255)

img.save("with-noise.png")
