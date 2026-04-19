import pygame
import random
import sys

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Practice 11")

clock = pygame.time.Clock()

# Colors
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)

# Snake
snake = [(100,100), (80,100), (60,100)]
direction = (CELL, 0)

# ---- FOOD WITH WEIGHT ----
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)

        if (x, y) not in snake:
            # value 1 or 3
            value = random.choice([1, 3])
            return {"pos": (x, y), "value": value, "timer": 0}

food = generate_food()

# Score & level
score = 0
level = 1
speed = 10

font = pygame.font.SysFont("Verdana", 20)

# -------- GAME LOOP --------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL):
                direction = (0, -CELL)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                direction = (0, CELL)
            elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                direction = (-CELL, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                direction = (CELL, 0)

    # ---- MOVE ----
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # WALL COLLISION
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        break

    # SELF COLLISION
    if head in snake:
        break

    snake.insert(0, head)

    # ---- FOOD TIMER ----
    food["timer"] += 1

    # если еда "протухла"
    if food["timer"] > 150:
        food = generate_food()

    # ---- EAT FOOD ----
    if head == food["pos"]:
        score += food["value"]
        food = generate_food()

        # ---- LEVEL ----
        if score % 5 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # ---- DRAW ----
    screen.fill(BLACK)

    # Snake
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, CELL, CELL))

    # Food (цвет зависит от value)
    if food["value"] == 3:
        pygame.draw.rect(screen, YELLOW, (*food["pos"], CELL, CELL))
    else:
        pygame.draw.rect(screen, RED, (*food["pos"], CELL, CELL))

    # UI
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
sys.exit()