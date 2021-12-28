import random 

#**********Function**********
def swap(x,j,k):
    if j != k:
        x[j],x[k] = x[k],x[j]
 

def is_in_order(x):
    for k in range(0,len(x) - 1):
        if x[k] > x[k+1]:
            return False 
    return True

def number_1(nums): #first sorting algorithm
    for i in range(len(nums)):
        k = min(nums[i:])
        indx = nums.index(k)
        swap(nums, i, indx)
    if is_in_order(nums) == True:
        return nums

def faster_number_1(nums): #this is my first function but faster 
    separator = 0 
    while separator < len(nums):
        so_far = nums[separator]
        idx = separator 
        for k in range(separator, len(nums)):
            if nums[k] < so_far:
                idx = k
                so_far = nums[idx]
        swap(nums,idx,separator)
        separator += 1

    
def number_2(numz):
    pointer = len(numz) - 1
    while not is_in_order(numz):
        for i in range(0, pointer):
            if numz[i] > numz[i+1]:
                swap(numz, i, (i+1))
        pointer -= 1
    return numz


def number_3(numie):
    pointer = 1
    while not is_in_order(numie):
        for i in range(pointer, 0, -1):
            if numie[i] < numie[i-1]:
                swap(numie, i, (i-1))
        pointer += 1
    return numie





#****************


numsz = [1,3,2,4]
print(numsz)
print(number_3(numsz))

