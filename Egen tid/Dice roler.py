import random

min_value = 1
max_value = 5

roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Terningene ruller....")
    print("Resultatene er: ")
    print("Tema=", random.randint(min_value, max_value))
    print("Vansklighet=",random.randint(min_value, max_value))
    
    roll_again = input("Rull terninger igjen?: ")