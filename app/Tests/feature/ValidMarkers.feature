Feature: Valid markers for player 1 and player 2
    Scenario: if player 1 chooses X, player 2 chooses O 
        When player 1 chooses "X"
        Then player 2 chooses "O"

    Scenario: if player 1 chooses O, player 2 chooses X
        When player 1 chooses "O"
        Then player 2 chooses "X"

    Scenario: if player 1 chooses x, player 2 chooses O 
        When player 1 chooses "x"
        Then player 2 chooses "O"

    Scenario: if player 1 chooses o, player 2 chooses X
        When player 1 chooses "o"
        Then player 2 chooses "X"