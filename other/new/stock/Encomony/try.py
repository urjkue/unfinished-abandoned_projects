import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Cell class
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = random.choice([True, False])

    def draw(self):
        color = WHITE if self.alive else BLACK
        pygame.draw.rect(screen, color, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# World class
class World:
    def __init__(self):
        self.cells = [[Cell(x, y) for y in range(GRID_HEIGHT)] for x in range(GRID_WIDTH)]

    def get_neighbor_count(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
                    if not (dx == 0 and dy == 0) and self.cells[nx][ny].alive:
                        count += 1
        return count

    def update(self):
        new_cells = [[Cell(x, y) for y in range(GRID_HEIGHT)] for x in range(GRID_WIDTH)]
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                cell = self.cells[x][y]
                neighbor_count = self.get_neighbor_count(x, y)
                if cell.alive:
                    new_cells[x][y].alive = 2 <= neighbor_count <= 3
                else:
                    new_cells[x][y].alive = neighbor_count == 3
        self.cells = new_cells

    def draw(self):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                self.cells[x][y].draw()

# Main loop
def main():
    world = World()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        world.draw()
        world.update()

        pygame.display.flip()
        clock.tick(5)  # Adjust speed of the simulation here

if __name__ == "__main__":
    main()
