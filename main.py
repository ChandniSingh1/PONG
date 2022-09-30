from turtle import Screen, Turtle
from Paddle import Paddle
from Ball import Ball
import time
from scoreboard import Score
positions = [(-450,0), (450,0)]

# screen set-up
screen = Screen()
screen.screensize(600,800, "Black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((positions[0]))
right_paddle = Paddle((positions[1]))
ball = Ball()
score = Score()

screen.onkeypress(left_paddle.up, "Up")
screen.onkeypress(left_paddle.down, "Down")
screen.onkeypress(right_paddle.up, "w")
screen.onkeypress(right_paddle.down, "s")
screen.listen()

# update screen loop
game = True
while game:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.keep_going()
    if ball.ycor() > 350 or ball.ycor() < -350:
        ball.bounce()
    elif ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce2()
    elif ball.xcor() > 450:
        score.l_point()
        ball.ball_reset()
    elif ball.xcor() < -450:
        score.r_point()
        ball.ball_reset()






screen.exitonclick()

