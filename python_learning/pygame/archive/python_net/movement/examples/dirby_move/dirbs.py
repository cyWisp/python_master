#!/usr/bin/env python
import pygame
import game_functions as gf
from settings import Settings
from d_player import Player

if __name__ == '__main__':

    # Initialization / settings
    pygame.init()
    game_settings = Settings()
    clock = pygame.time.Clock()

    # Configure window
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Dirbs")
    
    # Initialize game objects
    player = Player(screen)

    # Main game loop
    while True:
        # Check for game events
        gf.check_events(player)
        
        # Update position of the player based on
        # Keypresses
        player.update()

        # Update objects on screen
        gf.update_screen(game_settings, screen, player)
        clock.tick(60)

    
    
