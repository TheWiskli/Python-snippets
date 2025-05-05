#Alderen til Brukeren
"""
Alder = int(input('Hvor Gammel er du?: '))

if Alder >= 20:
    print("FAEN MEG GAMMAL NOKK TIL ALT!")
elif 18<= Alder < 20:
    print("Kan ikke handle sprit enda, men lettis drikker kan du!")
else:
    print("Føkk off!")


Tallet = float(input("Gi meg et tall: "))

if Tallet > 0:
    print("Tallet er større enn 0")
elif Tallet == 0:
    print("Tallet er 0!")
else:
    print("Tallet er mindre enn 0")



rekord = 10.5

tid = float(input("Tiden ble: "))

if tid < rekord:
    mellomrom = float(rekord) - float(tid)
    print("Slo ikke rekorden, men har", mellomrom, "minutter fra rekorden.")


x1 = float(input("Oppgi x1: "))
y1 = float(input("Oppgi y1: "))
x2 = float(input("Oppgi x2: "))
y2 = float(input("Oppgi y2: "))

hoya = x1*x2 + y1*y2

if hoya == 0:
    print ("De er Ortogonale huzah!")
elif hoya > 0:
    print ("Too dayum high!")
else:
    print("Too dayum low!")



for n in range(3,7):
    print(n)

n = 3 
while n <= 7:
    print(n)
    n = n + 1

n = 1
while n<51:
    partall = 2*n
    print(partall)
    n = n + 1

for n in range(50):
    oddetall = 2*n + 1
    print(oddetall)

for oddetall in range(1,100,2):
    print(oddetall)

sum = 0
for a in range(1,10):
    if a%3 == 0:
        print(a)
        sum = a+sum
    elif a%5 ==0:
        print(a)
        sum = a+sum
print("\n")
print(sum)

n=0
sum=0
while n < 10:
    if n%3 == 0:
        sum = sum + n
        n = n + 1
    elif n%5 == 0:
        sum  = sum + n
        n = n + 1
    else:
        n = n + 1

print(sum)

"""