from geompreds import orient2d


def parse_point(line):
    x, y = line.strip().split()
    return (float(x), float(y))


with open("in_out_samples/1.in", 'r') as fin:
    n = int(fin.readline())
    for _ in range(n):
        a, b, c = parse_point(fin.readline()), parse_point(
            fin.readline()), parse_point(fin.readline())
        det = orient2d(a, b, c)
        if (det > 0):
            print("stanga")
        elif (det < 0):
            print("dreapta")
        else:
            print("coliniare")
