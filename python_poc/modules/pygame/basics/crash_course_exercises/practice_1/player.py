import pygame

class Player():

    def __init__(self, screen):
        # Initialize the player and set its starting position
        self.screen = screen

        # Load the player image and get its rect
        self.image = pygame.image.load("./assets/character_1.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new player at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # Draw the player at its current location
        self.screen.blit(self.image, self.rect)
        
