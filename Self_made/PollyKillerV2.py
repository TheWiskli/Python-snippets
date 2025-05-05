import numpy as np
import time

list_del1 = []
list_del2 = []

def LeddMaker(list,leddAntall):
    for listLoop in range(leddAntall):
        ledje = input(float("Skriv tallet som blir brukt fra venstre: "))
        list.append(ledje)
    svar = input(list, "Stemmer dette? y/n?: ")
    if svar == "n":
        list.clear()
        LeddMaker(list,leddAntall)
    else:
        return list
    
#sette opp antal ledd i første del problemet
print("Skriv inn antall ledd i første del av oppgaven")
del1_ledd = input("Antall ledd: ")

LeddMaker(list_del1,del1_ledd)

#andre del
print("Skriv inn antall ledd i andre del av oppgaven")
del2_ledd = input("Antall ledd: ")

LeddMaker(list_del2,del2_ledd)


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