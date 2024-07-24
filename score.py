from turtle import Turtle
import random

colors = ['red', 'sky blue', 'aquamarine', 'white', 'violet']


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color(random.choice(colors))
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()

    def inc_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align='center', font=('Arial', 20, 'normal'))

    def resets(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update()
