# *****************************
# Author: John Velis
# Date: 7/4/2020
# Title: The Interview
# *****************************

import os
from time import sleep

from tb_quest_game_screen_methods import *
from tb_quest_game_objects import *

# *****************************
#
#     Initialize Player
#
# *****************************
player = Player(' ',3,' ')

display_header('The Game')

player.name = input('What is your name?')

display_header('Orientation')
print(f'Hello {player.name}')
print()
sleep(1)
user_response = input("Would you like to play the game?")
if user_response == 'yes':
    print('That is great, but first we need to get some information from you.')
    print()
    player.age = input('How old are you?')
    print()
    player.rank = input('Would you like to begin as a Private or a Sargent. Playing the game as a Sargent will be more difficult.')
    if player.rank != 'Private' or player.rank != 'Sargent':
        print('You must choose either \"Private\" or \"Sargent\".')
else:
    print('That\'s too bad')

