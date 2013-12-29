#started 26Dec2013

import pygame, sys, random, math
from polygon_CLASS_Poly import *
from polygon_SETTINGS import *

def run_game(): 
	pygame.init()
	screen.fill(GRAY)
	pygame.display.set_caption('Polygon Madness!!!')

	#create polys, put them in an array called "polys"
	for poly in range (0,num_poly):
		poly = Poly(num_vertex,radius,RED, (center[0], (center[1]+ poly*5)), move_x, move_y, radius)
		polys.append(poly)
			
	run = True
	while run == True:

		for deg in range (1,360):
			screen.fill(GRAY)
			for poly in range (0,num_poly):
				polys[poly].update_position(polys, poly)
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
