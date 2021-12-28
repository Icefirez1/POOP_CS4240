# ###########################################################
#   Authors: Morrison with revision by Chris Agrella
#   Date created:  2021-08-30
#   Date last modified:  2021-09-17
#   FREE CODE FOR WRITING TESTS
#   Usage for a non-float return value
#       run_test(function_name, expected_output, [arg1, arg2, .... ])
#   Usage for a float return value
#       run_test_float(function_name, expected_output, [arg1, arg2, .... ])
# ############################################################
TOLERANCE = 1e-6


def close_enough(x, y):
    return abs(x - y) < TOLERANCE


def run_test(function, expected, args):
    # print(f"args = {args}")
    if len(args) == 1:
        # print("made it into the if statement")
        args = args[0]
        # print(f"args = {args}")
        if function(args) == expected:
            print(f"PASS for case {args} ({function(args)})")
        else:
            print(
                f"FAIL because f({args}) != {expected}. Failed Output: {function(args)}"
            )
    else:
        if function(*args) == expected:
            print(f"PASS for case {args} ({function(*args)})")
        else:
            print(
                f"FAIL because f({args}) != {expected}. Failed Output: {function(*args)}"
            )

def run_test_float(function, expected, args):
    if type(args) == list and len(args) == 1:
        args = args[0]
        if close_enough(function(args), expected):
            print(f"PASS for case {args} ({function(args)})")
        else:
            print(
                f"FAIL because f({args}) != {expected}. Failed Output: {function(args)}"
            )
        return
    else:
        if close_enough(function(*args), expected):
            print(f"PASS for case {args} ({function(*args)})")
        else:
            print(
                f"FAIL because f({args}) != {expected}. Failed Output: {function(*args)}")

