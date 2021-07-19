'''
# ***    LOGIC 1    ***


def distance(xi,yi,xj,yj):
    return (((xj-xi)**2)+((yj-yi)**2))**0.5


def isTriangle(max,a,b):
    if ((a+b) > max) :
        print("\n Triangle")
    else:
        print("\n Not a Triangle")


x1,y1,x2,y2,x3,y3 = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())

d1 = distance(x1,y1,x2,y2)
print(d1)
d2 = distance(x2,y2,x3,y3)
print(d2)
d3 = distance(x3,y3,x1,y1)
print(d3)



if d1>d2:
    if d1>d3:
        isTriangle(d1,d2,d3)
    else:
        isTriangle(d3,d1,d2)
elif d2>d3:
    isTriangle(d2,d1,d3)
else:
    isTriangle(d3,d1,d2)

'''

#   ***    LOGIC 2    ***

import math

def slope(xi,yi,xj,yj):
    if (x1==xj):
        return (math.inf)
    else:
        return ((yj - yi) / (xj - xi))

x1,y1,x2,y2,x3,y3 = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())

s1 = slope(x1,y1,x2,y2)
print(s1)
s2 = slope(x2,y2,x3,y3)
print(s2)


if s1 == s2 :
    print("\n Not a Triangle")
else:
    print("\n Triangle")