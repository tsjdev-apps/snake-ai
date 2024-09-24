import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game settings
FPS = 10

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Font for score display
font = pygame.font.SysFont('arial', 30)

# Function to draw the grid (optional)
def draw_grid():
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.grow_flag = False

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new_pos = ((cur[0] + (x * CELL_SIZE)) % SCREEN_WIDTH, (cur[1] + (y * CELL_SIZE)) % SCREEN_HEIGHT)

        # If snake collides with itself, game over
        if new_pos in self.positions[2:]:
            self.reset()
        else:
            self.positions = [new_pos] + self.positions[:-1]
            if self.grow_flag:
                self.positions.append(self.positions[-1])
                self.grow_flag = False

    def reset(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def grow(self):
        self.grow_flag = True

    def change_direction(self, dir):
        if (dir[0] * -1, dir[1] * -1) == self.direction:
            return
        else:
            self.direction = dir

    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, self.color, rect)

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                         random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, self.color, rect)

# Main game loop
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    score = 0

    while True:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_w, pygame.K_UP]:
                    snake.change_direction(UP)
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    snake.change_direction(DOWN)
                elif event.key in [pygame.K_a, pygame.K_LEFT]:
                    snake.change_direction(LEFT)
                elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                    snake.change_direction(RIGHT)

        # Move the snake
        snake.move()

        # Check if snake eats the food
        if snake.get_head_position() == food.position:
            snake.grow()
            score += 1
            food.randomize_position()

        # Draw snake and food
        snake.draw(screen)
        food.draw(screen)

        # Display the score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Control the game speed
        clock.tick(FPS)

if __name__ == "__main__":
    main()
