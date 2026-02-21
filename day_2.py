#Subscripting
print("Hello"[0]) #The "0" denotes the position in the string to print.
                  #The position is called the "index"
                  

#Strings are characters, usually in quotations
print("Hello " + "123" + "456")

#Integers are whole numbers
print(123)
print(123+456) #print will perform mathematical functions on Integers

#Large integers are denoted with underscore "_" instead of commas
print(123,456,789)
print(123_456_789)

#Float data types are decimal numbers
print(3.14159)

#Boolean data types are "true" or "false"
print(True)

#"type" function checks data type of input
print(type(1234))

#"int" function converts a string to an integer
print(int("123"))

#"str" function converts an integer into a string
print(str(123))

#Mathetical functions
print(5+10)
print(10-5)
print(5*10)
print(10/5) #A single slash performs "implicit typecasting" and converts the output to float
print(10//5)#A double slash divides the numbers and keeps the output as an integer
print(10**5)

#PEMDAS in descending order. In Python, PEMDAS is performed left to right
# ()
# **
# * OR /
# + OR -

print(5 * 5 + 5 / 5 - 5)
print(5 / 5 - 5 * 5 + 5)

#"round" function rounds float numbers up or down. You can also specify how many places to round to
print(round(5.25))
print(round(5.98))
print(round(5.987654, 3))
print(round(5.987654321, 6))

#"+=" allows you to add a number to a variable without needing to redefine the variable
score = 0
print(score)
score += 5
print(score)


#f-strings allows for mixed data types to be printed in a single string
#f-strings use the letter "f" before the quotations
#f-strings use curly brackets "{}" to invoke mixed data type variables
integer = 5
float_number = 5.0
is_5 = True

print(f"The integer is {integer}, the float number is {float_number}, and the boolean value is {is_5}")

print(6+4/2-(1*2))





