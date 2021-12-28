def trimmed_sum(x,limit):
    out = 0 
    for k in x: 
        if k <= limit: 
            out += k  

def trimmed_sum_better(x,limit):
    return sum([k for k in x if k <= limit])

def foo (x):
    '''prec: x is a numerical list .
    postc: returns the sum of the cubes of the nonegative elements o x
    '''
    return sum([i**3 for i in x if i >= 0])









#*****************************
x = [1,2,3,4,5,6,7,8,9,10]
y = []
for k in x:
    y.append(k*k)
print(y)

print([k*k for k in x])
lol = [-3,4,-2,8]
print (foo(x))

zoo = {"cat" : 5, "dog": 3, "tapir": 9, "okapi":2 , "hyena":1 }
rare = {k:v for k,v in zoo.items() if v <= 2}
print (rare)