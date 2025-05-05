n=int(input("Figur nr: "))
total = 0

hn = n*2
bn = n*2
hd = (n+1)**2
bd = (n+2)*(n+1)-1
hl = 1
reinsdyr = hn+bn+hd+bd+hl

for i in range(1, n+1):
    figur = i * reinsdyr
print(figur)