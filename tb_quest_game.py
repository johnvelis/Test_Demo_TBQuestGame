# *****************************
# Author: John Velis
# Date: 6/10/2020
# Title: The Interview
# *****************************

import os
from time import sleep

# *****************************
#
#     Display Header
#
# *****************************
def display_header(title):
    os.system('cls') # use 'clear' on linux
    print()
    print('\t' + title)
    print()

display_header('The Game')
print('Hello World')
print()
name = input('What is your name?')

display_header('Orientation')
print(f'Hello {name}')
print()
sleep(2)
user_response = input("Would you like to play the game?")
if user_response == 'yes':
    print("Okay, let's go!")
else:
    print('That\'s too bad')

