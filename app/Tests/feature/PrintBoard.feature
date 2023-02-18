Feature: print board
    Scenario: empty board
        When my board is empty
        Then the board should not have filled cells