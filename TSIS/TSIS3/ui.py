import pygame
from persistence import load_scores

def menu(screen):
    font = pygame.font.SysFont("Arial", 40)

    while True:
        screen.fill((0,0,0))

        screen.blit(font.render("1 - Play", True, (255,255,255)), (200,200))
        screen.blit(font.render("2 - Leaderboard", True, (255,255,255)), (200,300))
        screen.blit(font.render("3 - Quit", True, (255,255,255)), (200,400))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "play"
                elif event.key == pygame.K_2:
                    return "leaderboard"
                elif event.key == pygame.K_3:
                    return "quit"


def leaderboard_screen(screen):
    scores = load_scores()
    font = pygame.font.SysFont("Arial", 30)

    while True:
        screen.fill((0,0,0))

        y = 100
        for i, s in enumerate(scores[:10]):
            text = f"{i+1}. Score: {s['score']} Dist: {s['distance']}"
            screen.blit(font.render(text, True, (255,255,255)), (100,y))
            y += 40

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return