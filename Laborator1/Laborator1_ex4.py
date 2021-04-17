from geompreds import orient2d, incircle
import math

# n = int(input("Cate puncte inserati? "))
# points = []

# iminx = 0
# imaxx = 0


# for i in range(0,n):
#     print("Punctul " + str(i + 1))
#     x = int(input("x: "))
#     y = int(input("y: "))
#     points.append(Point(x,y))

def get_distance(a, b):
    return math.sqrt(math.pow((a[0] - b[0]), 2) + math.pow((a[1] - b[1]), 2))


def new_distance_dif(p1, p2, r):
    return get_distance(p1, r) + get_distance(p2, r) - get_distance(p1, p2)


def new_best_distance_div(p1, p2, r):
    return (get_distance(p1, r) + get_distance(p2, r)) / get_distance(p1, p2)


# points = [(-4, -0), (-3, 2), (-6, -2), (-2, 2), (0, -1), (2, -4),
#           (-4, 2), (4, -2), (6, 2), (8, 8), (-8, 0), (10, 0)]

points = [(1, 2), (4, 4), (8, 3), (8, 5), (3, 7), (5, 5), (4, 1)]

points.sort(key=lambda point: point[0], reverse=False)

print(points)

infFront = []
supFront = []

for (ipoint, point) in enumerate(points):
    if ipoint <= 1:
        infFront.append(point)
    else:
        infFront.append(point)
        n = len(infFront)

        while(True):
            if n <= 2:
                break

            orientation = orient2d(infFront[n-3], infFront[n-2], infFront[n-1])
            if orientation > 0:
                break
            else:
                infFront.pop(n-2)
                n -= 1
c_hull = infFront

for (ipoint, point) in enumerate(reversed(points)):
    if ipoint <= 1:
        supFront.append(point)
    else:
        supFront.append(point)
        n = len(supFront)

        while(True):
            if n <= 2:
                break

            orientation = orient2d(supFront[n-3], supFront[n-2], supFront[n-1])
            if orientation > 0:
                break
            else:
                supFront.pop(n-2)
                n -= 1

points = list(set(points) - set(infFront) - set(supFront))

print(points)

for point in supFront:
    if point not in c_hull:
        c_hull.append(point)

numberOfIterations = len(points)

for i in range(numberOfIterations):
    minDistance = math.inf
    posBestPoint = -1
    bestPoint = -1
    for (irpoint, rpoint) in enumerate(points):
        minDistCurr = math.inf
        posCurr = -1
        for i in range(len(c_hull)-1):
            dist = new_distance_dif(c_hull[i], c_hull[i+1], rpoint)
            if dist < minDistCurr:
                print(c_hull[i], c_hull[i+1])
                print(dist)
                minDistCurr = dist
                posCurr = i

        if new_distance_dif(c_hull[0], c_hull[len(c_hull) - 1], rpoint) < minDistCurr:
            posCurr = len(c_hull) - 1
        print(c_hull[0], c_hull[len(c_hull) - 1])
        print(new_distance_dif(c_hull[0], c_hull[len(c_hull) - 1], rpoint))

        if posCurr < (len(c_hull) - 1):
            minDistCurr = new_best_distance_div(
                c_hull[posCurr], c_hull[posCurr + 1], rpoint)
        else:
            minDistCurr = new_best_distance_div(
                c_hull[posCurr], c_hull[0], rpoint)

        if minDistCurr < minDistance:
            minDistance = minDistCurr
            posBestPoint = posCurr
            bestPoint = irpoint
    # print("best point: ", points[bestPoint])
    # print("p1: ", c_hull[posBestPoint])

    c_hull.insert(posBestPoint + 1, points[bestPoint])
    points.pop(bestPoint)


print(c_hull)
