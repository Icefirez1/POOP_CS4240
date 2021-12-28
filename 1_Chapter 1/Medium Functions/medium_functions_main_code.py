#################################################
#  Author: Al Pagar
#  Date: 09/09/21
#  medium_functions.py
#################################################
from run_tests import run_test, run_test_float, close_enough
###################FREE CODE######################################
def is_leap(year):
    """prec:  year is a modern year
postc: returns True if the year leaps.
"""
    out = False
    if year %4 == 0:
        out = not out
        if year % 100 == 0:
            out = not out
            if year % 400 == 0:
                out = not out
    return out
##############END FREE CODE######################################


###################Problem 1################
def meanie(theList):
    """Precondition: theList is a non-empty list of numbers
Postcondition: return the mean of the numbers."""
    mean = sum(theList)/len(theList)
    return mean

###################Problem 2################
# 1 is January, 2 is February, etc.
def is_leap(yar):
    integerz = int(yar/4)
    float = yar/4
    if (integerz == float):
        return 1
    else:
        return 0

def day_in_year(year, month, day):
    """prec:  year/month/day is a valid date
    postc: returns the ordinal position of the day in the year
    (Feb 15 is the 46th day of year 2000).
    Hint:  The built-in function sum is your friend. Learn about it."""
    lengths = [31, 28 + is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sumz = sum(lengths)
    total = sum(lengths[:month]) - (lengths[month-1] - day)
    return total

###################Problem 3################
def days_left_in_year(year, month, day):
    """prec:  year/month/day is a valid date
    postc: returns the number of days left in the year
    (Feb 15 is the 46th day of year 2000)."""
    lengths = [31, 28 + is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sumz = sum(lengths)
    total = sum(lengths[:month]) - (lengths[month-1] - day)
    day_left = ((365 + is_leap(year)) - total)
    return day_left
###################Problem 4################
def days_to_graduation(yearz, monthz, dayz):
    """prec:  year/month/ is a valid date before graduation
    in 2020 or 2021.  It's 29 May 2021.
    postc: returns the number of days until graduation 
    If the year is illegal, or if a date after 29 May 2021 is entered,
    return "ILLEGAL INPUT"  """
    if (yearz !=2021):
        if(yearz != 2020):
            return -1
    if (yearz == 2021):
        if(dayz >= 29 and monthz >= 5):
            return -1
        if(monthz >= 5):
            return -1
    total_days_left = 366 + day_in_year(2021,5,21)
    day_number = day_in_year(yearz,monthz,dayz)
    if (yearz == 2021):
        day_number = day_number + 366
    day_til_grad = total_days_left - day_number
    return day_til_grad



###################Problem 5################
def pad(x):
    if (x<10):
        return "0" + str(x)
    if (x>10):
        return x


def dhms(secs):
    """prec:  secs is a nonnegative integer (second)
    postc: return a STRING of the form d:hh:mm:ss, where d is the number
    of days, h is the number of hours, m is the number     of minutes, and
    s is the number of seconds, h < 24, 0 <= m, s, < 60.  Give each of
    h, m, s a two character width, padding with zeroes as needed.  """
    
    days = (secs//86400)
    time = str(days) + ":"
    secs = secs % 86400

    hour = (secs//3600)
    time = time + str(pad(hour))
    secs = secs % 3600

    minutes = (secs//60)
    time = time + ":" + str(pad(minutes))
    secs = secs % 60

    time = time + ":" + str(pad(secs))
    return time

###################Problem 6################
def water_closet(theString):
    """precondition: thesString is a string.
postcondition: returns a tuple (c, w, l) where c is the number of
characters in theString, w is the number of words, and l is the number of
lines in the string"""
    c = len(theString)
    w = theString.count(" ") + 1
    l = theString.count("\n") + 1
    if (theString == ""):
        return (0,0,0)
    return (c, w, l)
###################Problem 7################
def math_case(x):
    """precondition: x is a number
postcondition: If x > 4, f(x) = x - 4, if x < -5, f(x) = x + 5,
otherwise, f(x) = 0."""
    if x > 4:
        return x - 4
    if x < -5:
        return x + 5
    return 0


#*****************MAIN FUNCTION******************
def main():
    print("###################Problem 1################")
    test = [[1,2,3,4,5,6]]
    expected = 3.5
    run_test_float(meanie, expected, test)
    test = [[-3, -2, 0, 0, 6, 5]]
    expected = 1.0
    run_test_float(meanie, expected, test)
    print("###################Problem 2################")
    test = [2000,2,15]
    expected = 46 
    run_test(day_in_year, expected, test)
    test = [2021,9,9]
    expected = 252
    run_test(day_in_year, expected, test)
    test = [2005,8,2] #my bday lol
    expected = 214
    run_test(day_in_year, expected, test)

    print("###################Problem 3################")
    test = [2000,2,15]
    expected = 320 
    run_test(days_left_in_year, expected, test)
    test = [2021,9,10]
    expected = 112
    run_test(days_left_in_year, expected, test)
    test = [2005,8,2] #my bday lol
    expected = 151
    run_test(days_left_in_year, expected, test)

    print("###################Problem 4################")
    test = [2020,9,10]
    expected = 253 
    run_test(days_to_graduation, expected, test)
    test = [2021,4,30]
    expected = 21
    run_test(days_to_graduation, expected, test)
    test = [2005,8,2] #my bday lol
    expected = -1
    run_test(days_to_graduation, expected, test)
    test = [2021,9,2] 
    expected = -1
    run_test(days_to_graduation, expected, test)

    print("###################Problem 5################")
    test = [1432]
    expected = "0:00:23:52"
    run_test(dhms, expected, test)
    test = [236112365817256]
    expected = "2732782011:18:34:16"
    run_test(dhms, expected, test)
    test = [1] 
    expected = "0:00:00:01" 
    run_test(dhms, expected, test)
    print("###################Problem 6################")
    test = [""]
    expected = (0,0,0)
    run_test(water_closet, expected, test)
    test = ["HI bestie"]
    expected = (9,2,1)
    run_test(water_closet, expected, test)
    test = ["heyyya dude \nhiiii man"] 
    expected = (22,4,2) 
    run_test(water_closet, expected, test)
    print("###################Problem 7################")
    print("freebie")

#***********MAINFRAME*************
main()