import pygame
from ball import BallGame


def main():
    pygame.init()

    game = BallGame()
    clock = pygame.time.Clock()

    running = True

    while running:
        game.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    game.move(0, -20)

                elif event.key == pygame.K_s:
                    game.move(0, 20)

                elif event.key == pygame.K_a:
                    game.move(-20, 0)

                elif event.key == pygame.K_d:
                    game.move(20, 0)

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()