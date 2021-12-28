
from math import e, log

def log_base(x, b = e):
    """prec:  x > 0 and b > 0 is a keyword argument
    postc: use the change-of-base formula to compute 
    the logarithm of x with base b.  The default is that
    the natural log of x is returned."""

    num = log(x)/log(b)
    return num



print(log_base(42,67))