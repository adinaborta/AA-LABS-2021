import numpy as np
from geompreds import orient2d
import matplotlib.pyplot as plt
from math import sqrt
from random import random
from sympy import Point, Polygon, Segment


def parse_point(line):
    x, y = line.strip().split()
    return (float(x), float(y))


def distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def is_between(a, c, b):
    return abs(distance(a, c) + distance(c, b) - distance(a, b)) < 1.0e-6


x_min, x_max = float("inf"), float("-inf")
y_min, y_max = float("inf"), float("-inf")
with open("in_out_samples/1.in", "r") as fin:
    num_p_poly = int(fin.readline())
    polygon = []
    for _ in range(num_p_poly):
        point = parse_point(fin.readline())
        polygon.append(point)

        if point[0] < x_min:
            x_min = point[0]

        if point[0] > x_max:
            x_max = point[0]

        if point[1] < y_min:
            y_min = point[1]

        if point[1] > y_max:
            y_max = point[1]

    # print(f"x_min: {x_min}, x_max: {x_max}")
    # print(f"y_min: {y_min}, y_max: {y_max}")

    num_p_check = int(fin.readline())
    checks = []
    for _ in range(num_p_check):
        checks.append(parse_point(fin.readline()))

    for point in checks:
        is_on_line = False
        for a, b in zip(polygon, polygon[1:] + [polygon[0]]):
            if is_between(a, point, b):
                is_on_line = True
                break

        if is_on_line:
            print(f"{point}: pe latura")
        else:
            martor = (x_max + random(), y_max + random())
            p_point, p_martor = map(Point, [point, martor])
            p_polygon = Polygon(*[Point(pct) for pct in polygon])
            num_intersect = len(Segment(p_point, p_martor).intersection(p_polygon))
            if num_intersect % 2 == 0:
                print(f"{point}: exterior")
            else:
                print(f"{point}: interior")


# line = plt.Polygon(
#     polygon,
#     color="blue",
#     alpha=0.3,
#     fill=True,
#     edgecolor=None,
# )
# plt.gca().add_line(line)
# plt.axis("equal")
# plt.show()
