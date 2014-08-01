#started 26Dec2013

import pygame, sys, random, math
from polygon_SETTINGS import *
from polygon_CLASS_Poly import *

wait_time_ms = 70

def run_game(): 
	pygame.init()
	screen.fill(LIME)
	pygame.display.set_caption('Polygon Madness!!!')
	global rotation_increment_deg
	global wait_time_ms

	#create polys, put them in an array called "polys"
	for i in range (0,num_poly):
		#create a random color for each poly
		poly_color = DICT_color[random.randint(1, len(DICT_color))]
		# num_vertex = random.randint(1, 7)
		num_vertex = 5
		
		poly = Poly(num_vertex, radius, poly_color, (center[0] + i*10, (center[1]+ i*5)), move_x, move_y, radius, rot_angle_deg=10)
		polys.append(poly)



	deg = 0
	run = True
	while run == True:

		deg += rotation_increment_deg
		if deg > 360:
			deg -= 360

		screen.fill(LIME)
		for i in range (0,num_poly):
			this_poly = polys[i]
			#rotate each poly

			this_poly.rot_angle_deg += this_poly.spin_rate_deg
			this_poly.rotate(deg)
			#move each poly
			this_poly.update_position(polys, poly)			
			#draw each ploy
			this_poly.draw()

		pygame.display.update()	

		#wait for ESCAPE keypress
		for event in pygame.event.get(): 
			keys = pygame.key.get_pressed()
			if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()

		pygame.time.wait(wait_time_ms)
run_game()
