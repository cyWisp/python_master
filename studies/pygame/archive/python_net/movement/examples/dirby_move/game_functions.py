#!/usr/bin/env python
import pygame

def check_events(player):
    for event in pygame.event.get():
        # Check if the user exits the program
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.moving_right = False

def update_screen(game_settings, screen, player):
    # Update images on the screen and flip to the new screen
    # Draw background
    screen.fill(game_settings.bg_color)

    # Draw player
    player.blitme()
    
    # Update screen
    pygame.display.flip()