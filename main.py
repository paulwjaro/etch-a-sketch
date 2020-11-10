from turtle import Turtle, Screen

etch = Turtle()
screen = Screen()


def move_forward():
    etch.forward(10)


def move_backward():
    etch.backward(10)


def turn_clockwise():
    etch.right(10)


def turn_counterclockwise():
    etch.left(10)


def clear_screen():
    screen.reset()


def quit_game():
    screen.bye()


screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="q", fun=quit_game)
screen.onkey(key="c", fun=clear_screen)

screen.listen()
screen.mainloop()
