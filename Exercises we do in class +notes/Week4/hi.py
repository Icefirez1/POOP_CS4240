####################################
# Author: Al Pagar
#  Date created: September 9 2021
#  Date last modified: 9 sep 2021
#  Program: hi.py
#  
####################################
def print_list(x):
    if(len(x)==0):
        return 
    first = x[0]
    rest = x[1:]
    print(first)
    print_list(rest)

#********MAIN*********8
x = ["nyah", "yah", "nyah"] 

print_list(x)