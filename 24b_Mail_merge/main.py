from pathlib import Path

PLACEHOLDER = "[name]"

cwd = Path(__file__).parent

with open(f"{cwd}/Input/Names/invited_names.txt", mode="r") as name_file:
    names = name_file.readlines()

with open(f"{cwd}/Input/Letters/starting_letter.txt", mode="r") as stating_letter:
    letter = stating_letter.read()

for name in names:
    stripped_name = name.strip("\n")
    new_letter = letter.replace(PLACEHOLDER, stripped_name)
    with open(f"{cwd}/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as named_letter:
        named_letter.write(new_letter)
