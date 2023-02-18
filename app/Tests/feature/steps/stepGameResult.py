import behave
from Tests.testUtils import parse_parameter_from_feature
from src.main import init_board, game_won, game_tie

@given('that we start with an empty board')
def step_impl(context):
    context.board = init_board()

# Game is won
@when('player with marker {marker} chose positions {position1}, {position2} and {position3}')
def step_impl(context, marker, position1, position2, position3):
    context.board[parse_parameter_from_feature(position1)] = parse_parameter_from_feature(marker)
    context.board[parse_parameter_from_feature(position2)] = parse_parameter_from_feature(marker)
    context.board[parse_parameter_from_feature(position3)] = parse_parameter_from_feature(marker)

@then('the game is won')
def step_impl(context):
    result = game_won(context.board)
    assert result == True

@then('the game is not won yet')
def step_impl(context):
    result = game_won(context.board)
    assert result == False

# Game is tie
@when("player1 chose positions {player1_choice1}, {player1_choice2}, {player1_choice3}, {player1_choice4} and {player1_choice5}")
def step_impl(context, player1_choice1, player1_choice2, player1_choice3, player1_choice4, player1_choice5):
    context.board[parse_parameter_from_feature(player1_choice1)] = "X"
    context.board[parse_parameter_from_feature(player1_choice2)] = "X"
    context.board[parse_parameter_from_feature(player1_choice3)] = "X"
    context.board[parse_parameter_from_feature(player1_choice4)] = "X"
    context.board[parse_parameter_from_feature(player1_choice5)] = "X"

@when("player2 chose positions {player2_choice1}, {player2_choice2}, {player2_choice3} and {player2_choice4}")
def step_impl(context, player2_choice1, player2_choice2, player2_choice3, player2_choice4):
    context.board[parse_parameter_from_feature(player2_choice1)] = "O"
    context.board[parse_parameter_from_feature(player2_choice2)] = "O"
    context.board[parse_parameter_from_feature(player2_choice3)] = "O"
    context.board[parse_parameter_from_feature(player2_choice4)] = "O"

@then("the game is tie")
def step_impl(context):
    result = game_tie(context.board)
    assert result == True