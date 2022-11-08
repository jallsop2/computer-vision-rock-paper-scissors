import random
import sys


def get_computer_choice():
    computer_choice = random.choice(range(0,3))
    return computer_choice

def get_user_choice():

    choices = ['rock','paper','scissors']

    while True:
        user_choice = input("\nRock Paper Scissors:")

        if type(user_choice) == 'str' and user_choice.lower() in choices:
            return choices.index(user_choice.lower())
        
        elif user_choice == 'quit':
            sys.exit()
        
        else:
            print("\n Please input rock paper or scissors.")

def get_winner(computer_choice,user_choice):
    res = (user_choice - computer_choice)%3
    if res == 1:
        print('You won!')
    elif res == 0:
        print('It is a tie')
    elif res == -1:
        print('You lost')

            

