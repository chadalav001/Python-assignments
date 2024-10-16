''' number guessing game'''

import random

def guess(x,y):

    number_to_guess = random.randint(x,y)
    while True:
        user = int(input(f"Enter a number {x} and {y} "))
        if user == number_to_guess:
            print(" Congrats you guessed right ")
            break
        elif user > number_to_guess:
            print(" Too high guess little low ")
        elif user < number_to_guess:
            print(" Too low guess little high")
        number = input(" ENTER TO Y TO EXIT & N TO CONTINUE  ").lower()
        if number == "y":
            print(" THANK YOU ")
            break
guess(1,100)
