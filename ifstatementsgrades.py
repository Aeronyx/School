# File: ifstatementsgrades.py
# Name: George Trammell
# Date: 9/14/19
# Desc: A program that calculates the appropriate grade based off user input.
# Sources: None
# OMH

import sys

# User input as float
try:
    float(sys.argv[1])
except ValueError:
    print('You didn\'t input a valid number. Please try again.')
    sys.exit(0)

numberGrade = float(sys.argv[1])

if numberGrade >= 4.85:
    print('A+')
elif numberGrade >= 4.65:
    print('A')
elif numberGrade >= 4.5:
    print('A-')
elif numberGrade >= 4.2:
    print('B+')
elif numberGrade >= 3.85:
    print('B')
elif numberGrade >= 3.5:
    print('B-')
elif numberGrade >= 3.2:
    print('C+')
elif numberGrade >= 2.85:
    print('C')
elif numberGrade >= 2.5:
    print('C-')
elif numberGrade >= 2.0:
    print('D+')
elif numberGrade >= 1.5:
    print('D')
elif numberGrade >= 1.0:
    print('D-')
elif numberGrade >= 0:
    print('F')