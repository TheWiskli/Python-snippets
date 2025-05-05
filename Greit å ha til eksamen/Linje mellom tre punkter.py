xA = float(input("Skriv inn x-verdien for punkt A: "))
yA = float(input("Skriv inn x-verdien for punkt A: "))

xB = float(input("Skriv inn x-verdien for punkt B: "))
yB = float(input("Skriv inn x-verdien for punkt B: "))

xC = float(input("Skriv inn x-verdien for punkt C: "))
yC = float(input("Skriv inn x-verdien for punkt C: "))


if (xC-xA)/(xB-xA) == (yC-yA)/(yB-yA):
    print("Punktene A,B og C ligger på linje")
else:
    print("Punktene er ikke på linje")