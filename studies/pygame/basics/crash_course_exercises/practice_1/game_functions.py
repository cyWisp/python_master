import sys, pygame

def check_events():

    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_screen(ai_settings, screen, player):

    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    # Draw the player
    player.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()