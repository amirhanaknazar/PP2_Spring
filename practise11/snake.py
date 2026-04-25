import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,200,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

snake = [(100,100), (80,100), (60,100)]
direction = "RIGHT"
score = 0

foods = [
    {"color": RED, "value": 1},
    {"color": BLUE, "value": 2},
    {"color": YELLOW, "value": 3}
]

def generate_food():
    while True:
        pos = (random.randrange(0, WIDTH, CELL),
               random.randrange(0, HEIGHT, CELL))
        if pos not in snake:
            return pos

food = generate_food()
food_data = random.choice(foods)
food_time = pygame.time.get_ticks()
food_lifetime = 5000

while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    x, y = snake[0]

    if direction == "UP":
        y -= CELL
    elif direction == "DOWN":
        y += CELL
    elif direction == "LEFT":
        x -= CELL
    elif direction == "RIGHT":
        x += CELL

    head = (x, y)

    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or head in snake:
        break

    snake.insert(0, head)

    if head == food:
        score += food_data["value"]
        food = generate_food()
        food_data = random.choice(foods)
        food_time = pygame.time.get_ticks()
    else:
        snake.pop()

    if pygame.time.get_ticks() - food_time > food_lifetime:
        food = generate_food()
        food_data = random.choice(foods)
        food_time = pygame.time.get_ticks()

    for s in snake:
        pygame.draw.rect(screen, GREEN, (s[0], s[1], CELL, CELL))

    pygame.draw.rect(screen, food_data["color"], (food[0], food[1], CELL, CELL))

    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(8)