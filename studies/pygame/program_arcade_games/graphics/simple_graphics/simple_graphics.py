#!/usr/bin/env python
import pygame

RES = (800, 600)
TITLE = "Simple Graphics"

# Colors
BG_COLOR = (0, 0, 0) # Black
GREEN = (0, 250, 0) 
RED = (250, 0, 0) 
BLUE = (0, 0, 250)
WHITE = (255, 255, 255)

PI = 3.141592653

def quit_game():
    pygame.quit()
    quit()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(RES)
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        
        screen.fill(BG_COLOR)

        # Draw lines and shapes
        
        # Draw a line from (0,0) to (100, 100) that's 5 pixels wide ============
        # pygame.draw.line(screen, GREEN, [0,0], [100,100], 5) 
        # params (screen, color, origin[x, y], end[x, y], width)
        pygame.draw.line(screen, GREEN, [0, 50], [800, 50], 3)
        pygame.draw.line(screen, GREEN, [0, 550], [800, 550], 3)

        # Draw several veritcal lines ====================================
        inc = 160
        for i in range(5):
            pygame.draw.line(screen, GREEN, [inc, 0], [inc, 50], 3)
            inc += 160

        # Draw a rectangle =================================================
        # params(screen, color, [x-position, y-position, width, height], pixel_width(line))
        pygame.draw.rect(screen, RED, [20, 100, 250, 100], 2)

        # Draw an arc as part of an ellipse ===============================
        pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], 0, PI / 2, 2)
        pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], PI / 2, PI, 2)
        pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], PI, 3 * PI / 2, 2)
        pygame.draw.arc(screen, RED, [20, 220, 250, 200], 3 * PI / 2, 2 * PI, 2)

        # This draws a triangle using the polygon command ==================
        pygame.draw.polygon(screen, WHITE, [[500, 200], [400, 300], [600, 300]], 5) 

        # Drawing Text =======================================
        # Select the font to use, size, bold (true) and italics (false)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        
        # Render the text. "True" means anti-aliased text.
        # White is the color. This creates an image of the letters,
        # but does not put it on the screen
        text = font.render("this is text", True, WHITE)

        # Put the image of the text on the screen at 250, 250
        screen.blit(text, (250, 250))


        pygame.display.flip()
        clock.tick(60)
    quit_game()
