import numpy as np
import time
    
#sette opp antal ledd i første del problemet
print("Skriv inn antall ledd i første del av oppgaven")
del1_ledd = input("Antall ledd: ")
deled1 = int(del1_ledd)

#liste oppsett av første del av problemet
list_del1 = []

for listLoop1 in range(deled1):
    svar = input("Skriv tallet som blir brukt fra venstre: ")
    del1_ledje = float(svar)
    list_del1.append(del1_ledje)
    
print("\n")
print(list_del1, "\nSjekk om det stemmer, hvis ikke start på nytt.")

#andre del
print("Skriv inn antall ledd i andre del av oppgaven")
del2_ledd = input("Antall ledd: ")
deled2 = int(del2_ledd)

#listen til del 2
list_del2 = []

for listLoop2 in range(deled2):
    svar = input("Skriv tallet som blir brukt fra venstre: ")
    del2_ledje = float(svar)
    list_del2.append(del2_ledje)

Start_tid = time.time()
time.sleep(1)

del1 = np.poly1d(list_del1)
del2 = np.poly1d(list_del2)
print("\n")
print(list_del1)
print(list_del2)

time.sleep(1)
print("\nFørste del: \n",del1)
print("\nAndre del: \n",del2)

time.sleep(1)
quotient, remainder = np.polydiv(del1,del2)

Slutt_tid = time.time()
Jobb_tid = Slutt_tid - Start_tid - 3

print("\nSvar : \n", quotient)
print("\nGjenstående : \n", remainder)
print("Tok",Jobb_tid, "Sekunder for å svare")

