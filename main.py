from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.reset_food()
        score_board.increase_score()
        snake.extend()
    # detect collision with wall
    if snake.head.xcor() < -295 or snake.head.xcor() > 295 or snake.head.ycor() > 270 or snake.head.ycor() < -295:
        score_board.reset()
        snake.reset()

    # detect collision with tail
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            is_game_on = False
            score_board.reset()
            snake.reset()

screen.exitonclick()
