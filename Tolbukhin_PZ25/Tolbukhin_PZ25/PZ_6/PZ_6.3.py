#Дано множество A из N точек на плоскости и точка B (точки заданы своими координатами x,y).
#Найти точку из множества A, наиболее близкую у точке B.
#Расстояние R между точками с координатами (x1, y1) и (x2, y2) вычисляется по фомуле:
#R = -1/2(x2-x1)^2+(y2-y1)^2
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def closest_point(points, x, y):
    min_distance = float('inf')
    closest = None
    for point in points:
        dist = distance(point[0], point[1], x, y)
        if dist < min_distance:
            min_distance = dist
            closest = point
    return closest

points_set = [(1, 2), (3, 4), (5, 6), (7, 8)]
point_B = (4, 5)
closest = closest_point(points_set, point_B[0], point_B[1])
print("Ближайшая точка из множества A:", closest)
