def f(x):
    return 1*x**2 - 4*x +1

h = 0.0001
x = -100

while (f(x+h)-f(x))/h < 0: # snu ulikhetstegn hvis man ikke får et svar. 
    x = x + 0.01


print(f"x-verdien til ekstremalpunktet er {x:.2}")
