def circle_area(r):
    return 3.14*r*r

def circle_peri(r):
    return 2*3.24*r

def rect_area(l,b):
    return l*b

def rect_peri(l,b):
    return 2*(l+b)


shape = input()
if shape=="circle":
    calc = input()
    rad=int(input())
    if calc=="area":
        print(circle_area(rad))
    else:
        print(cicle_peri(rad))
elif shape == "rectangle":
    calc = input()
    lth = int(input())
    brd = int(input())
    if calc=="area":
        print(rect_area(lth,brd))
    else:
        print(rect_peri(lth,brd))

else:
    exit()