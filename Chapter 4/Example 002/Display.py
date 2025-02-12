import arcade
from __future__ import annotations
from random import choice

"""
Class Purpose: 
    This class constructs Display objects. It contains methods that animate objects on the screen. 

    Attributes:
        + screen_title (str): The title that appears at the top of the screen. 
        + rectangle (Rectangle): A rectangle object.
        + delta_time (int): 
        + interval (int): 

    Instance methods: 
        + __init__(): None
            Function purpose: 
                The constructor for the Display class

        + on_update(): None
            Function purpose: 
                Updates the position of objects to render in the display. 

        + on_draw(): None
            Function purpose: 
                Draws the updated objects on the screen.
        
        + draw(): Rectangle
            Function purpose: 
                draw
"""
# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

class Display: 
    # Constructor
    def __init__()

    # Instance methods
    """
    Instance methods: 
        on_update:
            Method purpose: 
                Updates the position of objects to render in the display.  
            Args: 
                self: the instance of the Display class.
                delta_time (int): TBD
            Returns: 
                None

        on_draw: 
            Method purpose: 
                Draws the updated objects on the screen.
            Args: 
                self: the instance of the Display class.
            Returns: 
                None

        change_colors: 
            Method purpose: 
                Changes the outline and fill colours according to the interval. 
            Args: 
                self: the instance of the Rectangle class.
            Returns: 
                None
    """

    def on_update(self, delta_time):
        for rectangle in self.rectangles: 
            rectangle.x += rectangle.speed_x
            rectangle.y += rectangle.speed_y

    def on_draw(self):
        # Clear the screen and start drawing
        arcade.start_render()

        # Draw the rectangles
        for rectangle in self.rectangles:
            rectangle.draw()

    def change_colors(self):
        for rectangle in self.rectangles: 
            rectangle.set_pen_color(choice(COLOR_PALETTE)).set_fill_color(
                choice(COLOR_PALETTE)
            )