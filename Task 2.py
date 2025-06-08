#CodeMetric Python Programming Intern 
# Task 2 
#Create a Number Guessing Game
#Develop an interactive guessing game using Python's random number generation.

import random


print("WELCOME TO GUESS THE NUMBER")


def number_guessing_game():
    min_number = random.randint(0,100)
    max_number = random.randint(0,100)
    if min_number > max_number:
        min_number, max_number = max_number, min_number
    correct_guess = random.randint(min_number, max_number)  
    attempts = 0

    print(f"Guess a number between {min_number} and {max_number}!")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))  
            attempts += 1
            
            if user_guess < min_number or user_guess > max_number:
                print("Please guess within the valid range!")
            elif user_guess < correct_guess:
                print("Too low! Try again.")
            elif user_guess > correct_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed correctly in {attempts} attempts.")
                break  

        except ValueError:
            print("Invalid input! Please enter an integer.")

number_guessing_game()