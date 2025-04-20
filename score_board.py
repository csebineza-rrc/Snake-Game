"""This module defines the ScoreBoard class."""

__author__ = "Cedrick S"
__version__ = "4.4.2025"

from turtle import Turtle

class ScoreBoard(Turtle):
    """Represents the ScoreBoard class which is going to display
    the scores of the user.
    """

    def __init__(self):
        """Initializes a new instance of the ScoreBoard class."""

        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 30, "bold"))
        self.hideturtle()

    def update_scoreboard(self):
        """Updates the score when the snake has collided with the food."""

        self.write(f"Score: {self.score}", align="center", font=("Arial", 30, "bold"))

    def increase_score(self):
        """Increases the score whenever the snake collides with the food."""

        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 30, "bold"))
        self.update_scoreboard()
    