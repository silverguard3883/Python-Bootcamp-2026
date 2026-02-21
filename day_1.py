###
print("Hello World\nHello World") #newline exercise
print("Hello" + " "+ "Zach") #string concatination exercise


print("Hello " + input("What is your name?") + "!") #Prompt a user for input on a single line of code

name = input("What is your name?") #Prompt user for input with a variable
print("Hello " + name)

print(len(name)) #Print length of string
print(len(input("What is your name?"))) #Prompt user for input and print the number of characters of the input


###Day 1 Project: Band Name Generator###

print("Welcome to the Band Name Gnerator!\n")
city = input("What is the name of the city your grew up in?\n")
pet = input("What kind of pet did you have as a child?\n")
print("Your band name could be the: " + city + " " + pet + "s")