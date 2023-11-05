"""
Password Generator Project
"""
import string
import random
from random import randint

letters = list(string.ascii_letters)
symbols = list(string.punctuation)

total_letters = int(input("How many letters would you like in your password?\n"))
total_symbols = int(input("How many symbols would you like?\n"))
total_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for i in range(0, total_letters):
    password_list.append(random.choice(letters))

for i in range(0, total_symbols):
    password_list.append(random.choice(symbols))

for i in range(0, total_numbers):
    password_list.append(str(randint(0, 9)))

random.shuffle(password_list)
PSSW = "".join(password_list)

print(PSSW)
