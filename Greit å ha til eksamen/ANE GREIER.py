x1 = float(input("x1:"))
y1 = float(input("y1:"))
x2 = float(input("x2:"))
y2 = float(input("y2:"))
parralellsjekker = (x1*x2)- (y1*y2)
print(parralellsjekker)
if parralellsjekker == 0:
    print("DEN ER PARALELL")
else:
    print("IKKE PARALLEL!")