#Scope: local vs. global

#This is a global variable
counter = 1

def increase_counter():
    
# """This is a local variable"""
# """It exists ONLY within the function"""
    counter = 2
    print(f"Counter = {counter}")
    
increase_counter()
print(f"Counter = {counter}")



# Modifying global scope

def increase_count():
    
    #This does not work 
    counter += 1
    
    #The "global" keyword allows you to modify a global variable with local scope. Generally not a good idea
    #global counter += 1
    
    #This also does the same thing
    return counter + 1
    

print(increase_counter())



#Global constants

#Variables that (usually) never change
#Standard practice it to uppercase the variable

PI = 3.14159






















