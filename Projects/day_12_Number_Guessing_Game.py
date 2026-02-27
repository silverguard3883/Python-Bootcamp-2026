import random

print("Welcome to the number guessing game!")

difficulty = input("Choose a difficulty: easy or hard ").lower()
player_attempts = 0

if difficulty == "easy":
    player_attempts = 10
elif difficulty == "hard":
    player_attempts = 5
else:
    print("Invalid input. Game over!")
    player_attempts = 0

correct_number = random.randint(1, 100)


def compare_numbers(player_guess):
    global player_attempts                                                                  #Calls global variable set above (can not see it while inside function)
    if player_guess > correct_number:
        print("Too high!")
        return player_attempts - 1
    elif player_guess < correct_number:
        print("Too low!")
        return player_attempts -1
    else:
        print(f"The correct number was {correct_number}! You win!")
        return 0

while player_attempts > 0:
    player_guess = int(input("Guess a whole number: "))
    player_attempts = compare_numbers(player_guess)                                         #Checks player's guess for correctness and victory condition
    if player_attempts == 0 and player_guess != correct_number:
        print(f"You've run out of guesses! The correct number was {correct_number}!")
    
        

    