# *****************************
# Author: John Velis
# Date: 6/10/2020
# Title: The Interview
# *****************************

from time import sleep

# *****************************
#
#     Display Header
#
# *****************************
def display_header(title):
    print()
    print('\t' + title)
    print()

display_header('The Game')
print('Hello World')
print()
name = input('What is your name?')
print(name)
print(f'Hello {name}')
print()
sleep(2)
user_response = input("Would you like to play the game?")
if user_response == 'yes':
    print("Okay, let's go!")
else:
    print('That\'s too bad')

