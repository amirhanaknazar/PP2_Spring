import pygame
from collections import deque

def flood_fill(surface, start_pos, fill_color):
    target_color = surface.get_at(start_pos)[:3]

    if target_color == fill_color:
        return

    w, h = surface.get_size()
    queue = deque([start_pos])

    while queue:
        x, y = queue.popleft()

        if 0 <= x < w and 0 <= y < h:
            current = surface.get_at((x, y))[:3]

            if current == target_color:
                surface.set_at((x, y), fill_color)

                queue.append((x+1, y))
                queue.append((x-1, y))
                queue.append((x, y+1))
                queue.append((x, y-1))


def draw_shape(surface, t, c, x1, y1, x2, y2, s):
    if t == "line":
        pygame.draw.line(surface, c, (x1, y1), (x2, y2), s)

    elif t == "rect":
        r = pygame.Rect(x1, y1, x2-x1, y2-y1)
        r.normalize()
        pygame.draw.rect(surface, c, r, s)

    elif t == "circle":
        r = int(((x2-x1)**2 + (y2-y1)**2) ** 0.5)
        pygame.draw.circle(surface, c, (x1, y1), r, s)

    elif t == "square":
        side = max(abs(x2-x1), abs(y2-y1))
        r = pygame.Rect(x1, y1, side, side)
        r.normalize()
        pygame.draw.rect(surface, c, r, s)

    elif t == "r_tri":
        pygame.draw.polygon(surface, c, [(x1,y1),(x1,y2),(x2,y2)], s)

    elif t == "eq_tri":
        mx = x1 + (x2-x1)//2
        pygame.draw.polygon(surface, c, [(mx,y1),(x1,y2),(x2,y2)], s)

    elif t == "rhomb":
        mx = x1 + (x2-x1)//2
        my = y1 + (y2-y1)//2
        pygame.draw.polygon(surface, c, [(mx,y1),(x2,my),(mx,y2),(x1,my)], s)