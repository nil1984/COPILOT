# Create a simple rock-paper-scissors game
# provide a welcome message
# prompt the user to enter a choice
# generate a random choice for the computer
# compare the user's choice with the computer's choice
# display the result
# ask the user if they want to play again
# if yes, repeat the process
# if no, display a goodbye message
# use one function for the game logic
# use another function for the main game loop
# use a third function to display the result
# use a fourth function to ask the user if they want to play again
# use a fifth function to display a goodbye message

import random

def game():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = input("Enter rock, paper, or scissors: ")
        computer_choice = random.choice(["rock", "paper", "scissors"])
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif user_choice == "rock":
            result = "You win!" if computer_choice == "scissors" else "You lose!"
        elif user_choice == "paper":
            result = "You win!" if computer_choice == "rock" else "You lose!"
        elif user_choice == "scissors":
            result = "You win!" if computer_choice == "paper" else "You lose!"
        display_result(user_choice, computer_choice, result)
        if not play_again():
            break
    print("Goodbye!")
    
def display_result(user_choice, computer_choice, result):
    print(f"You chose {user_choice}. The computer chose {computer_choice}. {result}")
    
def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == "yes"


game()

# Output:
# Welcome to Rock-Paper-Scissors!
# Enter rock, paper, or scissors: rock
# You chose rock. The computer chose scissors. You win!
# Do you want to play again? (yes/no): yes
# Enter rock, paper, or scissors: paper
# You chose paper. The computer chose rock. You win!
# Do you want to play again? (yes/no): yes
# Enter rock, paper, or scissors: scissors
# You chose scissors. The computer chose rock. You lose!
# Do you want to play again? (yes/no): no

# Goodbye!


    
    