"""
Filename: handle_keyboard.py
Author: Amitai Ben Shalom
Description: Handle keyboard events in the main file
"""

from consts import *
from bezierCurve import BezierCurve


def change_to_shifted_key(key):
    """
    Change the key to the shifted key
    :param key: int representing the key
    :param pressed: list of pressed keys
    :return: int representing the shifted key
    """

    non_shifted = r"`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./"
    shifted = r'~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'

    try:
        char_key = chr(key)
    except:
        char_key = None

    # check if key is pressed with shift
    if char_key != None and char_key in non_shifted:
        char_key = shifted[non_shifted.index(char_key)]

    return ord(char_key) if char_key != None else key


def handle_key_press2(key, curser_pos, curser_jump, text, color, width, size_factor):
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
    shift = ctrl = False
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
        shift = True

    if pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]:
        ctrl = True

    # key = change_to_shifted_key(key, pressed)  # change the key to the shifted key if needed

    # check if space was pressed
    if key == pygame.K_SPACE:
        curser_pos = (curser_pos[0] + curser_jump[0], curser_pos[1])
        text.append(pygame.K_SPACE)

    # check if ctrl + c was pressed
    if key == CLEAR and ctrl:
        text.clear()
        curser_pos = CURSOR_START

    # check if backspace was pressed
    if key == DELETE_LAST:
        if text:
            if text[-1] == pygame.K_RETURN:
                curser_pos = (CURSOR_START[0], curser_pos[1] - curser_jump[1])

            else:
                curser_pos = (curser_pos[0] - curser_jump[0], curser_pos[1])

            text.pop()
        
        else:
            curser_pos = CURSOR_START

    # check if cntrl + l was pressed
    if key == TOGGLE_CONTROL_LINES and ctrl:
        show_control_lines = not show_control_lines

    # check if cntrl + k was pressed
    if key == CHANGE_COLOR and ctrl:
        color = COLORS[(COLORS.index(color) + 1) % len(COLORS)]

    # check if + was pressed
    if key == INCREASE_SIZE:
        size_factor += 0.2
        curser_jump = (CURSOR_JUMP[0] * size_factor, CURSOR_JUMP[1] * size_factor)

    # check if - was pressed
    if key == DECREASE_SIZE:
        size_factor -= 0.2 if size_factor > 0.5 else 0
        curser_jump = (CURSOR_JUMP[0] * size_factor, CURSOR_JUMP[1] * size_factor)
    
    # check if enter was pressed
    if key == pygame.K_RETURN:
        curser_pos = (CURSOR_START[0], curser_pos[1] + curser_jump[1])
        text.append(pygame.K_RETURN)

    if key == pygame.K_PERIOD:
        raw_letter = ENCODED_LETTERS[LETTERS.index(".")]
        letter = []

        for curve in raw_letter:
            letter.append(BezierCurve(*curve, color, width) * size_factor + curser_pos)

        text.append(letter)
        curser_pos = (curser_pos[0] + curser_jump[0], curser_pos[1])

    if shift and key == pygame.K_QUESTION:
        raw_letter = ENCODED_LETTERS[LETTERS.index("?")]
        letter = []

        for curve in raw_letter:
            letter.append(BezierCurve(*curve, color, width) * size_factor + curser_pos)

        text.append(letter)
        curser_pos = (curser_pos[0] + curser_jump[0], curser_pos[1])

    if shift and key == pygame.K_EXCLAIM:
        raw_letter = ENCODED_LETTERS[LETTERS.index("!")]
        letter = []

        for curve in raw_letter:
            letter.append(BezierCurve(*curve, color, width) * size_factor + curser_pos)

        text.append(letter)
        curser_pos = (curser_pos[0] + curser_jump[0], curser_pos[1])
    
    try:
        key = chr(key)
    except:
        return
    
    if not ctrl and key.isalpha():
        raw_letter = ENCODED_LETTERS[LETTERS.index(key.upper())]  # only the control points of the letter
        letter = []  # list of Bezier curves for the letter to be rendered
        
        for curve in raw_letter:
            letter.append(BezierCurve(*curve, color, width) * size_factor + curser_pos)

        text.append(letter)
        curser_pos = (curser_pos[0] + curser_jump[0], curser_pos[1])

    return 