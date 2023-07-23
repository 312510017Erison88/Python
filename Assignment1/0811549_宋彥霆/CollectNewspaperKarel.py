from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: 0811549  宋彥霆
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
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

def move_to_newspaper():
    """
    pre-condition:Karel is at avenue 3 ,street 4
    post-condition:Karel is at avenue 6 ,street 3
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def take_back_home():
    """
    pre-condition:Karel is at avenue 6,street 3
    post-condition:Karel is at avenue 3 ,street 4
    """
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()

def main():
    """
    Makes Karel go to pick newspaper
    and turn back to home
    and put down newspaper
    """
    move_to_newspaper()
    take_back_home()
    put_beeper()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
