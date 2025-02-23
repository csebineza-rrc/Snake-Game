"This module defines the Snake class."

__author__ = "Cedrick S"
__version__ = "1.1.2025"

from turtle import Screen, Turtle
import time


POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    """Represents the Snake class."""

    def __init__(self):
        """
        Initializes a new instance of the Snake class.
        """
        # Attributes
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """ 
        Creates the initial snake segments. This method will initialize 
        three-squared segments positions which are set in a straight line, and
        sets their shape color to green.
        """

        for position in POSITIONS:
            segment = Turtle("square")
            segment.color("green")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        """
        Creates the inititial starting point of how the snake should move and
        its direction.
        """

        # Move segments from tail to head
        for seg_num in range(len(self.segments) - 1, 0, - 1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Move the snake forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Moves the snake up, when the up key arrow is pressed.
        """

        self.head.setheading(90)

    def down(self):
        """
        Moves the snake to the downward position when the down arrow is 
        pressed.
        """

        self.head.setheading(270)

    def left(self):
        """
        Moves the snake to the left position.
        """

        self.head.setheading(180)

    def right(self):
        """
        Moves the snake to the right position when the downward key is pressed.
        """

        self.head.setheading(0)
