svar = input("Verdi nå = ")
verdi = float(svar)
svar = input("Verdiendring i prosent = ")
prosent = float(svar)

vekstfaktor = 1 + prosent/100
år = 0

while år < 5:
    år + 1
    verdi = verdi*vekstfaktor
print("Etter ",år, "år er verdien", int(verdi), "kr.")