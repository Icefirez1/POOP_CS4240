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

print(water_closet(""))
print(water_closet("HI bestie"))
print(water_closet("heyyya dude \nhiiii man"))