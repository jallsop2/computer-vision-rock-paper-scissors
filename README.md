#Rock Paper Scissors Computer Vision Project

The aim of theis project is to create a program ro allow me to play rock paper scissors against the computer, using my webcam.

##Milestone 2
I created a computer vision model to detect whether I am signing rock paper scissors or nothing using the webcam.
This is made using Teachable Machine an online tool for creating machine learing models.

## Milestone 4
I set up the python 3.8 environment needed for tensorflow using conda, with the command:
```
conda create -n my_env python=3.8
```

Then I created the manual_rps.py file to manually run a game of rock paper scissors.

```python
import random
import sys


def get_computer_choice():
    computer_choice = random.choice(range(0,3))
    return computer_choice

def get_user_choice():

    choices = ['rock','paper','scissors']

    while True:
        user_choice = input("\nRock Paper Scissors:")

        if isinstance(user_choice,str) == True and user_choice.lower() in choices:
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
    elif res == 2:
        print('You lost')

            
def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice,user_choice)

play()
```