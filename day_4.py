import random #Imports the "random" module into code
import day_4_module #Imports a custom module I create (for demo/testing purposes)

random_number = random.randint(1, 10) #Generates random number between 1 - 10
print(random_number)

print(day_4_module.my_number) #Calls custom module and specifies a variable to use


random_number_0_to_1 = random.random() #Calls the random function from the random module (same name, different things) to generate a float number between 0 and 1
random_number_1_to_10 = random.random() * 10
print(random_number_0_to_1)
print(random_number_1_to_10)

random_float_number = random.uniform(1, 10)

#Coin Flip

coin_flip = random.randint(0,1)
if coin_flip == 1:
    print("Heads")
else:
    print("Tails")
    
    
    
#Lists
#Lists are data structures that stores data for parsing

"""
list = [item1, item2] #Lists use square brackets []
"""

states_in_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado"]
print(states_in_america) #Print entire list
print(states_in_america[2]) #Print 3rd item (2nd index) in list

states_in_america[5] = "Washington" #Overwrites 6th item (5th index) in the list
print(states_in_america)

states_in_america.append("Delaware") #Adds item to end of list
states_in_america.extend(["Montana", "Texas"]) #Adds a list or other iterable structure to the list

print(states_in_america)


#Pick a random name from a list of names

names = ["Alice", "Bob", "Charlie", "David", "Ethan", "Fiona", "Georgia"]

print(random.choice(names)) #Choose an index at random from a list

#List of Lists

meat = ["chicken", "beef"]
veggies = ["broccoli", "green beans", "salad"]
carbs = ["rice", "potatoes", "bread"]

groceries = [meat, veggies, carbs]

print(groceries) #Print list of list
print(groceries[0]) #Print specific list in list
print(groceries[0][0]) #Print 1st item (0th index) in list within a list







