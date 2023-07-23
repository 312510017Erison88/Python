from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name:  0811549  宋彥霆
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""
def turn_right():
    """
    Makes Karel rotate 90 degrees clockwise
    """
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    """
    Makes Karel rotate 180 degrees clockwise
    """
    turn_left()
    turn_left()

def first_go_up():
    """
    Makes Karel goes up and turn right
    """
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if on_beeper():
        turn_right()
    else:
        put_beeper()
        turn_right()


def first_go_down():
    """
    Makes Karel goes down and turn left
    """
    turn_right()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    turn_left()

def go_straight():
    """
    Makes Karel move four times
    """
    move()
    move()
    move()
    move()


def build_pillar():
    """
    Makes Karel build a pillar
    """
    first_go_up()
    go_straight()
    first_go_down()



def main():
    """
    makes Karel build pillars
    """
    while front_is_clear():
        build_pillar()

####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)