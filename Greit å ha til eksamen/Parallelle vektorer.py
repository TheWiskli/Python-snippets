def Prikke_produkt(Vector1, Vector2):
    return sum(x * y for x, y in zip(Vector1, Vector2))
def magnituden(Vector):
    return sum(x**2 for x in Vector)*0.5
def er_vektor_Parallelle(Vector1, Vector2):
    Prikke_produkt_resultat = Prikke_produkt(Vector1, Vector2)
    produkt_av_magnituden = magnituden(Vector1) *magnituden(Vector2)

    toleranse = 1e-10

    return abs(Prikke_produkt_resultat - produkt_av_magnituden) < toleranse


vector_a = [5, -2]
vector_b = [10, -4]

print(Prikke_produkt(vector_a,vector_b))
print(magnituden(vector_a))
print(magnituden(vector_b))
print( magnituden(vector_a) * magnituden(vector_b))
print(er_vektor_Parallelle(vector_a,vector_b))

if er_vektor_Parallelle(vector_a, vector_b):
    print("vektorene er parallelle.")
else:
    print("Vektorene er ikke parallelle.")