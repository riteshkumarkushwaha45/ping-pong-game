from turtle import *
from paddle import *
from ball import *
from score import *
import time

screen=Screen()
screen.setup(800,600)
screen.title("PING PONG")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Score()

screen.onkeypress(fun=r_paddle.go_up,key="Up")
screen.onkeypress(fun=r_paddle.go_down,key="Down")
screen.onkeypress(fun=l_paddle.go_up,key="w")
screen.onkeypress(fun=l_paddle.go_down,key="s")

is_game_on=True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>=290 or ball.ycor()<=-290:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>400:
        score.inc_score_l()
        ball.reset_pos()
        ball.move_speed*=0.9
    if ball.xcor()<-400:
        score.inc_score_r()
        ball.reset_pos()
        ball.move_speed*=0.9


screen.exitonclick()