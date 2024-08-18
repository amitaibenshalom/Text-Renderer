"""
Filename: handle_keyboard.py
Author: Amitai Ben Shalom
Description: Handle keyboard events in the main file
"""

from consts import *
from bezierCurve import BezierCurve

def handle_key_press(key, curser_pos, curser_jump, text, color, width, size_factor):
    """
    Handle a key press event
    :param key: int representing the key that was pressed
    :param curser_pos: tuple of x, y coordinates for the cursor
    :param curser_jump: tuple of x, y coordinates for the cursor jump
    :param text: list of Bezier curves representing the text
    :param color: tuple of RGB values for the color
    :param width: int representing the width of the curve
    :param size_factor: float representing the size factor of the text
    """

    if key == SPACE:
        curser_pos = (curser_pos[0] + curser_jump[0], curser_pos[1])
        text.append(SPACE)

    if key == NEW_LINE:
        curser_pos = (CURSOR_START[0], curser_pos[1] + curser_jump[1])
        text.append(NEW_LINE)

    if key == DOT:
        raw_letter = ENCODED_LETTERS[LETTERS.index(".")]
        letter = []

        for curve in raw_letter:
            letter.append(BezierCurve(*curve, color, width) * size_factor + curser_pos)

        text.append(letter)
        curser_pos = (curser_pos[0] + curser_jump[0], curser_pos[1])

    if key == QUESTION_MARK:
        raw_letter = ENCODED_LETTERS[LETTERS.index("?")]
        letter = []

        for curve in raw_letter:
            letter.append(BezierCurve(*curve, color, width) * size_factor + curser_pos)

        text.append(letter)
        curser_pos = (curser_pos[0] + curser_jump[0], curser_pos[1])

    if key == EXCLAMATION_MARK:
        raw_letter = ENCODED_LETTERS[LETTERS.index("!")]
        letter = []

        for curve in raw_letter:
            letter.append(BezierCurve(*curve, color, width) * size_factor + curser_pos)

        text.append(letter)
        curser_pos = (curser_pos[0] + curser_jump[0], curser_pos[1])
    
    try:
        key = chr(key)
    except:
        return curser_pos

    if key.isalpha():
        raw_letter = ENCODED_LETTERS[LETTERS.index(key.upper())]  # only the control points of the letter
        letter = []  # list of Bezier curves for the letter to be rendered
        
        for curve in raw_letter:
            letter.append(BezierCurve(*curve, color, width) * size_factor + curser_pos)

        text.append(letter)
        curser_pos = (curser_pos[0] + curser_jump[0], curser_pos[1])

    return curser_pos