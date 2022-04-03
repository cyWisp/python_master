#!/usr/bin/env python
import pygame

RES = {'width': 800, 'height': 600}
TITLE = "Movement Testing"
IMAGES = {'dirby': '../images/dirby.png'}
BG_COLOR = (120, 120, 120)

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y, self.speed = 100, 100, 0
        self.move_up, self.move_down, self.move_right, self.move_left = False, False, False, False
        self.image = pygame.image.load(IMAGES['dirby'])
    
    def get_event(self, event):
        if event.key == pygame.K_d:
            self.move_right = True
        elif event.key == pygame.K_a:
            self.move_left = True
    
    def move(self):
        if self.move_right and self.x < RES['width']:
            self.speed = 5
        elif self.move_left and self.x > 0:
            self.speed = -5
        self.x += self.speed

    def update(self):
        self.screen.blit(self.image, (self.x, self.y))

    
def run():
    pygame.init()
    screen = pygame.display.set_mode((RES['width'], RES['height']))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    dirby = Player(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                dirby.get_event(event)
            elif event.type == pygame.KEYUP:
                dirby.get_event(event)
            dirby.move()

            print(event)
        screen.fill(BG_COLOR)
        dirby.update()

        pygame.display.update()
        clock.tick()

if __name__ == '__main__':
    run()