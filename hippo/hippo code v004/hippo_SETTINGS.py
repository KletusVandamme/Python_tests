#test
import pygame, sys, random, math
pygame.init()

# Screen parameters
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

# Set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 153, 0)
BLUE = (51, 51, 255)
YELLOW = (255, 255, 100)
LT_YELLOW = (255, 255, 150)
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
center = (screen_width/2,screen_height/2)
side_bar_w=200
wait_time_ms = 0

#side_bar properties
side_bar_color = LT_YELLOW



#sky_rect properties
sky_rect_color = SKY
sky_rect_x = 0
sky_rect_y = 0
sky_rect_w = screen_width
sky_rect_h = 450

#hippo image
hippo_x = 300
hippo_y = 200

#food_rect properties
food_rect_color = LIME
food_rect_hover_color = BLUE
food_rect_grab_color = RED
food_rect_x = 200
food_rect_y = hippo_x + 175
food_rect_w = 50

#rectangle for hippo's mouth
rect_hippo_x = hippo_x + 40
rect_hippo_y = hippo_y + 120
rect_hippo_w = 120
rect_hippo_h = 120

