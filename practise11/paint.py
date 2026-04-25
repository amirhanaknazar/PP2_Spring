import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255,255,255))
clock = pygame.time.Clock()

BLACK = (0,0,0)
color = BLACK

tool = "square"
start_pos = None
drawing = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                tool = "square"
            elif event.key == pygame.K_r:
                tool = "right"
            elif event.key == pygame.K_t:
                tool = "triangle"
            elif event.key == pygame.K_h:
                tool = "rhombus"

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            drawing = False

            x1, y1 = start_pos
            x2, y2 = end_pos

            if tool == "square":
                side = max(abs(x2-x1), abs(y2-y1))
                pygame.draw.rect(screen, color, (x1, y1, side, side), 2)

            elif tool == "right":
                points = [(x1,y1), (x1,y2), (x2,y2)]
                pygame.draw.polygon(screen, color, points, 2)

            elif tool == "triangle":
                points = [(x1,y2), (x2,y2), ((x1+x2)//2, y1)]
                pygame.draw.polygon(screen, color, points, 2)

            elif tool == "rhombus":
                cx = (x1+x2)//2
                cy = (y1+y2)//2
                points = [(cx,y1), (x2,cy), (cx,y2), (x1,cy)]
                pygame.draw.polygon(screen, color, points, 2)

    pygame.display.update()
    clock.tick(60)