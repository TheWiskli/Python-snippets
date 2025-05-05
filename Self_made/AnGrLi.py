from math import sqrt as bob

print("AnnenGradsLikning Løser!")
svar = input("a = ")
a = float(svar)
if a == 0:
    print("med a=0 blir det ikke en andregradslikning, DUMBASS!")
else:
    svar = input("b = ")
    b = float(svar)
    svar = input("c = ")
    c = float(svar)
    d = b**2-4*a*c
    if d < 0:
        print("Ingen Løsning!")
    elif d == 0:
        x1 =  -b/(2*a)
        print("En løsning x = ", round(x1,2))
    else:
        x1 = (-b+bob(d))/(2*a)
        x2 = (-b-bob(d))/(2*a)
        print("To løsninger x1 =", round(x1,2), "og x2 =", round(x2,2))