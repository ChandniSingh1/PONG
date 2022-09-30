from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, cordinate):
        super().__init__()
        self.penup()
        self.color("White")
        self.setx(-450)
        self.shape("square")
        self.shapesize(stretch_wid=None, stretch_len=5, outline=None)
        self.setheading(90)
        self.goto(cordinate)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
