"""
Gammel Variant av "for" løkken, funker men har et problem med append løsningen

"""
#liste oppsett av første del av problemet
list_del1 = [None] * deled1
print(list_del1)   
#løkken til å bytte innholdet None til tall
for fyll_del1 in list_del1:
    svar = input("Skriv tallet som blir brukt fra høyre: ")
    del1_ledje = float(svar)

    list_del1.append(del1_ledje)
    print(list_del1)
    list_del1 = list_del1[-deled1:]
    print(list_del1)
#pga en eller annen måte så må man sette inn 
#det første tallet til noe helt annet når jeg ikke trenger det