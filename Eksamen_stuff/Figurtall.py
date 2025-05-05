

n = input("hvor mange figurer skal du lage? ")
n = int(n) # Gjør n om til en integer 
hode = 0  # Setter startverdi til de ulike kroppsdelene til figuren til null
kropp = 0
hale = 0
Totalt = 0 # Lager en verdi som skal gi totalt antall kvadrat til alle figurene som er blitt laget
figur = 0  # Setter startverdi til figurtallet


for i in range(1,n+1): # lager en for-løkke som starter på figur 1 og fortsetter til figur n. 
    hode = i**2                 # Regner ut antall i hode til figuren
    kropp = i * (i+1) *2 + i    # Regner ut antall i kroppen til figuren
    hale = i                    # Regner ut antall i halen til figuren
    figur = hode + kropp + hale # Finner summen av de ulike kroppsdelene
    Totalt = figur + Totalt     # Summerer denne figuren med summen av de foregående figurene etter
                                # vært som løkken kjøres på nytt og på nytt.
    
print(f"Du trenger {Totalt} små blå kvadrat for å lage de {n} første figurene og i den siste figuren trengte du {figur} små blå")