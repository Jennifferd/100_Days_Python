from art import logo
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty() -> int:
    """Checks the level of difficulty desired"""
    diffidulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diffidulty == "easy":
        return EASY_LEVEL
    elif diffidulty == "hard":
        return HARD_LEVEL

def check_answer(guess: int, answer: int):
    """check is the number was guesses"""
    if  guess < answer:
        print("Too low.")
        print("Guess again.")
    elif guess > answer:
        print("Too high.")
        print("Guess again.")
    else: 
        print(f"You got it! The answer was {answer}.")
        
def game ():
    number_to_guess = randint(1, 100)
    guessed_number = 0
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = set_difficulty()

    while attempts != 0 and guessed_number != number_to_guess:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))
        check_answer(guessed_number, number_to_guess)
        attempts -= 1

    if guessed_number != number_to_guess:
        print("You have run out of guesses, you lose.")

game()
