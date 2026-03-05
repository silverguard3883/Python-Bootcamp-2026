"""
#Object oriented programming

#Breaks specific tasks into subcomponents, called CLASS

#OOP is based off real-world models
Use a restauraunt for example. A restaurant has a chef, waiter, and host, with a manager overSEEing them.
Each subcomponent (chef, waiter, host) has 2 characteristics:
    -Something it HAS, called an *attribute*
    -Somthing it DOES, called a *method*
    
    
Using the waiter as an example:
    A waiter HAS these ATTRIBUTES:
        is_holding_a_plate = True
        tables_responsible = [4,5,6]
        
    A waiter DOES these METHODS:
        def take_customer_order(table, order)
            #takes order to chef
        
        def take_customer_payment(amount)
            #adds money to restaurant
            
A CLASS is a blueprint for an object. If multiple objects have the same attributes and methods, they belong to the same CLASS

Classes are declared using "Pascal Case" --> object = ThisIsTheObjectsClassInPascalCase


import turtle

tim_the_turtle = turtle.Turtle()    #This line declares a variable and assigns it the Turtle class from the turtle module
                                    #variable = module.Class()
                                    
                                    
from turtle import Turtle           #This line imports ONLY the Turtle class from the turtle module

classy_timmy = Turtle()             #This line declares a variable and assigns it the class we imported from the above module


print(tim_the_turtle)
print(classy_timmy)



#car_speed = car.speed              #This line declares a variable, then assigns the "speed" attribute from the "car" object
#car_stop = car.stop()             #This line declares a variable, then assigns the "stop" method from the "car" object

from turtle import Turtle, Screen
tim = Turtle()
print(tim)
tim.shape("turtle")
tim.color("purple")
tim.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
"""

from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("fieldname", ["item1", "item2", "item3"])
table.add_column("fieldname2", ["item1", "item2", "item3"])
table.align = "l"









