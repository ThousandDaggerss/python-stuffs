"""
Colection of useful functions
"""
import os

def clear_terminal():
    """This function clears the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
