from PIL import Image

img = Image.open("with-noise.png")
width, height = img.size

print width, height