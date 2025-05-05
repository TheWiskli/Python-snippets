from time import sleep as pause
from random import randint as rnd

terningliste = []
terningskast = 30
kjangser = 10
antallSeksere = 0
for s in range(kjangser):
    for i in range(terningskast):
        terning = rnd(1,6)
        if terning == 6:
            terningskast=terningskast-1
            antallSeksere=antallSeksere+1
        else:
            terningliste.append(terning)
    print(terningliste, "Antall Radioaktive atomer igjen:",terningskast,"Antall nye grunnstoffer:",antallSeksere)
    pause(0.5)
    terningliste.clear()