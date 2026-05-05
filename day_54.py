from flask import Flask
app = Flask(__name__)

"""
Flask is a FRAMEWORK; like a library, but has its own rules that MUST be followed
"""

print(__name__)

"""Homepage for URL used by Flask (https://127.0.0.1:5000/)"""
@app.route('/')

def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)

"""Functions can have inputs/functionalities/output"""

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

"""First-class objects can be passed as args (int/string/float, etc. """

def calculate(calc_function, a, b):
    return calc_function(a, b)

result = calculate(add, 2, 3)
print(result)

result = calculate(sub, 2, 3)
print(result)
result = calculate(mul, 2, 3)
print(result)
result = calculate(div, 2, 3)
print(result)

"""Nested functions"""

# def outer_function():
#     print("I'm outer function")
#
#     def nested_function():
#         print("I'm nested function")
#     nested_function()
# outer_function()

"""Functions can be returned from other functions"""
def outer_function():
    print("I'm outer function")

    def nested_function():
        print("I'm nested function")
    return nested_function

inner_function = outer_function()
inner_function()


"""Python decorators"""
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("Greeting")

decorated_function = delay_decorator(say_hello)
decorated_function()