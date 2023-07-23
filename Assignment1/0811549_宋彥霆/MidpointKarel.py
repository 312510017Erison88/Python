from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: 0811549  宋彥霆
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
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

def function1():
    """
    Makes Karel put beeper to the left end and go the right end
    """
    put_beeper()
    while front_is_clear():
        move()
    turn_around()

def fuction2():
    """
    Makes Karel put beeper to the right and go to the left to pick beeper,facing east finally
    """
    if not on_beeper():
        put_beeper()
        move()
        while not on_beeper():
            move()
        pick_beeper()
        turn_around()
        move()
    else:
        pass

def function3():
    """
    Makes Karel put beeper to the left and go to the right to pick beeper, facing west finally
    """
    if not on_beeper():
        put_beeper()
        move()
        while not on_beeper():
            move()
        pick_beeper()
        turn_around()
        move()
    else:
        pass

def main():
    """
    Makes Karel put beeper at the midpoint
    """
    function1()
    while not on_beeper():
        fuction2()
        function3()
####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)