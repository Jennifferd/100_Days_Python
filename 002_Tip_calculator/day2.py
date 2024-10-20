print("Welcome to the tip calculator.")
bill = float (input("What was the total bill? "))
tip = int (input("What porcentage tip would you like to give? 10, 12, or 15? "))
people = int (input("How many people to split the bill? "))

tbill = bill * (100 + tip)/100
ttip = round ((tbill/ people), 2)
ttip = "{:.2f}".format(ttip) # This take the float into an string that uses that particular format

print(f"Each person should pay ${ttip}")
