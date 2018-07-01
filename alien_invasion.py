import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    # start the main cycle
    while True:
        # spy on the mouse and keyboard
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                sys.exit()
        # display the screen we draw
        pygame.display.flip()


run_game()