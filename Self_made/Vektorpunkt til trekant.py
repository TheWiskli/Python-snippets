
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))

AB_squared = (c-a)**2+(d-b)**2
BC_squared = (e-c)**2+(f-d)**2
AC_squared = (e-a)**2+(f-b)**2

if (AB_squared == BC_squared + AC_squared) or (BC_squared == AB_squared + AC_squared) or (AC_squared == AB_squared + BC_squared):
    print("Punktene danner en rettvinklet trekant")
else:
    print("Punktene danner ikke en rettvinklet trekant")