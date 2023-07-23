"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    make image shrink into half image
    """
    img = SimpleImage(filename)
    blank = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(blank.width):
        for y in range(blank.height):
            pixel_img = img.get_pixel(x*2, y*2)
            pixel_blank = blank.get_pixel(x, y)
            pixel_blank.red = pixel_img.red
            pixel_blank.green = pixel_img.green
            pixel_blank.blue = pixel_img.blue
    return blank


def main():
    """
    print original image and shrink image
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
