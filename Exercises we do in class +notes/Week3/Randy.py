####################################
# Author: Al Pagar
#  Date created: 2 sep 2021
#  Date last modified: 2 sep 2021
#  Program: Randy.py
# 
# functions
####################################

import random 

#random.randint is INCONSISTANT. It is not a pure function
for k in range(10):
    print(random.randint(1,6), random.randint(1,6))

