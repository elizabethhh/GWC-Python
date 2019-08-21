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
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Building():

    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width   = width
        self.height  = height
        self.color   = color

    def draw(self):
        
        pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height])

    def move(self, speedx):
        speedx = -3
        self.x_point += speedx


class Scroller(object):
    def __init__(self, width, height, base, color, speed):
        self.width  = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.buildings = []
        self.add_buildings() # Add builings each time a new instance is created
        #self.scroll_end = scroll_end

    def add_buildings(self):
        """
        Will add a randomly generated building that fits within the width and height
        of the scroller
        """
        current_width = 0 # How wide the scroller is right now
        while current_width <= self.width:
            self.add_building(current_width)
            current_width += self.buildings[-1].width
            #self.scroll_end = current_width

    def add_building(self, x_location):
        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a buildng.
        Adds a building to list of buildings.
        """
        # The building width will be a random integer between 1/20th and 1/4th of the width
        building_width = random.randint((self.width // 20), (self.width // 4))

        max_height = self.base - self.height # this sets the maximum height each building can be

        # The building width will be a random integer between 1/4th and just under the max_height
        building_height = random.randint((max_height // 4), (max_height - 1))

        y_location = self.base - building_height # This tells the building where along the y-axis to draw itself

        self.buildings.append(Building(x_location, y_location, building_width, building_height, self.color))

    def draw_buildings(self):
        """
        This calls the draw method on each building.
        """
        for building in self.buildings:
            building.draw()

    def move_buildings(self):
        for building in self.buildings:
            building.move(self.speed)
        new_building_location = self.buildings[-1].x_point + self.buildings[-1].width

        self.add_building(new_building_location)

    
            

FRONT_SCROLLER_COLOR = (144,238,144)
MIDDLE_SCROLLER_COLOR = (60,179,113)
BACK_SCROLLER_COLOR = (46,139,87)
BACKGROUND_COLOR =(238,232,170)

front_scroller = Scroller(SCREEN_WIDTH, 400, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 150, SCREEN_HEIGHT, MIDDLE_SCROLLER_COLOR, 3)
back_scroller = Scroller(SCREEN_WIDTH, 0, SCREEN_HEIGHT, BACK_SCROLLER_COLOR, 3)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here
    back_scroller.draw_buildings()
    middle_scroller.draw_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()
    middle_scroller.move_buildings()
    back_scroller.move_buildings()
    


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
