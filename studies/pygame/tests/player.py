#!/usr/bin/env python
import pygame

class Player:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color
        
        self.x = 50
        self.y = 570
        self.speed_x = 5
        self.speed_y = 7
        self.size = 10

        self.moving_right, self.moving_left = False, False
        self.jump = False

    def draw(self):
        pygame.draw.circle(self.screen, self.color, [self.x, self.y], self.size)
    
    def move(self):
        if self.moving_right:
            self.x += self.speed_x
        if self.moving_left:
            self.x -= self.speed_x
        
        if self.jump:
            self.y -= self.speed_y
        else:
            if self.y < 570:
                self.y += self.speed_y


