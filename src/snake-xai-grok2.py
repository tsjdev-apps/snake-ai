import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Screen dimensions
width = 800
height = 600

# Snake and food size
block_size = 20

# Game window
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game by Grok 2')

# Clock to control game speed
clock = pygame.time.Clock()

# Font for game over message
font_style = pygame.font.SysFont(None, 50)

def our_snake(block_size, snake_list):
    """Draw the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], block_size, block_size])

def message(msg, color):
    """Display a message on the screen."""
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = width / 2
    y1 = height / 2

    # Change in snake position
    x1_change = 0       
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            game_display.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    x1_change = block_size
                    y1_change = 0
                elif event.key in [pygame.K_UP, pygame.K_w]:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    y1_change = block_size
                    x1_change = 0

        # Check if snake hits the boundary
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_display.fill(black)
        
        # Draw food
        pygame.draw.rect(game_display, red, [foodx, foody, block_size, block_size])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        our_snake(block_size, snake_List)
        pygame.display.update()

        # Check if snake ate the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(15)  # Snake speed

    pygame.quit()
    quit()

game_loop()