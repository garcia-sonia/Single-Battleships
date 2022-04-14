
# Board for holding our ships locations
MY_BOARD = [[' '] * 8 for x in range(8)]

# Board for holding our guesses including hits and misses
GUESS_BOARD = [[' '] * 8 for x in range(8)]

letters_to_numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

def print_board(board):
    print('     A B C D E F G H')
    print('     ---------------')
    row_number = 1
    for row in board:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number +=1

''' 
Function to create the ships
'''

def create_ships():
    pass

''' 
Function to ask user what column and row they want to place the ship on
'''

def get_ship_location():
    pass


''' 
Function to count how many times the ship is hit and game over when 5 hits
'''

def count_hit_ships():
    pass

create_ships()
turns=10
# while turns > 0: