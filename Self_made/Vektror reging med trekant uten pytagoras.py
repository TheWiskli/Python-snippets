
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))

ABx = c-a
ABy = d-b

ACx = e-a
ACy = f-b

BCx = e-c
BCy = f-d



if ABx*ACx + ABy*ACy == 0:
    print("Trekanten er rettvinklet ved 90 grader i punkt A")
elif ABx*BCx + ABy*BCy == 0:
    print("Trekanten er rettvinklet ved 90 grader i punkt B")
elif ACx*BCx + ACy*BCy == 0:
    print("Trekanten er rettvinklet ved 90 grader i punkt C")
else:
    print("Trekanten er ikke rettvinklet.")