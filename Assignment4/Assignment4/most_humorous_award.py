"""
File: most_humorous_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the most humorous award for stanCodeXNCTU MSE Fall 2020.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
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


def shrink(figure_img):
    """
    :param figure_img: str,
    :return img: SimpleImage,
    make image shrink into 5/21 times the original image
    """
    img = figure_img
    blank = SimpleImage.blank(img.width // 21 * 5, img.height // 21 * 5)
    for x in range(blank.width):
        for y in range(blank.height):
            pixel_blank = blank.get_pixel(x, y)
            pixel_img = img.get_pixel(21 * x // 5, 21 * y // 5)
            pixel_blank.red = pixel_img.red
            pixel_blank.green = pixel_img.green
            pixel_blank.blue = pixel_img.blue
    return blank


def shrink_2(figure_img):
    """
    :param figure_img: str,
    :return img: SimpleImage,
    make image shrink into 1/6 times the original image
    """
    img = figure_img
    blank = SimpleImage.blank(img.width // 6, img.height // 6)
    for x in range(blank.width):
        for y in range(blank.height):
            pixel_blank = blank.get_pixel(x, y)
            pixel_img = img.get_pixel(6 * x, 6 * y)
            pixel_blank.red = pixel_img.red
            pixel_blank.green = pixel_img.green
            pixel_blank.blue = pixel_img.blue
    return blank


def combine(background_img, figure_img):
    """
    :param background_img:
    :param figure_img:
    :return:background_img
    combine figure with the background
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            pixel_figure = figure_img.get_pixel(x, y)
            pixel_background = background_img.get_pixel(x + 350, y+7)
            bigger = max(pixel_figure.red, pixel_figure.blue)
            avg = (pixel_figure.red + pixel_figure.green + pixel_figure.blue) // 3
            if pixel_figure.green < 0.9 * bigger or avg < 40:
                pixel_background.red = pixel_figure.red
                pixel_background.green = pixel_figure.green
                pixel_background.blue = pixel_figure.blue
    return background_img


def combine_bottom(figure_img, cat):
    """
    :param figure_img:
    :param cat:
    :return : figure_img
    combine first edited image with the cat picture
    """
    for x in range(cat.width):
        for y in range(cat.height):
            pixel_figure = figure_img.get_pixel(x, y + 289)
            pixel_cat = cat.get_pixel(x, y)
            pixel_figure.red = pixel_cat.red
            pixel_figure.green = pixel_cat.green
            pixel_figure.blue = pixel_cat.blue
    return figure_img


def main():
    """
    I love to watch NBA game and see Curry as my icon,
    so it is incredible to block him in the NBA court.
    """
    background = SimpleImage("image_contest/curry_shoot.jpg")
    figure = SimpleImage("image_contest/figure1.jpg")
    new_figure = shrink(figure)
    edited = combine(background, new_figure)
    background2 = SimpleImage("image_contest/surprise.jpg")
    background2 = shrink_2(background2)
    result = combine_bottom(edited, background2)
    result.show()


if __name__ == '__main__':
    main()
