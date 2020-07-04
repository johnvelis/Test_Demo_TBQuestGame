import os

# *****************************
#
#     Display Header
#
# *****************************
def display_header(title):
    if os.name == 'nt':
        os.system('cls') # windows
    else:
        os.system('clear') # linux
    print()
    print('\t' + title)
    print()