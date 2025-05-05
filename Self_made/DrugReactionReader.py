import math

dager = 15

def f(t):
    return 100*math.e**(-0.012*t)
sum = 0

for i in range(0,dager,1):
    a = f(i*24)
    sum = sum + a
    print(a)
    print("Dag", i, "Det er", sum, "mg i korppen")
