# Legend
# X for placing ship and hit battleship
# ' ' for available space
# '-' for missed shot

from random import randint

while True:
    answer = input('Welcome to Battleships. Would you like to read the rules? (yes/no)')
    if answer.lower().strip() == 'no':
        print ('ok')
        break
    if answer.lower().strip() == 'yes':
        print ('These are the rules: bla bla bla')
        break

while True:
    answer = input('Would you like to play Battleships? (yes/no) ')

    if answer.lower().strip() == 'no':
        print('That\'s Ok, maybe another time :)')
        print('Bye bye now')
        break

    if answer.lower().strip() == 'yes':
        
        # Board for holding our ships locations
        MY_BOARD = [[' '] * 5 for x in range(5)]

        # Board for holding our guesses including hits and misses
        GUESS_BOARD = [[' '] * 5 for i in range(5)]

        letters_to_numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4}

        def print_board(board):
            print('  A B C D E')
            print('  ---------')
            row_number = 1
            for row in board:
                print("%d|%s|" % (row_number, "|".join(row)))
                row_number += 1

        ''' 
        Function to create the ships
        '''

        def create_ships(board):
            for ship in range(5):
                ship_row, ship_column = randint(0, 4), randint(0, 4)
                while board[ship_row][ship_column] == 'X':
                    ship_row, ship_column = get_ship_location()
                board[ship_row][ship_column] = 'X'
        ''' 
        Function to ask user what column and row they want to place the ship on
        '''

        def get_ship_location():
            row = input("\nEnter the row of the ship: ").upper()
            while row not in "12345":
                print('Not an appropriate choice, please select a valid row')
                row = input("Enter the row of the ship: ").upper()
            column = input("Enter the column of the ship: ").upper()
            while column not in "ABCDE":
                print('Not an appropriate choice, please select a valid column')
                column = input("Enter the column of the ship: ").upper()
            return int(row) - 1, letters_to_numbers[column]


        ''' 
        Function to count how many ships are hit and game over when 5 ships are hit
        '''

        def count_hit_ships(board):
            count = 0
            for row in board:
                for column in row:
                    if column == "X":
                        count += 1
            return count


        if __name__ == "__main__":
            create_ships(MY_BOARD)
            turns = 10
        while turns > 0:
            print('Guess a ship\'s location:\n')
            print_board(GUESS_BOARD)
            row, column = get_ship_location()
            if GUESS_BOARD[row][column] == "-":
                print("You guessed that one already.")
            elif MY_BOARD[row][column] == "X":
                print("\nIT\'S A HIT! WAY TO GO!")
                GUESS_BOARD[row][column] = "X" 
                turns -= 1  
            else:
                print("\nYOU MISSED...")
                GUESS_BOARD[row][column] = "-"   
                turns -= 1     
            if count_hit_ships(GUESS_BOARD) == 5:
                print("\nYOU WIN!")
                break
            print("You have " + str(turns) + " turns left\n")
            if turns == 0:
                print("YOU RAN OUT OF TURNS")
                break