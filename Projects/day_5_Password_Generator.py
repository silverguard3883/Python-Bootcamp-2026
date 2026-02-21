import random

print("Welcome to the Python Password Generator!\n")

# Letters
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

# Numbers
numbers = [
    '0','1','2','3','4','5','6','7','8','9'
]

# Symbols
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', ';', ':',
    "'", '"', ',', '.', '<', '>',
    '/', '?', '\\', '|', '`', '~'
]

password = [] #Creates empty list called "password"

letters_in_password = int(input("How many letters would you like in your password?: "))

for letter in range(1, letters_in_password + 1): #Checks entire list of "letters" using "letter" as the index and "letters_in_password + 1" as the maximum range
    random_letter = random.choice(letters)       #Randomly selects an index from the "letters" list
    #print(random_letter)                        #Used for debugging
    password.append(random_letter)               #Adds random letter selections to password list
    

symbols_in_password = int(input("How many symbols would you like in your password?: "))

for symbol in range(1, symbols_in_password + 1):
    random_symbol = random.choice(symbols)
    #print(random_symbol)
    password.append(random_symbol)

numbers_in_password = int(input("How many numbers would you like in your password?: "))

for number in range(1, numbers_in_password + 1):
    random_number = random.choice(numbers)
    #print(random_number)
    password.append(random_number)

random.shuffle(password)                         #"shuffle" function randomly reorders all items in list; in this case, it's randomizing the characters in the password list and assigning them to new indexes

random_password = ""                             #Creates a string called "random_password"

for password_character in password:              #Iterates through the (now randomized) "password" list using "password_character" as an index
    random_password += password_character        #Adds the item (character for the random password) found at the current index to the "random_password" string

print(f"You new password is: {random_password}")    








