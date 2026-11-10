# https://github.com/felipeg1234/lab10-FG-SI
# Partner 1: Felipe Gaitan
# Partner 2: Seth Imig

import math

def add(a, b): return a + b

def subtract(a, b): return a - b

def mul(a, b): return a * b

def div(a, b):
    if a == 0: raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0: raise ValueError
    return math.log(a, b)

def exp(a, b): return math.pow(a, b)

def square_root(a):
    if a < 0: raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b): return math.hypot(a, b)