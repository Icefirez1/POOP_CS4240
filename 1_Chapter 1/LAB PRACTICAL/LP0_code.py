from rt import run_test, run_test_float, close_enough


#################### Problem 1 ################3
def describe_string(s):
    """prec:  s is a string
    postc:  returns "LONG" if the string has 10 or
    more characters and "SHORT" otherwise."""
    if (len(s) >= 10):
        return "LONG"
    else: 
        return "SHORT"

# ##################### Problem 2 #########################
def add_evens(nums):
    """prec: nums is a list of integers.  
    postc:  returns the sum of the EVEN numbers in numss."""
    sum = 0
    for i in nums: 
        if (i%2 == 0):
            sum = sum + i
    return sum

# ##################### Problem 3 #########################
def opposite_letter(ch):
    """prec:  ch is a one-character string
    postc: returns the "opposite" letter in the alphabet
    in lower case:
    A -> z
    a -> z
    B -> y
    b -> y
    C -> x 
    c -> x 
    etc."""
    ch = ch.lower()
    num = (ord("z")) - ord(ch)
    letter = chr(ord("a") + num)
    return letter
# ##################### Problem 4 #########################
def zipper_strings(a, b):
    """prec: a, b are strings.
    post:  returns a string that, starting with a,
    alternates characters of a and b.  When one list is
    exhausted, the rest of the other is tacked onto the end."""
    out = ""
    Done = True
    s1num = len(a)
    s1numc = 0
    s2num = len (b)
    s2numc = 0 
    while Done: 
        if s1num != s1numc: 
            out = out + a[s1numc]
            s1numc = s1numc + 1
        if s2num != s2numc: 
            out = out + b[s2numc]
            s2numc = s2numc + 1
        if s1num == s1numc and s2num == s2numc: 
            Done = False
    return out
# ##################### Problem 5 #########################
def maximum_product(lists):
    """prec: lists is a nonempty list of numerical lists.
    Note that one of the numerical lists could be empty and 
    that the product of an empty list is 1.
    postc:  returns THE LIST with the largest product.
    In the event of a tie, it returns the first such list."""
    sumlist = []
    for i in lists:
        productz = 1
        for k in i: #if variables are named weird cuz i thought it was sum at first lol 
            productz = productz * k
        sumlist.append(productz)
    maximum = max(sumlist)
    for j in range(len(lists)):
        if sumlist[j] == maximum: 
            return lists[j]

# ##################### Problem 6 #########################
def nuggets(limit, nugget_list):
    """prec: limit is an nonnegative integer
    postc: nugget_list is a list of nonnegative integers
    returns a list from nugget_list that has the
    highest total without exceeding the limit. """
    backpack = 0 
    backpack_list = [] 
    while backpack != limit: 
        lookin = max(nugget_list) 
        if (lookin > limit - backpack):
            nugget_list.remove(lookin)
        if (lookin <= limit - backpack):
            backpack = backpack + lookin 
            backpack_list.append(lookin)
            nugget_list.remove(lookin)
    backpack_list.sort()
    return backpack_list

print("************* Tests for Problem 1 **************")
run_test(describe_string, "LONG", ["antidisestablishmentarianism"])
run_test(describe_string, "SHORT", ["urmom"])
run_test(describe_string, "LONG", ["ProceduralAndObjectOrientedProgramming"])

print("************* Tests for Problem 2 **************")
run_test(add_evens, 30, [[1,4,7,9,10,16]])
print("************* Tests for Problem 3 **************")
run_test(opposite_letter, "z", ["a"])
run_test(opposite_letter, "y", ["b"])
run_test(opposite_letter, "n", ["m"])
print("************* Tests for Problem 4 **************")
run_test(zipper_strings, "cdaotggie", ["cat", "doggie"])
print("************* Tests for Problem 5 **************")
run_test(maximum_product, [6,6,6], [[[1,2], [5,6,7], [3, 0], [6,6,6]]])
print("************* Tests for Problem 6 **************")
run_test(nuggets, [4, 16], [20, [1, 2, 4, 8, 16]])
