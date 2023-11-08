"""
Caesar Cipher Project
"""
from utils.tools import clear_terminal
from utils.logos import LOGO1


def caesar_cipher(direction, text, shift):
    """ Returns the cipher text for the given text and shift.
        Parameters:
            direction (str): 'encode' or 'decode'
            text (str): Text to be encoded or decoded
            shift (int): Shift value
        Returns:
            str: Cipher text"""

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = ""

    if direction == "encode":
        for char in text:
            if char.isalpha():
                position = alphabet.index(char)
                new_position = (position + shift) % 26
                cipher_text += alphabet[new_position]
            else:
                cipher_text += char
        return cipher_text

    elif direction == "decode":
        for char in text:
            if char.isalpha():
                position = alphabet.index(char)
                new_position = (position - shift) % 26
                cipher_text += alphabet[new_position]
            else:
                cipher_text += char
        return cipher_text

def main():
    """ Main function """
    clear_terminal()
    title = LOGO1
    
    print(title)
    print("Welcome to the Caesar Cipher program.")
    while True:
        direction = input("Choose direction (encode/decode): ")
        if direction not in ["encode", "decode"]:
            print("Invalid direction. Please choose 'encode' or 'decode'.")
            continue

        text = input("Enter the text (letters only, no numbers or symbols): ")
        if not text.isalpha():
            print("Invalid input. Please use letters only (no numbers or symbols).")
            continue

        shift = input("Enter the shift (a number): ")
        if not shift.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        shift = int(shift)

        result = caesar_cipher(direction, text, shift)
        print(f"Result: {result}")

        option = input("Press enter to continue or type 'leave' to close the program: ")
        if option.lower() == 'leave':
            break

if __name__ == "__main__":
    main()
