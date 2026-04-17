import pygame
import sys
import datetime
from clock import draw_clock

pygame.init()

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    draw_clock(screen, minutes, seconds)

    pygame.display.flip()
    clock.tick(1)  