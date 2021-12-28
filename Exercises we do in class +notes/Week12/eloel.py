from sys import argv
import re
regex = argv[1] #a.*e.*i.*o.*u.*y
seeker = re.compile(regex)
with open("hughJass.txt", "r") as fp:
    for line in fp:
        if seeker.match(line):
            print(line, end="")
    