def are_anagrams(s1, s2):
    """prec: s1 and s2 are strings
    postc: return True if s1 is an anagram of s2, case INSENSITIVE."""
    check = s2[::-1]
    if (s1 == check):
        return True
    else:
        return False


#********MAIN*********

print(are_anagrams("golf", "fwlog"))