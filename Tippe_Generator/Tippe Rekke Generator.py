from random import choices as rng
from time import sleep as pause
import StjerneTallSjekker

#randomGenerator for Eurojackpot
def EuroJackpot_RekkeGeneratorCombo(RekkeNummer):
    Euro_HovedTall_Velger = Euro_MainList_HovedTall + Euro_Vinnertall_Hovedtall
    Euro_StjerneTall_Velger = Euro_MainList_StjerneTall + Euro_Vinnertall_Stjernetall
    for RekkeMaker in range(5):
        ValgtTall = rng(Euro_HovedTall_Velger)
        Euro_HovedTall_Generert.append(ValgtTall)
        while ValgtTall in Euro_HovedTall_Velger:
            Euro_HovedTall_Velger.remove(ValgtTall)
    for RekkeMakerS in range(2):
        ValgtTall_S = rng(Euro_StjerneTall_Velger)
        Euro_StjerneTall_Generert.append(ValgtTall_S)
        while ValgtTall_S in Euro_StjerneTall_Velger:
            Euro_StjerneTall_Velger.remove(ValgtTall_S)
    Euro_HovedTall_Generert.sort()
    Euro_StjerneTall_Generert.sort()
    print(f" Rekke {RekkeNummer}: Hovedtallene er {Euro_HovedTall_Generert} og Stjernetallene er {Euro_StjerneTall_Generert}")
    Euro_HovedTall_Generert.clear()
    Euro_StjerneTall_Generert.clear()
def EuroJackpot_RekkeGeneratorNormal(RekkeNummer):
    Euro_HovedTall_Velger = Euro_MainList_HovedTall
    Euro_StjerneTall_Velger = Euro_MainList_StjerneTall
    for RekkeMaker in range(5):
        ValgtTall = rng(Euro_HovedTall_Velger)
        Euro_HovedTall_Generert.append(ValgtTall)
        while ValgtTall in Euro_HovedTall_Velger:
            Euro_HovedTall_Velger.remove(ValgtTall)
    for RekkeMakerS in range(2):
        ValgtTall_S = rng(Euro_StjerneTall_Velger)
        Euro_StjerneTall_Generert.append(ValgtTall_S)
        while ValgtTall_S in Euro_StjerneTall_Velger:
            Euro_StjerneTall_Velger.remove(ValgtTall_S)
    Euro_HovedTall_Generert.sort()
    Euro_StjerneTall_Generert.sort()
    print(f" Rekke {RekkeNummer}: Hovedtallene er {Euro_HovedTall_Generert} og Stjernetallene er {Euro_StjerneTall_Generert}")
    Euro_HovedTall_Generert.clear()
    Euro_StjerneTall_Generert.clear()
def EuroJackpot_RekkeGeneratorVinn(RekkeNummer):
    Euro_HovedTall_Velger = Euro_Vinnertall_Hovedtall
    Euro_StjerneTall_Velger = Euro_Vinnertall_Stjernetall
    for RekkeMaker in range(5):
        ValgtTall = rng(Euro_HovedTall_Velger)
        Euro_HovedTall_Generert.append(ValgtTall)
        while ValgtTall in Euro_HovedTall_Velger:
            Euro_HovedTall_Velger.remove(ValgtTall)
    for RekkeMakerS in range(2):
        ValgtTall_S = rng(Euro_StjerneTall_Velger)
        Euro_StjerneTall_Generert.append(ValgtTall_S)
        while ValgtTall_S in Euro_StjerneTall_Velger:
            Euro_StjerneTall_Velger.remove(ValgtTall_S)
    Euro_HovedTall_Generert.sort()
    Euro_StjerneTall_Generert.sort()
    print(f" Rekke {RekkeNummer}: Hovedtallene er {Euro_HovedTall_Generert} og Stjernetallene er {Euro_StjerneTall_Generert}")
    Euro_HovedTall_Generert.clear()
    Euro_StjerneTall_Generert.clear()

def ExternListe(ListeNavn):
    try:
        with open(ListeNavn, "r") as file:
            Item = [int(line.strip()) for line in file.readlines()]
        return Item
    except FileNotFoundError:
        print(f"Finner ikke filen for {ListeNavn}")

#Valg av spill
def playLotto():
    pause(0.5)
    print("    Hvilken Rekke Generator du ønsker du å bruke.")
    pause(0.2)
    print("    1. Helt Tilfeldige tall")
    pause(0.2)
    print("    2. Kun Vinnertall")
    pause(0.2)
    print("    3. Combo Generatoren")
    pause(0.2)
    Lotto_RekkeValg = int(input("    Tast tallet til venstre og trykk enter for hvilken du vil ha: "))
    pause(1)
    match Lotto_RekkeValg:
        case 1:
            RekkeAntall = int(input("Hvor mange rekker med tall vil du ha?: "))
            if RekkeAntall < 2 or RekkeAntall > 10:
               print("Du kan ikke ha mindre enn 2 rekker og mer enn 10 rekker om gangen.")
            else:
                for RekkeSkaper in range(RekkeAntall):
                    Lotto_RekkeGeneratorNormal(RekkeSkaper+1)
                    pause(0.5)
        case 2:
            RekkeAntall = int(input("Hvor mange rekker med tall vil du ha?: "))
            if RekkeAntall < 2 or RekkeAntall > 10:
               print("Du kan ikke ha mindre enn 2 rekker og mer enn 10 rekker om gangen.")
            else:
                for RekkeSkaper in range(RekkeAntall):
                    Lotto_RekkeGeneratorVinn(RekkeSkaper+1)
                    pause(0.5)
        case 3:
            RekkeAntall = int(input("Hvor mange rekker med tall vil du ha?: "))
            if RekkeAntall < 2 or RekkeAntall > 10:
               print("Du kan ikke ha mindre enn 2 rekker og mer enn 10 rekker om gangen.")
            else:
                for RekkeSkaper in range(RekkeAntall):
                    Lotto_RekkeGeneratorCombo(RekkeSkaper+1)
                    pause(0.5)
    print("")
    print("  Husk spillevett!")
def playViking():
    pause(0.5)
    print("    Hvilken Rekke Generator du ønsker du å bruke.")
    pause(0.2)
    print("    1. Helt Tilfeldige tall")
    pause(0.2)
    print("    2. Kun Vinnertall")
    pause(0.2)
    print("    3. Combo Generatoren")
    pause(0.2)
    Viking_RekkeValg = int(input("    Tast tallet til venstre og trykk enter for hvilken du vil ha: "))
    pause(1)
    match Viking_RekkeValg:
        case 1:
            RekkeAntall = int(input("Hvor mange rekker med tall vil du ha?: "))
            if RekkeAntall < 2 or RekkeAntall > 10:
               print("Du kan ikke ha mindre enn 2 rekker og mer enn 10 rekker om gangen.")
            else:
                for RekkeSkaper in range(RekkeAntall):
                    Viking_RekkeGeneratorNormal(RekkeSkaper+1)
                    pause(0.5)
        case 2:
            RekkeAntall = int(input("Hvor mange rekker med tall vil du ha?: "))
            if RekkeAntall < 2 or RekkeAntall > 10:
               print("Du kan ikke ha mindre enn 2 rekker og mer enn 10 rekker om gangen.")
            else:
                for RekkeSkaper in range(RekkeAntall):
                    Viking_RekkeGeneratorVinn(RekkeSkaper+1)
                    pause(0.5)
        case 3:
            RekkeAntall = int(input("Hvor mange rekker med tall vil du ha?: "))
            if RekkeAntall < 2 or RekkeAntall > 10:
               print("Du kan ikke ha mindre enn 2 rekker og mer enn 10 rekker om gangen.")
            else:
                for RekkeSkaper in range(RekkeAntall):
                    Viking_RekkeGeneratorCombo(RekkeSkaper+1)
                    pause(0.5)
    print("")
    print("  Husk spillevett!")
def playEuroJackpot():
    pause(0.5)
    print("    Hvilken Rekke Generator du ønsker du å bruke.")
    pause(0.2)
    print("    1. Helt Tilfeldige tall")
    pause(0.2)
    print("    2. Kun Vinnertall")
    pause(0.2)
    print("    3. Combo Generatoren")
    pause(0.2)
    Euro_RekkeValg = int(input("    Tast tallet til venstre og trykk enter for hvilken du vil ha: "))
    pause(1)
    match Euro_RekkeValg:
        case 1:
            RekkeAntall = int(input("Hvor mange rekker med tall vil du ha?: "))
            if RekkeAntall < 2 or RekkeAntall > 10:
               print("Du kan ikke ha mindre enn 2 rekker og mer enn 10 rekker om gangen.")
            else:
                for RekkeSkaper in range(RekkeAntall):
                    EuroJackpot_RekkeGeneratorNormal(RekkeSkaper+1)
                    pause(0.5)
        case 2:
            RekkeAntall = int(input("Hvor mange rekker med tall vil du ha?: "))
            if RekkeAntall < 2 or RekkeAntall > 10:
               print("Du kan ikke ha mindre enn 2 rekker og mer enn 10 rekker om gangen.")
            else:
                for RekkeSkaper in range(RekkeAntall):
                    EuroJackpot_RekkeGeneratorVinn(RekkeSkaper+1)
                    pause(0.5)
        case 3:
            RekkeAntall = int(input("Hvor mange rekker med tall vil du ha?: "))
            if RekkeAntall < 2 or RekkeAntall > 10:
               print("Du kan ikke ha mindre enn 2 rekker og mer enn 10 rekker om gangen.")
            else:
                for RekkeSkaper in range(RekkeAntall):
                    EuroJackpot_RekkeGeneratorCombo(RekkeSkaper+1)
                    pause(0.5)
    print("")
    print("  Husk spillevett!")
#Starter modulen i progammet    
def play():
    print("Hei! Velkommen til William sin Lotto Tipping rekke generator!")
    print("Først og fremst er det viktig å forstå at dette er ikke en garanti for bedre kjangse")
    print("men at du får litt bedre genererte tallrekker basert fra tidligere vinnertall og eller ei.")
    input("Ved å presse enter samtykker du at dette er på eget ansvar.")
    pause(0.5)
    print("  Good! Du vil nå få en liste over forskjellige tippespill du kan spille")
    pause(0.5)
    print("  1. Ordinær Lotto")
    pause(0.5)
    print("  2. Viking Lotto")
    pause(0.5)
    print("  3. Euro Jackpot")
    pause(0.5)
    SpillValg = int(input("  Skriv tallet til venstre for spillet du vill spille: "))
    match SpillValg:
        case 1:
            playLotto()
        case 2:
            playViking()
        case 3:
            playEuroJackpot()


#EuroJackpot Lister
Euro_MainList_HovedTall = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
Euro_MainList_StjerneTall = [1,2,3,4,5,6,7,8,9,10,11,12]
# Tall fra september 2023 til første uken i Januar 2024
Euro_Vinnertall_Hovedtall = ExternListe('Python-snippets/Tippe_Generator//Euro_Vinnertall_Hovedtall.txt')
Euro_Vinnertall_Stjernetall = ExternListe('Python-snippets/Tippe_Generator/Euro_Vinnertall_Stjernetall.txt')
Euro_HovedTall_Generert = []
Euro_StjerneTall_Generert = []

#Ordinær Lotto Lister
Lotto_Mainlist = []
Lotto_Vinnertall = []
Lotto_Generert = []

#Vikinglotto Lister
Viking_Mainlist_Hovedtall = []
Viking_Mainlist_Stjernetall = []
Viking_Vinnertall_Hovedtall = []
Viking_Vinnertall_StjerneTall = []
Viking_HovedTall_Generert = []
Viking_StjerneTall_Generert = []


play()