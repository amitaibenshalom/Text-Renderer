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
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = WHITE
# LETTER_SIZE = [20, 20]

# text
DEFAULT_COLOR = BLACK
DEFAULT_WIDTH = 2
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# bezier curve
NUM_POINTS = 30
CONTROL_LINE_COLOR = GRAY
CONTROL_LINE_WIDTH = 1

# control keys
QUIT = pygame.K_ESCAPE
CLEAR = pygame.K_0
DELETE_LAST = pygame.K_BACKSPACE
TOGGLE_CONTROL_LINES = pygame.K_9
CHANGE_COLOR = pygame.K_8
INCREASE_WIDTH = pygame.K_7
DECREASE_WIDTH = pygame.K_6
