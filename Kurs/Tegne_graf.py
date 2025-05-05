import numpy as np #Importerer numpy for å lage arange eller linespace
import matplotlib.pyplot as plt # importerer plotlib for å tenge graf

def f(x): # Definerer funksjonen f(x)
    return 0.3*x**2+2*x-4

"""
def g(x): # Definerer funksjoner g(x)
    return -2*x+4
"""
xlist = np.arange(-5,10,.1) # Lager x-verdier fra -5 til 10 med 0.1 mellomrom, 
# Kan også bruke xlist = np.linespace(-5,10,100) for å få fra -5 til 10 med 100 punkter mellom
ylist = f(xlist) # lager y-verdier til f(x) fra xlist

#ylist1 = g(xlist) # lager y-verdier til g(x) fra xlist
plt.plot(xlist,ylist, "-b", label=("f(x)")) # plotter graf til f(x), "-b" betyr heltrukket linje i blå
#plt.plot(xlist,ylist1, "--y", label=("g(x)")) # plotter graf til g(x), "--y" betyr stiplet linje i gul
plt.title("Min første graf") # gir tittel til grafen
plt.xlabel("Tid / [s]") # gir navn til x-akse
plt.ylabel("Posisjon / [m]") # gir navn til yakse
plt.legend()    # Viser label gitt i ploting av f(x) og g(x)
plt.xlim(-1,5) # Begrenser x-aksen mellom -5 og 10
plt.ylim(-10,f(10)) # Begrenser yaksen mellom -10 og f(10) 
plt.axhline(y=0, color="k") # Tegner inn x-aksen
plt.axvline(x=0, color="k") # Tegner inn y-aksen
plt.grid(True)  # viser rutesystem
plt.show() # viser grafen