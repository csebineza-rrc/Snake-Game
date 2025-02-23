"""
Description: A program that creates the infamous snake game.
"""

__author__ = "Cedrick S"
__version__ = "2.2.2025"

from turtle import Screen, Turtle

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
    segments.append(position)


game_is_on = True
while game_is_on:
    for seg in segment:
        seg.forward(20)

