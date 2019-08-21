
import pygame
import random

pygame.init()

#Define colors
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
colors = [WHITE, RED, BLUE, YELLOW, GREEN, PINK, SALMON, ORANGE, VIOLET]


size = (750, 500)
screen = pygame.display.set_mode(size)

#Title
pygame.display.set_caption("Pong Game")

#Loop until user clicks close button
done = False

x = random.randint(-50,700)
y = 0
dx = random.randint(-10,10)
dy = random.randint(-10,10)

#Set radius of circle
radius = 35


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

    screen.fill(BLACK)
    
    # --- Drawing code should go here
    
    pygame.draw.circle(screen, colors[rand_col], (50+x, 100+y), radius)
    x += dx
    y += dy
    if x < -50 or x > 700:
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
