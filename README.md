# Wordle Game

This project is an implementation of the Wordle game using Python. The Wordle game is a word-guessing game where the player tries to guess a target word by inputting guesses and receiving feedback on their correctness. The game provides a visually appealing interface solely through code, allowing for an enjoyable gaming experience.

## Game Features

- **Randomized Word Selection**: The game randomly selects a target word from a word bank containing various words to ensure each gameplay session is unique.
- **Interactive Guessing Interface**: The game provides a user-friendly interface for inputting guesses and receiving feedback on the correctness of the guesses.
- **Color-Coded Feedback**: The game uses color-coded letters to indicate the correctness of each guessed letter, making it easy for the player to understand the feedback.
- **Previous Guesses Display**: The game displays the player's previous guesses along with the corresponding feedback, allowing them to keep track of their progress.
- **Limited Guesses**: The player has a limited number of guesses (6 in this implementation) to guess the target word correctly.

## Installation

To run the Wordle game, follow these steps:

1. Clone the repository:
  - ```git clone https://github.com/your-username/wordle-game.git```
2. Navigate to the project directory:
  - ```cd wordle-game```
3. Run the game:
  - ```python wordle.py```

## How to Play

1. The game will display the previous guesses and their feedback, along with a keyboard layout for letter input.

2. Input your guess by typing the letters on the keyboard and pressing Enter.

3. The game will provide feedback on your guess, indicating correct letters in the correct positions (displayed in green), correct letters in the wrong positions (displayed in black), and incorrect letters (displayed in red).

4. Continue making guesses until you either guess the target word correctly or exhaust all of your guesses.

5. If you guess the word correctly, the game will display a "You win!!!" message. Otherwise, it will reveal the correct word.

6. Enjoy playing the Wordle game!

## Customization

You can customize the game by modifying the `word_bank` list in the `_init_` method of the `Wordle` class. Feel free to add or remove words from the list to expand or narrow down the word choices for the game.

## Requirements

- Python 3.x

## Acknowledgments

- The Wordle game was inspired by the popular online game "Wordle".
- Special thanks to the Python community for providing excellent resources and modules for developing games.
