# Country Guessing Game
Welcome to the Country Guessing Game! This is a simple Python-based word guessing game where you try to guess the name of a randomly chosen country one letter at a time or by entering the entire word. The game provides you with hints about the number of letters in the word and displays your progress as you make correct guesses.

## How to Play
Make sure you have Python installed on your machine.
Clone this repository or download the main.py file.
Run the main.py file using a Python interpreter.
## Rules
You have a limited number of turns to guess the correct word.
Each incorrect guess deducts 10 points from your score.
You can guess a single letter or the entire word.
Guess the entire word correctly to win the game and see your final score.
If you run out of turns before guessing the word, the game ends, and the correct word is revealed.
## Example Gameplay
The game will display a series of underscores indicating the number of letters in the word to guess: _ _ _ _ _ _ _.
You can start guessing letters. For example, if you guess 'a', and the word contains an 'a', the display might become: _ _ _ a _ _ _.
Continue guessing until you either correctly guess the entire word or run out of turns.
## About the Code
The game is implemented in Python and uses the built-in random module to choose a random country from a list. The chosen country is then displayed with underscores for each letter, and the player's input is used to reveal correct letters.

The code is structured into functions to enhance readability and modularity. Feel free to explore, modify, and enhance the code to add your own features or improve the user experience.

## File Structure
main.py: The main Python script containing the game logic.
countries.txt: A list of countries used by the game to choose a random word.
