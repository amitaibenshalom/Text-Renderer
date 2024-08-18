"""
Filename: renderEngine.py
Author: Amitai Ben Shalom
Description: Object representing a render engine for the text editor
"""

import pygame
from consts import *
from bezierCurve import BezierCurve
# from handle_keyboard import handle_key_press
from cursor import Cursor

class RenderEngine(object):
    """
    Class representing a render engine for the text editor
    """

    def __init__(self):
        """
        Initialize the render engine
        """
        pygame.init()
        pygame.display.set_caption("Text Editor")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.text = []
        self.cursor = Cursor(CURSOR_START, CURSOR_LENGTH, CURSOR_COLOR, CURSOR_WIDTH)
        self.color = DEFAULT_COLOR
        self.width = DEFAULT_WIDTH
        self.size_factor = DEFAULT_SIZE_FACTOR
        self.show_control_lines = False

    def render_text(self):
        """
        Draw the text on the screen
        """
        for letter in self.text:

            if not isinstance(letter, list):
                continue
            
            for curve in letter:
                curve.draw(self.screen, self.show_control_lines)

    def render_cursor(self):
        """
        Draw the cursor on the screen
        """
        self.cursor.render_cursor(self.screen, self.size_factor)

    def render_config(self):
        """
        Draw the configuration on the screen (currently only the color)
        """
        pygame.draw.rect(self.screen, self.color, (10, 10, 20, 20))

    def handle_key_press(self, key):
        """
        Handle a key press event
        :param key: int representing the key that was pressed
        """
        shift = ctrl = False  # flags for shift and ctrl keys
        pressed = pygame.key.get_pressed()  # get the state of the keyboard

        # check if shift is pressed
        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            shift = True

        # check if ctrl is pressed
        if pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]:
            ctrl = True

        # key = change_to_shifted_key(key, pressed)  # change the key to the shifted key if needed

        # check if space was pressed
        if key == pygame.K_SPACE:
            self.cursor.move(self.cursor.jump[0], 0)
            self.text.append(pygame.K_SPACE)
            return

        # check if ctrl + c was pressed
        if key == CLEAR and ctrl:
            self.text.clear()
            self.cursor.reset()
            return

        # check if backspace was pressed
        if key == DELETE_LAST:
            if self.text:
                if self.text[-1] == pygame.K_RETURN:
                    self.cursor.set_pos(CURSOR_START[0], self.cursor.get_pos[1] - self.cursor.jump[1])
                else:
                    self.cursor.move(-self.cursor.jump[0], 0)
                self.text.pop()
            
            else:
                self.cursor.reset()
            return

        # check if cntrl + l was pressed
        if key == TOGGLE_CONTROL_LINES and ctrl:
            self.show_control_lines = not self.show_control_lines
            return

        # check if cntrl + k was pressed
        if key == CHANGE_COLOR and ctrl:
            self.color = COLORS[(COLORS.index(self.color) + 1) % len(COLORS)]
            return

        # check if + was pressed
        if key == INCREASE_SIZE:
            self.size_factor += 0.2
            self.cursor.scale(self.size_factor)
            return

        # check if - was pressed
        if key == DECREASE_SIZE:
            self.size_factor -= 0.2 if self.size_factor > 0.5 else 0
            self.cursor.scale(self.size_factor)
            return

        # check if enter was pressed
        if key == pygame.K_RETURN:
            self.cursor.set_pos(CURSOR_START[0], self.cursor.pos[1] + self.cursor.jump[1])
            self.text.append(pygame.K_RETURN)
            return

        # check if period was pressed
        if key == pygame.K_PERIOD:
            raw_letter = ENCODED_LETTERS[LETTERS.index(".")]
            letter = []

            for curve in raw_letter:
                letter.append(BezierCurve(*curve, self.color, self.width) * self.size_factor + self.cursor.get_pos())

            self.text.append(letter)
            self.cursor.move(self.cursor.jump[0], 0)
            return

        # check if question mark was pressed
        if shift and key == pygame.K_SLASH:
            raw_letter = ENCODED_LETTERS[LETTERS.index("?")]
            letter = []

            for curve in raw_letter:
                letter.append(BezierCurve(*curve, self.color, self.width) * self.size_factor + self.cursor.get_pos())

            self.text.append(letter)
            self.cursor.move(self.cursor.jump[0], 0)
            return
            
        # check if exclamation mark was pressed
        if shift and key == pygame.K_1:
            raw_letter = ENCODED_LETTERS[LETTERS.index("!")]
            letter = []

            for curve in raw_letter:
                letter.append(BezierCurve(*curve, self.color, self.width) * self.size_factor + self.cursor.get_pos())

            self.text.append(letter)
            self.cursor.move(self.cursor.jump[0], 0)
            return
        
        try:
            key = chr(key)
        except:
            return

        if not ctrl and key.isalpha():
            raw_letter = ENCODED_LETTERS[LETTERS.index(key.upper())]  # only the control points of the letter
            letter = []  # list of Bezier curves for the letter to be rendered
            
            for curve in raw_letter:
                letter.append(BezierCurve(*curve, self.color, self.width) * self.size_factor + self.cursor.get_pos())

            self.text.append(letter)
            self.cursor.move(self.cursor.jump[0], 0)