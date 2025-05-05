import math

"""
r = float(input("Hva er radiusen til sylinderen? "))
h = float(input("Hva er høyden på sylinderen? "))
v = math.pi*(r**2)*h

print(f"Volumet er lik {v:.2f}")

"""


hour = 0
def PerPrH(hour):
    return 100*hour+50

def KnutPrH(hour):
    return 70*hour+130

while KnutPrH(hour)>PerPrH(hour):
    hour = hour + 0.1

print(f"Per tjerner mer enn Knut etter de har jobbet mer enn {hour:.2f} timer")