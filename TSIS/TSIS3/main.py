import pygame
from racer import run_game
from ui import menu, leaderboard_screen

pygame.init()

screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Racer TSIS3")

while True:
    choice = menu(screen)

    if choice == "play":
        run_game(screen)

    elif choice == "leaderboard":
        leaderboard_screen(screen)

    elif choice == "quit":
        pygame.quit()
        exit()