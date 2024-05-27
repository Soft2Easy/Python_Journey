from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_code, y_code):
        super().__init__()
        self.shape('square')
        self.create_paddle_(x_code, y_code)
        self.x_pos = x_code
        self.y_pos = y_code

    def create_paddle_(self, x_cod, y_cod):
        self.color('White')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cod, y_cod)

    def go_up(self):
        new_y = self.ycor() + 20
        self.create_paddle_(self.x_pos, new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.create_paddle_(self.x_pos, new_y)


