
import pygame, sys, random, math
pygame.init()

# Screen parameters
screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

# Set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 153, 0)
BLUE = (51, 51, 255)
YELLOW = (255, 255, 156)
LIME = (0, 255, 0)
GRAY = (126, 126, 126) 
CYAN = (  0, 255, 255)
SKY = (135, 206, 250)
SKY2 = (176, 226, 255)
SLATE = (112, 128, 144)
MATT_01 = (102,153,102)
MATT_02 = (102,153,128)
MATT_03 = (102,153,153)        
MATT_04 = (102,128,102)
MATT_05 = (192,192,192)
# background_color = SLATE

DICT_color = {1: BLUE, 2: RED, 3: BLACK, 4: GREEN}

#game parameters
num_poly = 3
num_vertex = 3
center = (screen_width/2,screen_height/2)
radius = 100
polys = []
move_x = 6
move_y = 9
rotation_increment_deg = 10
wait_time_ms = 70





