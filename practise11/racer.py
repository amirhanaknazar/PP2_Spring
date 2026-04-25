import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (50,50,50)
BLUE = (0,100,255)
RED = (255,0,0)

player = pygame.Rect(170, 500, 50, 80)
enemy = pygame.Rect(random.randint(50,300), -100, 50, 80)

player_speed = 6
enemy_speed = 5
coins = 0

coin_types = [
    {"color": (205,127,50), "value": 1},
    {"color": (192,192,192), "value": 2},
    {"color": (255,215,0), "value": 3}
]

coin = random.choice(coin_types)
coin_x = random.randint(40, WIDTH-40)
coin_y = -20

while True:
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 20:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH-70:
        player.x += player_speed

    enemy.y += enemy_speed
    coin_y += 5

    if enemy.y > HEIGHT:
        enemy.y = -100
        enemy.x = random.randint(50,300)

    if coin_y > HEIGHT:
        coin = random.choice(coin_types)
        coin_x = random.randint(40, WIDTH-40)
        coin_y = -20

    coin_rect = pygame.Rect(coin_x-12, coin_y-12, 24, 24)

    if player.colliderect(enemy):
        break

    if player.colliderect(coin_rect):
        coins += coin["value"]
        coin = random.choice(coin_types)
        coin_x = random.randint(40, WIDTH-40)
        coin_y = -20

        if coins % 5 == 0:
            enemy_speed += 1

    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)
    pygame.draw.circle(screen, coin["color"], (coin_x, coin_y), 12)

    text = font.render(f"Coins: {coins}", True, BLACK)
    screen.blit(text, (280, 20))

    pygame.display.update()
    clock.tick(60)