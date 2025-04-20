"This module defines the Snake class."

__author__ = "Cedrick S"
__version__ = "1.1.2025"

from turtle import Screen, Turtle
import time

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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
            self.add_segment(position)
           
    def add_segment(self, position):
        """ Adds a segment to the snake.

        Args:
            position (int): The position of the segment.
        """

        segment = Turtle("square")
        segment.color("green")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """Extends the length of the snake."""

        self.add_segment(self.segments[-1].position())

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

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Moves the snake to the downward position when the down arrow is 
        pressed.
        """

        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        """
        Moves the snake to the left position.
        """

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Moves the snake to the right position when the downward key is pressed.
        """

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
       