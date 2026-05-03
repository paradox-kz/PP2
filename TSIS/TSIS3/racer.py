import pygame
import random
import sys

pygame.init()

# -------- SETTINGS --------
WIDTH, HEIGHT = 400, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()

# -------- LOAD IMAGES --------
bg = pygame.image.load("assets/AnimatedStreet.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

player_img = pygame.image.load("assets/Player.png")
player_img = pygame.transform.scale(player_img, (50, 100))

enemy_img = pygame.image.load("assets/Enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (50, 100))

coin_img = pygame.image.load("assets/coin.png")
coin_img = pygame.transform.scale(coin_img, (30, 30))

# 🛡 NEW
shield_img = pygame.image.load("assets/shield.png")
shield_img = pygame.transform.scale(shield_img, (35, 35))

# ⚡ NEW
boost_img = pygame.image.load("assets/boost.png")
boost_img = pygame.transform.scale(boost_img, (35, 35))

# -------- SOUND --------
pygame.mixer.music.load("assets/background.wav")
pygame.mixer.music.play(-1)

crash_sound = pygame.mixer.Sound("assets/crash.wav")

# -------- FONT --------
font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 48)

# -------- GAME VARIABLES --------
player_rect = player_img.get_rect(center=(WIDTH//2, HEIGHT-100))

enemies = []
coins = []
powerups = []

SPEED = 5
score = 0
coin_score = 0

shield = False
boost_active = False
boost_timer = 0
BOOST_DURATION = 3000  # 3 sec

bg_y = 0
coin_angle = 0

# -------- SPAWN --------
def spawn_enemy():
    x = random.randint(50, WIDTH-50)
    rect = enemy_img.get_rect(center=(x, -100))
    enemies.append(rect)

def spawn_coin():
    x = random.randint(50, WIDTH-50)
    rect = coin_img.get_rect(center=(x, -50))
    coins.append(rect)

def spawn_power():
    x = random.randint(50, WIDTH-50)
    rect = pygame.Rect(x, -50, 35, 35)
    p_type = random.choice(["shield", "boost"])
    powerups.append((rect, p_type))

# -------- GAME OVER --------
def game_over():
    crash_sound.play()
    pygame.mixer.music.stop()

    screen.fill((0,0,0))
    text1 = big_font.render("GAME OVER", True, (255,0,0))
    text2 = font.render(f"Score: {score}", True, (255,255,255))

    screen.blit(text1, (80, 200))
    screen.blit(text2, (140, 260))

    pygame.display.flip()
    pygame.time.delay(2000)

# -------- MAIN LOOP --------
running = True
spawn_timer = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # movement
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += 5

    # -------- BOOST LOGIC --------
    current_speed = SPEED
    if boost_active:
        current_speed = SPEED * 2
        if pygame.time.get_ticks() - boost_timer > BOOST_DURATION:
            boost_active = False

    # -------- BACKGROUND --------
    bg_y += current_speed
    if bg_y >= HEIGHT:
        bg_y = 0

    screen.blit(bg, (0, bg_y))
    screen.blit(bg, (0, bg_y - HEIGHT))

    # -------- SPAWN --------
    spawn_timer += 1

    if spawn_timer % 60 == 0:
        spawn_enemy()

    if spawn_timer % 90 == 0:
        spawn_coin()

    if spawn_timer % 200 == 0:
        spawn_power()

    # -------- ENEMIES --------
    for enemy in enemies[:]:
        enemy.y += current_speed

        if enemy.colliderect(player_rect):
            if shield:
                shield = False
                enemies.remove(enemy)
            else:
                game_over()
                running = False

        if enemy.top > HEIGHT:
            enemies.remove(enemy)
            score += 1

        screen.blit(enemy_img, enemy)

    # -------- COINS --------
    coin_angle += 5

    for coin in coins[:]:
        coin.y += current_speed
        rotated = pygame.transform.rotate(coin_img, coin_angle)
        screen.blit(rotated, coin)

        if coin.colliderect(player_rect):
            coin_score += 1
            coins.remove(coin)

        if coin.top > HEIGHT:
            coins.remove(coin)

    # -------- POWER UPS --------
    for p in powerups[:]:
        rect, p_type = p
        rect.y += current_speed

        if p_type == "shield":
            screen.blit(shield_img, rect)
        else:
            screen.blit(boost_img, rect)

        if rect.colliderect(player_rect):
            if p_type == "shield":
                shield = True
            elif p_type == "boost":
                boost_active = True
                boost_timer = pygame.time.get_ticks()

            powerups.remove(p)

        elif rect.top > HEIGHT:
            powerups.remove(p)

    # -------- PLAYER --------
    screen.blit(player_img, player_rect)

    if shield:
        pygame.draw.rect(screen, (0,255,255), player_rect, 3)

    # -------- HUD --------
    score_text = font.render(f"Score: {score}", True, (255,255,255))
    coin_text = font.render(f"Coins: {coin_score}", True, (255,255,0))

    screen.blit(score_text, (10,10))
    screen.blit(coin_text, (10,40))

    if shield:
        screen.blit(shield_img, (300, 10))

    if boost_active:
        screen.blit(boost_img, (300, 50))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()