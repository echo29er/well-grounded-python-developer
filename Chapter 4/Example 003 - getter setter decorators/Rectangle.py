import arcade
from __future__ import annotations

"""
Class Purpose: 
    This class constructs Rectangle objects.

    Attributes:
        + x (int): Defines the position of the rectangle on the screen.
        + y (int): Defines the position of the rectangle on the screen.
        + width (int): Defines the position of the rectangle on the screen.
        + height (int): Defines the position of the rectangle on the screen.
        + pen_color (tuple): Defines the color used to outline the rectangle.
        + fill_color (tuple): Defines the color used to fill the rectangle.

    Instance methods: 
        + __init__(): None
            Function purpose: 
                The constructor for the Rectangle class

        + x(): x # Getter
            Function purpose: 
                Returns the x value, treating x as a private attribute. 

        + x(): None # Setter
            Function purpose: 
                Assigns a value to x, treating x as a private attribute. 

        + y(): y # Getter
            Function purpose: 
                Returns the y value, treating y as a private attribute. 

        + y(): None # Setter
            Function purpose: 
                Assigns a value to y, treating y as a private attribute.
"""

class Rectangle: 
    # Constructor
    def __init__(
        self, 
        x: int,
        y: int, 
        width: int, 
        height: int, 
        pen_color: str = "BLACK",
        fill_color: str = "BLUE",
    ):

        self._x = x # use _x to denote it's a private attribute
        self._y = y # use _y to denote it's a private attribute
        self.width = width
        self.height = height
        self.pen_color = pen_color
        self.fill_color = fill_color

    # Instance methods (CONTINUE FROM HERE)
    """
    Instance methods: 
        set_pen_color:
            Method purpose: 
                Set the outline color of the Rectangle instance.  
            Args: 
                self: the instance of the Rectangle class.
                color (tuple): color to set the outline.
            Returns: 
                Self i.e. Rectangle object    

        set_fill_color: 
            Method purpose: 
                Set the fill color of the Rectangle instance.
            Args: 
                self: the instance of the Rectangle class.
                color (tuple): color to set the fill.
            Returns: 
                Self i.e. Rectangle object 

        draw: 
            Method purpose: 
                Draw the rectangle
            Args: 
                self: the instance of the Rectangle class.
            Returns: 
                None
    """

    def set_pen_color(self, color: tuple) -> Rectangle:
        self.pen_color = color
        return self

    def set_fill_color(self, color: tuple) -> Rectangle: 
        self.fill_color = color
        return self

    def draw(self): 
        arcade.draw_xywh_rectangle_filled(
            self.x, self.y, self.width, self.height, self.fill_color
        )
        arcade.draw_xywh_rectangle_outline(
            self.x, self.y, self.width, self.height, self.pen_color, 3
        )