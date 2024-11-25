import turtle as t
from random import choice

color_list = [(239, 254, 244), (254, 239, 250), (88, 253, 166), (42, 18, 177), (213, 237, 90), (250, 139, 85),
              (108, 148, 250), (244, 110, 206), (236, 245, 254), (167, 1, 143), (160, 14, 1), (117, 82, 248),
              (4, 212, 97), (3, 139, 62), (251, 67, 36), (235, 38, 138), (9, 107, 195), (183, 182, 252),
              (208, 104, 6), (35, 34, 252), (45, 242, 51), (191, 31, 151), (96, 248, 252), (6, 209, 215),
              (237, 157, 215), (30, 28, 108), (107, 6, 65), (109, 18, 5), (243, 168, 155)]


def paint_row(num):
    for _ in range(num):
        timmy.pendown()
        color = choice(color_list)
        timmy.dot(20, color)
        timmy.penup()
        timmy.forward(50)


timmy = t.Turtle()
t.colormode(255)
timmy.penup()
x = -250
y = -250
timmy.goto(x, y)
for _ in range(10):
    paint_row(10)
    y += 50
    timmy.goto(x, y)

screen = t.Screen()
screen.exitonclick()
