import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display dimensions
dis_width = 800
dis_height = 600

# Border thickness
border_thickness = 10

# Initialize display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Set the clock and snake properties
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 10  # Increased speed

# Set fonts for text
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

"""
border_thickness: int
    The thickness of the border around the game area.

dis: pygame.Surface
    The display surface where the game is rendered.

clock: pygame.time.Clock
    The clock object to control the game's frame rate.

snake_block: int
    The size of each block that makes up the snake.

snake_speed: int
    The speed of the snake, controlling the game's frame rate.

font_style: pygame.font.Font
    The font used for displaying messages on the screen.

score_font: pygame.font.Font
    The font used for displaying the score on the screen.
"""

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Function to display messages on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Initial movement direction
    x1_change = 0
    y1_change = 0

    # Snake properties
    snake_List = []
    Length_of_snake = 1

    # Initial position of the food
    foodx = round(random.randrange(border_thickness, dis_width - snake_block - border_thickness) / 10.0) * 10.0
    foody = round(random.randrange(border_thickness, dis_height - snake_block - border_thickness) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Check for boundary collision
        if x1 >= dis_width - border_thickness or x1 < border_thickness or y1 >= dis_height - border_thickness or y1 < border_thickness:
            game_close = True

        dis.fill(blue)

        # Draw the border
        pygame.draw.rect(dis, white, [0, 0, dis_width, border_thickness])  # Top border
        pygame.draw.rect(dis, white, [0, 0, border_thickness, dis_height])  # Left border
        pygame.draw.rect(dis, white, [0, dis_height - border_thickness, dis_width, border_thickness])  # Bottom border
        pygame.draw.rect(dis, white, [dis_width - border_thickness, 0, border_thickness, dis_height])  # Right border

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check for collision with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        pygame.display.update()

        # Check if snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(border_thickness, dis_width - snake_block - border_thickness) / 10.0) * 10.0
            foody = round(random.randrange(border_thickness, dis_height - snake_block - border_thickness) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()