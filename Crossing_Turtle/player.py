STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def Level_Up(self):
        if self.ycor()>FINISH_LINE_Y:
            self.setposition(STARTING_POSITION)
            return True

