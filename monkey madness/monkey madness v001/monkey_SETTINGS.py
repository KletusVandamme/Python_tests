#test
import pygame, sys, random, math
from monkey_CLASS import *
pygame.init()

myfont = pygame.font.SysFont("Emilbus Mono", 50)

# Screen parameters
screen_width, screen_height = 1400, 800
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
BROWN = (139,69,19)

#game parameters
center = (screen_width/2,screen_height/2)
side_bar_w=200
wait_time_ms = 0

#side_bar properties
side_bar_color = LT_YELLOW

#import images
monkey_image = pygame.image.load("monkey_body_v001.png")
back_image = pygame.image.load("backdrop_v004.png")
arm_left = pygame.image.load("monkey_arm_left_v001.png")
arm_right = pygame.image.load("monkey_arm_right_v001.png")
banana = pygame.image.load("banana v001.png")


