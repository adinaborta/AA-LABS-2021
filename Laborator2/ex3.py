# pozitia unui punct fata de cercul circumscris unui triunghi
import numpy as np
from geompreds import orient2d
import matplotlib.pyplot as plt


def define_circle(p1, p2, p3):
    """
    Returns the center and radius of the circle passing the given 3 points.
    In case the 3 points form a line, returns (None, infinity).
    """
    temp = p2[0] * p2[0] + p2[1] * p2[1]
    bc = (p1[0] * p1[0] + p1[1] * p1[1] - temp) / 2
    cd = (temp - p3[0] * p3[0] - p3[1] * p3[1]) / 2
    det = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])

    if abs(det) < 1.0e-6:
        return (None, np.inf)

    # Center of circle
    cx = (bc * (p2[1] - p3[1]) - cd * (p1[1] - p2[1])) / det
    cy = ((p1[0] - p2[0]) * cd - (p2[0] - p3[0]) * bc) / det

    radius = np.sqrt((cx - p1[0]) ** 2 + (cy - p1[1]) ** 2)
    return ((cx, cy), radius)


def parse_point(line):
    print(line)
    x, y = line.strip().split()
    return (float(x), float(y))


def theta(a, b, c, d):
    x = np.array(
        [
            [a[0], a[1], a[0] * a[0] + a[1] * a[1], 1],
            [b[0], b[1], b[0] * b[0] + b[1] * b[1], 1],
            [c[0], c[1], c[0] * c[0] + c[1] * c[1], 1],
            [d[0], d[1], d[0] * d[0] + d[1] * d[1], 1],
        ]
    )
    return np.linalg.det(x)


with open("in_out_samples/3.in", "r") as fin:
    a, b, c, d = (
        parse_point(fin.readline()),
        parse_point(fin.readline()),
        parse_point(fin.readline()),
        parse_point(fin.readline()),
    )

    print(a, b, c, d)

    det = orient2d(a, b, c)
    # daca a, b, c formeaza viraj la stanga
    # inversam a si c pentru a forma unul si a putea aplica formula
    if det < 0:
        cpy = a
        a = c
        c = cpy

    title = None
    res = theta(a, b, c, d)
    if abs(res - 0) < 1.0e-6:
        title = "conciclice"
    elif res > 0:
        title = "in interior"
    else:
        title = "in exterior"

    center, radius = define_circle(a, b, c)
    print(center, radius)
    if center is not None:
        circle = plt.Circle(center, radius, fill=False)
        plt.title(title)
        plt.axis("equal")
        ax = plt.gca()
        ax.add_patch(circle)
        plt.plot(d[0], d[1], "ro")
        plt.show()
