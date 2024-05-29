#Pong Game
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from pong_score import Scoreboard
caption = Turtle()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is__on = True

while game_is__on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        time.sleep(0.3)
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        time.sleep(0.3)
        score.r_point()
        
    if score.l_score >= 9 or score.r_score >= 9:
        game_is__on = False
        score.game_over()
        score.winner()




screen.exitonclick()
