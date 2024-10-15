# Python-Guessing_Game

Welcome to **Sam's Guessing Game**, a fun and interactive number guessing game where the player tries to guess a randomly generated number based on the difficulty level they choose. The game provides hints to the player, indicating if their guess is higher or lower than the actual number. Once the player guesses correctly, they can choose to replay the game or exit.

## Features

- **Difficulty Levels**: The player selects a difficulty level, which determines the range of numbers they can guess from (e.g., 1-100, 1-200, etc.).
- **Hints**: After each guess, the game will tell the player whether their guess is greater or lesser than the actual number.
- **Replay Option**: After completing a game, the player can choose to replay or quit.
- **Track Attempts**: The game tracks how many attempts it took for the player to guess the correct number.

## How to Play

1. **Select Difficulty**: Choose a difficulty level from 1 to 10, where each level represents a range of numbers (e.g., Level 1 is from 1 to 100, Level 2 is from 1 to 200, etc.).
2. **Guess the Number**: You will be prompted to guess the randomly generated number within the selected range.
3. **Hints**: After each guess, you'll be told whether your guess was too high or too low.
4. **Win the Game**: Once you guess the correct number, the game will tell you how many attempts you made. You can then choose to play again or exit.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/afolabisamguy/Python-Guessing_Game.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Python-Guessing_Game
    ```

3. Ensure you have Python installed. This game is written in Python 3.

## Running the Game

To start the game, run the following command:

```bash
python main.py
```

Follow the on-screen instructions to select your difficulty level and start guessing!

## Example Gameplay

```
Welcome to Sam's Guessing Game
PLease enter the difficulty level
Press 1 for 1 - 100
Press 2 for 1 - 200
...
Press 10 for 1 - 1000

The number is random between 1 to 100, guess the number:
> 50
Your guess is lesser than the number.
> 75
Your guess is greater than the number.
> 63
You're correct.. You are somewhat of a genius!
It took You 3 attempts.

Press Y to play again or N to Quit:
```

## License

This project is licensed under the MIT License.
