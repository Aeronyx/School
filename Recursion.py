# File: Recursion.py
# Name: George Trammell
# Date: 10/15/19
# Desc: GCD using Euclid's Algorithm
# Sources: Googled Euclid's Algorithm (https://en.wikipedia.org/wiki/Euclidean_algorithm)
# On my honor, I have neither given nor received unauthorized aid.

def findGCD(a, b):
    if b == 0:
        return a
    else:
        return findGCD(b, a%b)

