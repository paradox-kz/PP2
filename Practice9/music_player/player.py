import pygame
import os


class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((700, 400))
        pygame.display.set_caption("Music Player")

        self.font = pygame.font.SysFont("Arial", 28)

        self.playlist = [
            "music/track1.mp3",
            "music/track2.mp3"
        ]

        self.current_track = 0
        self.is_playing = False

        self.track_length = 10  # длина трека в секундах (пример)
        self.load_track()

    def load_track(self):
        track_path = self.playlist[self.current_track]
        pygame.mixer.music.load(track_path)

        sound = pygame.mixer.Sound(track_path)
        self.track_length = int(sound.get_length())

    def play(self):
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.load_track()
        self.play()

    def previous_track(self):
        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.load_track()
        self.play()

    def draw_progress_bar(self):
        current_time = pygame.mixer.music.get_pos() / 1000  # ms → sec

        if current_time < 0:
            current_time = 0

        progress = min(current_time / self.track_length, 1)

        bar_x = 50
        bar_y = 230
        bar_width = 500
        bar_height = 20

        pygame.draw.rect(
            self.screen,
            (100, 100, 100),
            (bar_x, bar_y, bar_width, bar_height)
        )

        pygame.draw.rect(
            self.screen,
            (0, 255, 0),
            (bar_x, bar_y, bar_width * progress, bar_height)
        )

        time_text = self.font.render(
            f"{int(current_time)} / {self.track_length} sec",
            True,
            (255, 255, 255)
        )

        self.screen.blit(time_text, (50, 260))

    def draw(self):
        self.screen.fill((30, 30, 30))

        track_name = os.path.basename(self.playlist[self.current_track])
        status = "Playing" if self.is_playing else "Stopped"

        text1 = self.font.render(
            f"Track: {track_name}",
            True,
            (255, 255, 255)
        )

        text2 = self.font.render(
            f"Status: {status}",
            True,
            (255, 255, 255)
        )

        controls = self.font.render(
            "P Play | S Stop | N Next | B Back | Q Quit",
            True,
            (200, 200, 200)
        )

        self.screen.blit(text1, (50, 80))
        self.screen.blit(text2, (50, 130))
        self.screen.blit(controls, (50, 330))

        self.draw_progress_bar()

        pygame.display.update()