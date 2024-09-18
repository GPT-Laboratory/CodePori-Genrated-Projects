import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define the screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Define snake properties
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Define the clock for controlling the game's speed
clock = pygame.time.Clock()

# Define fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the player's score
def show_score(score):
    value = score_font.render(f"Your Score: {score}", True, WHITE)
    screen.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])

# Function to display a message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

# The main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Movement deltas
    dx = 0
    dy = 0

    # Snake body and length
    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            show_score(snake_length - 1)
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
                if event.key == pygame.K_LEFT:
                    dx = -SNAKE_BLOCK
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = SNAKE_BLOCK
                    dy = 0
                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -SNAKE_BLOCK
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = SNAKE_BLOCK

        # Boundaries check
        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
            game_close = True
        x += dx
        y += dy
        screen.fill(BLACK)

        # Draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        # Update snake's head position
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collisions with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        # Check if the snake eats the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Start the game
game_loop()
