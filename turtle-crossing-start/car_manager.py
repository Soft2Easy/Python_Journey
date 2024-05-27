from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 100


class CarManager:
    def __init__(self):
        self.speed_ = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def generate_cars(self):
        car_ = Turtle('square')
        car_.shapesize(stretch_len=1.5)
        car_.color(random.choice(COLORS))
        car_.penup()
        y_pos_ = random.randint(-250, 250)
        car_.goto(250, y_pos_)
        self.all_cars.append(car_)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed_)

    def accelerate_(self):
        self.speed_ += MOVE_INCREMENT
