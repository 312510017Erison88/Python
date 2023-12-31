"""
File: stanCodoshop.py
Name:0811549  宋彥霆
----------------------------------------------
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
-----------------------------------------------


TODO:
    Given a list of image objects, compute and display a no man image
    based on these images. There will be at least 3 images and they will all
    be the same size.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_distance = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)**(1/2)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total = 0
    result = []                 # To store the averaged pixel
    for i in range(len(pixels)):
        total += pixels[i].red
    red = total / len(pixels)
    total = 0
    for i in range(len(pixels)):
        total += pixels[i].green
    green = total / len(pixels)
    total = 0
    for i in range(len(pixels)):
        total += pixels[i].blue
    blue = total / len(pixels)
    result.append(red)
    result.append(green)
    result.append(blue)
    return result


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages
    """
    distance = []       # To store the color_distance
    average = []        # To store averaged pixels from those picture
    a = 0               # To know the position of smallest pixel in pixels' list
    average.extend(get_average(pixels))
    for i in range(len(pixels)):
        distance.append(get_pixel_dist(pixels[i], average[0], average[1], average[2]))
    smallest = distance[0]
    for i in range(1, len(pixels)):
        if distance[i] < smallest:
            smallest = distance[i]
            a = i
    return pixels[a]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    new_list = []                       # To store the pixels which is going to compare
    for x in range(result.width):
        for y in range(result.height):
            for z in range(len(images)):
                img_pixel = images[z].get_pixel(x, y)
                new_list.append(img_pixel)
            best_pixel = get_best_pixel(new_list)
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue
            new_list = []              # Make a list empty
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
