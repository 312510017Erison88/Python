"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao
-----------------------
File: breakout.py
Name:0811549  宋彥霆
-----------------------

YOUR DESCRIPTION HERE
This program is to design the game which make
 the ball bounce between bricks and paddle
"""
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()

    # Add animation loop here!
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    stick_paddle = True                        # The switch to make the ball not stick to the paddle
    while True:
        pause(FRAME_RATE)
        if graphics.flag is True:
            if graphics.ball.x+graphics.ball.width >= graphics.window.width or graphics.ball.x <= 0:
                vx = -vx
            if graphics.ball.y <= 0:
                vy = -vy
            graphics.ball.move(vx, vy)

            test = graphics.collisions()
            if graphics.ball.y <= graphics.paddle.y - 40 or graphics.ball.y >= graphics.paddle.y + 30:
                stick_paddle = True
            if test == graphics.condition_1:            # ball collide left top of the ball
                if test is graphics.paddle:
                    if stick_paddle:
                        vy = -vy
                        stick_paddle = False
                else:
                    graphics.window.remove(test)        # remove the brick
                    graphics.break_brick -= 1
                    if graphics.break_brick == 0:
                        break
                    vy = -vy
                    vx = vx

            elif test == graphics.condition_2:          # ball collide left bottom of the ball
                if test is graphics.paddle:
                    if stick_paddle:
                        vy = -vy
                        stick_paddle = False
                else:
                    graphics.window.remove(test)        # remove the brick
                    graphics.break_brick -= 1
                    if graphics.break_brick == 0:
                        break
                    vy = -vy
                    vx = vx
            elif test == graphics.condition_3:          # ball collide right top of the ball
                if test is graphics.paddle:
                    if stick_paddle:
                        vy = -vy
                        stick_paddle = False
                else:
                    graphics.window.remove(test)        # remove the brick
                    graphics.break_brick -= 1
                    if graphics.break_brick == 0:
                        break
                    vy = -vy
                    vx = vx
            elif test == graphics.condition_4:          # ball collide right bottom of the ball
                if test is graphics.paddle:
                    if stick_paddle:
                        vy = -vy
                        stick_paddle = False
                else:
                    graphics.window.remove(test)
                    graphics.break_brick -= 1
                    if graphics.break_brick == 0:
                        break
                    vy = -vy
                    vx = vx

            if graphics.ball.y > graphics.window.height:
                graphics.lives -= 1
                graphics.lives_label.text = 'Lives:   ' + str(graphics.lives)
                graphics.window.add(graphics.lives_label, 0, graphics.lives_label.height)
                if graphics.lives >= 1:
                    graphics.reset_ball()
                else:                                   # lose game condition
                    break


if __name__ == '__main__':
    main()
