from random import choice as rnd
from time import  sleep as pause

def CupMaker(item):
    for CupMakeing in range(4):
        RandomCup = rnd(item)
        if not RandomCup:
            item.remove(RandomCup)
            MasterCupList(RandomCup)
            RandomCup = rnd(item)
            CorseChoser =rnd(RandomCup)
            GeneratedCupList.append(CorseChoser)
            RandomCup.remove(CorseChoser)
            item.remove(RandomCup)
        else:
            CorseChoser =rnd(RandomCup)
            GeneratedCupList.append(CorseChoser)
            RandomCup.remove(CorseChoser)
            item.remove(RandomCup)

MushroomCup = ["Mario Kart Stadium", "Water Park", "Sweet Sweet Canyon", "Thwomp Ruins"]
FlowerCup = ["Mario Circuit (Flower Cup)", "Toad Harbour", "Twisted Mansion", "Shy Guy Falls"]
StarCup = ["Sunshine Airport", "Dolphin Shoals", "Electrodrome", "Mount Wario"]
SpesialCup = ["Cloud Cruise", "Bone Dry Dunes", "Bowser's Castle", "Rainbow Road (Spesial Cup)"]
EggCup = ["Yoshi Circut", "Excitebike Arena", "Dragon Driftway", "Mute City"]
CrossingCup = ["Baby Park", "Cheese Land", "Wild Woods", "Animal Crossing"]
ShellCup = ["Moo Moo Meadows", "Mario Circuit (Shell Cup)", "Cheep Cheep Beach", "Toad's Turnpike"]
BananaCup = ["Dry Dry Desert", "Donut Plains 3", "Royal Raceway", "DK Jungle"]
LeafCup = ["Wario Stadium", "Sherbert Land", "Melody Motorway", "Yoshi Valley"]
LightningCup = ["Tick-Tock Clock", "Piranha Plant Pipeway", "Grumble Volcano", "Rainbow Road (Lighting Cup)"]
TriforceCup = ["Wario's Gold Mine", "Rainbow Road (Triforce Cup)", "Ice Ice Outpost", "Hyrule Circuit"]
BellCup = ["Koopa City", "Ribbon Road", "Super Bell Subway", "Big Blue"]

CupList = [MushroomCup, FlowerCup, StarCup, SpesialCup, EggCup, CrossingCup, ShellCup, BananaCup, LeafCup, LightningCup, TriforceCup, BellCup]
MasterCupList = [MushroomCup, FlowerCup, StarCup, SpesialCup, EggCup, CrossingCup, ShellCup, BananaCup, LeafCup, LightningCup, TriforceCup, BellCup]
GeneratedCupList = []

Rounds = int(input("Hvor mange runder skal dere ha: "))

for randcorseMaker in range(Rounds):
    CupMaker(CupList)
    print(f"Cup Nummer: {randcorseMaker+1}")
    print(GeneratedCupList)
    print("")
    CupList.clear()
    CupList.extend(MasterCupList)
    GeneratedCupList.clear()
    pause(0.5)