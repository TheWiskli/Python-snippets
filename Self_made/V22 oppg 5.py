def f(x):
    return x/(1+x**2)

x=0
h=0.01
while f(x) <= f(x+h):
    print("x:", x)
    print("f(x):", f(x))
    print("f(x+h):", f(x+h))
    x=x+h
    
print(f"Ende resultat av x={x} f(x) {f(x)} og f(x+h) {f(x+h)}")