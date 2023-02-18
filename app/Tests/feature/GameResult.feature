Feature: board disposal when it is over
    Scenario: player won the game in horizontal below
        Given that we start with an empty board
        When  player with marker "X" chose positions "1", "2" and "3"
        Then  the game is won

    Scenario: player won the game in horizontal middle
        Given that we start with an empty board
        When  player with marker "X" chose positions "4", "5" and "6"
        Then  the game is won

    Scenario: player won the game in horizontal above
        Given that we start with an empty board
        When  player with marker "X" chose positions "7", "8" and "9"
        Then  the game is won

    Scenario: player won the game in vertical left
        Given that we start with an empty board
        When  player with marker "X" chose positions "1", "4" and "7"
        Then  the game is won

    Scenario: player won the game in vertical middle
        Given that we start with an empty board
        When  player with marker "X" chose positions "2", "5" and "8"
        Then  the game is won

    Scenario: player won the game in vertical right
        Given that we start with an empty board
        When  player with marker "X" chose positions "3", "6" and "9"
        Then  the game is won

    Scenario: player won the game in diagonal from left
        Given that we start with an empty board
        When  player with marker "X" chose positions "3", "5" and "7"
        Then  the game is won

    Scenario: player won the game in diagonal right
        Given that we start with an empty board
        When  player with marker "X" chose positions "1", "5" and "9"
        Then  the game is won

    Scenario: the game is tie if board is filled but not in a win position
        Given that we start with an empty board
        When  player1 chose positions "2", "3", "4", "8" and "9"
        And   player2 chose positions "1", "5", "6" and "7"
        Then  the game is tie        