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

	num_poly = 1
	num_vertex = 5
	center = (500,500)
	radius = 100
	polys = []
	move_x = 10
	move_y = 15
	rotation_increment_deg = 0


	for poly in range (0,num_poly):
		poly = Poly(num_vertex,radius,RED, (center[0], (center[1]+ poly*5)), move_x, move_y, radius)
		polys.append(poly)

			
	run = True
	while run == True:

		for deg in range (1,360):
			screen.fill(GRAY)

			for poly in range (0,num_poly):
				
				# # move poly
				# # if you are off screen, reverse direction
				# if (polys[poly].loc[0] + move_x + radius) >= screen_width or (polys[poly].loc[0] + move_x - radius) <=0:
				# 	move_x = move_x * -1
				# if (polys[poly].loc[1] + move_y + radius) >= screen_height or (polys[poly].loc[1] + move_y - radius) <=0:
				# 	move_y = move_y * -1
				# # modify location
				# polys[poly].loc = (polys[poly].loc[0] + move_x, polys[poly].loc[1] + move_y) #polys[poly].loc[0] + 10
				# modify rotation
				polys[poly].update_position(polys, poly)
				polys[poly].draw(deg)

			pygame.display.update()	

			#wait for ESCAPE keypress
			for event in pygame.event.get(): 
				keys = pygame.key.get_pressed()
				if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
					pygame.quit()
					sys.exit()


			pygame.time.wait(25)

				

run_game()
