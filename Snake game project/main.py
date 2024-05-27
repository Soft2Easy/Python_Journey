from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Python Chronicles')
screen.tracer(0)

python = Snake()
food_ = Food()
scoreboard_ = ScoreBoard()

screen.listen()
screen.onkey(python.up_, 'Up')
screen.onkey(python.down_, 'Down')
screen.onkey(python.left_, 'Left')
screen.onkey(python.right_, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    python.move_()

    # Detect collision with Food
    if python.head.distance(food_) < 15:
        food_.refresh_()
        python.extend()
        scoreboard_.score_counter()

    # Detect Collision with the wall
    if python.head.xcor() > 280 or python.head.xcor() < -280 or python.head.ycor() > 280 or python.head.ycor() < -280:
        scoreboard_.reset()
        python.reset()

    # Detect collision with tail
    for seg_ in python.build_up[1:]:
        if seg_ == python.head:
            pass
        elif python.head.distance(seg_) < 10:

            scoreboard_.reset()
            python.reset()

screen.exitonclick()
