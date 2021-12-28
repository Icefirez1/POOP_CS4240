
from random import shuffle

def zipper(x,y):
    p = 0 
    q = 0 
    out = []
    while p < len(x) and q < len(y):
        if x[p] < y[q]:
            out.append(x[p])
            p += 1
        else: 
            out.append(y[q])
            q += 1
    out += x[p:]
    out += y[q:]
    return out

def merge_sort(x):
    if len(x) <= 1:
        return x
    mid = len(x)//2
    first = x[:mid]
    second = x[mid:]
    return zipper(merge_sort(first), merge_sort(second))

   

#***************MAIN*****************
"""x = [1,2,3,4,5,6,7]
y = [11,12,13,14,15,16,17]
print(zipper(x,y))
"""
listz = list(range(100))
shuffle(listz)
print(listz)
print(merge_sort(listz))
