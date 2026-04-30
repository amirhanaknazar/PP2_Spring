import pygame, sys, datetime
from tools import draw_shape, flood_fill

pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("TSIS 2 Paint FINAL")

canvas = pygame.Surface((W, H))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

# state
color = (0, 0, 0)
tool = "brush"
size = 5

drawing = False
x1 = y1 = 0
last = (0, 0)

# text
typing = False
text = ""
text_pos = (0, 0)
font = pygame.font.SysFont("Arial", 28)

# undo stack
history = []

def save_state():
    history.append(canvas.copy())
    if len(history) > 20:
        history.pop(0)

def undo():
    if history:
        global canvas
        canvas = history.pop()

def save_image():
    name = datetime.datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
    pygame.image.save(canvas, name)
    print("Saved:", name)

UI_H = 80

while True:
    screen.fill((220, 220, 220))
    screen.blit(canvas, (0, 0))

    mx, my = pygame.mouse.get_pos()

    # preview surface (IMPORTANT FIX)
    preview = canvas.copy()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

        if e.type == pygame.KEYDOWN:

            if typing:
                if e.key == pygame.K_RETURN:
                    img = font.render(text, True, color)
                    canvas.blit(img, text_pos)
                    typing = False
                    text = ""

                elif e.key == pygame.K_ESCAPE:
                    typing = False
                    text = ""

                elif e.key == pygame.K_BACKSPACE:
                    text = text[:-1]

                else:
                    text += e.unicode

            else:
                if e.key == pygame.K_1: size = 2
                if e.key == pygame.K_2: size = 5
                if e.key == pygame.K_3: size = 10

                if e.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    undo()

                if e.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    save_image()

        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.pos[1] < UI_H:
                continue

            save_state()

            if tool == "fill":
                flood_fill(canvas, e.pos, color)

            elif tool == "text":
                typing = True
                text_pos = e.pos
                text = ""

            else:
                drawing = True
                x1, y1 = e.pos
                last = e.pos

        if e.type == pygame.MOUSEBUTTONUP:
            if drawing:
                drawing = False

                if tool not in ["brush", "eraser"]:
                    draw_shape(canvas, tool, color, x1, y1, e.pos[0], e.pos[1], size)

        if e.type == pygame.MOUSEMOTION and drawing:
            if tool == "brush":
                pygame.draw.line(canvas, color, last, e.pos, size)
                last = e.pos

            elif tool == "eraser":
                pygame.draw.line(canvas, (255,255,255), last, e.pos, size*3)
                last = e.pos

    # preview line
    if drawing and tool not in ["brush", "eraser"]:
        draw_shape(preview, tool, color, x1, y1, mx, my, size)
        screen.blit(preview, (0,0))

    # text preview
    if typing:
        t = font.render(text + "|", True, color)
        screen.blit(t, text_pos)

    pygame.display.update()
    clock.tick(120)