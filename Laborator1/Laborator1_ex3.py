import matplotlib.pyplot as pl
from math import ceil, log
from geompreds import orient2d


def parse_point(line):
    x, y = line.strip().split()
    return (float(x), float(y))


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
