from geompreds import orient2d, incircle

P = tuple(int(i) for i in input("Coordonatele lui P: ").split())
Q = tuple(int(i) for i in input("Coordonatele lui Q: ").split())
R = tuple(int(i) for i in input("Coordonatele lui R: ").split())

viraj = orient2d(P, Q, R);

if viraj > 0:
    print("Viraj la stanga")
elif viraj < 0:
    print("Viraj la dreapta")
else
    print("Puncte coliniare")


