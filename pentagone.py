import math
longueur = float(input())
x0, y0 = longueur, 0
pent = math.pi/3
x1, y1 = x0/2, math.tan(pent)*(longueur/2)
x2,y2 = x1 - x0, y1
x3,y3 = -x0, 0
x4,y4 = x2 , -y1
x5,y5 = x1 , y4
print(f"{x0} {y0}")
print(f"{x1} {y1}")
print(f"{x2} {y2}")
print(f"{x3} {y3}")
print(f"{x4} {y4}")
print(f"{x5} {y5}")
