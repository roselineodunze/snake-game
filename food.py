import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.speed("fastest")
        self.reset_food()

    def reset_food(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 260)
        self.goto(random_x, random_y)
