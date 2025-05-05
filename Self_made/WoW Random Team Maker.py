from random import choice as rnd
from time import sleep as pause

Players = 5
#Lists used for Races and Factions
Faction_List = ["Horde", "Alliance"]
Horde_Race = ["Blood Elf", "Goblin", "Orc", "Pandaren", "Tauren", "Troll", "Undead", "Dracthyr"]
Alliance_Race = ["Draenei", "Dwarf", "Gnome", "Human", "Night Elf", "Worgen", "Pandaren", "Dracthyr"]
Race_List = []

#Lists for Race spesific Classes they dont use! On top is the Master List with all classes that is going to be a copy to be used multiple times.
Master_Class_List = ["Death Knight","Demon Hunter", "Druid", "Hunter", "Mage", "Monk", "Paladin", "Prest", "Rouge", "Shaman", "Warlock", "Warrior", "Evoker"]
#Multi Faction races
Pandaren_Class = ["Warlock", "Paladin", "Druid", "Demon Hunter", "Evoker"]
Dracthyr_Class = ["Death Knight", "Demon Hunter", "Druid", "Hunter", "Mage", "Monk", "Paladin", "Prest", "Rouge", "Shaman", "Warlock", "Warrior"]
#Horde Races
Orc_Class = ["Priest", "Paladin", "Druid", "Demon Hunter", "Evoker"]
Undead_Class = ["Shaman", "Paladin", "Druid", "Demon Hunter", "Evoker"]
Tauren_Class = ["Mage", "Rouge", "Warlock", "Demon Hunter", "Evoker"]
Troll_Class = ["Paladin", "Demon Hunter", "Evoker"]
Blood_Elf_Class = ["Shamam", "Druid", "Evoker"]
Goblin_Class = ["Monk", "Paladin", "Druid", "Demon Hunter", "Evoker"]
#Alliance Races
Human_Class = ["Shaman", "Druid", "Demon Hunter", "Evoker"]
Dwarf_Class = ["Druid", "Demon Hunter", "Evoker"]
Night_Elf_Class = ["Warlock", "Shaman", "Paladin", "Evoker"]
Gnome_Class = ["Shaman", "Paladin", "Druid", "Demon Hunter", "Evoker"]
Draenei_Class = ["Rouge", "Warlock", "Druid", "Demon Hunter", "Evoker"]
Worgen_Class = ["Monk", "Shaman", "Paladin", "Demon Hunter", "Evoker"]
#the Rnd list used to choose what class the user is using 
Class_List = ["Death Knight", "Demon Hunter", "Druid", "Hunter", "Mage", "Monk", "Paladin", "Prest", "Rouge", "Shaman", "Warlock", "Warrior", "Evoker"]

#Start of the Program
Faction_Chooser = input("Which Faction are you going to choose?: ")
pause(1)
#First choosing the Faction that the players are going to play.
match Faction_Chooser:
    case "Horde":
        print("For The HORDE!")
        Race_List.extend(Horde_Race)
        pause(1)
    case "Alliance":
        print("For the ALLIANCE!")
        Race_List.extend(Alliance_Race)
        pause(1)
    case "Random":
        Faction_Suprise = rnd(Faction_List)
        print(f"Alright! You guys are: {Faction_Suprise}")
        pause(1)
        if Faction_Suprise == "Horde":
            Race_List.extend(Horde_Race)
        elif Faction_Suprise == "Alliance":
            Race_List.extend(Alliance_Race)

#Where the random race is chosen by the machine as many players in the team.
for rnd_Selector in range(Players):
    Race_Result = rnd(Race_List)
    match Race_Result: #After getting the race from the random generator it goes through the Races list of incompadeble classes and removes them from the Class_List.
        case "Pandaren":
            for item in Pandaren_Class:
                if item in Class_List:
                    Class_List.remove(item)
        case "Dracthyr":
            for item in Dracthyr_Class:
                if item in Class_List:
                    Class_List.remove(item)
        case "Orc":
            for item in Orc_Class:
                if item in Class_List:
                    Class_List.remove(item)
        case "Undead":
            for item in Undead_Class:
                if item in Class_List:
                    Class_List.remove(item)
        case "Tauren":
            for item in Tauren_Class:
                if item in Class_List:
                    Class_List.remove(item)
        case "Troll":
            for item in Troll_Class:
                if item in Class_List:
                    Class_List.remove(item)
        case "Blood Elf":
            for item in Blood_Elf_Class:
                if item in Class_List:
                    Class_List.remove(item)
        case "Goblin":
            for item in Goblin_Class:
                if item in Class_List:
                    Class_List.remove(item)
        case "Human":
            for item in Human_Class:
                if item in Class_List:
                    Class_List.remove(item)
        case "Dwarf":
            for item in Dwarf_Class:
                if item in Class_List:
                    Class_List.remove(item)
        case "Night Elf":
            for item in Night_Elf_Class:
                if item in Class_List:
                    Class_List.remove(item)
        case "Gnome":
            for item in Gnome_Class:
                if item in Class_List:
                    Class_List.remove(item)
        case "Draenei":
            for item in Draenei_Class:
                if item in Class_List:
                    Class_List.remove(item)
        case "Worgen":
            for item in Worgen_Class:
                if item in Class_List:
                    Class_List.remove(item)
    
    Class_Result = rnd(Class_List)
    print("\n")
    print("Race:", Race_Result)
    print("Class:", Class_Result)
    pause(0.5)
    Race_List.remove(Race_Result)
    Class_List.clear()
    Master_Class_List.remove(Class_Result)
    Class_List.extend(Master_Class_List)