def f(x):
    return x**2+2*x-6

x = -10
h = 0.001
while f(x) >= f(x+h):
    x = x+h
    print(x)

print(x)