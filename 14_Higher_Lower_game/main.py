from art import logo, vs
from game_data import data
import random
import os

def get_random_account() -> dict:
    """ Return a random data from data """
    return random.choice(data)

def ask_to_guess(option_a: dict, option_b: dict) -> chr:
    """ Shows options and asks user to choose"""
    # Print the options to choose
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

    # Ask user to guess 
    choise = input("Who has more followers? Type 'A' or 'B': ").upper()
    return choise

def higher_score(option_a: dict, option_b: dict) -> chr:
    """ Returns which account has the higher score """
    if option_a['follower_count'] >= option_b['follower_count']:
        higher = 'A'
    else:
        higher = 'B'
    return higher


def game():
    # Generate 2 random account to guess
    data_A = {}
    data_B = {}
    data_A = get_random_account()
    data_B = get_random_account()
    score = 0
    continue_playing = True

    #  Print header of the game 
    print(logo)

    while continue_playing:
        data_A = data_B
        while data_A == data_B:
            data_B = get_random_account()

        # Print the options to choose
        guess = ask_to_guess(data_A, data_B)
        answer = higher_score(data_A, data_B)
        os.system('cls')
        print(logo)
        # Check the guess
        if answer == guess:
            # increase the score and generate a new random
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            # If guess incorrect, end game
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_playing = False

game()
