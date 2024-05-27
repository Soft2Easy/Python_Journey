from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
# Tracer pauses the game updates
screen.tracer(0)

# Create a paddle
paddle_ = Paddle(-350, 0)
opponent_ = Paddle(350, 0)
ball_ = Ball()
scoreboard_ = ScoreBoard()

screen.listen()
screen.onkey(paddle_.go_up, 'Up')
screen.onkey(paddle_.go_down, 'Down')

screen.onkey(opponent_.go_up, 'W'.lower())
screen.onkey(opponent_.go_down, 'S'.lower())

# Update the game
game_on = True
while game_on:
    time.sleep(ball_.move_speed)
    screen.update()
    ball_.movement_()

    # Detect Collision with wall
    if ball_.ycor() > 280 or ball_.ycor() < -280:
        ball_.bounce_y()

    if ball_.distance(opponent_) < 50 and ball_.xcor() > 320 or ball_.distance(paddle_) < 50 and ball_.xcor() < -320:
        ball_.bounce_x()

    if ball_.xcor() > 360:
        ball_.ball_reposition()
        scoreboard_.l_point()
    if ball_.xcor() < -360:
        ball_.ball_reposition()
        scoreboard_.r_point()

screen.exitonclick()
