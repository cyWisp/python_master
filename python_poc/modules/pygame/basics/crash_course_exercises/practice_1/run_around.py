#!/usr/bin/env python
import sys, pygame
from pygame.locals import *
from settings import Settings
from player import Player
import game_functions as gf

def run():

    # Initialize and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.title)

    # Create the player
    player = Player(screen)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events
        gf.check_events()
        
        # Update screen and on-screen objects
        gf.update_screen(ai_settings, screen, player)
        
if __name__ == '__main__':

    run()