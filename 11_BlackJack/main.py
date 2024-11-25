# Blackjack Project 

from art import logo
import random
import os

def deal_card() -> int:
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards: list[int]) -> int:
    score = sum(cards)
    if len(cards) == 2 and score == 21:
        return 0
   
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user: int, computer: int) -> None:
    if user == computer:
        print("It's a drawn")
    elif computer == 0:
        print("Opponent got Blackjack. You lose")
    elif user == 0:
        print("You got Blackjack. You win!")
    elif user > 21:
        print("You went over. You lose")
    elif computer > 21:
        print("Opponent went over. You win!")
    else:
        if user > computer:
            print("You win!")
        else:
            print("You lose")

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': " ).lower()

while play == "y":
    print(logo)

    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    continue_dealing = 1
    while continue_dealing:
        if computer_score == 0 or user_score == 0 or user_score >21:
            # Game ends
            print(f"  Your final hand: {user_cards}, final score: {sum(user_cards)}")
            print(f"  Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            compare(user_score, computer_score)
            continue_dealing = 0
        else:
            # Game has not ended
            print(f"  Your cards: {user_cards} current score: {sum(user_cards)}")
            print(f"  Computer's first card: {computer_cards[0]}")
            other_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if other_card == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                # Computer plays
                while computer_score < 17 and computer_score != 0:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)
                print(f"  Your final hand: {user_cards}, final score: {sum(user_cards)}")
                print(f"  Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
                compare(user_score, computer_score)
                continue_dealing = 0
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': " ).lower()
    os.system('cls')
