from art import logo
import random

print(logo)
number_to_guess = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# print(f"The correct answer is {number_to_guess}") # For testing purpose
diffidulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if diffidulty == "easy":
    attempts = 10
elif diffidulty == "hard":
    attempts = 5

while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    if guessed_number == number_to_guess:
        print(f"You got it! The answer was {number_to_guess}.")
        attempts = 0
    elif guessed_number > number_to_guess:
        print("Too high.")
        print("Guess again.")
        attempts -= 1
    else: # guessed_number < number_to_guess
        print("Too low.")
        print("Guess again.")
        attempts -= 1
if guessed_number != number_to_guess:
    print("You have run out of guesses, you lose.")
    