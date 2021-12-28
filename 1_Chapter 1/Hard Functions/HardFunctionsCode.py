#################################################
#  Author:
#  Date:
#  harder_functions.py
#
# Make these happen using RECURSION!

from run_tests import close_enough, run_test, run_test_float
###################Problem 1################
def rectangle(m, n):
    """Precondition: m and n are nonnegative integers.
Postcondition:  returns a string containing
a rectangle of *s to the screen that 
has m rows and n columns"""
    if (m == 0):
        return ""
    return ("*" * n + "\n") + rectangle (m-1,n)

###################Problem 2################
def power(base, exp):
    """prec:  base is a number, exp is an integer`
postc: computes base**exp from scratch (no using libraries
or built-in functions).  Pay attention to the case where exp < 0!"""
    if (exp == 0):
        return 1
    if (exp < 0):
        exp = -exp 
        base = 1/base
    return base * power(base, exp-1)

###################Problem 3################
def convert_to_binary(n):
    """prec: n is an integer
    postc: retrns a string containing a binary representation of n.
    return """
    if n == 0: 
        return "0"
    if n == 1: 
        return "1"
    last = str(n%2)
    rest = n//2
    return convert_to_binary(rest) + last

###################Problem 4################
def sum_of_digits(n):
    """precondition: n is an integer
postcondition:  returns the sum of the digits of n.  You should
be able to take negative input; in such cases disregard the - sign.  """
    if n < 0: 
        n = -n 
    if n < 10: 
        return n
    last = n % 10 
    rest = n //10
    return last + sum_of_digits(rest)

###################Problem 5################
def super_summer(f, n):
    """precondition: f is a function that is defined for all nonnegative
integers.
postcondition:  returns sum(f(k), k = 1..n) """
    if n == 0: 
        return 0
    return super_summer(f, (n - 1)) + f(n)
###################Problem 6################
def reverse_string(x):
    """prec: x is a string
    postc:  return a string containing x is reverse."""
    if len(x) == 0: 
        return ""
    if len(x) == 1: 
        return x
    first = x[0]
    rest = x[1:]
    return reverse_string(rest) + first

###################Problem 7################
def sum_from(n, x):
    """prec:  n is an integer, x is a list of integers.
postc: returns a sublist of x whose sum is n if it exists
and the graveyard object None otherwise.  """
    if n == 0: 
        return []
    if x == []:
         return None
    
    first = x[0]
    rest = x[1:]
    try1 = sum_from(n, rest)
    if try1 != None: 
        return try1
    try2 = sum_from(n - first, rest)
    if try2 != None: 
        return [first, try2]
    return None # so i could never figure it out recursivly, like it does the numbers but idk how to put it into one list 
    # sorry to dissapoint Dr. Morrison

def main():
    # run your tests in this main function
    print("###################Problem 1################")
    print("###################Problem 2################")
    print("###################Problem 3################")
    print("###################Problem 4################")
    print("###################Problem 5################")
    print("###################Problem 6################")
    print("###################Problem 7################")

main()