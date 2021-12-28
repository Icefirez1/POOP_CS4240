####################################
# Author: Al Pagar
#  Date created: 30 Aug 2021
#  Date last modified: 30 Aug 2021
#  Program: stringPlay.py
# 
# string thing with a bunch of problems doin stuff with strings 
# amazing explanation ik (jk)
####################################

###############Problem 0#################
#   Example problem to show how this works.
#   arg is a lower-case string with at least two instances
#   of the letter q
#   Find the substring of arg between the first and last q
#########################################

arg = "quoque"
start = arg.find("q")
end = arg.rfind("q")
my_result = arg[start + 1: end]
result = "uo"  ##this is my given result
print(result == my_result)  ##prints True if you succeeded.
arg = "miasma"
start = arg.find("a")
end = arg.rfind("a")
my_result = arg[start + 1: end]
result = "sm"  ##this is my given result
print(result == my_result)  ##prints True if you succeeded.

###############Problem 1#################
#   Remove all instances of the lower-case letter
#   s from a string.  
#########################################

arg = "sissyphus"
my_result = arg.replace("s", "")
result = "iyphu"
print(result == my_result)

###############Problem 2#################
#   arg is guaranteed to have at least two letters
#   and be an alphabetical string
#   Create a string with the first and last letters of arg.
#########################################

arg = "heinous"
newstring1 = arg[0] + arg[len(arg)-1]
result = "hs"
print(newstring1 == result)

arg = "Washington"
newstring1 = arg[0] + arg[len(arg)-1]
result = "Wn"
print(newstring1 == result)

###############Problem 3#################
#   head has an even number of letters
#   tail has an even number of letters
#   Create a string whose first half is the first
#   half of head and the second half of tail.
#########################################

head = "cerebellum"
tail = "wagger"
headlength = int(len(head) / 2)
firstpart = head[0:headlength]
taillength = int(len(tail)/2)
secondpart = tail[taillength:]
combinestring = firstpart + secondpart
result = "cerebger"
print(combinestring == result)

###############Problem 4#################
#   arg is any string
#   Find out how many times the letter b occurs 
#   in arg, case INsensitive
#########################################

arg = "Babbage"
num = arg.count("b") + arg.count("B")
result = 3
print(num == result)

###############Problem 5#################
#   arg is any string
#   Find out how many times the letter b occurs 
#   in the first 10 letters of arg, case INsensitive
#########################################

arg = "Babbage"
tempstr = arg[:10]
num = tempstr.count("b") + tempstr.count("B")
result = 3
print(num == result)

arg = "flibbertygibbet"
tempstr = arg[:10]
result = 2
num = tempstr.count("b") + tempstr.count("B")
print(num == result)

###############Problem 6#################
#   arg is any string
#   Find out how many times the letter b occurs 
#   in the first 10 letters of arg, case INsensitive
#########################################

arg = "Babbage"
tempstr = arg[:10]
num = tempstr.count("b") + tempstr.count("B")
result = 3
print(num == result)

arg = "flibbertygibbet"
tempstr = arg[:10]
result = 2
num = tempstr.count("b") + tempstr.count("B")
print(num == result)

###############Problem 7#################
#   arg is any string
#   center the string in a string of length 30
#   padded with !s.  
#   if the string has more than 30 characers, just
#   display it.  (no conditional logi on your part needed)
#########################################

arg = "wabbit"
arg = arg.center(30,"!")
result = "!!!!!!!!!!!!wabbit!!!!!!!!!!!!"
print (arg == result)

###############Problem 8#################
#   arg is any string
#   get rid of all of the whitespace on the left, if any
#   replace any spaces on the right with @s.
#########################################

arg = "        wabbit    "
arg = arg.lstrip()
arg = arg.replace(" ", "@")
result = "wabbit@@@@"
print(arg == result)