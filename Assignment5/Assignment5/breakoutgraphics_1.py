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
The basic element or function that the game may need.
Here is coder place
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50    # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 0.5  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
NUM_LIVES = 3


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.color = 'black'
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, window_width/2-paddle_width/2, window_height-paddle_offset)

        # Center a filled ball in the graphical window.
        self.ball = GOval(2*ball_radius, 2*ball_radius)
        self.ball.color = 'black'
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, window_width / 2 - ball_radius, window_height/2 - ball_radius)

        # Default initial velocity for the ball.
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if (random.random() > 0.5):
            self.__dx = -self.__dx

        # Initialize our mouse listeners.
        onmousemoved(self.control_paddle)

        # Draw bricks.
        for j in range(brick_rows):
            for i in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.color = 'red'
                self.brick.filled = True
                self.brick.fill_color = 'red'
                if 2 <= j <= 3:
                    self.brick.color = 'orange'
                    self.brick.filled = True
                    self.brick.fill_color = 'orange'
                if 4 <= j <= 5:
                    self.brick.color = 'yellow'
                    self.brick.filled = True
                    self.brick.fill_color = 'yellow'
                if 6 <= j <= 7:
                    self.brick.color = 'green'
                    self.brick.filled = True
                    self.brick.fill_color = 'green'
                if 8 <= j <= 9:
                    self.brick.color = 'blue'
                    self.brick.filled = True
                    self.brick.fill_color = 'blue'
                if 10 <= j <= 11:
                    self.brick.color = 'indigo'
                    self.brick.filled = True
                    self.brick.fill_color = 'indigo'
                self.window.add(self.brick, i*brick_width+i*brick_spacing, brick_offset+brick_height*j+brick_spacing*j)

                # create lives label
                self.lives = NUM_LIVES
                self.lives_label = GLabel('Lives: ' + str(self.lives))
                self.lives_label.font = '-20'

                # create score label
                self.score = 0
                self.score_label = GLabel('Score: ' + str(self.score))
                self.score_label.font = '-20'
                self.win_score = brick_rows * brick_cols

                #onmouseclicked
                onmouseclicked(self.start_game_cover)
                self.open = False
                self.flag = False

                # game end condition
                self.break_brick = brick_rows * brick_cols

                # definition for testing collision point
                self.condition_1 = 0
                self.condition_2 = 0
                self.condition_3 = 0
                self.condition_4 = 0

    def control_paddle(self, event):
        self.paddle.x = event.x - self.paddle.width // 2
        self.paddle.y = self.window.height - PADDLE_OFFSET
        if self.paddle.x + self.paddle.width > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        if self.paddle.x < 0:
            self.paddle.x = 0

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def reset_ball(self):
        self.set_ball_position()
        self.flag = False
        self.set_ball_velocity()
        self.window.add(self.ball)

    def set_ball_position(self):
        self.ball.x = self.window.width / 2 - self.ball.width / 2
        self.ball.y = self.window.height / 2 - self.ball.height / 2

    def set_ball_velocity(self):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if (random.random() > 0.5):
            self.__dx = -self.__dx

    # define collision condition
    def collisions(self):
        left_top_ball = self.window.get_object_at(self.ball.x, self.ball.y)
        left_bottom_ball = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        right_top_ball = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        right_bottom_ball = self.window.get_object_at(self.ball.x + self.ball.width,
                                                          self.ball.y + self.ball.height)
        if left_top_ball is not None and left_top_ball is not self.lives_label and left_top_ball is not self.score_label:
            self.condition_1 = left_top_ball
            return self.condition_1
        elif left_bottom_ball is not None and left_bottom_ball is not self.lives_label and left_bottom_ball is not self.score_label:
            self.condition_2 = left_bottom_ball
            return self.condition_2
        elif right_top_ball is not None and right_top_ball is not self.lives_label and right_top_ball is not self.score_label:
            self.condition_3 = right_top_ball
            return self.condition_3
        elif right_bottom_ball is not None and right_bottom_ball is not self.lives_label and right_bottom_ball is not self.score_label:
            self.condition_4 = right_bottom_ball
            return self.condition_4

    # create lose game image
    def lose_game(self):
        self.end_game = GRect(self.window.width, self.window.height)
        self.end_game.color = 'light pink'
        self.end_game.filled = True
        self.end_game.fill_color = 'light pink'
        self.window.add(self.end_game)
        self.end_label = GLabel('You lose the game!')
        self.end_label.font = '-30'
        self.end_label.color = 'blue'
        self.window.add(self.end_label, self.window.width/2-self.end_label.width/2, self.window.height/2)

    # create win game image
    def win_game(self):
        self.win_game = GRect(self.window.width, self.window.height)
        self.win_game.color = 'light pink'
        self.win_game.filled = True
        self.win_game.fill_color = 'light pink'
        self.window.add(self.win_game)
        self.end_label1 = GLabel('You win the game!')
        self.end_label1.font = '-30'
        self.end_label1.color = 'blue'
        self.window.add(self.end_label1, self.window.width/2-self.end_label1.width/2, self.window.height/2)
        self.final_score = GLabel('Final score: '+str(self.win_score))
        self.final_score.font = '-20'
        self.final_score.color = 'blue'
        self.window.add(self.final_score, self.window.width / 2 - self.final_score.width / 2, self.window.height / 2 + self.window.height/5)

    # create start game image
    def initial_image(self):
        self.background = GRect(self.window.width, self.window.height)
        self.background.color = 'light pink'
        self.background.filled = True
        self.background.fill_color = 'light pink'
        self.window.add(self.background)
        self.ini_label1 = GLabel('Play the game!')
        self.ini_label1.font = '-35'
        self.ini_label1.color = 'blue'
        self.window.add(self.ini_label1, self.window.width/2-self.ini_label1.width/2, self.window.height/3)
        self.startlabel = GLabel('Start!')
        self.startlabel.font = '-30'
        self.startlabel.color = 'brown'
        self.window.add(self.startlabel, self.window.width / 2 - self.startlabel.width / 2,
                        self.window.height / 2 + self.window.height / 5)
        self.startbottom = GRect(self.startlabel.width+50, self.startlabel.height+25)
        self.startbottom.color = 'black'
        self.window.add(self.startbottom, self.window.width / 2 - self.startlabel.width / 2 - 25,
                        self.window.height / 2 + 75)

    # onnmouseclicked function
    def start_game_cover(self, event):
        if self.open:
            self.flag = True
        bottom = self.window.get_object_at(event.x, event.y)
        if bottom is not None and bottom is self.startlabel or bottom is self.startbottom:
            self.window.remove(self.ini_label1)
            self.window.remove(self.startlabel)
            self.window.remove(self.startbottom)
            self.window.remove(self.background)
            self.open = True


