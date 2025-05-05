import random

def pick_winner(names):
    while len(names) > 1:
        removed_number = random.randint(1, len(names))
        print(removed_number)
        removed_name = names.pop(removed_number - 1)
        print(removed_name)
        if removed_number == len(names) + 1:
            print(f"The winner is: {removed_name}")
            return
        print(f"Removed: {removed_name}")
    print(f"The winner is: {names[0]}")

if __name__ == "__main__":
    participants = {
        1: "Alice",
        2: "Bob",
        3: "Charlie",
        4: "David",
        5: "Emma",
        6: "Frank",
        7: "Grace",
        8: "Henry",
        9: "Ivy",
        10: "Jack",
        11: "Katie",
        12: "Leo"
    }
    participant_names = list(participants.values())
    pick_winner(participant_names)