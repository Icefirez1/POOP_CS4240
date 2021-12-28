from math import log, e, sin, cos, asin, pi
from run_tests import close_enough, run_test, run_test_float
## you can now use log(x) for the natural log of x.
## You can only use the imported functions that I specify.
def greet(name = "Stranger"):
    """prec:  name is a keyword argument with default value "Stranger"
    postc: returns the string Hello, name!"""  
    return "Hello " + name
    

def log_base(x, b = e):
    """prec:  x > 0 and b > 0 is a keyword argument
    postc: use the change-of-base formula to compute 
    the logarithm of x with base b.  The default is that
    the natural log of x is returned."""

    num = log(x)/log(b)
    return num

def truncate(s, n = 3):
    """prec:  s is a string, n is a nonnegative integer
    and a keyword argument.  if len(s) > n return s; otherwise
    truncate at n.  By default, n = 3.""" 
    
    if (len(s) > n):
        return s
    if (len(s) <= n):
        return s[:n]
     
def protean_sin(x, radians = True ):
    """prec: x is a number, radians is a boolean and a
    keyword argument.  
    postc: returns sin(x) using radians if radians is True
    and sin(x) in degrees if radians is false.
    The default is True"""
    if (radians):
        return sin(x)
    else:
        return sin(x*(pi/180))



def protean_asin(x, radians = True):
    """prec: x is a number, -1 <= x <= 1.
    radians is a keyword argument.  
    postc: returns sin(x) using radians if radians is True
    and arcsin(x) in degrees if radians is false.
    The default is True."""
    if (radians):
        return sin(x)
    else:
        return asin((x*180)/pi) 


#*******MAIN FUNCTION*********
def main():
    run_test(greet, "Hello Al", ["Al"])
    run_test_float(log_base, 0.8889281468629106, [42,67])
    run_test_float(log_base,1.3862943611198906 , [4])
    run_test(truncate, "urmom", ["urmom", 2])
    run_test(truncate, "hello", ["hello"])
    run_test_float(protean_sin, 0 , [pi, True] )
    run_test_float(protean_asin, 0 , [pi, True] )
    
#*******RUNNING OF MAIN**********
main()
 