from random import randint
from time import sleep as s

min_value = 1
max_value = 6

def list_maker(num_lists):
    lists = []
    for i in range(lists):
        user_input = input(f)

def fourD4Roll(blocks):
    blocks = 1
    for a in range(blocks):
        for b in range(6):
            for c in range(4):
                t_kast = randint(min_value,max_value)
                skill_list.append(t_kast)
                smallest = min(skill_list)
                skill_list.remove(smallest)
            Skill = sum(skill_list)
            block_number.append(Skill)

blocks = input("Hvor mange stat bloks trenger du?: ")
fourD4Roll(blocks)
print(skill_list)
print(block_number)