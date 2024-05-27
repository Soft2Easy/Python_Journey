from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.build_up = []
        self.create_snake()
        self.head = self.build_up[0]

    def create_snake(self):

        for pos_ in STARTING_POSITIONS:
            self.add_segment(pos_)

    def add_segment(self,pos_):
        snake_ = Turtle('square')
        snake_.color('white')
        snake_.penup()
        snake_.goto(pos_)
        self.build_up.append(snake_)

    def reset(self):
        for snake in self.build_up:
            snake.goto(1000, 1000)
        self.build_up.clear()
        self.create_snake()
        self.head = self.build_up[0]

    def extend(self):
        self.add_segment(self.build_up[-1].position())

    def move_(self):

        for snake_num in range(len(self.build_up) - 1, 0, -1):
            x_cod = self.build_up[snake_num - 1].xcor()
            y_cod = self.build_up[snake_num - 1].ycor()
            self.build_up[snake_num].goto(x_cod, y_cod)
        self.build_up[0].forward(MOVING_DISTANCE)

    def up_(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down_(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left_(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right_(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


