buffer = 10000
N = 100
sum = 0
figur = 0
klosse = 0
for i in range(1, N+1):
    rest = buffer-sum
    if sum >= buffer-figur:
        print(f"Figur {klosse}, klosser {figur}")
        break
    else:
        figur = figur + i**2
        sum = sum + figur
        klosse = klosse + 1
        rest = buffer-sum
        print(f"Figur {klosse}, klosse {figur}")
print (f"det er {rest:,} klosser til overs")