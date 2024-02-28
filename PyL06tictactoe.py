import random

def evaluate(board):
    if "xxx" in board:
        print("The player who uses x won!")
        return False
    elif "ooo" in board:
        print("The player who uses o won!")
        return False
    elif "-" not in board:
        print("Draw!")
        return False
    else:
        print("Game continues.")
        return True

def move(board, position, mark):
    board = list(board)
    if 0 <= position < 20 and board[position] == "-":
        board[position] = mark
    return ''.join(board)

def player_move(board, user_symbol):
    position = int(input("What is your position from 0 to 19?: "))
    if 0 <= position < 20 and board[position] == "-":
                board = move(board, position, user_symbol)
    else:
        print("Invalid move. Try again.")
        
    return board

def pc_move(board, pc_symbol):
    position = random.randint(0, 19)
    while board[position] != "-":
        position = random.randint(0, 19)
    board = move(board, position, pc_symbol)
    return board

def game_tictactoe():
    board = 20 * "-"
    user_symbol = input("Choose your symbol, x or o: ").lower()
    if user_symbol == "x":
        pc_symbol = "o"  
    else:
        pc_symbol = "x"
    
    play_on = True
    while play_on:
        print(board)
        board = player_move(board, user_symbol)
        play_on = evaluate(board)
        if not play_on:
            break
        board = pc_move(board, pc_symbol)
        play_on = evaluate(board)
        print(board)

game_tictactoe()