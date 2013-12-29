#started Dec 19
# this is branched from 011 - and uses test3.py and flash_config2.py

import pygame, sys, random, math
from settings import *
# from Functions import *
from classes import *
from pygame.locals import *
from test_modules import *
from Draw_Fixed_Obj import *
from matt_test_CLASS_Box import *

screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

def run_game(): 
	pygame.init()
	screen.fill(GRAY)

	pygame.display.set_caption('Flash Cards')

	num_vertex = 7
	angle_delta = 360/num_vertex
	vertices = []
	center = (500,500)
	diameter = 100


	poly1 = Poly(num_vertex, diameter, color=RED, loc=center)
	poly1.create()
			
	run = True
	while run == True:
		for deg in range (1,360):
			screen.fill(GRAY)
			poly1.draw(deg)
			pygame.display.update()

			#wait for ESCAPE keypress
			for event in pygame.event.get(): 
				keys = pygame.key.get_pressed()
				if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
					pygame.quit()
					sys.exit()


			pygame.time.wait(50)

run_game()
