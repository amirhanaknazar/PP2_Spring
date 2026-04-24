import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# Font
font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()

# Snake starting position
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"

# Food function
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)

        # Food must not appear on snake body
        if (x, y) not in snake:
            return (x, y)

food = generate_food()

score = 0
level = 1
speed = 8

# Game over function
def game_over():
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, (WIDTH // 2 - 70, HEIGHT // 2))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

running = True

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Current head
    head_x, head_y = snake[0]

    # Move snake
    if direction == "UP":
        head_y -= CELL
    elif direction == "DOWN":
        head_y += CELL
    elif direction == "LEFT":
        head_x -= CELL
    elif direction == "RIGHT":
        head_x += CELL

    new_head = (head_x, head_y)

    # Check wall collision
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        game_over()

    # Check collision with itself
    if new_head in snake:
        game_over()

    # Add new head
    snake.insert(0, new_head)

    # Check food collision
    if new_head == food:
        score += 1
        food = generate_food()

        # Increase level every 4 foods
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL, CELL))

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL, CELL))

    # Draw score and level
    info = font.render(f"Score: {score}   Level: {level}", True, WHITE)
    screen.blit(info, (10, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()