####################################
# Author: Al Pagar
#  Date created: September 9 2021
#  Date last modified: 9 sep 2021
#  Program: jif.py
#  
####################################

def choose(n,k):
    if (k<0 or k >n):
        return 0
    if (k == 0):
        return 1 
    if (k == n):
        return 1
    return (choose(n-1,k-1) + choose(n-1,k))

#*********MAIN*********
print(choose(4,2))
print(choose(52,5))
print(choose(10,5))

