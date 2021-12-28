def a(x):
    '''prec: x is a list of strings 
    postc: returns the strings in x in the first half of the alphabet
    '''
    lists = []
    list2 = []
    for i in x:
        if ord(i[0].upper()) >= 101 and ord(i[0].upper()) <= 115:
            lists.append(i)
    print (lists)
    return ([list2.append(i) for i in x if ord(i[0].upper()) >= 101 and ord(i[0].upper()) <= 115])




def super_sum(f, n):
    ''' f i s a function defined on the nonnegative integers 
    n is a non-negative integer 
    postc: return sum(f(k), k = 1..n)
    '''

def intersect(A,B):
    ''' prec: A, B are sets 
    post: returns a set with all elements in A and B'''