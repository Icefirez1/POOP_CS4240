####################################
# Author: Al Pagar
#  Date created: September 9 2021
#  Date last modified: 9 sep 2021
#  Program: nagging.py
#  
####################################

def nag():
    x = input("Enter a number 1-4: ")
    x = int(x)
    if (x <= 4 and x >= 1):
        print("You chose {x}.")
    elif (x == 69):
        return
    else:
        print("wrong number dummy")
        nag()

#********MAIN*********
nag()