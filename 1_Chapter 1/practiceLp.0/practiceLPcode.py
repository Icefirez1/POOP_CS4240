from rtz import close_enough, run_test, run_test_float #okay uhm its not working for some reason lol



#QUESTIONS FOR DOCTOR MORRISON 

#side note: try to fix why rtz isnt working 



#*****************PROBLEM 1*******************
def trim_sum(nums, limit):
    """nums is a numerical list, limit is a number
    returns the sum of all elements in nums that are
    <= limit"""
    sum = 0 
    for i in nums:
        if (i <= limit):
            sum = sum + i
    return sum

######################Problem 2###########################
def filter_sum(s):
    """prec: s is a string
    postc:  the total of all digits in the string is returned."""
    out = 0
    
    for j in range(len(s)):
        if (s[j].isdigit()):
            out = out + int(s[j])


    return out
######################Problem 3###########################
def sort_letters_backward(word):
    """prec: word is a lower-case string
    postc: returns a string with the letters in word sorted in reverse 
    alphabetical order
    """
    wordlist = []
    for j in range(len(word)):
        worldlist = wordlist.append(word[j])
    wordlist.sort()
    wordlist.reverse()
    newword = ""
    for i in range(len(word)):
        newword = newword + wordlist[i]
    return newword
######################Problem 4###########################

def comb_nest(*x): #i dont remember what starguments are 
    """prec: x is a star argument; you pass in a comma separated
    list of lists.  
    postc:  returns a list containing the sum of each of 
    the nested lists inside of x.  
    """
    sumlist = []
    for i in x:
        sumlist.append(sum(i))
    return sumlist


#____________________________________I GOT TO HERE__________________________________________________________________________________

######################Problem 5###########################
def paranoid_number(n):
    """prec: n is a nonnegative integer
    postc: returns the nth paranoid number
    paranoid_number(0) = 1
    paranoid_number(1) = 3
    paranoid_number(n+2) = 5*paranoid_number(n+1) -  6*paranoid_number(n) 
    """
    if n == 1:
        return 3
    if n == 0: 
        return 1
    
    return 5 * paranoid_number(n-1) - 6 * paranoid_number(n - 2)

######################Problem 6###########################
def generate_anagrams(word): #tbh i have no idea what to do for this one 
    """prec: word is a string with distinct letters
    postc:  generates a list containing all anagrams of 
    word in alphabetical order.  """
    amount_of_anagrams = word
    return [""]


def main():
    ## do your testing here.
    print("*************** Problem 1 Tests **************")
    run_test(trim_sum, 13, [[5, 12, 11, 2, 6], 10])
    print("*************** Problem 2 Tests **************")
    run_test(filter_sum, 10, ["c1o2w3s4moo"])
    print("*************** Problem 3 Tests **************")
    run_test(sort_letters_backward, "rmmhea", ["hammer"])
    print("*************** Problem 4 Tests **************")
    run_test(comb_nest, [6, 15, 15], [[1,2,3], [7, 8], [10,3,2]])

    print("*************** Problem 5 Tests **************")
    print(run_test(paranoid_number, 1, [0]))
    print(run_test(paranoid_number, 3, [1]))
    print("*************** Problem 6 Tests **************")
    run_test(generate_anagrams, ['act', 'atc', 'cat', 'cta', 'tac', 'tca'], ["cat"])
main()