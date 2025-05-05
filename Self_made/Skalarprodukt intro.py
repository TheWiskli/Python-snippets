#Skalarprodukt

print("Skriv inn kordinatene til vektoren u= [x1,y1]")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("Skriv inn kordinatene til vektoren v= [x2,y2]")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

skalarprodukt = x1*x2 + y1*y2

if skalarprodukt == 0:
    print("Vektorene er ortogonale")
    print(skalarprodukt)
elif skalarprodukt > 0:
    print("Vinkelen mellom vektorene er spiss.")
    print(skalarprodukt)
else:
    print("Vinkelen mellom vektorene er stump")
    print(skalarprodukt)