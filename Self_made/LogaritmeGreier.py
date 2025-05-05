from pylab import log

a = 0
b = 5
noyaktighet = 0.0001

def f(x):
    return 13500 * 1.025**x - 15000

m =(a + b)/2

while abs(f(m)) >= noyaktighet:
    if f(a)*f(m) < 0:
        b = m
        print(m)
    else:
        a = m
        print(m)
    m = (a+b)/2

print("Løsningen er nærmest lik", round(m,4))