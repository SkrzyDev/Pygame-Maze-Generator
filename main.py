import pygame
import sys

# Settings
WIDTH, HEIGHT = 800, 600

# Maze settings
COLS, ROWS = 20, 20
CELL_SIZE = WIDTH // COLS

# Maze variables
DIRECTIONS = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0)
}
OPPOSITE = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

# Maze generation
"""
To create the maze firstly create a grid of cells, where each cell can have
walls on its north, south, east, and west sides.
Start with all walls intact

To generate a maze:
- Pick a starting cell and mark it as visited.
- While there are unvisited cells:
    - Choose a random unvisited neighboring cell.
    - Remove the wall between the current cell and the chosen cell.
    - Move to the chosen cell and mark it as visited.
    - If there are no unvisited neigboring cells, backtrack to the previous
    cell with unvisited neighbors and continue.
"""
class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.visited = False
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

    def draw(self):
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE
        if self.walls['N']:
            pygame.draw.line(screen, (200, 200, 200), (x, y), (x + CELL_SIZE, y), 2)
        if self.walls['S']:
            pygame.draw.line(screen, (200, 200, 200), (x, y + CELL_SIZE), (x, y + CELL_SIZE), 2)
        if self.walls['E']:
            pygame.draw.line(screen, (200, 200, 200), (x + CELL_SIZE, y), (x + CELL_SIZE, y), 2)
        if self.walls['W']:
            pygame.draw.line(screen, (200, 200, 200), (x, y), (x, y + CELL_SIZE), 2)

def create_grid():
    return [[Cell(x, y) for y in range(ROWS)] for x in range(COLS)]

# Setup pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Maze Generator")

# Maze & grid
grid = create_grid()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    screen.fill((20, 20, 20))

    for row in grid:
        for cell in row:
            cell.draw()

    pygame.display.flip()

pygame.quit()