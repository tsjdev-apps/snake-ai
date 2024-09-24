import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
BLOCK_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 30
SCREEN_WIDTH = BLOCK_SIZE * GRID_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock to control frame rate
clock = pygame.time.Clock()

# Snake initial position and body
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = 'RIGHT'

# Initial food position
food_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game over flag
game_over = False

def draw_snake(snake):
    for segment in snake:
        x = segment[0] * BLOCK_SIZE
        y = segment[1] * BLOCK_SIZE
        pygame.draw.rect(screen, GREEN, (x, y, BLOCK_SIZE, BLOCK_SIZE))

def draw_food(position):
    x = position[0] * BLOCK_SIZE
    y = position[1] * BLOCK_SIZE
    pygame.draw.rect(screen, RED, (x, y, BLOCK_SIZE, BLOCK_SIZE))

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a) and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key in (pygame.K_RIGHT, pygame.K_d) and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'
            elif event.key in (pygame.K_UP, pygame.K_w) and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key in (pygame.K_DOWN, pygame.K_s) and snake_direction != 'UP':
                snake_direction = 'DOWN'

    # Update snake position
    head_x, head_y = snake[0]
    if snake_direction == 'LEFT':
        head_x -= 1
    elif snake_direction == 'RIGHT':
        head_x += 1
    elif snake_direction == 'UP':
        head_y -= 1
    elif snake_direction == 'DOWN':
        head_y += 1

    new_head = (head_x, head_y)

    # Check for collisions with boundaries
    if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
        game_over = True
        break

    # Check for collisions with self
    if new_head in snake:
        game_over = True
        break

    # Insert new head
    snake.insert(0, new_head)

    # Check if snake has eaten the food
    if new_head == food_position:
        # Generate new food position
        while True:
            food_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food_position not in snake:
                break
    else:
        # Remove tail segment
        snake.pop()

    # Draw everything
    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food_position)
    pygame.display.flip()

    # Control the frame rate
    clock.tick(10)  # Adjust the speed as necessary

# Game over
pygame.quit()
sys.exit()
