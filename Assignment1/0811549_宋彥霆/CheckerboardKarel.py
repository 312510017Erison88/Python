from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: 0811549  宋彥霆
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""
def turn_right():
    """
    Makes Karel rotate 90 degrees clockwise
    """
    turn_left()
    turn_left()
    turn_left()

def fill_first_line():
    """
    pre-condition:Karel is at avenue 1 ,street 1
    Makes Karel complete one street to the right，and facing north finally
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_left()

def fill_second_line():
    """
    pre-condition:Karel is at right and facing north
    Makes Karel complete the first street to the left，and facing north finally
    """
    if on_beeper():
        move()
        if left_is_clear():
            turn_left()
            move()
            put_beeper()
        else:
            move()
            put_beeper()
    else:
        move()
        turn_left()
        put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_right()
def fill_third_line():
    """
    pre-condition:Karel is at left and facing north
    Makes Karel complete the one street to the right，and facing north finally
    """
    if on_beeper():
        move()
        if right_is_clear():
            turn_right()
            move()
            put_beeper()
        else:
            move()
            put_beeper()
    else:
        move()
        turn_right()
        put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_left()

def main():
    """
    Makes Karel complete the street orderly
    """
    fill_first_line()
    while front_is_clear():
        fill_second_line()
        if front_is_clear():
            fill_third_line()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)