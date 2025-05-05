a = float(print("x-verdien på sirkelen"))
b = float(print("y-verdien på sirkelen"))
r = float(print("Sirkelen sin radius"))
s = float(print("x-verdien på punktet P"))
t = float(print("y-verdien på punktet P"))

SirkelLikning = (a-s)**2 + (b-t)**2

if SirkelLikning < r**2:
    print("Punktet ligger innenfor sirkelen")
elif SirkelLikning == r**2:
    print("Punktet ligger på sirkelen")
else:
    print("Sirkelen ligger utenfor sirkelen.")