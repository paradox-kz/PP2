import pygame
from datetime import datetime


class MickeyClock:
    def __init__(self, screen):
        self.screen = screen
        self.width = 1200
        self.height = 900

        self.center = (self.width // 2, self.height // 2)

        self.background = pygame.image.load(
            "images/background.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            (self.width, self.height)
        )

        self.hand = pygame.image.load(
            "images/mickey_hand.png"
        ).convert_alpha()

    def get_angles(self):
        now = datetime.now()

        minute = now.minute
        hour = now.hour

        minute_angle = -(minute * 6)
        second_angle = -(hour*30+minute*0.5)

        return minute_angle, second_angle

    def draw_hand(self, angle, length):
        hand = pygame.transform.scale(
            self.hand,
            (80, length)
        )

        rotated = pygame.transform.rotate(hand, angle)

        rect = rotated.get_rect(center=self.center)

        self.screen.blit(rotated, rect)

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        minute_angle, second_angle = self.get_angles()

        self.draw_hand(minute_angle, 140)
        self.draw_hand(second_angle, 190)

        pygame.display.update()