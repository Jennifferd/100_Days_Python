# Caeser encoding by shifting

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text_in, shift_in, dir):
    cipher_text = ""
    if dir == 'encode':
        for letter in text_in:
            if letter in alphabet:
                index_letter = alphabet.index(letter)
                index_plus = index_letter + shift_in
                if index_plus >= len(alphabet):
                    new_index = index_plus - 26
                else:
                    new_index = index_plus
                cipher_text += alphabet[new_index]
            else:
                cipher_text += letter
        print(f"The encoded text is {cipher_text}") 

    elif dir == 'decode':
        for letter in text_in:
            if letter in alphabet:
                index_letter = alphabet.index(letter)
                index_minus = index_letter - shift_in
                if index_minus < 0:
                    new_index = index_minus + 26
                else:
                    new_index = index_minus
                cipher_text += alphabet[new_index]
            else:
                cipher_text += letter
        print(f"The decoded text is {cipher_text}") 


should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
