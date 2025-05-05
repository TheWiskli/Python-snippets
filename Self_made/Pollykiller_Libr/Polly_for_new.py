"""
Ny variant med hjelp av Joakim Viken (Skyller han en �l)
"""

#sette opp antal ledd i første del problemet
print("Skriv inn antall ledd i første del av oppgaven")
del1_ledd = input("Antall ledd: ")
deled1 = int(del1_ledd)

#liste oppsett av første del av problemet
list_del1 = []

for index1 in range(deled1):
    svar = input("Skriv tallet som blir brukt fra høyre: ")
    del1_ledje = float(svar)
    list_del1.append(del1_ledje)
print(list_del1)