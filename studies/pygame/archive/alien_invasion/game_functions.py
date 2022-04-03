#!/usr/bin/env python
import sys, pygame

def check_events(ship):
    # Respond to keypress and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Ship movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                # Move ship to the right
                ship.moving_right = True
            elif event.key == pygame.K_a:
                # Move ship to the left
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.moving_right = False
            elif event.key == pygame.K_a:
                ship.moving_left = False



def update_screen(ai_settings, screen, ship):
    # Update images on the screen and flip to the new screen
    # Redraw the screen and flip to the new screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()


                
