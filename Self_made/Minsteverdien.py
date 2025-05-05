
def f(x):
    return x**2-3*x+4

a=0
b=5
x=a
fmin = f(a)
fmax = f(a)
h =0.01


list_x = []
while x<=b:
    list_x.append(f(x))
    x=x+h

print(list_x)
list_x.sort()
print(f"Minste verdien er {list_x[0]}")

"""while x<=b:
    if f(x) < fmin:
        fmin = f(x)
        xmin = x
    x = x+h
print(f" Lavest x verdi er {fmin:.2f}, på x verdien {xmin:.2}")

x=a

while x<=b:
    if f(x) > fmax:
        fmax = f(x)
        xmax = x
    x = x+h
print(f" Høyest x verdi er {fmax:.2f}, på x verdien {xmax:.2}")"""