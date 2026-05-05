from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route("/bye")
def bye():
    return "Bye!"

@app.route("/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/<name/<int:number>")
def greet(name, number):
    return f"Hello, {name}, you are {number} years old!"


@app.route("/<path:name>")      #Allows for / in URL path
def greet(name):
    return f"Hello, {name}!"


@app.route("/")
def greet(name):
    return ('<h1 style="color:blue">Hello, {name}!</h1>'
            '<p>This is a paragraph</p>')     #Flask allows in-line HTML styling

"""Using decorators to render HTML"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.is_logged_in = False

def is_user_logged_in(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])

@is_user_logged_in
def create_blog_post(user):
    print(f"This is {user.name}'s blog")

new_user = User("john")
new_user.is_logged_in = True
create_blog_post(new_user)

if __name__ == '__main__':
    app.run(debug=True)