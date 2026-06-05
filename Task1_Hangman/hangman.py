# Task 1 - Hangman Game
# Concepts used: random, while loop, if-else, strings, lists, OOP (class, object)

import random

# ----------------------------------------
# CLASS - HangmanGame
# Using a class to group all game data and
# functions together in one place
# ----------------------------------------
class HangmanGame:

    # __init__ is called automatically when we create an object
    # It sets up all the starting values for the game
    def __init__(self):
        self.words = ["python", "coding", "laptop", "science", "hangman"]
        self.secret_word = random.choice(self.words)   # pick a random word
        self.guessed_letters = []                       # empty list at start
        self.wrong_guesses = 0                          # start at 0
        self.max_wrong = 6                              # max 6 wrong guesses

    # Method to show the word with blanks for unguessed letters
    def show_word(self):
        display = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display = display + letter + " "
            else:
                display = display + "_ "
        return display

    # Method to check if the player has won
    def check_win(self):
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False   # at least one letter still missing
        return True            # all letters guessed

    # Method to take a guess from the player
    def make_guess(self, guess):

        # Only accept a single alphabet letter
        if len(guess) != 1:
            print("Please enter only one letter at a time.")
            return

        if not guess.isalpha():
            print("Please enter a valid letter.")
            return

        # Already guessed before
        if guess in self.guessed_letters:
            print("You already guessed that letter. Try again.")
            return

        # Add to guessed list
        self.guessed_letters.append(guess)

        # Check if correct or wrong
        if guess in self.secret_word:
            print("Good guess!")
        else:
            self.wrong_guesses = self.wrong_guesses + 1
            print("Wrong! Chances left:", self.max_wrong - self.wrong_guesses)

    # Method to start and run the full game loop
    def play(self):
        print("Welcome to Hangman!")
        print("Guess the word one letter at a time.")
        print("You have 6 chances.\n")
        print("The word has", len(self.secret_word), "letters.")

        # Keep playing until wrong guesses reach the limit
        while self.wrong_guesses < self.max_wrong:

            print("\nWord:", self.show_word())
            print("Wrong guesses so far:", self.wrong_guesses)
            print("Letters guessed:", self.guessed_letters)

            guess = input("Enter a letter: ")
            self.make_guess(guess)

            # Check if player won after each guess
            if self.check_win():
                print("\nCongratulations! You guessed the word:", self.secret_word)
                return

        # If loop ends naturally, player lost
        print("\nGame Over! You ran out of chances.")
        print("The word was:", self.secret_word)


# ----------------------------------------
# Create an object of HangmanGame and play
# ----------------------------------------
game = HangmanGame()   # creating an object from the class
game.play()            # calling the play method on the object
