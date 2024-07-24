from turtle import Screen

import _tkinter

from snake import Snake
from food import food
from score import scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('SNAKE GAME')
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()
food = food()
scoreboard = scoreboard()
snake.create_snake()

screen.listen()
screen.onkey(fun=snake.up, key='w')
screen.onkey(fun=snake.down, key='s')
screen.onkey(fun=snake.left, key='a')
screen.onkey(fun=snake.right, key='d')

game_is_on = True

try:
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 13:
            food.refresh()
            snake.extend()
            scoreboard.inc_score()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            snake.resets()
            scoreboard.resets()

        for segments in snake.segments[1:]:
            if snake.head.distance(segments) < 5:
                snake.resets()
                scoreboard.resets()

    screen.exitonclick()

except _tkinter.TclError:
    pass