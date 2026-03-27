import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S State Quiz")
screen.addshape("blank_states_img.gif")
map = turtle.Turtle()
map.shape("blank_states_img.gif")


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()                           #Have to turn the .csv into a list to make it iterable
guessed_states = []

while len(guessed_states) < len(all_states):
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States correct. Guess a state",
                                   prompt="Input a U.S state").title()
    print(user_answer)

    if user_answer == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        missed_states = data[~data.state.isin(guessed_states)][["state", "x", "y"]]
        missed_states.to_csv("missed_states.csv", index=False)
        break

    if user_answer in all_states:
        guessed_states.append(user_answer)
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_data = data[data.state == user_answer]                #Gets the row of data where the index (state name) matches the user's guess
        state_name.goto(state_data.x.item(), state_data.y.item())
        state_name.write(state_data.state.item())



