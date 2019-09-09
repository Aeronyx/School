# File: Basic Formulas Math Practice.py
# Name: George Trammell
# Date: 9/9/19
# Desc: Python Math Practice
# Sources: None
# OMH
import sys
from math import sin, cos, sqrt

""" 1. Trying to compute F = (Gm(1)m(2))/r^2 """

# Randomly assigned values
G = 2
mass1 = 5
mass2 = 11
radius = 4

# Incorrect Equation
force = G * mass1 * mass2 / radius * radius # Expected 6.875; returns 110

# Fix:
forceFix1 = (G * mass1 * mass2) / radius**2

forceFix2 = G * mass1 * mass2 / (radius * radius)

""" 2. Compose a program that uses math.sin() and math.cos() 
to check that the value of cos^2(θ) + sin^2(θ) is approximately 
1.0 for any θ entered as a command-line argument. """

# User shell input
theta = float(sys.argv[1])

# Trig and Output
approximate = ((cos(theta)**2) + (sin(theta)**2))
print(approximate)

""" 3. Suppose that x and y are two floats that represent the 
Cartesian coordinates of a point (x, y) in the plane. Write a 
program that, given x and y, will calculate and print out the 
distance of the point from the origin. """

# User input
x = float(input('x: '))
y = float(input('y: '))

# Distance Formula
print(sqrt((x**2) + (y**2)))