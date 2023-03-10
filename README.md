# tic-tac-toe

## Summary
- [About this repo](#about-this-repo)
- [Testing with BDD](#testing-with-bdd)
- [Further references](#further-references)
___

## About this repo

This repo is intended to practice the basics of BDD (Behavior Driven Development) in a simple game (`tic-tac-toe`) written in Python

## Testing with BDD

To test the tic-tac-toe game, we created 3 feature files:
- **GameResult**: to test if the game is tie, won or not finished yet
- **PrintBoard**: to test the game board printing
- **ValidMarkers**: to test if the users (Player 1 and Player 2) chose the correct markers ("X" or "O")

## How to run the tests

```bash
# cd to the app/ directory
cd app
```

```bash
# run behave in python
python -m behave
```

## How to play the game


```bash
# run this command to play the game
python src/main.py
```
___

## Further references

- [About tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe)
- [About BDD](https://cucumber.io/docs/bdd/)
- [About Behave](https://github.com/behave/behave)