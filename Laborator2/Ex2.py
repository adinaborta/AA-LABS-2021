from geompreds import orient2d, incircle
import math

points = [(4, 5), (5, 7), (5, 9), (2, 5), (4, 2), (6, 3)]

# points = [(1, 6), (3, 2), (5, 4), (2, 7)]

minn = points[0][0]
start = 0
cnt = 0


def next(index):
    return index + 1 if index != len(points)-1 else 0


x_monoton_y_monoton = 'x'
# x_monoton_y_monoton = 'y'

if x_monoton_y_monoton == 'x':

    for (i, point) in enumerate(points):
        if point[0] < minn:
            minn = point[0]
            start = i

    index = next(start)
    print("Parcurgere: " + str(points[start]), end=" ")

    while index != start:
        if points[index][0] > points[next(index)][0]:
            cnt = 1
        if cnt == 1 and points[index][0] < points[next(index)][0]:
            cnt = -1
            break
        print(str(points[index]), end=" ")
        index = next(index)

    if cnt == 1:
        print("\nEste x monoton")
    else:
        print("\nNu este x monoton")

if x_monoton_y_monoton == 'y':

    for (i, point) in enumerate(points):
        if point[1] < minn:
            minn = point[1]
            start = i

    index = next(start)
    print("Parcurgere: " + str(points[start]), end=" ")

    while index != start:
        if points[index][1] > points[next(index)][1]:
            cnt = 1
        if cnt == 1 and points[index][1] < points[next(index)][1]:
            cnt = -1
            break
            print(str(points[index]), end=" ")
        index = next(index)

    if cnt == 1:
        print("Este y monoton")
    else:
        print("Nu este y monoton")
