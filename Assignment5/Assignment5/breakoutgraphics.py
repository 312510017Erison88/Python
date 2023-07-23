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
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 4.0  # Initial vertical speed for the ball.
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

                # create label
                self.lives = NUM_LIVES
                self.lives_label = GLabel('Lives: ' + str(self.lives))
                self.lives_label.font = '-20'

                #onmouseclicked
                self.flag = False
                onmouseclicked(self.game_start)

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

    # onnmouseclicked
    def game_start(self, event):
        self.flag = True

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
        if left_top_ball is not None and left_top_ball is not self.lives_label:
            self.condition_1 = left_top_ball
            return self.condition_1
        elif left_bottom_ball is not None and left_bottom_ball is not self.lives_label:
            self.condition_2 = left_bottom_ball
            return self.condition_2
        elif right_top_ball is not None and right_top_ball is not self.lives_label:
            self.condition_3 = right_top_ball
            return self.condition_3
        elif right_bottom_ball is not None and right_bottom_ball is not self.lives_label:
            self.condition_4 = right_bottom_ball
            return self.condition_4
