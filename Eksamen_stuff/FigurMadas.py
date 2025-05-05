#MotherBlocker

n = int(input("Figur nr "))

for N in range(1, n+1):
    hvit=n**2
    fig = (n+2)**2
    grønn = fig-hvit
print(f"{fig} i figur nr {n}, hvor det er {hvit} hvite og {grønn} grønne")