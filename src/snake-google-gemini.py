import pygame
import random

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SNAKE_SIZE = 10
FOOD_SIZE = 10
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling game speed
clock = pygame.time.Clock()

# Snake and food initial positions
snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
food = (random.randint(0, SCREEN_WIDTH // SNAKE_SIZE) * SNAKE_SIZE,
        random.randint(0, SCREEN_HEIGHT // SNAKE_SIZE) * SNAKE_SIZE)

# Initialize direction
direction = "right"

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        direction = "up"
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        direction = "down"
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        direction = "left"
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        direction = "right"

    # Update snake position based on direction
    if direction == "up":
        x, y = snake[0]
        snake.insert(0, (x, y - SNAKE_SIZE))
    elif direction == "down":
        x, y = snake[0]
        snake.insert(0, (x, y + SNAKE_SIZE))
    elif direction == "left":
        x, y = snake[0]
        snake.insert(0, (x - SNAKE_SIZE, y))
    elif direction == "right":
        x, y = snake[0]
        snake.insert(0, (x + SNAKE_SIZE, y))

    # Check if snake has eaten food
    if snake[0] == food:
        food = (random.randint(0, SCREEN_WIDTH // SNAKE_SIZE) * SNAKE_SIZE,
                random.randint(0, SCREEN_HEIGHT // SNAKE_SIZE) * SNAKE_SIZE)
    else:
        snake.pop()

    # Check for collision with self or boundaries
    if snake[0] in snake[1:] or snake[0][0] < 0 or snake[0][0] >= SCREEN_WIDTH or snake[0][1] < 0 or snake[0][1] >= SCREEN_HEIGHT:
        running = False

    # Draw background, snake, and food
    screen.fill(BACKGROUND_COLOR)
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], FOOD_SIZE, FOOD_SIZE))

    # Update display
    pygame.display.flip()

    # Control game speed
    clock.tick(10)

# Quit Pygame
pygame.quit()