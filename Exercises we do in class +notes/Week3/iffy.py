####################################
# Author: Al Pagar
#  Date created: 2 sep 2021
#  Date last modified: 2 sep 2021
#  Program: iffy.py
# 
# IF STATEMENT
####################################

#___________FUNCTIONS__________-

def foo(x):
    """" preconditions: x is an integer
    post conidtions: returns x as a positive if negative or returns it regulalrly"""
    if (x<0): #if the predicate is truthy, block executes 
        x = -x
    return x

def dusty(age):
    reply = ""
    if (age < 21):
        reply = "get tf out of here, punk"
    elif (age < 65): 
        reply = "name ur poison, baw"
    elif (age < 120):
        reply = "Shall  I cash yer soashal, Geezer?"
    else: 
        reply = "bestie ur a whole vampire"
    return reply 
#_____________MAIN___________

print(foo(5))
print(foo(-3))
print(foo(0))

print(dusty(21))
print(dusty(16))
print(dusty(91))
print(dusty(300))