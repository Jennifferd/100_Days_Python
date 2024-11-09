from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race, enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    y = -70 + turtle_index * 30
    new_turtle.goto(x=-230, y=y)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won, the {winning_color} turtle is the winner")
            else:
                print(f"You've lost, the {winning_color} turtle is the winner")
            is_race_on = 0
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        turtle.position()


screen.exitonclick()
