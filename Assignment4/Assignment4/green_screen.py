"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def max(a, b):
    """
    return the bigger one between a and b
    """
    if a >= b:
        return a
    if b > a:
        return b


def combine(background_img, figure_img):
    """
    :param background_img: background_img
    :param figure_img: figure_img
    :return: figure_img
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            pixel_figure = figure_img.get_pixel(x, y)
            pixel_background = background_img.get_pixel(x, y)
            bigger = max(pixel_figure.red, pixel_figure.blue)
            if pixel_figure.green > 2*bigger:
                pixel_figure.red = pixel_background.red
                pixel_figure.green = pixel_background.green
                pixel_figure.blue = pixel_background.blue
    return figure_img


def main():
    """
    To put figure into background
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
