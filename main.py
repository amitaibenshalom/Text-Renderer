"""
Filename: main.py
Author: Amitai Ben Shalom
Description: Main file for the project - run me!
"""

from consts import *
from bezierCurve import BezierCurve

# initialize pygame
pygame.init()

# set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Text Editor")


def main():
    
    curser_pos = (0, 0)
    show_control_lines = False
