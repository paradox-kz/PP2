import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    # canvas (чтобы рисунок сохранялся)
    canvas = pygame.Surface((640, 480))
    canvas.fill((0, 0, 0))

    # UI
    font = pygame.font.SysFont("Arial", 20)

    radius = 15
    mode = 'draw'   # draw / rect / circle / eraser
    color = (0, 0, 255)

    drawing = False
    start_pos = None

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:

                # --- COLORS ---
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)

                # --- MODES ---
                elif event.key == pygame.K_1:
                    mode = 'draw'
                elif event.key == pygame.K_2:
                    mode = 'rect'
                elif event.key == pygame.K_3:
                    mode = 'circle'
                elif event.key == pygame.K_4:
                    mode = 'eraser'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos

                elif event.button == 3:
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False

                    if mode == 'rect':
                        draw_rect(canvas, color, start_pos, event.pos)

                    elif mode == 'circle':
                        draw_circle(canvas, color, start_pos, event.pos)

            if event.type == pygame.MOUSEMOTION and drawing:

                if mode == 'draw':
                    pygame.draw.circle(canvas, color, event.pos, radius)

                elif mode == 'eraser':
                    pygame.draw.circle(canvas, (0,0,0), event.pos, radius)

        # рисуем canvas
        screen.blit(canvas, (0, 0))

        # --- UI TEXT ---
        mode_text = font.render(f"Mode: {mode}", True, (255,255,255))
        size_text = font.render(f"Size: {radius}", True, (255,255,255))

        screen.blit(mode_text, (10, 10))
        screen.blit(size_text, (10, 30))

        pygame.display.flip()
        clock.tick(60)


# -------- RECT --------
def draw_rect(surface, color, start, end):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    width = abs(start[0] - end[0])
    height = abs(start[1] - end[1])

    pygame.draw.rect(surface, color, (x, y, width, height), 2)


# -------- CIRCLE --------
def draw_circle(surface, color, start, end):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    radius = int((dx**2 + dy**2) ** 0.5)

    pygame.draw.circle(surface, color, start, radius, 2)


main()