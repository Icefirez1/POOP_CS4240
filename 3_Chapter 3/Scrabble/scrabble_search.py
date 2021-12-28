from sys import argv
#*********Functions************
def here(L, target):
    start = 0
    end = len(L) - 1
    while start <= end: 
        middle = (start + end)// 2 
        midpoint = L[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        elif midpoint == target:
            return True
    return False



#*********************MAIN*************
with open('scrabble.txt', "r") as f:
    wordlist = f.readlines()
    for k in range(len(wordlist)):
        wordlist[k] = wordlist[k].strip()
    wordwanted = argv[1].upper()
    print(here(wordlist, wordwanted))


