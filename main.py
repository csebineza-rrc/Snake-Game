"""
Description: A program that creates the infamous snake game.
"""

__author__ = "Cedrick S"
__version__ = "2.2.2025"

from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("cyan")
screen.title("Snake Game")

# Creating the snake object
snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)

    # Moving the snake using the snake object
    snake.move()

screen.exitonclick()
