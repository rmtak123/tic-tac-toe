import behave
from Tests.testUtils import parse_parameter_from_feature
from src.main import set_players_markers

@when('player 1 chooses {player1_mark}')
def step_impl(context, player1_mark):
    context.player1_mark = parse_parameter_from_feature(player1_mark)

@then('player 2 chooses {expected_mark}')
def step_impl(context, expected_mark):
    players_dict = set_players_markers(context.player1_mark)    
    assert players_dict["Player 2"] == parse_parameter_from_feature(expected_mark)