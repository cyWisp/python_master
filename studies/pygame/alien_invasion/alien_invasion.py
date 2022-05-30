#!/usr/bin/env python
import pygame, sys
from settings.settings import Settings
from ship.ship import Ship
from game.functions import check_events, update_screen

def run_game():
    # Initialize game and create a screen object

    ai_settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        check_events(ship)

        # Update the screen with all objects
        update_screen(ai_settings, screen, ship)

if __name__ == '__main__':
    run_game()