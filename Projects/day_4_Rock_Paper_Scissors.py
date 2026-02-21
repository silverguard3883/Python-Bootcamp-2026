import random

print("Welcome to Rock, Paper, Scissors!")
player_choice = input("Make your selection by typing in rock, paper, or scissors: ").lower()

rock_paper_scissors = ["rock", "paper", "scissors"]

computer_choice = random.choice(rock_paper_scissors)
print(computer_choice)

if player_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    elif computer_choice == "rock":
        print("You tied!")
    else:
        print("You lose!")

if player_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    elif computer_choice == "paper":
        print("You tied!")
    else:
        print("You lose!")
        
if player_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    elif computer_choice == "scissors":
        print("You tied!")
    else:
        print("You lose!")