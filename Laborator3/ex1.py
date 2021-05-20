# we transform a halfplane from a * x + b * y + c <= 0 to y >=/<= lim or x >=/<= lim
# we will encode the result as a vector of length 3:
# 0: 'x' if it is a horizontal halfplane, 'y' if it is a vertical halfplane
# 1: '<=' if it is a left halfplane, '>=' if it is a right halfplane
# 2: lim
def transform_halfplane(a, b, c):
    res = [0] * 3
    if a == 0:
        res[0] = "y"
        if b < 0:
            res[1] = ">="
        else:
            res[1] = "<="
        res[2] = -c / b
    else:
        res[0] = "x"
        if a < 0:
            res[1] = ">="
        else:
            res[1] = "<="
        res[2] = -c / a

    return res


with open("in_out_samples/1_in.txt") as fin:
    num_tests = int(fin.readline())
    for _ in range(num_tests):
        num_halfplanes = int(fin.readline())
        halfplanes = []
        for _ in range(num_halfplanes):
            halfplane = list(map(lambda x: int(x), fin.readline().split()))
            transformed_halfplane = transform_halfplane(*halfplane)
            halfplanes.append(transformed_halfplane)

        horizontal_left_halfplanes = [
            hp for hp in halfplanes if hp[0] == "x" and hp[1] == "<="
        ]
        horizontal_right_halfplanes = [
            hp for hp in halfplanes if hp[0] == "x" and hp[1] == ">="
        ]
        vertical_left_halfplanes = [
            hp for hp in halfplanes if hp[0] == "y" and hp[1] == "<="
        ]
        vertical_right_halfplanes = [
            hp for hp in halfplanes if hp[0] == "y" and hp[1] == ">="
        ]

        xmin = None
        for hp in horizontal_left_halfplanes:
            if xmin is None or hp[2] < xmin:
                xmin = hp[2]

        xmax = None
        for hp in horizontal_right_halfplanes:
            if xmax is None or hp[2] > xmax:
                xmax = hp[2]

        ymin = None
        for hp in vertical_left_halfplanes:
            if ymin is None or hp[2] < ymin:
                ymin = hp[2]

        ymax = None
        for hp in vertical_right_halfplanes:
            if ymax is None or hp[2] > ymax:
                ymax = hp[2]

        if (xmin is not None and xmax is not None and xmin < xmax) or (
            ymin is not None and ymax is not None and ymin < ymax
        ):
            print("intersectia este vida")
        else:
            if xmin is None or xmax is None or ymin is None or ymax is None:
                print("intersectia este nevida, nemarginita")
            else:
                print("intersectia este nevida, marginita")