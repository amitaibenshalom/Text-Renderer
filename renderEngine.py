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
        # global SIZE_FACTOR_STEP
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
        color_box_pos = (10, 10)
        color_box_size = (20, 20)

        # draw the color box
        pygame.draw.rect(self.screen, self.color, (color_box_pos, color_box_size))

        # draw lines to separate the color from the rest of the screen
        # pygame.draw.line(self.screen, BLACK, (0, color_box_pos[1] + color_box_size[1] + 10), (SCREEN_WIDTH, color_box_pos[1] + color_box_size[1] + 10), 2)
        
        # draw lines under each row of letters
        for i in range(CURSOR_START[1] + CURSOR_JUMP[1], SCREEN_HEIGHT, CURSOR_JUMP[1]):
            pygame.draw.line(self.screen, GRAY, (0, i - 5), (SCREEN_WIDTH, i - 5), 1)

    def get_last_line_length(self):
        """
        Get the length of the last line in the text
        :return: int representing the length of the last line
        """
        length = 0

        for letter in self.text:
            if letter == pygame.K_RETURN:
                length = 0
            else:
                length += 1

        return length

    def change_to_shifted_key(key):
        """
        Change the key to the shifted key
        :param key: char representing the key that was pressed
        :return: char representing the shifted key
        """
        non_shifted = r"`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./"
        shifted = r'~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
        
        # check if key is pressed with shift
        if key in non_shifted:
            key = shifted[non_shifted.index(key)]

        return key

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

        # check if ctrl + c was pressed
        if key == CLEAR and ctrl:
            self.text.clear()
            self.cursor.reset()
            return

        # check if backspace was pressed
        if key == DELETE_LAST:
            
            if self.text:
                self.cursor.move(-self.cursor.jump[0], 0)
                self.text.pop()
                
                if self.cursor.get_pos()[0] < CURSOR_START[0]:
                    # there must have been a newline character before the cursor - THAT WE ALREADY REMOVED, now remove the actual letter
                    if self.text and self.text[-1] != pygame.K_RETURN:  # if there are still letters in the text
                        self.text.pop()

                    self.cursor.set_pos(CURSOR_START[0] + self.get_last_line_length() * self.cursor.jump[0], self.cursor.get_pos()[1] - self.cursor.jump[1])
                
            
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

        # check if cntrl + + was pressed
        if key == INCREASE_SIZE and ctrl:
            self.size_factor += SIZE_FACTOR_STEP if self.size_factor < MAX_SIZE_FACTOR else 0
            self.width = int(DEFAULT_WIDTH * self.size_factor)
            self.cursor.scale(self.size_factor)
            return

        # check if cntrl + - was pressed
        if key == DECREASE_SIZE and ctrl:
            self.size_factor -= SIZE_FACTOR_STEP if self.size_factor > MIN_SIZE_FACTOR else 0
            self.width = int(DEFAULT_WIDTH * self.size_factor)
            self.cursor.scale(self.size_factor)
            return

        # check if enter was pressed
        if key == pygame.K_RETURN:
            self.cursor.set_pos(CURSOR_START[0], self.cursor.get_pos()[1] + self.cursor.jump[1])
            self.text.append(pygame.K_RETURN)
            return
        
        # check if tab was pressed
        if key == pygame.K_TAB:
            self.cursor.move(self.cursor.jump[0] * TAB_SIZE, 0)
            for i in range(TAB_SIZE):
                self.text.append(pygame.K_SPACE)
            return

        # check if space was pressed
        if key == pygame.K_SPACE:
            self.cursor.move(self.cursor.jump[0], 0)
            self.text.append(pygame.K_SPACE)
            
            if self.cursor.get_pos()[0] > SCREEN_WIDTH:
                self.cursor.set_pos(CURSOR_START[0], self.cursor.get_pos()[1] + self.cursor.jump[1])
                self.text.append(pygame.K_RETURN)
            return

        # handle all other keys (letters, numbers, shifted versions, etc.)
        try:
            key = chr(key)
        except:
            return  # ignore non-letter keys

        if shift:
            key = RenderEngine.change_to_shifted_key(key)

        if not ctrl and key.upper() in LETTERS:
            raw_letter = ENCODED_LETTERS[LETTERS.index(key.upper())]  # only the control points of the letter
            letter = []  # list of Bezier curves for the letter to be rendered
            
            for curve in raw_letter:
                letter.append(BezierCurve(*curve, self.color, self.width) * self.size_factor + self.cursor.get_pos())

            self.text.append(letter)
            self.cursor.move(self.cursor.jump[0], 0)

            if self.cursor.get_pos()[0] > SCREEN_WIDTH:
                self.cursor.set_pos(CURSOR_START[0], self.cursor.get_pos()[1] + self.cursor.jump[1])
                self.text.append(pygame.K_RETURN)