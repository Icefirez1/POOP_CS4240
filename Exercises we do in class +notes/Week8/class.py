import math
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x 
        self.y = y 
    def distance_to(self, q):
        return math.hypot(self.x - q.x, self.y - q.y)
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __eq__(self, other):
        if type(other) != Point:
            return False
        if self is other: 
            return True 
        return self.x == other.x and self.y == other.y
        
    def reflection_across_x(self):
        return Point(self.x, -self.y)
    def reflection_across_y(self):
        return Point(-self.x, self.y)
    def reflection_across_x_equals_y(self):
        return Point(self.y, self.x)

if __name__ == "__main__":
    p = Point(3,4)
    q = Point(0,0)
    print(p.x)
    print(p.y)
    print(p.distance_to(q))
    print(p)
    a = Point(2,3)
    b = Point(2,3)
    print(a == b)
    