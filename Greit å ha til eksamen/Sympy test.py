import sympy as sym
x = sym.Symbol('x')
y = sym.diff((1/4)*x**2+1)

print(y)