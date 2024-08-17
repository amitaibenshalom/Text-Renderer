"""
Filename: main.py
Author: Amitai Ben Shalom
Description: Main file for the project - run me!
"""

import time
from consts import *
from bezierCurve import BezierCurve

# initialize pygame
pygame.init()

# set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Text Editor")


def render_text(surface, text, show_control_lines):
    """
    Draw the text on the screen
    :param text: list of Bezier curves representing the text
    """
    for letter in text:

        if letter is None:
            continue
        
        for curve in letter:
            curve.draw(surface, show_control_lines)


def render_config(surface, color, width):
    """
    Draw the configuration on the screen
    :param color: tuple of RGB values for the color
    :param width: int representing the width of the curve
    """
    # font = pygame.font.Font(None, 36)
    # text = font.render(f"Color: {color}, Width: {width}", 1, BLACK)
    # textpos = text.get_rect()
    # textpos.centerx = surface.get_rect().centerx
    # surface.blit(text, textpos)
    pygame.draw.rect(surface, color, (10, 10, 20, 20))


def render_cursor(surface, pos):
    """
    Draw the cursor on the screen
    :param pos: tuple of x, y coordinates for the cursor
    """
    pygame.draw.line(surface, CURSOR_COLOR, pos, (pos[0], pos[1] + 30), CURSOR_WIDTH)

def main():
    
    curser_pos = CURSOR_START
    color = DEFAULT_COLOR
    width = DEFAULT_WIDTH
    show_control_lines = False

    # list (of bezier curves) to store the letters
    text = []

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # handle keyboard input
            if event.type == pygame.KEYDOWN:

                if event.key == QUIT:
                    pygame.quit()
                    return
                
                elif event.key == CLEAR:
                    text.clear()
                    curser_pos = CURSOR_START

                elif event.key == DELETE_LAST:
                    if text:
                        text.pop()
                        curser_pos = (curser_pos[0] - 20, curser_pos[1])
                        
                elif event.key == TOGGLE_CONTROL_LINES:
                    show_control_lines = not show_control_lines

                elif event.key == CHANGE_COLOR:
                    color = COLORS[COLORS.index(color) + 1] if COLORS.index(color) + 1 < len(COLORS) else COLORS[0]

                elif event.key == INCREASE_WIDTH:
                    width += 1

                elif event.key == DECREASE_WIDTH:
                    width -= 1 if width > 1 else 0

                else:
                    # add the letter to the text
                    if event.key == pygame.K_SPACE:
                        curser_pos = (curser_pos[0] + CURSOR_JUMP[0], curser_pos[1])
                        text.append(None)
                        continue

                    if event.key == pygame.K_RETURN:
                        curser_pos = (CURSOR_START[0], curser_pos[1] + CURSOR_JUMP[1])
                        continue

                    if event.unicode.isalpha():
                        print(event.unicode)
                        raw_letter = ENCODED_LETTERS[LETTERS.index(event.unicode.upper())]  # only the control points of the letter
                        letter = []  # list of Bezier curves for the letter to be rendered
                        
                        for curve in raw_letter:
                            letter.append(BezierCurve(*curve, color, width) + curser_pos)

                        text.append(letter)
                        curser_pos = (curser_pos[0] + CURSOR_JUMP[0], curser_pos[1])
                        

        # render text
        screen.fill(BACKGROUND_COLOR)
        render_config(screen, color, width)
        render_text(screen, text, show_control_lines)
        render_cursor(screen, curser_pos)

        pygame.display.flip()
        time.sleep(0.1)


if __name__ == "__main__":
    main()