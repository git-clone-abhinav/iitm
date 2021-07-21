import math
class Point:
    # constructor for class with default arguments
    def __init__(self, x=0, y=0):
        # assigning the value of x to object attribute x
        self.x = x
        # assigning the value of y to object attribute y
        self.y = y

    # Create move method
    def move(self,dx,dy):
        # incrementing the value of x by dx
        self.x += dx
        # incrementing the value of y by dy
        self.y += dy

    # Create value method
    def value(self):
        # return the tuple with the value of x and y
        return (self.x,self.y)

    # Create duplicate method
    def duplicate(self):
        # return a new object of Point classwith the value of x and y
        return Point(self.x,self.y)

class Line:
    # constructor for class with default arguments
    def __init__(self,startPoint,endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint

    def length(self):
        # using value function of Pointobject to obtain x and y as tuple from startPoint
        x1,y1 = self.startPoint.value()
        # using value function of Pointobject to obtain x and y as tuple from endPoint
        x2,y2 = self.endPoint.value()
        # returning the absolute distance
        return ((x2-x1)**2+(y2-y1)**2)**0.5

    def slope(self):
        # using value function of Pointobject to obtain x and y as tuple from startPoint
        x1,y1 = self.startPoint.value()
        # using value function of Pointobject to obtain x and y as tuple from endPoint
        x2,y2 = self.endPoint.value()
        # preventing the zero division error
        if x1 != x2:
            return (y2-y1)/(x2-x1)
        else:
            return (math.inf)