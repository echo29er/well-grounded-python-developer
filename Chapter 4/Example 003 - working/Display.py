from __future__ import annotations
import arcade
from random import choice
from Rectangle import Rectangle, COLOR_PALETTE

"""
Class Purpose: 
    This class constructs Display objects. It contains methods that animate objects on the screen. 

    Attributes:
        + screen_title (str): The title that appears at the top of the screen. 
        + rectangle (Rectangle): A rectangle object.
        + delta_time (int): 
        + interval (int): 

"""
# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

class Display(arcade.Window): # Inherit from arcade.Window
    # Constructor
    def __init__(self, screen_title):
        """Initialize the window
        """
        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, screen_title)

        # Create the retangles collection
        self.rectangles = []

        # Set the background window
        arcade.set_background_color(arcade.color.WHITE)


    # Instance methods
    def append(self, rectangle):
        """Add a rectangle to the display"""
        self.rectangles.append(rectangle)

    def on_update(self, delta_time):
        """
            Method purpose: 
                Updates the position of objects to render in the display.  
            Args: 
                self: the instance of the Display class.
                delta_time (int): TBD
            Returns: 
                None
        """
        for rectangle in self.rectangles: 
            rectangle.x += rectangle.speed_x
            rectangle.y += rectangle.speed_y

    def on_draw(self):
        """
            Method purpose: 
                Draws the updated objects on the screen.
            Args: 
                self: the instance of the Display class.
            Returns: 
                None
        """
        # Clear the screen and start drawing
        self.clear()

        # Draw the rectangles
        for rectangle in self.rectangles:
            rectangle.draw()

    def change_colors(self, delta_time):
        """
            Method purpose: 
                Changes the outline and fill colours according to the interval. 
            Args: 
                self: the instance of the Rectangle class.
                delta_time (float): Time elapsed since last update.
            Returns: 
                None
        """
        for rectangle in self.rectangles: 
            rectangle.set_pen_color(choice(COLOR_PALETTE)).set_fill_color(
                choice(COLOR_PALETTE)
            )