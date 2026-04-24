import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fill background
screen.fill(WHITE)

clock = pygame.time.Clock()

# Default settings
current_color = BLACK
tool = "brush"
drawing = False
start_pos = None
brush_size = 5

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            # Color selection
            if event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_k:
                current_color = BLACK

            # Tool selection
            elif event.key == pygame.K_p:
                tool = "brush"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_t:
                tool = "rectangle"
            elif event.key == pygame.K_e:
                tool = "eraser"

        # Mouse pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # Mouse released
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            # Draw circle
            if tool == "circle":
                radius = int(((end_pos[0] - start_pos[0]) ** 2 +
                              (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)

            # Draw rectangle
            elif tool == "rectangle":
                rect = pygame.Rect(start_pos,
                                   (end_pos[0] - start_pos[0],
                                    end_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, current_color, rect, 2)

        # Brush and eraser while moving mouse
        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "brush":
                pygame.draw.circle(screen, current_color, event.pos, brush_size)

            elif tool == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, 12)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()