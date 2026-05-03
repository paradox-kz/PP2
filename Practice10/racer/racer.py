#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
 
#Screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0
 
#Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("images/AnimatedStreet.png")
 
DISPLAYSURF = pygame.display.set_mode((400,600))
pygame.display.set_caption("Game")
 
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
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
                   

# -------- Coin --------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        while True:
            x = random.randint(40, SCREEN_WIDTH-40)
            y = 0
            self.rect.center = (x, y)

            # НЕ пересекаться с врагами
            if not pygame.sprite.spritecollideany(self, enemies):
                break

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()
    

# -------- INIT --------
P1 = Player()
E1 = Enemy()

# СНАЧАЛА создаём enemies
enemies = pygame.sprite.Group()
enemies.add(E1)

# ПОТОМ создаём Coin (важно!)
C1 = Coin()
 
coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
# Speed event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
# -------- GAME LOOP --------
while True:
       
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5     

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))

    # UI
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10,10))

    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 120, 10))
 
    # Draw + move
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    # ---- COIN COLLISION ----
    collected = pygame.sprite.spritecollide(P1, coins, True)
    if collected:
        COINS += 1

        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
    
    # ---- ENEMY COLLISION ----
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('images/crash.wav').play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
           
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)