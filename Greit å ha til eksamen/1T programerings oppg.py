def f(x):
    return (1-2*x)/(x-2)

x=8
while x>=-8:
    print (x, f(x))
    x=x-1
    if x == 0:
        x=x-2