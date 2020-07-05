import os

# *****************************
#
#     Display Header
#
# *****************************
def display_header(title):
    """function to clear the terminal and display a header

    Args:
        title (string): header text
    """
    if os.name == 'nt':
        os.system('cls') # windows
    else:
        os.system('clear') # linux
    print()
    print('\t' + title)
    print()