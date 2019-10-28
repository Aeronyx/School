# George Trammell, Oct. 27

from PIL import Image

def complexmandel(c, z=complex(0,0), escapeCounter=0):
    # calculate
    z = z**2+c
    escapeCounter += 1
    # escape counter
    if abs(z) >= 2 or escapeCounter > maxIteration:
        return escapeCounter
    return complexmandel(c, z, escapeCounter)

maxIteration = 150
xmin, xmax = -1.786855640471913, -1.7868495279035415
ymin, ymax = -0.0000030074879759922624, 0.0000031050803954713047
imgx, imgy = 1000, 1000
image = Image.new("RGB", (imgx, imgy))

# def color(x, y):
#     c1 = x/250
#     c2 = y/250
#     image.putpixel((x+500, y+500), (complexmandel(complex(c1, c2), 0, 0)))

# for x in range(-500, 500):
#     for y in range(-500, 500):
#         color(x, y)

## CLASS CODE
for y in range(imgy):
    cy = y * (ymax-ymin)/(imgy) + ymin
    for x in range(imgx):
        cx = x * (xmax-xmin)/(imgx) + xmin
        c = complex(cx, cy)
        iterations = complexmandel(c)
        r = 0
        g = (iterations*y)%150
        b = (iterations*5)%150
        image.putpixel((x, y), (r, g, b))

image.save("mandel.png", "PNG")