import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPEED = 5
SCORE = 0
COINS = 0

font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 60)
game_over = big_font.render("Game Over", True, BLACK)

# Background
background = pygame.image.load("images/AnimatedStreet.png")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Practice 11")

# -------- Enemy --------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.reset()

# -------- Player --------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed = pygame.key.get_pressed()

        if self.rect.left > 0 and pressed[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH and pressed[K_RIGHT]:
            self.rect.move_ip(5, 0)

# -------- Coin --------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # value: 1 or 5
        self.value = random.choice([1, 5])

        if self.value == 5:
            self.image = pygame.image.load("images/gold_coin.png")
        else:
            self.image = pygame.image.load("images/coin.png")

        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

        self.reset()

    def reset(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

# -------- INIT --------
P1 = Player()
E1 = Enemy()

# создаём несколько монет
coins = pygame.sprite.Group()
for _ in range(3):
    c = Coin()
    coins.add(c)

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
for c in coins:
    all_sprites.add(c)

# speed increase timer
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# -------- GAME LOOP --------
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))

    # ---- UI ----
    score_text = font.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font.render(f"Coins: {COINS}", True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (SCREEN_WIDTH - 120, 10))

    # ---- DRAW ----
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # ---- COIN COLLISION ----
    collected = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected:
        COINS += coin.value

        # создаём новую монету
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

        # ---- SPEED FROM COINS ----
        if COINS % 5 == 0:
            SPEED += 1

    # ---- ENEMY COLLISION ----
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("images/crash.wav").play()
        time.sleep(0.5)

        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()

        for e in all_sprites:
            e.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)