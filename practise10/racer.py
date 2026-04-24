import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 400
HEIGHT = 600

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)

# Game clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 25)

# Player settings
player_width = 50
player_height = 90
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 120
player_speed = 6

# Enemy settings
enemy_width = 50
enemy_height = 90
enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -100
enemy_speed = 5

# Coin settings
coin_radius = 12
coin_x = random.randint(40, WIDTH - 40)
coin_y = -20
coin_speed = 4

# Collected coins
coins = 0

running = True

while running:
    screen.fill(GRAY)

    # Draw road lines
    for y in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, y, 10, 20))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player with keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 20:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width - 20:
        player_x += player_speed

    # Move enemy downward
    enemy_y += enemy_speed

    # Respawn enemy
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 100)

    # Move coin downward
    coin_y += coin_speed

    # Respawn coin
    if coin_y > HEIGHT:
        coin_y = -20
        coin_x = random.randint(40, WIDTH - 40)

    # Create rectangles for collision
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    coin_rect = pygame.Rect(coin_x - coin_radius, coin_y - coin_radius,
                            coin_radius * 2, coin_radius * 2)

    # Check collision with enemy
    if player_rect.colliderect(enemy_rect):
        game_over = font.render("GAME OVER", True, RED)
        screen.blit(game_over, (WIDTH // 2 - 70, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # Check collision with coin
    if player_rect.colliderect(coin_rect):
        coins += 1
        coin_y = -20
        coin_x = random.randint(40, WIDTH - 40)

    # Draw player car
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw enemy car
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))

    # Draw coin
    pygame.draw.circle(screen, YELLOW, (coin_x, coin_y), coin_radius)

    # Show coins in top right
    coin_text = font.render(f"Coins: {coins}", True, BLACK)
    screen.blit(coin_text, (WIDTH - 120, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()