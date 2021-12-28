######################Problem 1###########################


def comb_nest(*x): #i dont remember what starguments are 
    """prec: x is a star argument; you pass in a comma separated
    list of lists.  
    postc:  returns a list containing the sum of each of 
    the nested lists inside of x.  
    """
    sumlist = []
    for i in x:
        sumlist.append(sum(i))
    return sumlist

#************MAIN************
k = [ [1,2,3], [7, 8], [10,3,2] ]
print(comb_nest([1,2,3]))