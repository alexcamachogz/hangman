# Hangman

This repository contains a command-line implementation of the popular Hangman game in Python. The game allows players to guess letters and uncover a hidden word before running out of lives.

## How to pay

1. Make sure you have Python installed on your machine.
2. Clone this repository to your local machine or download the source code.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the `main.py` script using the command `python main.py`.
5. The game will start by displaying a hangman art and a series of blank spaces representing the hidden word.
6. Enter a letter as your guess and press Enter.
7. The game will check if the letter is present in the hidden word. If it is, the letter will be revealed in the corresponding blank space(s).
8. If the letter has already been guessed in the current game, you will receive a message indicating that you have already guessed that letter.
9. If the letter is not present in the hidden word, you will lose one life and the hangman art will progress.
10. The game will continue until one of two conditions is met:
    * You correctly guess all the letters in the word. In this case, you win the game.
    * You run out of lives (represented by the hangman art being fully displayed). In this case, you lose the game.
12. After the game ends, you will see a message indicating whether you won or lost.

## Customization

You can customize the game by modifying the hangman_words.py file. This file contains a list of words that can be chosen for the game. Feel free to add, remove, or modify the words according to your preference.

## Dependencies

This project has no external dependencies. It only requires Python 3.x to be installed on your machine.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

## Acknowledgments

* The ASCII art for the hangman stages is provided by the hangman_art.py module, which is adapted from an open-source project.
* The inspiration for this Hangman game implementation comes from various online resources and tutorials.
