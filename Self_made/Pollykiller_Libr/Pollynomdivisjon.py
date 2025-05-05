import numpy as np

#sette opp antal ledd i første del problemet
print("Skriv inn antall ledd i første del av oppgaven")
del1_ledd = input("Antall ledd: ")
deled1 = int(del1_ledd)

#liste oppsett av første del av problemet
list_del1 = [None] * deled1

#løkken til å bytte innholdet None til tall
for fyll_del1 in list_del1:
    svar = input("Skriv tallet som blir brukt fra høyre: ")
    del1_ledje = float(svar)

    list_del1.append(del1_ledje)
    list_del1 = list_del1[-deled1:]
#pga en eller annen måte så må man sette inn 
#det første tallet til noe helt annet når jeg ikke trenger det

print(list_del1, "Sjekk om det stemmer, hvis ikke start på nytt.")

print("\nSkriv inn antall ledd i andre del av oppgaven")
del2_ledd = input("Antall ledd: ")
deled2 = int(del2_ledd)

list_del2 = [None] * deled2


for fyll_del2 in list_del2:
    svar = input("Skriv tallet som blir brukt fra høyre: ")
    del2_ledje = float(svar)

    list_del2.append(del2_ledje)
    list_del2 = list_del2[-deled2:]

del1 = np.poly1d(list_del1)
del2 = np.poly1d(list_del2)
print("\n")
print(list_del1)
print(list_del2)
print("\nFørste del: \n",del1)
print("\nAndre del: ",del2)

quotient, remainder = np.polydiv(del1,del2)

print("\nSvar : \n", quotient)
print("\nGjenstående : \n", remainder)