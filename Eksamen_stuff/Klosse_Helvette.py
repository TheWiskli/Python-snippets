figure = int(input("Legg til figuren varianten: "))
cube_list = list(range(1, figure + 1))
opphoyd_Cube = [element **2 for element in cube_list]
cube_tot_square = sum(opphoyd_Cube)
print(cube_list, opphoyd_Cube, cube_tot_square)

"""
# svar = input("Oppgave B: Hvilken Figur skal jeg kombinere til?: ")
# list_figs = int(svar)
"""

grenseLand = 100 #Lagde en variabel for 10k 
n=5 #antall figurer jeg vil lage
figur = 0
sum = 0
for i in range(1,n+1):
    figur = figur + i**2
    sum = sum + figur
    print(f"Figur {i}. Antall klosser i figuren er {figur:,} og total klosser {sum:,}")
    if sum > grenseLand: #Når koden merker at du har brukt over klosse grensen.
        sum = sum - figur #Forteller at de må gå tilbake til forigje antalle total klosser brukt
        i = i-1 #Forteller å gå tilbake til forrigje figur antallet
        break
rest = grenseLand-sum
print(" ")
print(f"Summen av klosser i de første {i:,} figurene er {sum:,} klosser")
print(f"Han har da {rest:,} klosser igjen")

"""
buffer = 10000
N = 100
sum = 0
figur = 0
klosse = 0
for i in range(1, N+1):
    rest = buffer-sum
    if sum >= buffer-figur:
        print(f"Figur {klosse:,} er nærmest grensen og totalt {sum:,} klosser blir brukt")
        break
    else:
        figur = figur + i**2
        sum = sum + figur
        klosse = klosse + 1
        rest = buffer-sum
        print(f"{klosse:,} Figurer {sum:,} klosser ({figur:,} i figuren)")
print (f"det er {rest:,} klosser til overs")
"""

