def sum_from(n, x):
    """prec:  n is an integer, x is a list of integers.
postc: returns a sublist of x whose sum is n if it exists
and the graveyard object None otherwise.  """
    if n == 0: 
        return []
    if x == []:
         return None
    
    first = x[0]
    rest = x[1:]
    try1 = sum_from(n, rest)
    if try1 != None: 
        return try1
    try2 = sum_from(n - first, rest)
    if try2 != None: 
        return [first, try2]
        return None # so i could never figure it out recursivly, like it does the numbers but idk how to put it into one list 
    # sorry to dissapoint Dr. Morrison
#*******************

print(sum_from(10,[5,5,4,3,2]))