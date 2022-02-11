import os

# this function returns an empty board
def create_empty_board(): 
    board = [['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], 
            ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], 
            ['0', '0', '0', '0', '0']]
    return board

# this function prints the board with coordonates
def print_board(board): 
    abcde = 'ABCDE'
    print('  1 2 3 4 5')
    for i in range(len(board)):
        print(abcde[i], end=' ')
        for item in board[i]:
            print(item, end=' ')
        print()

# this function does not let you put ships close each other
def is_ship_too_close(board, x, y):
    if x-1 >= 0 and board[x-1][y] == "X":
        return True
    if x+1 < len(board[0]) and board[x+1][y] == "X":
        return True
    if y-1 >= 0 and board[x][y-1] == "X":
        return True
    if y+1 < len(board[0]) and board[x][y+1] == "X":
        return True
    return False

# this function gives the coordonates an x symbol which represents the ship
def create_ship(board):
    x, y = get_ship_coordinates(board)
    board[x][y] = "X"
    return board

# this function creates a board
def create_player_board(number_ships): 
    board = create_empty_board()
    print_board(board)
    for i in range(number_ships):
        board = create_ship(board)
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(board)
        
    return board

# this function returns each player's board after they put ships on
def init_players_boards():
    number_ships = 3 
    player1_board = create_player_board(number_ships)
    os.system('cls' if os.name == 'nt' else 'clear')        
    print("Player2's placement phase")  
    player2_board = create_player_board(number_ships)     
    return[player1_board, player2_board]

# this function is for validation of the input 
def validate_coordinates(inp):
    if (len(inp) != 2):
        raise Exception("Invalid input!")
    x = 0
    if (inp[0] == "A"):
        x=0
    elif (inp[0] == "B"):
        x=1
    elif (inp[0] == "C"):
        x=2
    elif (inp[0] == "D"):
        x=3
    elif (inp[0] == "E"):
        x=4
    else:
        raise Exception("Invalid input!")        
    try:
        y = int(inp[1])-1
    except:
        raise Exception("Invalid input!")        
    if y > 4 or y < 0:
        raise Exception("Invalid input!")       
    return (x, y)
    
# this function returns x and y of the input
def get_shooting_coordinates(player_name):
    while True:
        inp = input("Take your shot" + " " + player_name + ": ")
        inp = inp.upper()
        try:
            x, y = validate_coordinates(inp)
        except Exception as e:
            print(e)
            continue
        return (x, y)

#this function gets the coordonates and makes some validations also
def get_ship_coordinates(board):
    while True:
        inp = input("Please place your ship: ")
        inp = inp.upper()
        try:
            x, y = validate_coordinates(inp)
        except Exception as e:
            print(e)
            continue
        if is_ship_too_close(board, x, y) is True:
            print("Ships are too close!")
            continue
        if board[x][y] == "X":
            print("You already marked that move. Please place your ship: ")
            continue
        return (x, y)

#this function initializes each player's board
def init_shooting_board():
    player1_shooting_board = create_empty_board()
    player2_shooting_board = create_empty_board()
    return (player1_shooting_board, player2_shooting_board)

# this function returns if the cell is hit or not
def is_ship_hit(x, y, ship_board): 
    if ship_board[x][y] == "X":
        return True
    else:
        return False

# this function marks the hit by putting h when is hit and m when is missed
def mark_shooting(x, y, shooting_board, ship_board): 
    if is_ship_hit(x, y, ship_board) is True:
        shooting_board[x][y] = "H"
    else:
        shooting_board[x][y] = "M"
    return shooting_board

# this function tells if a player has won
def has_won(shooting_board): 
    mark_S = 0
    for i in range(0, len(shooting_board)):
        for j in range(0, len(shooting_board[i])):
            if shooting_board[i][j] == "H":
                mark_S = mark_S + 1
    if mark_S == 3:
        return True

    return False


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Player1 starts the game. ")
    player1_ship_board, player2_ship_board = init_players_boards()
    player1_shooting_board, player2_shooting_board = init_shooting_board()
    turn = 0
    while True:
        if turn % 2 == 0:
            print_board(player1_shooting_board)
            x, y = get_shooting_coordinates("Player1")
            mark_shooting(x, y, player1_shooting_board, player2_ship_board)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(player1_shooting_board)
            print("Player1's board:")
            if has_won(player1_shooting_board):
                print("Player1 has won the battle! ")
                break
        else:
            print_board(player2_shooting_board)
            x, y = get_shooting_coordinates("Player2")
            mark_shooting(x, y, player2_shooting_board, player1_ship_board)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(player2_shooting_board)
            print("Player2's board:")
            if has_won(player2_shooting_board):
                print("Player2 has won the battle! ")
                break
        turn = turn + 1

    
if __name__ == "__main__":
    main()