# https://github.com/felipeg1234/lab10-FG-SI
# Partner 1: Felipe Gaitan
# Partner 2: Seth Imig

import math

def add(a, b): return a + b

def sub(a, b): return a - b

def mul(a, b): return a * b

def div(a, b):
    if a == 0: raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0: raise ValueError
    return math.log(a, b)

def exp(a, b): return math.pow(a, b)

def square_root(a):
    if a < 0: raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b): return math.hypot(a, b)