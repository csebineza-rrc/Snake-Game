"This module defines the Food class."

__author__ = "Cedrick S"
__version__ = "2.2.2025"

from turtle import Turtle
import random

class Food (Turtle):
    """Represents the Food class."""

    def __init__(self):
        """
        Initializes a new instance of the Food class.
        """

        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("black")
        self.speed("fastest")
        random_x = random.randint(-670, 670)
        random_y = random.randint(-670, 670)
        self.goto(random_x, random_y)
