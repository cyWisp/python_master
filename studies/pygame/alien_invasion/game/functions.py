import sys, pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ship.rect.centerx += 1

def update_screen(settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    screen.fill(settings.bg_color)
    ship.blitme()

    pygame.display.flip()