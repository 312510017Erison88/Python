"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao
-----------------------
File: breakout_1.py
Name:0811549  宋彥霆
-----------------------

YOUR DESCRIPTION HERE
This program is to design the game which make
 the ball bounce between bricks and paddle
"""
from campy.gui.events.timer import pause
from breakoutgraphics_1 import BreakoutGraphics
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
import random

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()

    # Add animation loop here!
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    stick_paddle = True                                      # The switch to make the ball not stick to the paddle
    score = 0
    graphics.window.add(graphics.score_label, graphics.window.width - graphics.score_label.width, graphics.score_label.height)
    graphics.window.add(graphics.lives_label, 0, graphics.lives_label.height)
    graphics.initial_image()
    while True:
        pause(FRAME_RATE)
        if graphics.flag is True:
            if graphics.ball.x + graphics.ball.width >= graphics.window.width or graphics.ball.x <= 0:
                vx = -vx
            if graphics.ball.y <= 0:
                vy = -vy
            graphics.ball.move(vx, vy)

            test = graphics.collisions()
            if graphics.ball.y <= graphics.paddle.y - 40 or graphics.ball.y >= graphics.paddle.y + 30:
                stick_paddle = True
            if test == graphics.condition_1:
                if test is graphics.paddle:
                    if stick_paddle:
                        vy = -vy
                        stick_paddle = False
                else:
                    graphics.window.remove(test)
                    graphics.break_brick -= 1
                    if graphics.break_brick == 0:
                        graphics.win_game()
                        break
                    score += 1
                    graphics.score_label.text = 'Score: ' + str(score)
                    graphics.window.add(graphics.score_label, graphics.window.width - graphics.score_label.width, 30)
                    vy = -vy
                    vx = vx

            elif test == graphics.condition_2:
                if test is graphics.paddle:
                    if stick_paddle:
                        vy = -vy
                        stick_paddle = False
                else:
                    graphics.window.remove(test)
                    graphics.break_brick -= 1
                    if graphics.break_brick == 0:
                        graphics.win_game()
                        break
                    score += 1
                    graphics.score_label.text = 'Score: ' + str(score)
                    graphics.window.add(graphics.score_label, graphics.window.width - graphics.score_label.width, 30)
                    vy = -vy
                    vx = vx
            elif test == graphics.condition_3:
                if test is graphics.paddle:
                    if stick_paddle:
                        vy = -vy
                        stick_paddle = False
                else:
                    graphics.window.remove(test)
                    graphics.break_brick -= 1
                    if graphics.break_brick == 0:
                        graphics.win_game()
                        break
                    score += 1
                    graphics.score_label.text = 'Score: ' + str(score)
                    graphics.window.add(graphics.score_label, graphics.window.width - graphics.score_label.width, 30)
                    vy = -vy
                    vx = vx
            elif test == graphics.condition_4:
                if test is graphics.paddle:
                    if stick_paddle:
                        vy = -vy
                        stick_paddle = False
                else:
                    graphics.window.remove(test)
                    graphics.break_brick -= 1
                    if graphics.break_brick == 0:
                        graphics.win_game()
                        break
                    score += 1
                    graphics.score_label.text = 'Score: ' + str(score)
                    graphics.window.add(graphics.score_label, graphics.window.width - graphics.score_label.width, 30)
                    vy = -vy
                    vx = vx

            """
            increase the speed and diminish the paddle with the increasing score
            """
            if score % 5 == 0:
                if vy < 0:
                    vy += -0.035
                vy += 0.035

            if graphics.ball.y > graphics.window.height:
                graphics.lives -= 1
                graphics.lives_label.text = 'Lives: ' + str(graphics.lives)
                graphics.window.add(graphics.lives_label, 0, graphics.lives_label.height)
                if graphics.lives >= 1:
                    graphics.reset_ball()
                else:
                    graphics.lose_game()
                    lose_final_score = GLabel('Final score: ' + str(score))
                    lose_final_score.font = '-20'
                    lose_final_score.color = 'blue'
                    graphics.window.add(lose_final_score, graphics.window.width / 2 - lose_final_score.width / 2, graphics.window.height / 2 + graphics.window.height/5)
                    break


if __name__ == '__main__':
    main()