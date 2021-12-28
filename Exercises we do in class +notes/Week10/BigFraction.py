import math 

class BigFraction(object):
    def __init__(self, num = 0, denom = 1):
        d = math.gcd(num, denom)
        num //= d
        denom //= d
        if denom < 0:
            num = -num
            denom = -denom
        self.num =  num
        self.denom = denom
    def __str__(self): 
        return f"{self.num}/{self.denom}"
    def __eq__(self, other):
        if other is BigFraction:
            return True
        if type(other) != BigFraction:
            return False 
        return self.num == other.num and self.denom == other.denom



#*********Main method************
def main():
    f = BigFraction(3,4)
    print(f)
    f = BigFraction(-3,-4)
    print(f)
    f = BigFraction(6,8)
    print(f)
    f = BigFraction(1048576, 7776)
    print(f)

#**********running of main*************8
main()