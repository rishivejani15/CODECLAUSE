import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
PIPE_WIDTH = 50
PIPE_GAP = 150
GRAVITY = 0.25
BIRD_SPEED = -7
FPS = 60
FONT = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Bird variables
bird_radius = 20
bird_x = 50
bird_y = HEIGHT // 2
bird_velocity = 0

# Pipe variables
pipe_x = WIDTH
pipe_gap_y = random.randint(PIPE_GAP, HEIGHT - PIPE_GAP)
pipe_top_height = pipe_gap_y - PIPE_GAP // 2
pipe_bottom_height = HEIGHT - pipe_gap_y - PIPE_GAP // 2
pipe_speed = 3

clock = pygame.time.Clock()
score = 0

# Main game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = BIRD_SPEED

    # Bird physics
    bird_velocity += GRAVITY
    bird_y += bird_velocity

    # Draw bird
    pygame.draw.circle(screen, BLUE, (bird_x, int(bird_y)), bird_radius)

    # Draw pipes
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, PIPE_WIDTH, pipe_top_height))
    pygame.draw.rect(screen, GREEN, (pipe_x, HEIGHT - pipe_bottom_height, PIPE_WIDTH, pipe_bottom_height))

    # Pipe movement
    pipe_x -= pipe_speed

    # Check collision
    bird_rect = pygame.Rect(bird_x - bird_radius, int(bird_y) - bird_radius, bird_radius * 2, bird_radius * 2)
    top_pipe_rect = pygame.Rect(pipe_x, 0, PIPE_WIDTH, pipe_top_height)
    bottom_pipe_rect = pygame.Rect(pipe_x, HEIGHT - pipe_bottom_height, PIPE_WIDTH, pipe_bottom_height)

    if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect) \
            or bird_y - bird_radius <= 0 or bird_y + bird_radius >= HEIGHT:
        running = False

    # Score handling
    if pipe_x + PIPE_WIDTH < bird_x - bird_radius:
        score += 1

    # Generate new pipes
    if pipe_x < -PIPE_WIDTH:
        pipe_x = WIDTH
        pipe_gap_y = random.randint(PIPE_GAP, HEIGHT - PIPE_GAP)
        pipe_top_height = pipe_gap_y - PIPE_GAP // 2
        pipe_bottom_height = HEIGHT - pipe_gap_y - PIPE_GAP // 2

    # Display score
    score_text = FONT.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
