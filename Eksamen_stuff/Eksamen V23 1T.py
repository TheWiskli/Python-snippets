def f(x):
    return 1/9 * (x + 1) * (x - 6)**2
def Areal(x):
    return bredde*f(x)
x_min = 0
x_max = 6


n = int(input("Velg maximum antall rektaneler du skal ha?: "))
pr_Bredde = float(input("Hvor stor bredde pr rektangel vil du ha?: "))
i=0
bredde = 0.000

while bredde <= x_max:
    print(f"Areal av {bredde} med lengde {f(bredde)} er {Areal(bredde)}")
    bredde = bredde + pr_Bredde
    n=n-1
    i=i+1
    if n <= 0:
        break

print(i, "Antall figurer brukt i grafen")