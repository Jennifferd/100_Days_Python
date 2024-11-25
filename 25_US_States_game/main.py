import turtle
import pandas
from states import States

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
all_x = data.x.to_list()
all_y = data.y.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = States()

answer_state = screen.textinput(title="Guess the State", prompt="What is a state name?").title()

guessed_states = []
while states.score < 50:
    if answer_state == "Exit":
        break
    if answer_state in all_states and answer_state not in guessed_states:
        index_state = all_states.index(answer_state)
        states.write_state(answer_state, all_x[index_state], all_y[index_state])
        states.increase_score()
        guessed_states.append(answer_state)

    answer_state = screen.textinput(title=f"{states.score}/50 States Correct", prompt="What is another state name?").title()

states_to_learn = [state for state in all_states if state not in guessed_states]
df_to_learn = pandas.DataFrame({"State": states_to_learn})
df_to_learn.to_csv("./states_to_learn.csv")
print(df_to_learn)
