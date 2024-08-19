"""
Filename: cursor.py
Author: Amitai Ben Shalom
Description: Object representing a cursor
"""

import time
from consts import *


class Cursor(object):
    """
    Class representing a cursor
    """

    def __init__(self, pos, length, color, width):
        """
        Initialize a cursor object
        :param pos: tuple of x, y coordinates for the cursor
        :param color: tuple of RGB values for the cursor color
        :param width: int representing the width of the cursor
        """
        self.pos = pos
        self.length = length
        self.color = color
        self.width = width
        self.jump = CURSOR_JUMP
        self.last_blink = time.time()  # time of the last cursor blink

    def move(self, x, y):
        """
        Move the cursor
        :param x: int representing the x coordinate to move the cursor
        :param y: int representing the y coordinate to move the cursor
        """
        self.pos = (self.pos[0] + x, self.pos[1] + y)

    def set_pos(self, x, y):
        """
        Set the cursor position
        :param x: int representing the x coordinate to set the cursor
        :param y: int representing the y coordinate to set the cursor
        """
        self.pos = (x, y)

    def scale(self, factor):
        """
        Scale the cursor
        :param factor: float representing the scale factor
        """
        self.length = int(CURSOR_LENGTH * factor)
        self.width = int(CURSOR_WIDTH * factor)
        self.jump = (int(CURSOR_JUMP[0] * factor), int(CURSOR_JUMP[1] * factor))

    def reset(self):
        """
        Reset the cursor to the initial position
        """
        self.pos = CURSOR_START

    def get_pos(self):
        """
        Get the cursor position
        :return: tuple of x, y coordinates for the cursor
        """
        return (self.pos[0], self.pos[1])


    def render_cursor(self, surface, size_factor, CURSOR_BLINK_TIME=0.5):
        """
        Draw the cursor on the screen
        :param pos: tuple of x, y coordinates for the cursor
        """
        if time.time() - self.last_blink < CURSOR_BLINK_TIME:
            # render the cursor
            pygame.draw.line(surface, self.color, self.pos, (self.pos[0], self.pos[1] + self.length), self.width)

        elif time.time() - self.last_blink < 2 * CURSOR_BLINK_TIME:
            # do not render the cursor (for blinking effect)
            pass

        else:
            # reset the last blink time
            self.last_blink = time.time()            