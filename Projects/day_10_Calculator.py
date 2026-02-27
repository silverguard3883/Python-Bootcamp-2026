"""Simple math functions that accept 2 numbers"""

def add(n1, n2):
    return n1 + n2
    
def subtract(n1, n2):
    return n1 - n2
    
def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2



"""Dictionary of math operations. **IMPORTANT NOTE** Do not include "()" in the values,
as doing so will cause the function to run without input, instead of waiting to be called
"""
math_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

"""Declared variable to be used in the loop"""

n1 = 0
n2 = 0
continue_calculations = ""


"""Calculator math loop"""
while continue_calculations != "quit":                          #Exit condition
    if n1 == 0:                                                 #Checks if the calculator has been run before and sets appropriate values
        n1 = float(input("What's the first number? "))
    else:
        print(f"The first number is {result}")
        
    print("+\n-\n*\n/")
    
    operation = input("Pick an operation: ")                    #Operation input corresponds to keys in dictionary
    
    n2 = float(input("What's the second number? "))
    
    result = math_operations[operation](n1, n2)                 #Calls on dictionary keys and performs the corresponding math operation on the numbers, using n1 and n2 as input
    
    print(f"{n1} {operation} {n2} = {result}")
    
    continue_calculations = input(f"Type 'y' to continue calculating {result}, type 'n' to start a new calculation, or type 'quit' to exit the program")
    
    if continue_calculations == "y":                            #Checks for further input of if exit condition is met
        n1 = result                                             #Checks if user wants to run further operations on the result they got
    elif continue_calculations == "n":                          #Resets the calculator
        n1 = 0
