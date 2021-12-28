############################################################
#   Author: Morrison
#   Date created:  2021-08-30
#   Date last modified:  2021-09-15
#   rt Module
#   Usage is as follows for non-floating point return values:
#       run_test(function, expected_output, [arg1, arg2, ....])
#   Usage for floating-point return values:
#       run_test(function, expected_output, [arg1, arg2, ....])
################# DO NOT CHANGE THIS CODE ###################
TOLERANCE = 1e-6
def close_enough(x,y):
    return abs(x - y) < TOLERANCE
def run_test(function, expected, args):
    if function(*args) == expected:
        print(f"PASS for case {args} for function {function.__name__}")
    else:
        print(f"FAIL because {function.__name__}({args}) != {expected}")
def run_test_float(function, expected, args):
    if close_enough(function(*args), expected):
        print(f"PASS for case {args} for function {function.__name__}")
    else:
        print(f"FAIL because {function.__name__}({args}) != {expected}")