import random
import sys

choices = ['rock','paper','scissors']

def get_computer_choice(choices):
    computer_choice = random.choice(choices)
    return computer_choice

def get_user_choice(choices):
    while True:
        user_choice = input("\nRock Paper Scissors:")

        if type(user_choice) == 'str' and user_choice.lower() in choices:
            return user_choice.lower()
        
        elif user_choice == 'quit':
            sys.exit()
        
        else:
            print("\n Please input rock paper or scissors.")
            

