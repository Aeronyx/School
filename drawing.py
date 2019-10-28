from PIL import Image
import math
import random

imgx = 200
imgy = 200

image = Image.new("RGB", (imgx, imgy))

#-----------------
# Drawing
#-----------------

# red stripe thing
for i in range(1, imgx):
    x = i
    r = (200%i) * 10
    for y in range(imgx):
        image.putpixel((x, y), (r, 0, 0))

for y in range((int((imgx/2) - 5)), (int((imgx/2) + 5))):
    for x in range(0, imgx):
        image.putpixel((x, y), (0, 0, 0))


# crayon drip
# for i in range(200):
#     x = random.randint(50, imgx-50)
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)

#     for y in range(imgy):
#         image.putpixel((x, y), (r, g, b))
#         moveType = random.random()
#         if moveType < .2:
#             x += 1
#         elif (moveType > .2) and (moveType < .4):
#             x -= 1

# for i in range(200):
#     y = random.randint(50, imgy-50)
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)

#     for x in range(imgx):
#         image.putpixel((x, y), (r, g, b))
#         moveType = random.random()
#         if moveType < .2:
#             y += 1
#         elif (moveType > .2) and (moveType < .4):
#             y -= 1

# ----------------
image.save("Dot.png", "PNG")