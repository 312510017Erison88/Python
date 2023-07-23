from simpleimage import SimpleImage


def enlarge(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    """
    img = SimpleImage(filename)
    blank = SimpleImage.blank(img.width*2, img.height*2)
    for x in range(blank.width):
        for y in range(blank.height):
            pixel_img = img.get_pixel(x//2, y//2)
            pixel_blank = blank.get_pixel(x, y)
            pixel_blank.red = pixel_img.red
            pixel_blank.green = pixel_img.green
            pixel_blank.blue = pixel_img.blue
    return blank


def main():
    """
    print original image and enlarged image
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_enlarge = enlarge("images/poppy.png")
    after_enlarge.show()


if __name__ == '__main__':
    main()