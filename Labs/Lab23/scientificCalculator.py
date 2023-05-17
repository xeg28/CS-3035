# --- CODE ---

from cmath import *
from decimal import *

# adds complex numbers, both real and imaginary
def complexNumberAdder(a, b):
    return a + b

# only adds the real part of the imaginary number
def complexPartialAdder(a, b):
    return a.real + b.real

# multpiplies two double values and returns a string with the specified precision
def precisionMultiplier(a, b, c):
    getcontext().prec = c
    return Decimal(a) * Decimal(b)
    
# A fuction that takes a math function two required values and one optional
def scientficCalculator(op, a, b, *c):
    if op == precisionMultiplier :
        return op(a,b,c[0])
    else:
        return op(a,b)

# testing the functions
print(scientficCalculator(complexNumberAdder,1+2j, 3+5j))
print(scientficCalculator(complexPartialAdder,1+2j, 3+5j))
print(scientficCalculator(precisionMultiplier,3.14159, 2.43221, 4))

# --- OUTPUT ---

# (4+7j)
# 4.0
# 7.641


