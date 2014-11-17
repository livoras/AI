from PIL import Image
img = Image.open("ai.png")

width, height = img.size

for x in xrange(width):
    for y in xrange(height):
        val = img.getpixel((x, y))
        if(val != 255 and val != 0): raise "FUCK"
#         if (val < 128):
#             img.putpixel((x, y), 0)
#         else:
#             img.putpixel((x, y), 255)

# img.save("ai.png")
