# W = forwards
# S = Backwards
# A = Counter-Clockwise
# D = Clockwise
# C = Clear
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_clockwise():
    tim.right(10)


def turn_anticlockwise():
    tim.left(10)


def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(key="d", fun=move_forward)
screen.onkey(key="a", fun=move_backward)
screen.onkey(key="w", fun=turn_clockwise)
screen.onkey(key="s", fun=turn_anticlockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()

