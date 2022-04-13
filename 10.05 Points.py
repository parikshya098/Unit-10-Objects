import math

class Point: 
    def __init__(self, Xvalue, Yvalue): 
        self.x = Xvalue 
        self.y = Yvalue 

    def ToString (self) : 
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __str__(self):
        return self.ToString()

def Distance(PointA, PointB):
    return math.sqrt((PointA.x - PointB.x) ** 2 + (PointA.y - PointB.y) ** 2) 

def MidPoint(PointA, PointB):
    X, Y = PointA.x + PointB.x / 2, PointA.y + PointB.y / 2 
    return Point(X, Y)

def XAngle(PointA, PointB):
    slope =  (PointB.y + PointA.y) / (PointB.x + PointA.x)
    XAngle = math.atan(slope) * 180 / math.pi
    return XAngle

file = open('10.05 Points.txt', 'r')
while True:
    line = file.readline()
    if not line:
        break
    words = line.split(',')
    nums = [float(x) for x in words]
    A = Point(nums[0], nums[1])
    B = Point(nums[2], nums[3])
    print(A, B, Distance(A, B), MidPoint(A, B), XAngle(A, B))