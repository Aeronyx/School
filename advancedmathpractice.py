# File: advancedmathpractice.py
# Name: George Trammell
# Date: 9/10/19
# Desc: More math practice.
# Sources: None
# OMH
import math as m
import sys

"""
1. Given the temperature t (in Fahrenheit) and the wind speed v 
(in miles per hour), the National Weather Service defines the 
effective temperature (the wind chill) to 
be: w = 35.74 + 0.6215 t + (0.4275 t - 35.75)*v**0.16 
Compose a program that takes two floats t and v from the command-line 
and writes the wind chill. Note: the formula is not valid if t is larger 
than 50 in absolute value or if v is larger than 120 or less than 3 
(you may assume that the values you get are in that range).
"""
t = float(sys.argv[1])
v = float(sys.argv[2])

w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v**0.16
print('The wind chill today is %s degrees.' %(round(w)))

"""
2. Compose a program that takes three floats x, y, and z 
as command-line arguments and writes True if the values are 
strictly ascending or descending (x<y<z or x>y>z), 
and False otherwise. You may need to look into Boolean operators 
in order to understand how to interpret these expressions.
"""
x = float(sys.argv[3])
y = float(sys.argv[4])
z = float(sys.argv[5])

print(bool((x < y < z)) or (x > y > z))
