from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def forwards():
    tim.forward(15)


def backwards():
    tim.backward(15)


def counter_clock():
    tim.left(15)


def clockwise():
    tim.right(15)


def clear_all():
    tim.clear()
    tim.penup()
    tim.home()


screen.onkey(fun=forwards, key='w')
screen.onkey(fun=backwards, key='s')
screen.onkey(fun=counter_clock, key='a')
screen.onkey(fun= clockwise, key='d')
screen.onkey(fun=clear_all, key='c')
screen.exitonclick()
