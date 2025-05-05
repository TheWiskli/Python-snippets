from math import pi
svar = input("Hvor lange er rotorbladene i meter? =")
radius = float(svar)
svar = input("Hva er vindstyrken i meter per sekund? =")
vindstyrke= float(svar)

areal = pi*radius**2
effekt = 0.0003*areal*vindstyrke**3

ef_day = effekt*24
ef_year = ef_day*300
cal_Elbil_pr_tur = ef_year/3000
cal_Elbil_Stor = cal_Elbil_pr_tur*80

print("Arealen er ", round(areal), "kvadratmeter.")
print("Effekten er ", round(effekt), "KW. ")
print("Pr dag ", round(ef_day), "KW og ", round(ef_year), "i året")
print("antal elbiler turbinen kan lade er:", round(cal_Elbil_pr_tur), "i året")
print("For hele Storheia kan de lade ", round(cal_Elbil_Stor), "fra hele parken")