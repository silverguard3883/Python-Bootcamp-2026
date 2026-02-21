#Conditionals

#if statement compares a case as "true" or "false"
print("Welcome to the rollercoaster!")
height = int(input("What is your height in inches? "))

if height > 60:
    print("You may ride the rollercoaster") #Indenting the lines of code creates a block of code
else:
    print("You are too small to ride this ride :(")

#"==" indicates an exact condition must be met for the if statement to be true   
number = int(input("Input the number 120: "))
if number == 120:
    print("Good job!")
else:
    print("Bruh...")

#Modulo (%) returns the remainder of a division operation
#Useful for checking if number is odd or even
number_to_check = int(input("Input a number: "))

odd_or_even = number_to_check % 2

if odd_or_even == 0:
    print(f"{number_to_check} is even")
else:
    print(f"{number_to_check} is odd")
    
    
 
#Nested if-else statements check boolean logic of multiple conditions

print("Welcome to the rollercoaster!")
height = int(input("What is your height in inches? "))
total_price = 0

if height > 60:
    print("You may ride the rollercoaster") #Indenting the lines of code creates a block of code
    age = int(input("Please enter your age: "))
    if age <= 12:
        print("Please pay $5")
        total_price = 5
    elif age >= 18:
        print("Please pay $15")
        total_price = 15
    else:
        print("Please pay $10")
        total_price = 10
    
    wants_photo_taken = input("Do you want a photo taken? Type 'Y' for yes, 'N' for no: ")
    if wants_photo_taken == "Y":
        print("Please pay $3")
        total_price += 3 #Adds 3 to total price
    
    print(f"Your total is ${total_price}")
else:
    print("You are too small to ride this ride :(")



#Logical operators
print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)













    
    