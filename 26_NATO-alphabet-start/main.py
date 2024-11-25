import pandas

# Dictionary in the format: {"A": "Alfa", "B": "Bravo"}
nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for (index, row) in nato_csv.iterrows()}

# List of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
word_list = [nato[letter] for letter in word]
print(word_list)
