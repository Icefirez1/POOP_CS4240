import random 

def is_in_order(x):
    for k in range(0,len(x) - 1):
        if x[k] > x[k+1]:
            return False 
    return True

def bozo(x):
    while not is_in_order(x):
        random.shuffle(x)


#*************
x = [4,6,1,3,8]
print(x)
bozo(x)
print(x)