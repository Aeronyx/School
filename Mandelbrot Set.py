# File: Mandelbrot Set.py
# Name: George Trammell
# Start Date: 10/25/19
# End Date: 11/2/19
# Desc: Using fractals and Pillow (a Python drawing library) to create art. This program generates
# three images: the first two are sections of the Mandelbrot set, and the third is from the Julia set.
# The most difficult part of this project was managing proper colors while controlling escape values to get
# the desired thematic result.
# Sources: https://www.atopon.org/mandel/#, https://en.wikipedia.org/wiki/Julia_set
# On my honor, I have neither given nor received unauthorized aid.

from PIL import Image # imports Pillow, the drawing library

#------------------------------
# Functions
#------------------------------
def complexmandel(c, z=complex(0,0), escapeCounter=0): # mandelbrot set
    # calculate z
    z = z**2+c
    escapeCounter += 1
    # escape counter, counts how many times complexmandel() was run
    if abs(z) >= 2 or escapeCounter > maxIteration: # if a value escapes, or if it reaches the maximum allowed function calls (doesn't escape)
        if escapeCounter > maxIteration: # return 0 if a value escapes
            return 0
        return escapeCounter
    return complexmandel(c, z, escapeCounter) # recursive function call

def complexjulia(z=complex(0,0), escapeCounter=0): # julia set
    c = complex(.31467,.01123) # set c value
    z = z**2+c
    escapeCounter += 1
    if abs(z) >= 2 or escapeCounter > maxIteration:
        return escapeCounter
    return complexjulia(z, escapeCounter)

maxIteration = 150 # maximum amount of recursions allowed

#------------------------------
# Fuchsia Infinity
#------------------------------
xmin, xmax = -0.1904296875, -0.1376953125 # coordinates for the desired section of each set
ymin, ymax = 0.6240234375, 0.6767578125

imgx, imgy = 1000, 1000 # image size, 1000x1000 pixels
fuchsiaInfinity = Image.new("RGB", (imgx, imgy)) # creates new image

for y in range(imgy): # all y's
    cy = y * (ymax-ymin)/(imgy) + ymin # calculate c at that y value
    for x in range(imgx): # all x's
        cx = x * (xmax-xmin)/(imgx) + xmin # calculate c at that x value
        c = complex(cx, cy) # create c, a complex number, using calculated values
        iterations = complexmandel(c) # sets iterations to escapeCounter, or 0
        r = int(iterations*4*x*y)%256 # color values
        g = 0
        b = int(iterations*4*-x*y)%100 # using the iterating variables, x and y, in the calculation creates a neat cross-stitching pattern that can often result in fractals of their own
        
        fuchsiaInfinity.putpixel((x, y), (r, g, b)) # places pixels

fuchsiaInfinity.save("fuchsiaInfinity.png", "PNG") # saves image

# ------------------------------
# Stairway to Heaven
# ------------------------------
xmin, xmax = -0.92578125, -0.69140625
ymin, ymax = 0.076171875, 0.310546875

stairwayToHeaven = Image.new("RGB", (imgx, imgy))
maxIteration = 256 # Increasing maxIteration for brighter colors

for y in range(imgy):
    cy = y * (ymax-ymin)/(imgy) + ymin
    for x in range(imgx):
        cx = x * (xmax-xmin)/(imgx) + xmin
        c = complex(cx, cy)
        iterations = complexmandel(c)
        if iterations > 100: # about to escape, on the edges
            b = iterations
        else:
            r = int(iterations*y//4)%150 # floored division and multiplication by the iterating variable y to achieve the 'staircase' effect
            b = 0
        if iterations <= 140 and iterations > 100: # about to escape, on the edges
            g = iterations
        elif iterations < 100: # otherwise, if not about to escape
            g = int(iterations*y//4)%150
        
        stairwayToHeaven.putpixel((x, y), (r, g, b))

stairwayToHeaven.save("stairwayToHeaven.png", "PNG")

# ------------------------------
# Hot v. Cold
# ------------------------------
hotVsCold = Image.new("RGB", (imgx, imgy))
xmin, xmax = 0, 2
ymin, ymax = 0, 2

# creates main Julia set fractal in the top left and bottom right corner
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

# creates top left 'hot' color scheme based on the Julia fractal
for y in range(imgy):
    cy = y * (ymax-ymin)/(imgy) + ymin
    for x in range(imgx):
        cx = x * (xmax-xmin)/(imgx) + xmin
        c = complex(cx, cy)
        iterations = complexjulia(c)
        r = 0
        g = (iterations*3)%256
        b = (iterations*6)%256
        if b > 80 or g > 80: # if the color value is important (greater than 80/256), print it
            hotVsCold.putpixel((x, y), (r, g, b))
        elif iterations > 1: # if it doesn't immediately escape
            r = int(iterations*30)%256
            g = int(iterations*7)%256
            b = int(iterations*10)%256
            hotVsCold.putpixel((x, y), (r, g, b))

# creates bottom right 'cold' color scheme based on the Julia fractal
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
            hotVsCold.putpixel((-x, -y), (r, g, b)) # flipped coordinate values for bottom left
        elif iterations > 1:
            r = int(iterations*5)%256
            g = 0
            b = int(iterations*20)%256
            hotVsCold.putpixel((-x, -y), (r, g, b)) # flipped coordinate values for bottom left

hotVsCold.save("hotVsCold.png", "PNG")

# Sam Curtis - I like that each picture has a different color scheme
# and idea behind it, and I appreciate all the creative names you gave 
# to them, but I want to understand the code a bit better and 
# there’s no comments. Make sure you explain what and how you 
# are making your pictures and also make sure you get the sources 
# and honor code at the top!
""" Added comments and sources. """

# I like the images you've created, especially the Stairway to Heaven. 
# The first thing that jumped out at me was that you referenced ymax in 
# Fuschia Infinity before you defined it, but I figure you knew this already 
# as you had it commented. I think for that one, it would be really cool if you
# zoomed all the way in and filled the image with the pattern.
""" Thanks! Stairway to Heaven was my favorite theme, and I worked hard to 
make the 'staircase' and to make the colors heavenly. I tried expanding Fuchsia Infinity 
and playing with the patters on a larger scale, but something about the 
contrast of the pink against the black really stuck out to me,
so I decided to keep it how it is. """