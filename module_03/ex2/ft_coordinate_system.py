import math


def distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


point1 = (10, 20, 5)
point2 = (0, 0, 0)

print(f"{distance(point1, point2):.2f}")
