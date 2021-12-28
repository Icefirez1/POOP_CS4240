# ##################### Problem 1 #########################
def nuggets(limit, nugget_list):
    """prec: limit is an nonnegative integer
    postc: nugget_list is a list of nonnegative integers
    returns a list from nugget_list that has the
    highest total without exceeding the limit. """
    backpack = 0 
    backpack_list = []
    while backpack != limit: 
        lookin = max(nugget_list)
        if (lookin > limit - backpack):
            nugget_list.remove(lookin)
        if (lookin <= limit - backpack):
            backpack = backpack + lookin 
            backpack_list.append(lookin)
            nugget_list.remove(lookin)
    backpack_list.sort()
    return backpack_list

#**********Main********
print(nuggets(20,[1, 2, 4, 8, 16]))