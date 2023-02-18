"""
Let's play tic tac toe!
This is a fun way to practice BDD with Behave
"""

from IPython.display import clear_output

# Initialize an empty board
def init_board():
    board = {"1":" ", "2":" ", "3":" ", "4":" ", "5":" ", "6":" ", "7":" ", "8":" ", "9":" "}
    return board

# Set the markers for player1 and player2
def validate_markers():
    valid_marks = ["X", "O", "x", "o"]
    message = "Player 1, please choose your mark: X or O: "
    
    player1_mark = input(message)

    while player1_mark not in valid_marks:
        player1_mark = input(message)
    
    return set_players_markers(player1_mark)

# Define the mark tuple for the players
def set_players_markers(player1_mark):
    if player1_mark.upper() == "X":
        player2_mark = "O"
    else:
        player2_mark = "X"

    # Consider either lower and upper case provided by the player
    player1_mark = player1_mark.upper()
    
    return {"Player 1":player1_mark, "Player 2":player2_mark}

# To change turns between the players
def change_turns(player_move):
    if player_move == "Player 1":
        return "Player 2"
    else:
        return "Player 1"

# Print the board
def print_board(board):
    
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-----")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-----")    
    print(board["1"] + "|" + board["2"] + "|" + board["3"])

    return board

# Check if any player won the game
def game_won(board):
    # Set of all the possible combinations to win the game
    return ((board["1"]  == board["2"] == board["3"] and board["1"] != " ")
        or  (board["1"]  == board["2"] == board["3"] and board["1"] != " ")
        or  (board["4"]  == board["5"] == board["6"] and board["4"] != " ")
        or  (board["7"]  == board["8"] == board["9"] and board["7"] != " ")
        or  (board["1"]  == board["4"] == board["7"] and board["1"] != " ")
        or  (board["2"]  == board["5"] == board["8"] and board["2"] != " ")
        or  (board["3"]  == board["6"] == board["9"] and board["3"] != " ")
        or  (board["3"]  == board["5"] == board["7"] and board["3"] != " ")
        or  (board["1"]  == board["5"] == board["9"] and board["1"] != " ")
    ) 

# The game is tie if no position is available
def game_tie(board):
    if " " not in board.values() and game_won(board) is False:
        return True
    else:
        return False
    
# Play
def play(board, players_dict):

    # Player 1 starts the game
    player_move = 'Player 1'

    # Keep on playing while the game is not won
    while game_won(board) is False:
        message = f'\n{player_move} ( {players_dict[player_move]} ), choose the position of your next move: '
        position = input(message)

        # Keep asking the position until a valid number is input
        while position not in board.keys() or board[position]  != ' ':
            print('\nYou chose a invalid position. Please, try again...')
            position = input(message)
        
        # Fill the chosen position with the appropriate mark
        board[position] = players_dict[player_move]
        print_board(board)

        # If the game is not won yet and not tie, change turns
        if game_won(board) is False and game_tie(board) is False:
            player_move = change_turns(player_move)
        elif game_tie(board):
            print(f'\nGame tie... no winners..\nGoodbye!\n')
            break
        else:
            print(f'\nCongratulations, {player_move} ( {players_dict[player_move]} ) !!\n You won the game!!\nGoodbye\n')
            break

######################################## MAIN #################################
if __name__ == "__main__":
    players_dict = validate_markers()
    board = init_board()
    play(board, players_dict)