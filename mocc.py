import math
def distance_points(x1,x2):
    result = math.sqrt((x2[1]-x1[1])**2 + (x2[0]-x1[0])** 2)
    return result
def longeur(*points):
    dis=0
    for i in points:
        dis += distance_points(i,points[1])
    return dis

print(longeur((19.5, 7.0), (16.0, 15.0), (21.0, 23.0), (23.5, 32.5)))
# print(distance_points((1,1),(1,2)))