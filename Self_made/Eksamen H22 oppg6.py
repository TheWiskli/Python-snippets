Ox = 0
Oy = 0

Ax = float(input("X-verdi på A:"))
Ay = float(input("Y-verdi på A:"))

Bx = float(input("X-verdi på B:"))
By = float(input("Y-verdi på B:"))

Cx = float(input("X-verdi på C:"))
Cy = float(input("Y-verdi på C:"))

OTx = (1/3)*(Ax+Bx+Cx)
OTy = (1/3)*(Ay+By+Cy)

print("Kordinatene til Tyngdepunktet er X =", round(OTx,2), "Y =", round(OTy, 2))