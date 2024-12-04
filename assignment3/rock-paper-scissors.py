#ASSIGNMENT 3

import random

def display_instructions():
    # print welcome message and menu
    print("\nWelcome to Rock Paper Scissors game:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

def get_player_choice():
    # prompt user to make a choice
    player_choice = int(input("Enter a choice: "))
    return player_choice

def get_computer_choice():
    # return computer choice (random number between 1 and 3)
    computer_choice = random.randrange(1, 4)
    print("Computer choice: ", computer_choice)
    return computer_choice

def display_winner(player_choice, computer_choice):
# determine the winner
    if player_choice == 1:  # rock
        if computer_choice == 1:
            return print("Draw")
        if computer_choice == 2:
            return print("Computer Wins!")
        if computer_choice == 3:
            return print("Player Wins!")

    if player_choice == 2:  # paper
        if computer_choice == 1:
            return print("Player Wins!")
        if computer_choice == 2:
            return print("Draw")
        if computer_choice == 3:
            return print("Computer Wins!")

    if player_choice == 3:  # scissors
        if computer_choice == 1:
            return print("Computer Wins!")
        if computer_choice == 2:
            return print("Player Wins!")
        if computer_choice == 3:
            return print("Draw!")

def Main():
    display_instructions()
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    display_winner(player_choice, computer_choice)

rematch = 'y'

while rematch != 'n':
    Main()
    rematch = input("\nDo you want to play again? (y/n) ")

print("\nThank you for playing Rock Paper Scissors game!")