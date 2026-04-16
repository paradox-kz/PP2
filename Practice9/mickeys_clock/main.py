import pygame
from clock import MickeyClock


def main():
    pygame.init()

    screen = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("Mickey Clock")

    app = MickeyClock(screen)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        app.draw()
        clock.tick(1)

    pygame.quit()


if __name__ == "__main__":
    main()