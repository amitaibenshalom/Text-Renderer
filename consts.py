"""
Constants file for the project
"""

import pygame
from pygame.locals import *
from letters_bezier_encoding import *

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
COLORS = [BLACK, RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, GRAY]

# screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
BACKGROUND_COLOR = WHITE
# LETTER_SIZE = [20, 20]

# text
TAB_SIZE = 4  # number of spaces in a tab
DEFAULT_COLOR = BLACK
DEFAULT_WIDTH = 3
DEFAULT_SIZE_FACTOR = 1.
MAX_SIZE_FACTOR = 5
MIN_SIZE_FACTOR = 0.5
SIZE_FACTOR_STEP = 0.2

# cursor
CURSOR_START = [10, 50]
CURSOR_LENGTH = 30
CURSOR_JUMP = [25, 40]
CURSOR_COLOR = GRAY
CURSOR_WIDTH = 2

# bezier curve
NUM_POINTS = 30
CONTROL_LINE_COLOR = GRAY
CONTROL_LINE_WIDTH = 1

# keyboard
QUIT = pygame.K_ESCAPE
CLEAR = pygame.K_c
DELETE_LAST = pygame.K_BACKSPACE
TOGGLE_CONTROL_LINES = pygame.K_l
CHANGE_COLOR = pygame.K_k
INCREASE_SIZE = pygame.K_EQUALS
DECREASE_SIZE = pygame.K_MINUS