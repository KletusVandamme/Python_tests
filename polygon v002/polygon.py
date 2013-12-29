#started 26Dec2013

import pygame, sys, random, math
# from pygame.locals import *
from polygon_CLASS_Poly import *
from polygon_SETTINGS import *

# screen_width, screen_height = 1000, 1000
# screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

def run_game(): 
	pygame.init()
	screen.fill(GRAY)

	pygame.display.set_caption('Polygon Madness!!!')

	num_poly = 50
	num_vertex = 5
	center = (500,500)
	diameter = 100
	polys = []

	for poly in range (0,num_poly):
		poly = Poly(num_vertex,diameter,RED, (center[0], (center[1]+ poly*5)))
		polys.append(poly)




	poly1 = Poly(num_vertex, diameter, color=RED, loc=center)
	# poly1.create()
			
	run = True
	while run == True:
		for deg in range (1,360):
			screen.fill(GRAY)
			poly1.draw(deg)

			for poly in range (1,num_poly):
				polys[poly].draw(deg)

			pygame.display.update()	

			#wait for ESCAPE keypress
			for event in pygame.event.get(): 
				keys = pygame.key.get_pressed()
				if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
					pygame.quit()
					sys.exit()


			pygame.time.wait(50)

run_game()
