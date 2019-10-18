from PIL import Image
import math
import random

imgx = 512
imgy = 512

image = Image.new("RGB", (imgx, imgy))

#-----------------
# Drawing
#-----------------

# stripe thing
# for i in range(1, imgx):
#     x = i
#     r = (100%i) * 5
#     for y in range(imgx):
#         image.putpixel((x, y), (r, 0, 0))

for i in range(80):
    x = random.randint(25, imgx-25)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    for y in range(imgy):
        image.putpixel((x, y), (r, g, b))
        moveType = random.random()
        if moveType < .2:
            x += 1
        elif (moveType > .2) and (moveType < .4):
            x -= 1

# ----------------
image.save("Dot.png", "PNG")