import math

a = float(input("Lengden til a: "))
b = float(input("Lengden til b: "))
c = float(input("Lengden til c: "))

cos_a = (b**2 + c**2 - a**2) / (2*b*c)
cos_b = (a**2 + c**2 - b**2) / (2*a*c)
cos_c = (a**2 + b**2 - c**2) / (2*a*b)

a_grad = math.degrees(math.acos(cos_a))
b_grad = math.degrees(math.acos(cos_b))
c_grad = math.degrees(math.acos(cos_c))

print("A er:", round(a_grad, 2), "grader")
print("B er:", round(b_grad, 2), "grader")
print("C er:", round(c_grad, 2), "grader")


"""
a_uk = float(input("Lengden til a: "))
b_uk = float(input("Lengden til b: "))
c_grader = float(input(" Gradene til side C: "))

c_grader = math.radians(c_grader)

c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(c_grader))

print("Lengden til side c er:", round(c, 2))
"""