from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

bids_dict = {}
more = True

while more:
    name = input("What is your name?: ")
    bid = int (input("What's your bid?: $"))
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    bids_dict[name] = bid
    if more_bids == 'no':
        more = False
    elif more_bids == 'yes':
        os.system('cls')

max = 0
name_max = ""
for key in bids_dict:
    if bids_dict[key] > max:
        name_max = key
        max = bids_dict[key]
        
print(f"The winner is {name_max} with a bid of ${max}.")
