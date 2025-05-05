#En kommentar om verden
"""
Det var en gang en kar som het pål, he was cool
"""
"""
print("Hello World")

print(4+4)
print("4+4")# kommer opp som tekst

tall = 10#Int
tall2 = "10"#String

print(tall *2)
print(tall2 *2)

print("\n")
tall3 = 10.5

print(tall3**2)


liste_1 = [1,2,3,4]
liste_2 = [1, 10.5, "Hei"]

print(type(tall))


f = 2
g = float(f)

print(g)




navnet = "Yasmina"
alder = 24
print("Hei", navnet, "Hyggelig å hilse på deg! " + "Du er", alder, "år gammel")

#F-string kobinere tekst (str) og int(alder)
print(f"Hei {navnet} Du er {alder} år gammel")
print("Hei {}! Du er {} år gammel".format(navnet,alder))



#Oppgaver
#1
temp_BERGEN_sep_19 = 12.2
temp_TRONDHEIM_sep_19 = 9.4
Omk_Rekt_M = 12
Area_sirc_kwm = 16
Kjemi_Ler_School = "Marius"
Kjemi_Ler_Sandsli = "Marius"
Grade_priv_17 = [2,2,5,4,6,3,5,3,5,4,5,6]
Grade_priv_18 = [4,5,3,6,5,4,3,5,6,5]

navn = input("Hva heter du? ")
alderen = input("Hvor gammel er du? ")
gammel = int(alderen)
print("Hei", navn)
print("Du er", gammel, "År gammel")

elgammel = 100 - gammel
print ("Du blir hundre år om", elgammel, "år.")


Temp_Far = int(input("Hvor mange grader er det i Fahrenheit?: "))

Temp_Cels = (Temp_Far - 32)*(5/9)
print(round(Temp_Cels,2), "i celsius")
"""
"""
Svar_en = int(input("Første Tall: "))
Svar_to = int(input("Andre tall: "))
Resultat = Svar_en + Svar_to
print("Resultatet er:", Resultat)
"""

a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

d = b**2-4*a*c

if d == 0:
    x1 = -b/(2*a)
    print("x1 =", x1)
elif d < 0:
    print("ingen løsning")
else:
    x1 = (-b+(d**(1/2))/(2*a))
    x2 = (-b-(d**(1/2))/(2*a))
    print("x1 er:", x1, "og x2 er:", x2)