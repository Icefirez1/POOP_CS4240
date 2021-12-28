from rt import close_enough, run_test, run_test_float
def power_rec(base, exp):
    """prec:  base is a number, exp is an integer
    postc: retuerns base**exp using a recursive version of the 
    divide and conquer power algorithm"""  
    if (exp < 0):
        base = 1/base
        exp = -exp
    if (exp == 0):
        return 1
    if (exp%2 == 1):
        exp = exp - 1
        num = base
    else: 
        num = 1
    return num * power_rec(base * base, exp//2)


def power_iter(x, b):
    """prec:se is a number, exp is an integer
    postc: returns base**exp using an itearative version of the 
    divide and conquer power algorithm"""  
    leftovers = 1
    while (b >= 2 or b < 0):
        if (b < 0):
            x = 1/x
            b = -b
        if (b%2 == 1):
            b = b-1
            leftovers = leftovers * x
        x = x * x 
        b = b//2
    return x * leftovers 


#************MAIN**************
def main():
    ##run tests here
    run_test(power_rec, 1024, [2, 10])
    run_test(power_rec, 81, [9, 2])
    run_test(power_rec, .25, [2, -2])
    run_test(power_iter, 1024, [2, 10])
    run_test(power_iter, 81, [9, 2])
    run_test(power_iter, .25, [2, -2])

    

#______________________________________
main()