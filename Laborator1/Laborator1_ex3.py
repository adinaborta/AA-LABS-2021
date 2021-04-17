from geompreds import orient2d, incircle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def return_orientation(l, r, Q, points):
    resp = binary_search_inf(l, r, Q, points)
    print(resp)

    if(resp == 0 or resp == -1):
        return resp
    else:
        return binary_search_sup(l, r, Q, points)


def binary_search_sup(l, r, Q, points):

    print(l, r)

    while points[l].x < Q.x or points[r].x > Q.x:
        if l >= r:
            m = int((l + r) / 2)
        else:
            m = int((l + r + len(points)) / 2 % len(points))

        if points[m].x >= Q.x:
            if m != len(points) - 1:
                r = m + 1
            else:
                r = 0

        if points[m].x < Q.x:
            if m != 0:
                l = m - 1
            else:
                l = len(points) - 1

        print(l, r)

    pr = (points[l].x, points[l].y)
    pl = (points[r].x, points[r].y)
    q = (Q.x, Q.y)

    o = orient2d(pl, pr, q)

    print(pl, pr, q)

    if o < 0:
        return 1
    elif o > 0:
        return -1
    else:
        return 0


def binary_search_inf(l, r, Q, points):

    if points[l].x > Q.x or points[r].x < Q.x:
        return -1

    print(l, r)

    while points[l].x < Q.x or points[r].x > Q.x:
        if l <= r:
            m = int((l + r) / 2)
        else:
            m = int((l + r + len(points)) / 2 % len(points))

        if points[m].x >= Q.x:
            if m != 0:
                r = m - 1
            else:
                r = len(points) - 1

        if points[m].x < Q.x:
            if m != len(points) - 1:
                l = m + 1
            else:
                l = 0

        print(l, r)

    pr = (points[l].x, points[l].y)
    pl = (points[r].x, points[r].y)
    q = (Q.x, Q.y)

    o = orient2d(pl, pr, q)

    print(pl, pr, q)

    if o < 0:
        return -1
    elif o > 0:
        return 1
    else:
        if pl[1] <= q[1] and pr[1] >= q[1] or pl[1] >= q[1] and pr[1] <= q[1]:
            return 0
        else:
            return -1


# n = int(input("Cate puncte inserati? "))
# points = []

# iminx = 0
# imaxx = 0


# for i in range(0,n):
#     print("Punctul " + str(i + 1))
#     x = int(input("x: "))
#     y = int(input("y: "))
#     points.append(Point(x,y))

#     if x > points[imaxx].x:
#         imaxx = i
#     if x < points[iminx].x:
#         iminx = i

# print("Punctul Q: ")
# x = int(input("x: "))
# y = int(input("y: "))
# Q = Point(x, y)


# points = [Point(3, 3), Point(9, 5), Point(12, 7), Point(9, 10), Point(4, 9), Point(2, 6)]
# Q = Point(3, 3)
# iminx = 5
# imaxx = 2

points = [Point(2, 9), Point(3, 3), Point(9, 1), Point(9, 10)]
Q = [Point(5, 1), Point(9, 5), Point(6, 7)]

for q in Q:
    iminx = 0
    imaxx = 1
    resp = return_orientation(iminx, imaxx, q, points)

    if resp == 0:
        print("Pe laturi")
    elif resp == 1:
        print("In interior")
    else:
        print("In exterior")
