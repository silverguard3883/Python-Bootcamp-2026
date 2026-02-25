quit_program = False
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
 'y', 'z']

def encipher(text, caesar_shift_amount, blank_label):
    output_text = ""                                                                #Creates empty string variable to add enciphered letters to

    for current_letter in text:                                                     #Iterates through the text to be enciphered one letter at a time
        if current_letter in letters:                                               #Checks that the plaintext input is a letter (handles unexpected input, like numbers or symbols)
            caesar_cipher = letters.index(current_letter) + caesar_shift_amount     #Finds the index of the letter in plaintext in the alphabet (a=0, b=1, etc.), shifts the index by the shift amount, then returns the letter at the shifted index
            caesar_cipher %= len(letters)                                           #Ensures text wraps around when position exceeds the length of the letters list
            output_text += letters[caesar_cipher]                                   #Adds the letter at the shifted index to the blank output text string
        else:
            output_text += currentletter                                            #If a character in the plaintext is not a letter, the function effectively ignores it by adding it to the empty output string
    print(f"{blank_label}: {output_text}")                                          #Formats the final output when the function is used


def encrypt(plaintext, caesar_shift_amount):                                
    encipher(plaintext, caesar_shift_amount, "Encrypted text: ")
    
def decrypt(ciphertext, caesar_shift_amount):
    encipher(ciphertext, -caesar_shift_amount, "Decrypted text: ")                  #The "-" before the caesar_shift_amount allows the shift to occur the opposite way without modifying the entire encipher function

def brute_force(bruteforce):
    for shift in range(len(letters)):                                               #Iterates through the entire list of letters
        encipher(ciphertext, -shift, f"Attempt {shift}")
    
    

while quit_program is False:
    user_choice = input("Type 'encrypt' to encrypt a message, type 'decrypt' to decrypt, or type 'brute force', to try all possible decryptions. Type 'quit' to exit the program: ").lower()
    
    if user_choice == "encrypt":
        plaintext = input("Type the text you want to encode: ").lower()
        caesar_shift_amount = int(input("What is the shift amount? "))
        encrypt(plaintext, caesar_shift_amount)
        
    elif user_choice == "decrypt":
        ciphertext = input("Type the text you want to decode: ").lower()
        caesar_shift_amount = int(input("What is the shift amount? "))
        decrypt(ciphertext, caesar_shift_amount)

    elif user_choice == "brute force":
        ciphertext = input("Type the text you want to decode: ").lower()
        brute_force(ciphertext)
    
    elif user_choice == "quit":
        quit_program = True
    
    else:
        print("Invalid input.")
























