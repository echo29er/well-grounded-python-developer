import arcade
from Display import Display
from Rectangle import Rectangle

def main():
    # Create the display instance
    display = Display("Example 01")

    # Create a rectangle instance
    rectangle = Rectangle(20, 20, 100, 200)

    # Append the rectangle to the display rectangles list
    display.append(rectangle)

    # Change the shape colors on a schedule
    arcade.schedule(display.change_colors, 1)

    # Run the application
    arcade.run()


if __name__ == "__main__":
    main()