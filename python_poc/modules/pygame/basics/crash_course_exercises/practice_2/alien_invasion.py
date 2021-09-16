import sys, pygame
# from pygame.locals import *
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship

def run():

    # Initialize  game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)

        # update ship in response to key commands
        ship.update()

        # update bullets on screen
        bullets.update()
        
        # Draw screen elements
        gf.update_screen(ai_settings, screen, ship, bullets)
        
if __name__ == '__main__':

    run()