import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
def winner(screen):
    """
    Displays the Game Over screen until the user presses a key or closes the window.
    """
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, (255, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # Draw the game over screen
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()

    # Wait for any key press or quit event
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            elif event.type == pygame.KEYDOWN:
                waiting = False
    




def show_go_screen():
    pass