x0 = -10   # Startpunkt
dx = 1E-5  # Forskjellen mellom x-verdier
x=0

def f(x):
    return x**2 - 2

while f(x0)*f(x0+dx)>=0:
    x0 = x0+dx 

punkt = (x0 + dx)/2       
print(f"f(x) har et ****punkt ved x-verdien {punkt:.3f}")
   