####################################
# Author: Al Pagar
#  Date created: 14 sep 2021
#  Date last modified: 14 sep 2021
# 
# hi bestie
####################################

def product (*x):
    out = 1 
    for item in x: 
        out *= item
    return out 

def zipout(x):
    #prec: x is a list
    for k in range(len(x)):
        x[k] = 0 



#**********MAIN************
x = [1,2,3,4]
print(x)
zipout(x)
print(x)

#print(product(1,2,3,4,5,6,7,8,9,10))

for i in range(100):
    print("ur mom " + str(i))


for l in "Cows":
    print(l.upper() * 10) 