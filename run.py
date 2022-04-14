# Legend
# X for placing ship and hit battleship
# ' ' for available space
# '-' for missed shot



from random import randint


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

def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        boar[ship_row][ship_column] = 'X'
''' 
Function to ask user what column and row they want to place the ship on
'''

def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]


''' 
Function to count how many ships are hit and game over when 5 ships are hit
'''

def count_hit_ships():
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

create_ships()
turns=10
# while turns > 0: