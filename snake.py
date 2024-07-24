# import turtle
from turtle import Turtle
# import random

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
up = 90
down = 270
right = 0
left = 180
colors = ['red', 'sky blue', 'aquamarine', 'white', 'violet']


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # def random_color(self):
    #     r = random.randint(0, 255)
    #     g = random.randint(0, 255)
    #     b = random.randint(0, 255)
    #     color = (r, g, b)
    #     return color

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        # turtle.colormode(255)
        new_segment.color('aquamarine')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(10)

    def resets(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.setheading(up) != down:
            self.head.setheading(up)

    def down(self):
        if self.head.setheading(down) != up:
            self.head.setheading(down)

    def right(self):
        if self.head.setheading(right) != left:
            self.head.setheading(right)

    def left(self):
        if self.head.setheading(left) != right:
            self.head.setheading(left)