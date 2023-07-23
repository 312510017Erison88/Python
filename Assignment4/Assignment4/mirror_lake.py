"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: img
    :return: blank
    """
    img = SimpleImage(filename)
    blank = SimpleImage.blank(img.width, 2*img.height)  # create the blank which height is double
    for x in range(img.width):
        for y in range(img.height):
            pixel_image = img.get_pixel(x, y)
            pixel_blank = blank.get_pixel(x, y)
            pixel_blank.red = pixel_image.red
            pixel_blank.green = pixel_image.green
            pixel_blank.blue = pixel_image.blue

            # down part of the blank image
            pixel_blank_down = blank.get_pixel(x, 2*img.height-y-1)
            pixel_blank_down.red = pixel_image.red
            pixel_blank_down.green = pixel_image.green
            pixel_blank_down.blue = pixel_image.blue
    return blank


def main():
    """
    print original image and edited image which is mirror image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
