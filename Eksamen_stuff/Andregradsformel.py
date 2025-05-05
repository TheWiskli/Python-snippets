
import math

# Formel for andregradslikninger
a = float(input(" skriv inn tallet a i andregradslikningen: " )) # Skriv inn verdien tallet foran x^2
b = float(input("Skriv inn tallet b i andregradslikningen: ")) # Skriv inn verdien tallet foran x
c = float(input("Skriv inn tallet c i andregradslikningen: "))  # Skriv inn verdien til konstanten
d = b**2-4*a*c # Regner ut tallet under kvadratroten i andregradsformelen


if d < 0: # Hvis tallet under kvadratroten er negativt, har andregradsformelen ingen løsning
    print("Andregradslikningen har ingen løsning.") 
elif d == 0: # Hvis tallet under kvadartroten er lik null, har andregradsformelen kun en løsning 
    x = -b/2*a
    print(f" Andregradslikningen har én løsning, x = {x:.2f}")
    
else: # Hvis andregradsformelen ikke har null eller kun en løsning, så har den to løsninger. 
    x_1 = (-b+math.sqrt(d))/(2*a)
    x_2 = (-b-math.sqrt(d))/(2*a)  
    print(f" Andregradslikningen har to løsninger, x_1 = {x_1:.2f} , og x_2 = {x_2:.2f} .") 
    # Gir begge løsningene med rundet av til 2 desimaler. 