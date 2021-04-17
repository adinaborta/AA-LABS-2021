import matplotlib.pyplot as plt
from geompreds import orient2d


def parse_point(line):
    x, y = line.strip().split()
    return (float(x), float(y))


points = []

with open("in_out_samples/calin.in", 'r') as fin:
    n = int(fin.readline())
    for _ in range(n):
        points.append(parse_point(fin.readline()))


start_index, leftmost_point = min(enumerate(points), key=lambda x: x[1][0])

# cat timp punctul din mijloc al tripletului este diferit de punctul de start (i.e. nu am ciclat)
a, b, c = (start_index -
           1) % len(points), start_index, (start_index + 1) % len(points)

convex_hull = [b]
while True:
    # if orient2d(points[a], points[b], points[c]) > 0:
    convex_hull.append(c)

    last_visited_point = c
    while len(convex_hull) > 2 and orient2d(points[convex_hull[-3]], points[convex_hull[-2]], points[convex_hull[-1]]) <= 0:
        convex_hull.pop(-2)

    print(convex_hull)
    a = convex_hull[-2]
    b = convex_hull[-1]
    c = (last_visited_point + 1) % len(points)
    if b == start_index:
        break

while orient2d(points[convex_hull[-3]], points[convex_hull[-2]], points[convex_hull[-1]]) <= 0:
    convex_hull.pop(-2)

print(convex_hull)
points.append(points[0])
points_x = [tmp[0] for tmp in points]
points_y = [tmp[1] for tmp in points]
plt.plot(points_x, points_y, color='black', marker='o', linestyle='-')
convex_hull = [points[tmp] for tmp in convex_hull]
convex_hull_x = [tmp[0] for tmp in convex_hull]
convex_hull_y = [tmp[1] for tmp in convex_hull]
plt.plot(convex_hull_x, convex_hull_y, color='green', marker='o')
plt.show()
print(convex_hull)
