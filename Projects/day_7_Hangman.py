#Hangman
import random

word_list = ["house", "monkey", "racecar", "sympathy"] #Sample word list for testing
guessed_letters = [] #List of letters to track which letters have already been guessed
game_over = False #Exit condition to indicate the game is over
hangman_health = 5

random_word = random.choice(word_list).lower() #Selects a random word for the player to guess
blank_display = "_" #Blank string for user readability


#This loop displays the length of the random word as blank lines for user readability
for letter in range(1, len(random_word)):
    blank_display += " _"
print(blank_display)


#Game loop to run until the user wins or loses the game
while game_over is False:
    
    #Ask user for input
    player_guess = input("Guess a letter in the word: ").lower()
    
    """
    Creates empty string that will be filled in as the player guesses words. Needs to be inside
    the while loop in order to reset as the missing letters are filled in by correct guesses
    """
    player_guess_display = ""
    
    """
    Checks if player has a guessed a word they've already guessed. PLACEMENT WAS IMPORTANT!!!
    Needed to place this check early in the loop so that their first guess at the start of the game would
    not be counted and penalized. If placed lower, the check would pass and penalize the player.
    Placing it early essentially "skips" the player's first guess, regardless of whether or not it'skips
    part of the word
    """
    if player_guess in guessed_letters:
        hangman_health -= 1
        print(f"You have already guessed {player_guess}. {hangman_health} guesses remaining")
    
    
    #Loop for user interface
    for letter in random_word:                                      #Iterates through the random unknown word with "letter" as the indexer
        if player_guess == letter:                                  #Checks if the player's guess is in the unknown word
            player_guess_display += letter                          #Replaces blank space ("_") with the corresponding letter of the unknown word
            guessed_letters += letter                               #Adds guessed word to list of letters already guessed
        elif letter in guessed_letters:                             #Checks if a previously guessed letter is correct
            player_guess_display += letter                          #Replaces blank space with the corresponding letter. This prevents the user interface from "forgetting" the correctly guessed letters in the word 
        else:
            player_guess_display += " _"                            #Keeps incorrect and unguessed letter spaces as blank
    print(player_guess_display)                                     #Displays all correct letters and blank spaces left in the unknown word
    
    
    #Loop for checking if the player guessed incorrectly
    if player_guess not in random_word:                             #Checks if the guessed letter is not in the unknown word
        guessed_letters += player_guess                             #Adds guessed word to list of letters already guessed
        hangman_health -= 1                                         #Decrements the number of guesses available to a player by 1
        print(f"Incorrect! {hangman_health} guesses remaining")     #Gives the player feedback on their progress
        
        if hangman_health == 0:                                     #Checks if the number of guesses available to the player is 0
            print("You lose!")                                      #Gives the player feedback on their progress
            game_over = True                                        #Switches the exit condition for the game (while) loop to True and ends the game loop
    
    #Loop for checking player victory        
    if " _" not in player_guess_display:                            #Checks if any blank spaces exist in the user interface
        print("You win!")                                           #Gives the player feedback on their progress
        game_over = True                                            #Switches the exit condition for the game (while) loop to True and ends the game loop
                                       
    







