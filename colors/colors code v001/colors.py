#started 26Dec2013

from __future__ import division
import pygame, sys, random, math
from colors_SETTINGS import *
from colors_CLASS import *
from numpy import *



# # from Numeric import *                #import numeric
# a = array((1,2,3,4,5))                 #create an array
# print a                                      #display the array
# print a[2]                                   #index into the array
# print a*2                                    #new array with twiced values

eye_array = []
num_eyes = 8
border = 1

#create an array of eyes
num_x = 9
num_y = 10
x_start = 1
y_start = 1

# pygame.init()
x, y = screen.get_size()

new_rect = Rect(500,500,50,50,0, BLUE)
new_rect.x_move = 50
new_rect.y_move = 15

init_loop = True
main_loop_iteration = 0

def run_game():
	#define screen objects
	pygame.init()
	pygame.display.set_caption('Color Madness!!!')
	# pygame.display.update()	
	global main_loop_iteration
	
	# my_array = pygame.surfarray.array2d(screen)
	# print my_array
	# print zeros(5)

	rect_size = 10
	rect_spacer = 1

	num_row = int(screen_height/(rect_size+ rect_spacer))
	# num_col = 5
	num_col = int(screen_width/(rect_size+ rect_spacer))

	text_box = Rect(200, 200, 300, 300, 0, WHITE)
	text_box_edge = Rect(200, 200, 300, 300, 10, BLACK)


	array_of_rows = []
	array_of_elements =[]
	color = [50,0,00]

	# num_row = 3
	# num_col = 20

	red_min = 0
	red_max = 255
	red_range = (red_max - red_min)

	green_min = 255
	green_max = 0
	green_range = (green_max - green_min)

	blue_min = 0
	blue_max = 255
	blue_range = (blue_max - blue_min)

	#create array
	# for each row
	for x in range (0,num_row):
		array_of_elements = []
		color[0] = int(red_min + x*(red_range/(num_row-1))) # create a spetrcum that goes from red_min to red_max as it moves from top to bottom on the screen
		for y in range (0,num_col):
			color[1] = int(green_min + y*(green_range/(num_col-1))) # create s spetrcum that goes from green_min to green_max as it moves from left to right on the screen
			color[2] = int(blue_min + y*(blue_range/(num_col-1))) # create s spetrcum that goes from blue_min to blue_max as it moves from left to right on the screen
			color_new = tuple(color)

			rect = Rect(y * (rect_size + rect_spacer), x * (rect_size + rect_spacer), rect_size, rect_size, 0, color_new)
			array_of_elements.append(rect)
		array_of_rows.append(array_of_elements)

	run = 1
	while run == 1:
		main_loop_iteration += 1
		#wait for ESCAPE keypress
		look_for_quit()
		# draw screen objects
		screen.fill(BLACK)
		array_of_rows[1][1].draw()

		for x in range (0,num_row):
			for y in range (0,num_col):
				array_of_rows[x][y].draw()

		mouse_x, mouse_y = pygame.mouse.get_pos()
		mouse_x = int(mouse_x)
		mouse_y = int(mouse_y)
		color_pick = array_of_rows[int(mouse_y/rect_size)][int(mouse_x/rect_size)].color
		text_box.color = color_pick
		text_box.draw()
		text_box_edge.draw()
		button_text(str(color_pick), (250, 250), color=BLACK, font_size=30)
		# button_text(str(int(mouse_x)), (200, 300), color=BLACK, font_size=30)
		pygame.display.update()

		pygame.time.wait(50)

#------------------------------------------------------------------------------

def button_text(text_display, (location_x, location_y), color=BLACK, font_size=30):
	myfont = pygame.font.SysFont("Arial", font_size)
	label = myfont.render(text_display, 1, color)
	screen.blit(label, (location_x, location_y))

def look_for_quit():
	for event in pygame.event.get(): 
		keys = pygame.key.get_pressed()
		if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
run_game()
