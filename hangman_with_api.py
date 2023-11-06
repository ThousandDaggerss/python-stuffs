"""
Hangman Project
"""
import os
import time
import requests
from dotenv import load_dotenv
from utils.tools import clear_terminal

load_dotenv()

API_KEY = os.getenv("X_RAPIDAPI_KEY")
HOST = os.getenv("X_RAPIDAPI_HOST")

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def hangman():
    """ Hangman game """

    # Clear the terminal screen
    clear_terminal()

    print("Welcome to Hangman!")
    time.sleep(1)

    # Make a request to the API endpoint
    url = "https://wordsapiv1.p.rapidapi.com/words/"

    querystring = {"random":"true"}

    headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": HOST}

    response = requests.get(url, headers=headers, params=querystring, timeout=10)

    # print(response.json())  # see the word just to test
    # print(response.status_code)  # if it's 200, it worked

    # Check if the request was successful
    if response.status_code == 200:
        # Get the word from the response
        word = response.json()['word']
        guessed_letters = []
        attempts = 6

        while attempts > 0:
            # Clear the terminal before displaying the new hangman stage and word state
            clear_terminal()
            # Display title every stage
            print("""
             _____ _____ _____ _____ _____ _____ _____ 
            |  |  |  _  |   | |   __|     |  _  |   | |
            |     |     | | | |  |  | | | |     | | | |
            |__|__|__|__|_|___|_____|_|_|_|__|__|_|___|""")
            # Display the current hangman stage
            print(stages[6 - attempts])

            # Display the current state of the word
            display_word = ""
            for letter in word:
                if letter in guessed_letters:
                    display_word += letter
                else:
                    display_word += "_"

            print(display_word)

            # Get the user's guess
            guess = input("\nGuess a letter: ")

            # Check if the guess is correct
            if guess in word:
                print("Correct guess!")
                guessed_letters.append(guess)
            else:
                print("Wrong guess!")
                attempts -= 1

            # Check if the word has been completely guessed
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word.")
                break

        # Clear the terminal one more time before displaying the final result
        clear_terminal()
        # Display title
        print("""
             _____ _____ _____ _____ _____ _____ _____ 
            |  |  |  _  |   | |   __|     |  _  |   | |
            |     |     | | | |  |  | | | |     | | | |
            |__|__|__|__|_|___|_____|_|_|_|__|__|_|___|""")
        # Show the word when the game is over
        print(stages[6 - attempts])  # Display the final hangman stage
        # show the word when game over
        print(f"The word was: {word}.\nGame over!")
        # sleep for 3 seconds
        time.sleep(4)
        # Clear the terminal
        clear_terminal()
    else:
        print("Failed to retrieve word from API.")

hangman()
