from turtle import Turtle

X_COR = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()  # when you call the snake class, it should have 3 squares
        self.head = self.squares[0]

    def create_snake(self):
        """Returns a snake"""
        for cor in X_COR:
            self.add_segment(cor)

    def add_segment(self, cor):
        new_square = Turtle(shape="square")
        new_square.color("green")
        new_square.penup()
        new_square.goto(cor)
        self.squares.append(new_square)

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def extend(self):
        self.add_segment(self.squares[-1].position())

    def move(self):
        """Helps the snake move in a joint body"""
        for num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[num - 1].xcor()
            new_y = self.squares[num - 1].ycor()
            self.squares[num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
