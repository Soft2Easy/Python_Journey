import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('White')
screen.tracer(0)
car_port = []

player_ = Player()
car_ = CarManager()

screen.listen()
screen.onkey(player_.attack, 'Up')

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_.move_cars()
    if counter == 6:
        car_.generate_cars()
        counter = 0

    for cars in car_.all_cars:

        if cars.distance(player_) < 20:
            player_.goto(0, -280)
            game_is_on = False

    if player_.ycor() > 280:
        car_.accelerate_()
        player_.goto(0, -280)
    counter += 1
