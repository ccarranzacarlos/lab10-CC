# https://github.com/[YOUR_USERNAME]/lab10-[YOUR_INITIALS]-[YOUR_INITIALS]
# Partner 1: Carlos Carranza Santos (Doing both roles)

"""
calculator.py
- Defines functions used to create a simple calculator
One function per operation, in order.
"""

import math

def square_root(a):
    """Calculate square root of a number"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    """Calculate hypotenuse using Pythagorean theorem"""
    return math.hypot(a, b)

def add(a, b):
    """Add two numbers"""
    return a + b

def sub(a, b):
    """Subtract b from a"""
    return a - b

def mul(a, b):
    """Multiply two numbers"""
    return a * b

def div(a, b):
    """Divide b by a"""
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    """Calculate logarithm base a of b"""
    if a <= 0 or a == 1:
        raise ValueError("Invalid base for logarithm")
    if b <= 0:
        raise ValueError("Cannot calculate logarithm of non-positive number")
    return math.log(b) / math.log(a)

def exp(a, b):
    """Calculate a raised to the power of b"""
    return a ** b
