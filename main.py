"""
Description: A program that creates the infamous snake game.
"""

__author__ = "Cedrick S"
__version__ = "2.2.2025"

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("cyan")
screen.title("Snake Game")


positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in positions:
    segment = Turtle("square")
    segment.color("green")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    
    # Move segments from tail to head
    for seg_num in range(len(segments) - 1, 0, - 1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    
    # Move the head forward
    segments[0].forward(20)
    # segments[0].left(90)  # Rotates the head by 90 degrees

