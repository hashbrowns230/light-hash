#Write a simple program to recommend the types of control gear for a specific length of LED strips. Provide additional information on the nominal wattage and current.

import math

def cgtype(p, l):
    load = p * l

    if load <= 35:
        print(load,'W, Use 35W')
    elif load <=100:
        print(load,'W, Use 100W')
    elif load <=200:
        print(load,'W, Use 200W')
    else:
        print(load,'W ,use', math.ceil(load/100), 'x 100W or', math.ceil(load/200), 'x 200W')
        
p = input('Enter power per meter:')
l = input('Enter length:')
fw = float(p)
fl = float(l)

tl = cgtype(fw, fl)
