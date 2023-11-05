"""
Hangman Project
"""
import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("X_RAPIDAPI_KEY")
HOST = os.getenv("X_RAPIDAPI_HOST")

# print(API_KEY)
# print(HOST)

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
=========''', '''
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

    print("Welcome to Hangman!")

    # Make a request to the API endpoint
    url = "https://wordsapiv1.p.rapidapi.com/words/"

    querystring = {"random":"true"}

    headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": HOST}

    response = requests.get(url, headers=headers, params=querystring, timeout=10)

    # print(response.json())  # Para ver a reposta e testar
    # print(response.status_code)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the word from the response
        word = response.json()['word']
        guessed_letters = []
        attempts = 6

        while attempts > 0:
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
        # show the word when game over
        print(f"The word was: {word}.\nGame over!")
    else:
        print("Failed to retrieve word from API.")

hangman()
