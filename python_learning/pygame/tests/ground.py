#!/usr/bin/env python
import pygame

class Ground:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color

        self.x = 0
        self.y = 580
        self.width = 800
        self.height = 20

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height]) 