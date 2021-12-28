def power_rec(base, exp):
    """prec:  base is a number, exp is an integer
    postc: retuerns base**exp using a recursive version of the 
    divide and conquer power algorithm"""  
    if (exp < 0):
        base = 1/base
        exp = -exp
    if (int(exp) == 2):
        return base * base
    if (exp == 0):
        return 1
    if (exp%2 == 1):
        exp = exp - 1
        num = base
    else: 
        num = 1
    return num * power_rec(base * base, exp//2)

print(power_rec(3,6))
print(power_rec(2,-2))