def find_root(a,b,tol,f):
    """prec: the function f is continous and changes sign on [a,b]. 
    postc: returns a value that is within tol of a root of f."""
    while b - a > 2 * tol:
        mid = (a+b)/2
        if f(a) * f(mid) < 0: #change sign on [a,mid]
            b = mid 
        elif f(mid) * f(b) <= 0: #change sign on [mid, b]
            a = mid 
    return mid

def smallest_factor(n):
    """if n is 1, return 1 
    returns the smallest postive factor of n larger than 1"""
    if n < 0:
        n = -n
    if n == 1: 
        return 1
    if n % 2 == 0:
        return 2 
    factor = 3
    while n % factor > 0 and factor * factor <=n:
        factor += 2
    return factor if factor* factor <= n else n

def prime_factorization(n):
    nums = []
    if n < 0:
        n = -n
    if n == 1:
        return []
    d = smallest_factor(n)
    while n != 1:
        nums.append(smallest_factor(n)) 
        n = int(n/smallest_factor(n))
    return nums 
#****************************88

print(find_root(1,2,.0001, lambda x: x*x -2))

print(smallest_factor(1001))

print(prime_factorization(37))
