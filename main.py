import pygame
import sys

# Settings
WIDTH, HEIGHT = 800, 600

# Setup pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Maze Generator")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    screen.fill((20, 20, 20))

    pygame.display.flip()

pygame.quit()