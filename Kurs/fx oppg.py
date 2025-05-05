import time
a = float(input("A = "))
b = float(input("B = "))
dx = 0

def f(x):
    return 0.03*x**3 - 0.75*x**2 + 5*x - 6
time.sleep(2)

c=float(input("C ="))
gen = (f(b)-f(a))/(b-a)
punkt = ((f(c) + dx)-f(c))/(dx)

print(f(5))
print(round(gen,2))
print(punkt)