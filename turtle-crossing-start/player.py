from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.player_()
        self.player_speed = STARTING_POSITION

    def player_(self):
        self.color('Black')
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def attack(self):
        self.forward(MOVE_DISTANCE)
        self.check_pos()

    def check_pos(self):
        if self.ycor() > 280:
            self.goto(STARTING_POSITION)



