import pygame

# Initialize Pygame
pygame.init()

# Set the screen size and background color
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
BG_COLOR = (255, 255, 255)

# Create a Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption('Move the Square')

# Set the dimensions of the square
SQUARE_SIZE = 50
SQUARE_COLOR = (0, 0, 0)

# Set the number of rows and columns in the grid
GRID_ROWS = 20
GRID_COLS = 20

# Calculate the width and height of each grid cell
CELL_WIDTH = SCREEN_WIDTH // GRID_COLS
CELL_HEIGHT = SCREEN_HEIGHT // GRID_ROWS

# Set the initial position of the square
square_row = 0
square_col = 0

# Set the movement speed of the square
MOVE_SPEED = 1
fps_controller = pygame.time.Clock()
# Set the direction of the square's movement
# Possible values: "up", "down", "left", "right"
rettning = "up"

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw the grid
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)

    # Move the square
    if event.type == pygame.KEYDOWN:
        if(event.key == pygame.K_UP or event.key == ord("w") and rettning != "DOWN"):
                rettning = "up"
        if(event.key == pygame.K_DOWN or event.key == ord("s") and rettning != "UP"):
                rettning = "down"
        if(event.key == pygame.K_LEFT or event.key == ord("a") and rettning != "RIGHT"):
                rettning = "left"
        if(event.key == pygame.K_RIGHT or event.key == ord("d") and rettning != "LEFT"):
                rettning = "right"
    if rettning == "right":
        square_col += MOVE_SPEED
        if square_col > GRID_COLS - 1:
            square_col = GRID_COLS - 1
            rettning = "down"
    elif rettning == "down":
        square_row += MOVE_SPEED
        if square_row > GRID_ROWS - 1:
            square_row = GRID_ROWS - 1
            rettning = "left"
    elif rettning == "left":
        square_col -= MOVE_SPEED
        if square_col < 0:
            square_col = 0
            rettning = "up"
    elif rettning == "up":
        square_row -= MOVE_SPEED
        if square_row < 0:
            square_row = 0
            rettning = "right"

    # Draw the square
    rect = (square_col * CELL_WIDTH, square_row * CELL_HEIGHT, SQUARE_SIZE, SQUARE_SIZE)
    pygame.draw.rect(screen, SQUARE_COLOR, rect)

    # Update the display
    pygame.display.update()
    fps_controller.tick(MOVE_SPEED)