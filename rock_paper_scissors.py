import random

# Define the choices and their corresponding ASCII art
choices = {
    0: "rock",
    1: "paper",
    2: "scissors"
}

ascii_art = {
    "rock": '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    "paper": '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    "scissors": '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}

# Initialize scores
user_score = 0
computer_score = 0

# Game loop
while True:
    print("Choose (0: rock, 1: paper, 2: scissors, 3: quit):")
    user_choice = input()

    if user_choice.isdigit():
        user_choice = int(user_choice)

        if user_choice in [0, 1, 2]:
            computer_choice = random.randint(0, 2)

            print("Your choice:")
            print(ascii_art[choices[user_choice]])
            print(f"You chose {choices[user_choice]}")

            print("Computer's choice:")
            print(ascii_art[choices[computer_choice]])
            print(f"Computer chose {choices[computer_choice]}")

            # Determine the winner
            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
                print("You win!")
                user_score += 1
            else:
                print("Computer wins!")
                computer_score += 1

            print(f"User Score: {user_score}")
            print(f"Computer Score: {computer_score}")
        elif user_choice == 3:
            break
        else:
            print("Invalid choice. Please choose 0, 1, 2, or 3 (to quit).")
    else:
        print("Invalid input. Please enter a number (0, 1, 2, or 3).")
