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
        + dir_x (int): Defines the direction of movement relative to the screen's x axes; these are either 1 or -1.
        + dir_y (int): Defines the direction of movement relative to the screen's y axes; these are either 1 or -1.
        + speed_x (int): Defines the speed at which the rectangle is moving in pixels per update.
        + speed_y (int): Defines the speed at which the rectangle is moving in pixels per update.

    Instance methods: 
        + __init__(): None
            Function purpose: 
                The constructor for the Rectangle class

        + set_pen_color(): Rectangle
            Function purpose: 
                Set the pen color

        + set_fill_color(): Rectangle
            Function purpose: 
                Set the fill color
        
        + draw(): Rectangle
            Function purpose: 
                draw
"""

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
        speed_y: int = 1
    ):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pen_color = pen_color
        self.fill_color = fill_color
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.speed_x = speed_x
        self.speed_y = speed_y

    # Instance methods
    def set_pen_color(self, color: tuple) -> Rectangle:
        """
            set_pen_color:
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
            set_fill_color: 
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
            draw: 
                Method purpose: 
                    Draw the rectangle based on the current state.
                Args: 
                    self: the instance of the Rectangle class.
                Returns: 
                    None
        """
        arcade.draw_xywh_rectangle_filled(
            self.x, self.y, self.width, self.height, self.fill_color
        )
        arcade.draw_xywh_rectangle_outline(
            self.x, self.y, self.width, self.height, self.pen_color, 3
        )