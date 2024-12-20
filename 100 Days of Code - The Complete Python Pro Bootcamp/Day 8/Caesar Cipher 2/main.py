alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def ceaser_cipher(text, shift_amount, direction):
    textToWork = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            if shifted_position < 0:
                shifted_position += 26
            else:
                shifted_position %= len(alphabet)
            textToWork += alphabet[shifted_position]
        else:
            textToWork += letter
    print(f"Here is the text: {textToWork}")

ceaser_cipher(text, shift, direction)


