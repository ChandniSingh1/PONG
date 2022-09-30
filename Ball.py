from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.movement_speed = 0.1

    def keep_going(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1
        self.movement_speed *= 0.9

    def bounce2(self):
        self.x_move *= -1
        self.movement_speed *= 0.9

    def ball_reset(self):
        self.goto(0,0)
        self.movement_speed = 0.1
        self.bounce2()





