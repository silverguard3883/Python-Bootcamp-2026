"""Errors and Exceptions"""

"""

try:
    Something that might cause an exception

except:
    Do something if there WAS and exception

else:
    Do this if there were no exceptions

finally:
    Do this no matter what happens

"""

#file not found
try:
    file = open("a.txt")
except:
    file = open("a.txt", "w")
    file.write("There was a \"file not found\" error")
    print("There was an error")

#Specifying errors
# try:
#     file = open("a.txt")
#     dict = {"key": "value"}
#     print(dict["jbhdcvbuidb"])
# except FileNotFoundError:
#     file = open("a.txt", "w")
#     file.write("There was a \"file not found\" error")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error I defined")

height = float(input("Please enter your height in inches: "))
weight = float(input("Please enter your weight in pounds: "))

if height > 100:

    """This is a custom made error named ValueError that the programmer made for this specific use case"""
    raise ValueError("Your height is too high")

bmi = weight / (height ** 2)
print("Your BMI is", bmi)



