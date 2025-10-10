# Week 10 - Activity 3: Readability, Maintainability & Refactoring- Tic-Tac-Toe - OOP
# Develop a project using the following tasks: (estimated time 30 minutes for first version of the development)
# Design (Top-Down)
# Plan the project structure with classes and functions
# Each class should have clear methods
# Implementation
# Create a 3×3 board and display it.
# Let two players take turns entering moves.
# Detect winner or draw.
# Use good OOP practices (encapsulation, methods, and attributes).
# Testing
# Run and debug the game using - manual testing
# Handle invalid inputs.
# Code Quality
# Run Pylint:
# Improve your score by fixing Pylint warnings and following Python style guidelines.
# Share your result with sharing GitHub link.

"""This is main class for playing tic tac toe."""


class TicTacToe:
    """Initializing empty board for tic tac toe."""

    _tic_tac_board = [["", "", ""], ["", "", ""], ["", "", ""]]

    def play(self, string, index):
        """It takes input from users and puts it into a board."""

        return "input is filled into a board"

    def main(self):
        """Main method to start playing a game."""
        counter = 0
        while counter <= 8:
            input_value = input("Enter X or O to play a tic tac toe game: ")
            if input_value.lower() not in ("x", "o"):
                print("Input value is wrong, please enter X or O to play a game")
                continue  # Continue to ask for input from user
            index = input("Enter index where you want to put your input: ")
            value = self.play(input_value, index)
            counter += 1
            print("counter is :: ", counter)
            print("Entered value is:", value)

        print("Game Over!")


if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.main()
