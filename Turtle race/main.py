import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
color_ = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
pos_ = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for tut_ in range(0, 6):
    new_tut = Turtle(shape='turtle')
    new_tut.color(color_[tut_])
    new_tut.penup()
    new_tut.goto(x=-230, y=pos_[tut_])
    all_turtles.append(new_tut)

if user_bet:
    is_race_on = True

while is_race_on:

    for tutle in all_turtles:

        if tutle.xcor() > 230:
            winning_color = tutle.pencolor()
            if winning_color == user_bet:
                print(f'You have won! The {winning_color} turtle is the winner!')
                is_race_on = False
            else:
                print(f'You have lost! The {winning_color} turtle is the winner!')
                is_race_on = False



        rand_dist = random.randint(0, 10)
        tutle.forward(rand_dist)


screen.exitonclick()
