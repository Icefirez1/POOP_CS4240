####################################
# Author: Al Pagar
#  Date created: 2 sep 2021
#  Date last modified: 2 sep 2021
#  Program: helpFunction.py
# 
# functions
####################################



def square(x):
    """preconditioin: x is a number.
    postcondition: returns the square of x
    """
    return x*x

def swap(x,j,k):
    """prec: x is a list.
j and k are valid indices less than len(x)
postc: swaps the values at the specified indices."""

    x[j], x[k] = x[k], x[j]

#***********MAIN************
print(square.__doc__)
x = [5,6,7,8]
print(x)
swap(x,0,1)
print(x)