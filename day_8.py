#Functions with Inputs

def greet():
    print("Hello")
    print("Nice to meet you")
    print("How are you?")
    
greet()     #Using the function is called "calling the function" in programming vernacular


#Below is a simple example of a function with a variable being passed into it
#An "argument" is the raw data being used in the function. In this case, whatever "something" is equal to
#A "paramater" is name of the raw data and is used by the function to refer to/call that data when an action is being performed with/on it

#def function(something):
    #Perform an action with "something"
    #Do another action
    #Do one more action


#Argument = whatever the user input as their name
#Parameter = the name of the argument for the function to refer to and do something with it

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Nice to meet you {name}")
    print(f"How are you {name}?")

name = input("What is your name? ")
greet_with_name(name)


#Functions with multiple Inputs
def greet_person_from_somewhere(name, location):
    print(f"Hello, {name}")
    print(f"How's the weather in {location}?")

#The display below shows "positional arguements"; the order of the inputs matters when parameters are not defined
greet_person_from_somewhere("Phoenix", "Zach")

#The display shows "keyword arguements"; the order of the arguements doesn't matter since each parameter is defined
greet_person_from_somewhere(location="Phoenix", name="Zach")










