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
        @property
        x:
            Method purpose: 
                Getter method of the Rectangle instance for the value of x. Getter identified by @property decorator. 
            Args: 
                self: the instance of the Rectangle class.
            Returns: 
                self._x value  

        @x.setter: 
            Method purpose: 
                Setter method of the Rectangle instance for the value of y. Setter identified by @x.setter decorator.
            Args: 
                self: the instance of the Rectangle class.
                value (int): the number of pixels to move in the horizontal axis.
            Returns: 
                None

        @property
        y:
            Method purpose: 
                Getter method of the Rectangle instance for the value of y. Getter identified by @property decorator. 
            Args: 
                self: the instance of the Rectangle class.
            Returns: 
                self._y value  

        @y.setter: 
            Method purpose: 
                Setter method of the Rectangle instance for the value of y. Setter identified by @y.setter decorator.
            Args: 
                self: the instance of the Rectangle class.
                value (int): the number of pixels to move in the vertical axis.
            Returns: 
                None
    """

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value: int):
        if self._x + value < 0: # Don't allow for negative values
            self._x = 0 
        elif self._x + self._width + value > Screen.max_x: 
            self._x = Screen.max_x - self._width
        else:
            self._x = value

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value: int):
        if self._y + value < 0: # Don't allow for negative values
            self._y = 0 
        elif self._y + self._height + value > Screen.max_y: 
            self._y = Screen.max_y - self._height
        else:
            self._y = value