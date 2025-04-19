"""
Description: A program that creates the infamous snake game.
"""

__author__ = "Cedrick S"
__version__ = "2.2.2025"

from turtle import Screen
from snake import Snake
from snake_food import Food
import time

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("cyan")
screen.title("Snake Game")

# Creating the snake and food object
snake = Snake()
food = Food()

# Event listeners for controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    snake.move() # Moving the snake using the snake object
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("non nom nom")

screen.exitonclick()
