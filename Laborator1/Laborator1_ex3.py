import matplotlib.pyplot as pl
from math import ceil, log
from geompreds import orient2d


def parse_point(line):
    x, y = line.strip().split()
    return (float(x), float(y))


<<<<<<< Updated upstream
def cond(lst, r, pas, l, point, type):
    if type == "inf":
        return lst[(r + pas) % l][0] < point[0]
    else:
        return lst[(r + pas) % l][0] > point[0]


def binary_search(point, lst, st, dr, type="inf"):
    l = len(lst)
    n = (dr - st + 1) if st < dr else(len(lst) - (st - dr - 1))
    pas = int(2 ** (ceil(log(n, 2)))) // 2
    r = st
    while pas != 0:
        if cond(lst, r, pas, l, point, type):
            r += pas
            r %= l
        pas //= 2
    return (r % l, (r + 1) % l)


def orientation(point, polygon, st, dr):
    i1, i2 = binary_search(point, polygon, st, dr)
    inf_orientation = orient2d(polygon[i1], polygon[i2], point)
    if inf_orientation < 0:
        return "outside"
    elif inf_orientation == 0:
        return "on egde"

    i1, i2 = binary_search(point, polygon, dr, st, type="sup")
    sup_orientation = orient2d(polygon[i1], polygon[i2], point)
    if sup_orientation < 0:
        return "outside"
    elif sup_orientation > 0:
        return "inside"
=======
def return_orientation(l, r, Q, points):
    resp = binary_search_inf(l, r, Q, points)
    print(resp)

    if(resp == 0 or resp == -1):
        return resp
    else:
        return binary_search_sup(l, r, Q, points)


def binary_search_sup(l, r, Q, points):

    print(l, r)

    while (l != r + 1) and (r != 0 or l != len(points) - 1):
        if l >= r:
            m = int((l + r) / 2)
        else:
            m = int((l + r + len(points)) / 2 % len(points))

        if points[m].x >= Q.x:
            if m != len(points) - 1:
                r = m + 1
            else:
                r = 0
        elif points[m].x < Q.x:
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
        if pl[1] <= q[1] and pr[1] >= q[1] or pl[1] >= q[1] and pr[1] <= q[1]:
            return 0
        else:
            return -1


def binary_search_inf(l, r, Q, points):

    if points[l].x > Q.x or points[r].x < Q.x:
        return -1

    print(l, r)

    while (l != r + 1) and (r != 0 or l != len(points) - 1):
        if l <= r:
            m = int((l + r) / 2)
        else:
            m = int((l + r + len(points)) / 2 % len(points))

        if points[m].x >= Q.x:
            if m != 0:
                r = m - 1
            else:
                r = len(points) - 1
        elif points[m].x < Q.x:
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
    imaxx = 3
    resp = return_orientation(iminx, imaxx, q, points)

    if resp == 0:
        print("Pe laturi")
    elif resp == 1:
        print("In interior")
>>>>>>> Stashed changes
    else:
        return "on edge"


with open("Laborator1/in_out_samples/3.in", 'r') as fin:
    n = int(fin.readline())
    polygon = []
    for _ in range(n):
        polygon.append(parse_point(fin.readline()))
    n = int(fin.readline())
    query_points = []
    for _ in range(n):
        query_points.append(parse_point(fin.readline()))


st = min(enumerate(polygon), key=lambda x: x[1][0])[0]
dr = max(enumerate(polygon), key=lambda x: x[1][0])[0]

for index, qp in enumerate(query_points):
    print(f"{index}: {orientation(qp, polygon, st, dr)}")

polygon.append(polygon[0])
xs, ys = zip(*polygon)
pl.plot(xs, ys)
qxs, qys = zip(*query_points)
pl.plot(qxs, qys, color="green", marker="o", linestyle="")
for index, (i_x, i_y) in enumerate(query_points):
    pl.text(i_x, i_y + 0.5, str(index))
pl.show()
