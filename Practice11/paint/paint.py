import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    canvas = pygame.Surface((640, 480))
    canvas.fill((0, 0, 0))

    radius = 10
    mode = 'blue'
    shape_mode = None

    drawing = False
    start_pos = None

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:

                # COLORS
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

                # SHAPES
                elif event.key == pygame.K_1:
                    shape_mode = "square"
                elif event.key == pygame.K_2:
                    shape_mode = "rtriangle"
                elif event.key == pygame.K_3:
                    shape_mode = "etriangle"
                elif event.key == pygame.K_4:
                    shape_mode = "rhombus"
                elif event.key == pygame.K_0:
                    shape_mode = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos

                elif event.button == 3:
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    end_pos = event.pos

                    if shape_mode:
                        draw_shape(canvas, shape_mode, start_pos, end_pos, mode)

            if event.type == pygame.MOUSEMOTION and drawing:

                if shape_mode is None:
                    pygame.draw.circle(canvas, get_color(mode), event.pos, radius)

        # ---- DRAW ----
        screen.blit(canvas, (0, 0))

        # ---- PREVIEW ----
        if drawing and shape_mode:
            current_pos = pygame.mouse.get_pos()
            temp_surface = canvas.copy()
            draw_shape(temp_surface, shape_mode, start_pos, current_pos, mode)
            screen.blit(temp_surface, (0, 0))

        pygame.display.update()
        clock.tick(60)


# -------- COLORS --------
def get_color(mode):
    if mode == 'blue':
        return (0,0,255)
    elif mode == 'red':
        return (255,0,0)
    elif mode == 'green':
        return (0,255,0)


# -------- SHAPES --------
def draw_shape(surface, shape, start, end, mode):
    color = get_color(mode)

    if shape == "square":
        size = max(abs(start[0]-end[0]), abs(start[1]-end[1]))
        pygame.draw.rect(surface, color, (start[0], start[1], size, size), 2)

    elif shape == "rtriangle":
        points = [start, (end[0], start[1]), end]
        pygame.draw.polygon(surface, color, points, 2)

    elif shape == "etriangle":
        size = abs(start[0] - end[0])
        height = size * math.sqrt(3) / 2

        points = [
            (start[0], start[1]),
            (start[0] + size, start[1]),
            (start[0] + size//2, start[1] - height)
        ]
        pygame.draw.polygon(surface, color, points, 2)

    elif shape == "rhombus":
        cx = (start[0] + end[0]) // 2
        cy = (start[1] + end[1]) // 2

        points = [
            (cx, start[1]),
            (end[0], cy),
            (cx, end[1]),
            (start[0], cy)
        ]
        pygame.draw.polygon(surface, color, points, 2)


main()