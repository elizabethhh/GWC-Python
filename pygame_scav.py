
import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
SALMON = (250, 128, 114)
ORANGE = (255, 165, 0)
VIOLET = (148, 0, 211)


size = (350, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

x = y = 0
dx = random.randint(-10,10)
dy = random.randint(-10,10)

radius = random.randint(20,80)

colors = [BLACK, WHITE, RED, BLUE, YELLOW, PINK, SALMON, ORANGE, VIOLET]
length = len(colors) - 1
rand_col = random.randint(0, length)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # --- Game logic should go here

    # --- Screen-clearing code goes here

    screen.fill(GREEN)
    
    # --- Drawing code should go here

    pygame.draw.circle(screen, colors[rand_col], (50+x, 100+y), radius)
    x += dx
    y += dy
    if x < -50 or x > 300:
        dx = -dx
        x += dx
    if y < -100 or y > 400:
        dy = -dy
        y += dy
    
    # --- Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

    clock.tick(60)
    

pygame.quit()
exit() 
