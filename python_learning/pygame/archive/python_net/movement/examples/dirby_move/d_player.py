#!/usr/bin/env python
import pygame

DIRBY_IMAGE = "./images/dirby.png"

class Player:
    def __init__(self, screen):
        # Initialize dirby and set his starting position
        self.screen = screen

        # Load dirby's image and get its rect (rectangular area)
        self.image = pygame.image.load(DIRBY_IMAGE)
        self.rect = self.image.get_rect()       # get rect of image
        self.screen_rect = screen.get_rect()    # get rect of screen

        # Start dirby at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx    # make centerx of image centerx of screen
        self.rect.bottom = self.screen_rect.bottom      # make bottom of image bottom of screen

        # Movement
        self.moving_right = False
    
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        # draw driby at his current location
        self.screen.blit(self.image, self.rect)

    # <rect(568, 736, 64, 64)>
    def get_info(self):
        print(f"image rect: {self.rect} | center: {self.rect.centerx} | bottom: {self.rect.bottom}")
