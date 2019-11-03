# George Trammell, Oct. 27

from PIL import Image
from math import sqrt
def complexmandel(c, z=complex(0,0), escapeCounter=0):
    # calculate
    z = z**2+c
    escapeCounter += 1
    # escape counter
    if abs(z) >= 2 or escapeCounter > maxIteration:
        if escapeCounter > maxIteration:
            return 0
        return escapeCounter

    return complexmandel(c, z, escapeCounter)

def complexjulia(z=complex(0,0), escapeCounter=0):
    c = complex(.31467,.01123)
    z = z**2+c
    escapeCounter += 1
    if abs(z) >= 2 or escapeCounter > maxIteration:
        return escapeCounter
    return complexjulia(z, escapeCounter)

maxIteration = 150


#------------------------------
# Fuchsia Infinity
#------------------------------
xmin, xmax = -0.1904296875, -0.1376953125
ymin, ymax = 0.6240234375, 0.6767578125

imgx, imgy = 1000, 1000
fuchsiaInfinity = Image.new("RGB", (imgx, imgy))

for y in range(imgy):
    cy = y * (ymax-ymin)/(imgy) + ymin
    for x in range(imgx):
        cx = x * (xmax-xmin)/(imgx) + xmin
        c = complex(cx, cy)
        iterations = complexmandel(c)
        r = int(iterations*4*x*y)%256 #100
        g = 0
        b = int(iterations*4*-x*y)%100 #256
        
        fuchsiaInfinity.putpixel((x, y), (r, g, b))

fuchsiaInfinity.save("fuchsiaInfinity.png", "PNG")

# ------------------------------
# Stairway to Heaven
# ------------------------------
xmin, xmax = -0.92578125, -0.69140625
ymin, ymax = 0.076171875, 0.310546875

stairwayToHeaven = Image.new("RGB", (imgx, imgy))
maxIteration = 256

for y in range(imgy):
    cy = y * (ymax-ymin)/(imgy) + ymin
    for x in range(imgx):
        cx = x * (xmax-xmin)/(imgx) + xmin
        c = complex(cx, cy)
        iterations = complexmandel(c)
        if iterations > 100:
            b = iterations
        else:
            r = int(iterations*y//4)%150
            b = 0

        if iterations <= 140 and iterations > 100: # 20
            g = iterations
        elif iterations < 100:
            g = int(iterations*y//4)%150
        
        stairwayToHeaven.putpixel((x, y), (r, g, b))

stairwayToHeaven.save("stairwayToHeaven.png", "PNG")

# ------------------------------
# Hot v. Cold
# ------------------------------

hotVsCold = Image.new("RGB", (imgx, imgy))

xmin, xmax = 0, 2
ymin, ymax = 0, 2

for y in range(imgy):
    cy = y * (ymax-ymin)/(imgy) + ymin
    for x in range(imgx):
        cx = x * (xmax-xmin)/(imgx) + xmin
        c = complex(cx, cy)
        iterations = complexjulia(c)
        r = 0
        g = (iterations*3)%256
        b = (iterations*3)%256
        
        hotVsCold.putpixel((x, y), (r, g, b))

for y in range(imgy):
    cy = y * (ymax-ymin)/(imgy) + ymin
    for x in range(imgx):
        cx = x * (xmax-xmin)/(imgx) + xmin
        c = complex(cx, cy)
        iterations = complexjulia(c)
        r = 0
        g = (iterations*3)%256
        b = (iterations*6)%256
        if b > 80 or g > 80:
            hotVsCold.putpixel((x, y), (r, g, b))
        elif iterations > 1:
            r = int(iterations*30)%256
            g = int(iterations*7)%256 # 0
            b = int(iterations*10)%256
            hotVsCold.putpixel((x, y), (r, g, b))

for y in range(imgy):
    cy = y * (ymax-ymin)/(imgy) + ymin
    for x in range(imgx):
        cx = x * (xmax-xmin)/(imgx) + xmin
        c = complex(cx, cy)
        iterations = complexjulia(c)
        r = 0
        g = (iterations*3)%256
        b = (iterations*6)%256
        if b > 80 or g > 80:
            hotVsCold.putpixel((-x, -y), (r, g, b))
        elif iterations > 1:
            r = int(iterations*5)%256
            g = 0
            b = int(iterations*20)%256
            hotVsCold.putpixel((-x, -y), (r, g, b))

hotVsCold.save("hotVsCold.png", "PNG")