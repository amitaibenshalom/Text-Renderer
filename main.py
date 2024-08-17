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


def main():
    
    curser_pos = (0, 0)
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
                    curser_pos = (0, 0)

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
                    if event.unicode.isalpha():
                        print(event.unicode)
                        raw_letter = ENCODED_LETTERS[LETTERS.index(event.unicode.upper())]  # only the control points of the letter
                        letter = []  # list of Bezier curves for the letter to be rendered
                        
                        for curve in raw_letter:
                            letter.append(BezierCurve(*curve, color, width) + curser_pos)

                        text.append(letter)
                        curser_pos = (curser_pos[0] + 20, curser_pos[1])
                        

        # clear the screen
        screen.fill(BACKGROUND_COLOR)

        # render the text
        for letter in text:
            for curve in letter:
                curve.draw(screen, show_control_lines)

        pygame.display.flip()
        time.sleep(0.1)


if __name__ == "__main__":
    main()