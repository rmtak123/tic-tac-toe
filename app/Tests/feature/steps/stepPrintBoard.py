import behave
from src.main import init_board, print_board

@when('my board is empty')
def step_impl(context):
    context.empty_board = init_board()

@then(u'the board should not have filled cells')
def step_impl(context):
    expected_board = {"1":" ", "2":" ", "3":" ", "4":" ", "5":" ", "6":" ", "7":" ", "8":" ", "9":" ", }
    assert context.empty_board == expected_board