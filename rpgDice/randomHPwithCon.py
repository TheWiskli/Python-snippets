from random import randint as random
from time import sleep as s

dice_low = 1
dice_high = 1
profesion = input("Hvilken class er du?: Skriv de første fire bokstaver i clasen")

if profesion == "barb":
    dice_high = 12
elif profesion == "figh" or "hunt" or "pala":
    dice_high = 10
elif 