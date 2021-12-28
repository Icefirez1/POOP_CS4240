#   Author: Morrison
#   Date:  2021-08-30
#   Program easyFunctions.py

#   FREE CODE FOR WRITING TESTS
#   Usage is demonstrated on examples below
################# DO NOT CHANGE THIS CODE ###################
def close_enough(x,y):
    return abs(x - y) < 1e6

def run_test(function, expected, args):
    print(f"args = {args}")
    if(len(args) == 1):
        print("made it into the if statement")
        args = args[0]
        print(f"args = {args}")
        if function(args) == expected:
            print(f"PASS for case {args}")
        else:
            print(f"FAIL because f({args}) != {expected}")
    else:
        if function(*args) == expected:
            print(f"PASS for case {args}")
        else:
            print(f"FAIL because f({args}) != {expected}")
        
def run_test_float(function, expected, args):
    if(type(args) == list and len(args) == 1):
        args = args[0]
        if close_enough(function(args), expected):
            print(f"PASS for case {args}")
        else:
            print(f"FAIL because f({args}) != {expected}")
        return
    else:
        if close_enough(function(*args), expected):
            print(f"PASS for case {args}")
        else:
            print(f"FAIL because f({args}) != {expected}")

############### END OF CODE NOT TO CHANGE ###########################
## sample problem with tests that returns a floating-point value.
def f2c(tempF):
    """precondition: tempF is a float or an int
    postc:  returns the equivalent temperature on the celsius scale."""
    print(tempF)
    return (tempF - 32)*5/9
test = [-40]   #put arguments in a list
expected = -40 #set this to expected output
run_test_float(f2c, expected, test)   #run test
test = [32]
expected = 0
run_test_float(f2c, expected, test)
test = [212]
expected = 100
run_test_float(f2c, expected, test)


## sample problem with tests that returns a non-float object
def get_first_name(name):
    """prec: name is given in the form last, first, and possibly a middle name in 
    a single string
    postc:  returns first name"""
    chunks = name.split()
    return chunks[1]
test = ["Roberts, Todd"]
expected = "Todd"
run_test(get_first_name, expected, test)
test = ["Morrison, John M."]
expected = "John"
run_test(get_first_name, expected, test)


## Problem 0
def c2f(tempC):
    """precondition: tempC is a float or an int
    postc: returns temperature in degrees farenheit
    """
    tempf = ((9/5)*float(tempC)) + 32

    return tempf 
print("*************** Problem 0 Tests ***************")
test_0_0 = [0]
expected_0_0 = 32
run_test_float(f2c, expected_0_0, test_0_0)
test_0_1 = [50]
expected_0_1 = 122
run_test_float(f2c, expected_0_1, test_0_1)
test_0_2 = [100]
expected_0_2 = 212
run_test_float(f2c, expected_0_2, test_0_2)


# Problem 1
def positive_part(x):
    """precondition: x is a float or an int
    postc:  returns x if x is nonnegative and 0 otherwise.
    """
    if (x > 0):
        return x
    else: 
        return 0
print("*************** Problem 1 Tests ***************")
test_1_0 = [2]
expected_1_0 = 2
run_test_float(positive_part, expected_1_0, test_1_0)
test_1_1 = [0]
expected_1_1 = 0
run_test_float(positive_part, expected_1_1, test_1_1)
test_1_2 = [-2]
expected_1_2 = 0
run_test_float(positive_part, expected_1_2, test_1_2)

## Problem 2
def truncate_string(s, n):
    """prec: s is a string, n is a nonnegative integer
    post:  returns s if s has length at most end; otherwise, 
    it truncates s to its first n characters."""
    if(len(s) < n):
        return s
    elif(len(s) > n):
        return s[:n]
print("*************** Problem 2 Tests ***************")
test_2_0 = ["catamaran", 5]
expected_2_0 = "catam"
run_test(truncate_string, expected_2_0, test_2_0)


## Problem 3
def xor(b1, b2):
    """prec b1 and b2 are booleans
    post: returns True if EXACTLY ONE of b1 or b2 is true.
    """
    if((b1 == True) and (b2 == True)):
        return False
    elif((b1 == True) or (b2 == True)):
        return True
    else:
        return False
        
print("*************** Problem 3 Tests ***************")
test_3_0 = [True, True]
expected_3_0 = False
run_test(xor, expected_3_0, test_3_0)
test_3_1 = [True, False]
expected_3_1 = True
run_test(xor, expected_3_1, test_3_1)
test_3_1 = [False, False]
expected_3_1 = False
run_test(xor, expected_3_1, test_3_1)



##Problem 4
def chop_at(s, ch):
    """s is a string, ch is a one-character string
    if ch is not present in s, just return s
    if it is find the last instance of ch in s and truncate 
    the string there (including ch)"""
    if (ch in s):
        num = s.index(ch)
        s = s[:num]
        return s
    else:
        return s
print("*************** Problem 4 Tests ***************")
test = ["Todd Roberts", "e"]
expected = "Todd Rob"
run_test(chop_at, expected, test)

## Problem 5
## Problem 5
def sort_string(s):
    """prec: s is a string of alphabetical characters
    post: returns s lower-cased and with its characters in alphabetical order.
    """
    s = s.lower()
    s = sorted(s)
    s2 = " "
    s = s2.join(s)
    s = s.replace(' ',"")
    return s
test = ["CowABUnga"]
expected = "aabcgnouw"
print("************Problem 5 Tests *************")
run_test(sort_string, expected, test)


## Problem 6
def are_anagrams(s1, s2):
    """prec: s1 and s2 are strings
    postc: return True if s1 is an anagram of s2, case INSENSITIVE."""
    check = s2[::-1]
    if (s1 == check):
        return True
    else:
        return False

print("**************PROBELM 6****************")
test = ["golf", "flog"]
expected = True
run_test(are_anagrams, expected, test)
test = ["butter", "rebut"]
expected = False
run_test(are_anagrams, expected, test)