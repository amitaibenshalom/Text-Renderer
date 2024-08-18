"""
Filename: main.py
Author: Amitai Ben Shalom
Description: Main file for the project - run me!
"""

import time
from consts import *
from renderEngine import RenderEngine
# from handle_keyboard import handle_key_press


def main():
    
    renderEngine = RenderEngine()
    
    # curser_jump = (CURSOR_JUMP[0] * size_factor, CURSOR_JUMP[1] * size_factor)
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
                
                renderEngine.handle_key_press(event.key)


        renderEngine.screen.fill(BACKGROUND_COLOR)
        renderEngine.render_text()
        renderEngine.render_cursor()
        renderEngine.render_config()

        pygame.display.flip()
        time.sleep(0.1)


if __name__ == "__main__":
    main()