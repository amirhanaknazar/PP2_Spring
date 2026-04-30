import pygame
import random
import sys

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

player_width = 50
player_height = 90
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 120
player_speed = 6

enemy_width = 50
enemy_height = 90
enemy_speed = 5
enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -100

coin_radius = 12
coin_speed = 4

coins = 0

def generate_coin_x():
    while True:
        x = random.randint(40, WIDTH - 40)

        if abs(x - enemy_x) > 100:
            return x

coin_x = generate_coin_x()
coin_y = -20


running = True

while running:
    screen.fill(GRAY)

    for y in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, y, 10, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 20:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width - 20:
        player_x += player_speed

    enemy_y += enemy_speed

    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 100)

    coin_y += coin_speed

    if coin_y > HEIGHT:
        coin_y = -20
        coin_x = generate_coin_x()

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    coin_rect = pygame.Rect(coin_x - coin_radius, coin_y - coin_radius,
                            coin_radius * 2, coin_radius * 2)

    if player_rect.colliderect(enemy_rect):
        text = font.render("GAME OVER", True, RED)
        screen.blit(text, (WIDTH // 2 - 70, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    if player_rect.colliderect(coin_rect):
        coins += 1
        coin_y = -20
        coin_x = generate_coin_x()

    pygame.draw.rect(screen, BLUE,
                     (player_x, player_y, player_width, player_height))

    pygame.draw.rect(screen, RED,
                     (enemy_x, enemy_y, enemy_width, enemy_height))

    pygame.draw.circle(screen, YELLOW, (coin_x, coin_y), coin_radius)

    text = font.render(f"Coins: {coins}", True, BLACK)
    screen.blit(text, (260, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()