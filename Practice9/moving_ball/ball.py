import pygame


class BallGame:
    def __init__(self):
        self.width = 600
        self.height = 400
        self.radius = 25
        self.step = 20

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Moving Ball Game")

        self.x = self.width // 2
        self.y = self.height // 2

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if self.radius <= new_x <= self.width - self.radius:
            self.x = new_x

        if self.radius <= new_y <= self.height - self.radius:
            self.y = new_y

    def draw(self):
        self.screen.fill((255, 255, 255))

        pygame.draw.circle(
            self.screen,
            (255, 0, 0),
            (self.x, self.y),
            self.radius
        )

        pygame.display.update()