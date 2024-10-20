# Rock Paper or Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

# ask a choise from user
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user >=3 or user < 0:
    print("You typed an invalid number, you lose!")
else:     
    print(game_images[user])
    # generate computer choise
    computer = random.randint(0,2)
    print("Computer chose:")
    print(game_images[computer])

    if user == computer:
        print("It's a draw")
    elif user == 0 and computer == 2:
        print("you win \n")
    elif computer == 0 and user == 2:
        print("you lose \n")
    elif user > computer:
        print("you win \n") 
    elif computer > user:
        print("you lose \n")    
