"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
possible_colors = [BLACK, WHITE, GREEN, RED, BLUE]
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")

snow_list = []

class SnowFlake():
    '''
    This class will be used to create the SnowFlake Objects.
    It takes: 
        size - an integer that tells us how big we want the snowflake
        position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
        wind - a boolean that lets us know if there is any wind or not.  
    '''
    def __init__(self, size, x_pos, y_pos, xspeed, yspeed, wind=False):
        self.size = size
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.wind = wind
        self.xspeed = xspeed
        self.yspeed = yspeed
    
    def fall(self, screen, screen_height,colors):
        """
        Take in a integer that represnts the speed at which the snowflake is falling in the y-direction.  
        A positive integer will have the snowflake falling down the screen. 
        A negative integer will have the snowflake falling up the screen. 
        
        If wind = True
            - the x direction of the snowflake changes
        """
        snow_color = random.choice(colors)
        wind = True
        for i in range(500):
            
            if wind == True:
                self.x_pos += self.xspeed
            
            if self.y_pos >= screen_height - self.size or self.y_pos < self.size:
                self.yspeed = self.yspeed * -1
            snow_list.append([x_pos,y_pos])
            self.y_pos += self.yspeed
            screen.fill(BLACK)
            pygame.draw.circle(screen, snow_color, [self.x_pos, self.y_pos + i], self.size)
            pygame.display.flip()
    def draw(self):
        """
        Uses pygame and the global screen variable to draw the snowflake on the screen
        """
        

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed

yspeed = random.randint(1, 8)

x_pos = random.randint(0,700)


#INITIALIZE YOUR SNOWFLAKE HERE! 

# Snow List

for i in range(500):
    x_pos = random.randrange(0,700)
    y_pos = random.randrange(0,500)
    snow_list.append([x_pos,y_pos])

wind_set = input("Do you want wind? ")    
if wind_set == "Yes" || wind_set == "yes":
    xspeed = 1
else:
    xspeed = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    
    # Begin Snow
    
    
    
    for i in range(len(snow_list)):
        pygame.draw.circle(screen,random.choice(possible_colors),snow_list[i],1)
        snow_list[i][1] += 1
        snow_list[i][0] += xspeed
        if snow_list[i][1] > 500:
            y_pos = random.randrange(-50, -10)
            snow_list[i][1] = y_pos
            x_pos = random.randrange(-700,700)
            snow_list[i][0] = x_pos
    


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
