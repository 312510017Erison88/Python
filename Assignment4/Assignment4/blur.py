"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return: new_img
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            pixel_new = new_img.get_pixel(x, y)
            if x == 0 and y != 0 and y != img.height-1:     # pixel at left boundary
                pixel_old = img.get_pixel(x, y)
                pixel_old4 = img.get_pixel(x, y + 1)
                pixel_old5 = img.get_pixel(x, y - 1)
                pixel_old6 = img.get_pixel(x + 1, y + 1)
                pixel_old7 = img.get_pixel(x + 1, y)
                pixel_old8 = img.get_pixel(x + 1, y - 1)
                pixel_new.red = (pixel_old.red + pixel_old4.red + pixel_old5.red + pixel_old6.red + pixel_old7.red + pixel_old8.red) // 6
                pixel_new.green = (pixel_old.green + pixel_old4.green + pixel_old5.green + pixel_old6.green + pixel_old7.green + pixel_old8.green) // 6
                pixel_new.blue = (pixel_old.blue + pixel_old4.blue + pixel_old5.blue + pixel_old6.blue + pixel_old7.blue + pixel_old8.blue) // 6
            elif y == 0 and x != 0 and x != img.width-1:    # pixel at top boundary
                pixel_old = img.get_pixel(x, y)
                pixel_old1 = img.get_pixel(x - 1, y + 1)
                pixel_old2 = img.get_pixel(x - 1, y)
                pixel_old4 = img.get_pixel(x, y + 1)
                pixel_old6 = img.get_pixel(x + 1, y + 1)
                pixel_old7 = img.get_pixel(x + 1, y)
                pixel_new.red = (pixel_old.red + pixel_old1.red + pixel_old2.red + pixel_old4.red + pixel_old6.red + pixel_old7.red) // 6
                pixel_new.green = (pixel_old.green + pixel_old1.green + pixel_old2.green + pixel_old4.green + pixel_old6.green + pixel_old7.green) // 6
                pixel_new.blue = (pixel_old.blue + pixel_old1.blue + pixel_old2.blue + pixel_old4.blue + pixel_old6.blue + pixel_old7.blue) // 6
            elif y == img.height-1 and x != 0 and x != img.width-1:     # pixel at bottom boundary
                pixel_old = img.get_pixel(x, y)
                pixel_old2 = img.get_pixel(x - 1, y)
                pixel_old3 = img.get_pixel(x - 1, y - 1)
                pixel_old5 = img.get_pixel(x, y - 1)
                pixel_old7 = img.get_pixel(x + 1, y)
                pixel_old8 = img.get_pixel(x + 1, y - 1)
                pixel_new.red = (pixel_old.red + pixel_old2.red + pixel_old3.red + pixel_old5.red + pixel_old7.red + pixel_old8.red) // 6
                pixel_new.green = (pixel_old.green + pixel_old2.green + pixel_old3.green + pixel_old5.green + pixel_old7.green + pixel_old8.green) // 6
                pixel_new.blue = (pixel_old.blue + pixel_old2.blue + pixel_old3.blue + pixel_old5.blue + pixel_old7.blue + pixel_old8.blue) // 6
            elif x == img.width-1 and y != 0 and y != img.height-1:     # pixel at right boundary
                pixel_old = img.get_pixel(x, y)
                pixel_old1 = img.get_pixel(x - 1, y + 1)
                pixel_old2 = img.get_pixel(x - 1, y)
                pixel_old3 = img.get_pixel(x - 1, y - 1)
                pixel_old4 = img.get_pixel(x, y + 1)
                pixel_old5 = img.get_pixel(x, y - 1)
                pixel_new.red = (pixel_old.red + pixel_old1.red + pixel_old2.red + pixel_old3.red + pixel_old4.red + pixel_old5.red) // 6
                pixel_new.green = (pixel_old.green + pixel_old1.green + pixel_old2.green + pixel_old3.green + pixel_old4.green + pixel_old5.green) // 6
                pixel_new.blue = (pixel_old.blue + pixel_old1.blue + pixel_old2.blue + pixel_old3.blue + pixel_old4.blue + pixel_old5.blue) // 6
            elif x == 0 and y == 0:                                     # pixel at left and top corner
                pixel_old = img.get_pixel(x, y)
                pixel_old4 = img.get_pixel(x, y + 1)
                pixel_old6 = img.get_pixel(x + 1, y + 1)
                pixel_old7 = img.get_pixel(x + 1, y)
                pixel_new.red = (pixel_old.red + pixel_old4.red + pixel_old6.red + pixel_old7.red) // 4
                pixel_new.green = (pixel_old.green + pixel_old4.green + pixel_old6.green + pixel_old7.green) // 4
                pixel_new.red = (pixel_old.blue + pixel_old4.blue + pixel_old6.blue + pixel_old7.blue) // 4
            elif x == 0 and y == img.height-1:                          # pixel at left and bottom corner
                pixel_old = img.get_pixel(x, y)
                pixel_old5 = img.get_pixel(x, y - 1)
                pixel_old7 = img.get_pixel(x + 1, y)
                pixel_old8 = img.get_pixel(x + 1, y - 1)
                pixel_new.red = (pixel_old.red + pixel_old5.red + pixel_old7.red + pixel_old8.red) // 4
                pixel_new.green = (pixel_old.green + pixel_old5.green + pixel_old7.green + pixel_old8.green) // 4
                pixel_new.red = (pixel_old.blue + pixel_old5.blue + pixel_old7.blue + pixel_old8.blue) // 4
            elif x == img.width-1 and y == 0:                           # pixel at right and top corner
                pixel_old = img.get_pixel(x, y)
                pixel_old1 = img.get_pixel(x - 1, y + 1)
                pixel_old2 = img.get_pixel(x - 1, y)
                pixel_old4 = img.get_pixel(x, y + 1)
                pixel_new.red = (pixel_old.red + pixel_old1.red + pixel_old2.red + pixel_old4.red) // 4
                pixel_new.green = (pixel_old.green + pixel_old1.green + pixel_old2.green + pixel_old4.green) // 4
                pixel_new.red = (pixel_old.blue + pixel_old1.blue + pixel_old2.blue + pixel_old4.blue) // 4
            elif x == img.width-1 and y == img.height-1:                # pixel at right and bottom corner
                pixel_old = img.get_pixel(x, y)
                pixel_old2 = img.get_pixel(x - 1, y)
                pixel_old3 = img.get_pixel(x - 1, y - 1)
                pixel_old5 = img.get_pixel(x, y - 1)
                pixel_new.red = (pixel_old.red + pixel_old2.red + pixel_old3.red + pixel_old5.red) // 4
                pixel_new.green = (pixel_old.green + pixel_old2.green + pixel_old3.green + pixel_old5.green) // 4
                pixel_new.red = (pixel_old.blue + pixel_old2.blue + pixel_old3.blue + pixel_old5.blue) // 4
            else:
                pixel_old = img.get_pixel(x, y)
                pixel_old1 = img.get_pixel(x - 1, y + 1)
                pixel_old2 = img.get_pixel(x - 1, y)
                pixel_old3 = img.get_pixel(x - 1, y - 1)
                pixel_old4 = img.get_pixel(x, y + 1)
                pixel_old5 = img.get_pixel(x, y - 1)
                pixel_old6 = img.get_pixel(x + 1, y + 1)
                pixel_old7 = img.get_pixel(x + 1, y)
                pixel_old8 = img.get_pixel(x + 1, y - 1)
                pixel_new.red = (pixel_old.red + pixel_old1.red + pixel_old2.red + pixel_old3.red + pixel_old4.red + pixel_old5.red + pixel_old6.red + pixel_old7.red + pixel_old8.red)//9
                pixel_new.green = (pixel_old.green + pixel_old1.green + pixel_old2.green + pixel_old3.green + pixel_old4.green + pixel_old5.green + pixel_old6.green + pixel_old7.green + pixel_old8.green) // 9
                pixel_new.blue = (pixel_old.blue + pixel_old1.blue + pixel_old2.blue + pixel_old3.blue + pixel_old4.blue + pixel_old5.blue + pixel_old6.blue + pixel_old7.blue + pixel_old8.blue) // 9
    return new_img


def main():
    """
    print original image and blurred one
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
