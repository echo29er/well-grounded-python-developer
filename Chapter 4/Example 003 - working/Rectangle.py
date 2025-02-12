from __future__ import annotations
import arcade
import Display

# Constants
COLOR_PALETTE = [
    arcade.color.BLACK,
    arcade.color.LIGHT_GRAY,
    arcade.color.LIGHT_CRIMSON,
    arcade.color.LIGHT_BLUE,
    arcade.color.LIGHT_CORAL,
    arcade.color.LIGHT_CYAN,
    arcade.color.LIGHT_GREEN,
    arcade.color.LIGHT_YELLOW,
    arcade.color.LIGHT_PASTEL_PURPLE,
    arcade.color.LIGHT_SALMON,
    arcade.color.LIGHT_TAUPE,
    arcade.color.LIGHT_SLATE_GRAY,
]

"""
Class Purpose: 
    This class constructs Rectangle objects.

    Attributes:
        - x (int): Defines the position of the rectangle on the screen.
        - y (int): Defines the position of the rectangle on the screen.
        + width (int): Defines the position of the rectangle on the screen.
        + height (int): Defines the position of the rectangle on the screen.
        + pen_color (tuple): Defines the color used to outline the rectangle.
        + fill_color (tuple): Defines the color used to fill the rectangle.

"""

class Rectangle: 
    # Constructor
    def __init__(
        self, 
        x: int,
        y: int, 
        width: int, 
        height: int, 
        pen_color: tuple = COLOR_PALETTE[0],
        fill_color: tuple = COLOR_PALETTE[1],
        dir_x: int = 1,
        dir_y: int = 1,
        speed_x: int = 1,
        speed_y: int = 1,
    ):

        self._x = x # use _x to denote it's a private attribute
        self._y = y # use _y to denote it's a private attribute
        self.width = width
        self.height = height
        self.pen_color = pen_color
        self.fill_color = fill_color
        self.dir_x = 1 if dir_x > 0 else -1
        self.dir_y = 1 if dir_y > 0 else -1
        self.speed_x = speed_x
        self.speed_y = speed_y

    # Instance methods (CONTINUE FROM HERE)

    @property
    def x(self):
        """
            Method purpose: 
                Getter method of the Rectangle instance for the value of x. Getter identified by @property decorator. 
            Args: 
                self: the instance of the Rectangle class.
            Returns: 
                self._x value  
        """
        return self._x
    
    @x.setter
    def x(self, value: int):
        """
            Method purpose: 
                Setter method of the Rectangle instance for the value of x. Setter identified by @x.setter decorator.
                Limit the self._x to within the screen dimensions
            Args: 
                self: the instance of the Rectangle class.
                value (int): the number of pixels to move in the horizontal axis.
            Returns: 
                None
        """
        if not (0 < value < Display.SCREEN_WIDTH - self.width):
            self.dir_x = -self.dir_x
        self._x += abs(self._x - value) * self.dir_x


    @property
    def y(self):
        """
            Method purpose: 
                Getter method of the Rectangle instance for the value of y. Getter identified by @property decorator. 
            Args: 
                self: the instance of the Rectangle class.
            Returns: 
                self._y value  
        """
        return self._y
    
    @y.setter
    def y(self, value: int):
        """
            Method purpose: 
                Setter method of the Rectangle instance for the value of y. Setter identified by @y.setter decorator.
                Limit the self._y to within the screen dimensions
            Args: 
                self: the instance of the Rectangle class.
                value (int): the number of pixels to move in the vertical axis.
            Returns: 
                None
        """
        if not (0 < value < Display.SCREEN_HEIGHT - self.height):
            self.dir_y = -self.dir_y
        self._y += abs(self._y - value) * self.dir_y

    
        # Instance methods
    def set_pen_color(self, color: tuple) -> Rectangle:
        """
            Method purpose: 
                Set the outline color of the Rectangle instance.  
            Args: 
                self: the instance of the Rectangle class.
                color (tuple): color to set the outline.
            Returns: 
                Self i.e. Rectangle object    
        """
        self.pen_color = color
        return self
    
    def set_fill_color(self, color: tuple) -> Rectangle: 
        """
            Method purpose: 
                Set the fill color of the Rectangle instance.
            Args: 
                self: the instance of the Rectangle class.
                color (tuple): color to set the fill.
            Returns: 
                Self i.e. Rectangle object 
        """
        self.fill_color = color
        return self

    def draw(self): 
        """
            Method purpose: 
                Draw the rectangle based on the current state.
            Args: 
                self: the instance of the Rectangle class.
            Returns: 
                None
        """
        arcade.draw_lbwh_rectangle_filled(
            self.x, self.y, self.width, self.height, self.fill_color
        )
        arcade.draw_lbwh_rectangle_outline(
            self.x, self.y, self.width, self.height, self.pen_color, 3
        )