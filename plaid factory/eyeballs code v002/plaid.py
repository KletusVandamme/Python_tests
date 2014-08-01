#started 26Dec2013
#test
from __future__ import division
import pygame, sys, random, math
from plaid_SETTINGS import *
from plaid_CLASS import *
from pygame.locals import *
from colors import *
import copy

def run_game():
	#define screen objects
	swatch_0_x = 50
	swatch_0_y = 200
	swatch_w = 100
	swatch_h = 100

	swatch_0 = Swatch(swatch_0_x, swatch_0_y, swatch_w, swatch_h, YELLOW)
	
	swatch_array_start_x = swatch_w*2

	pygame.init()
	pygame.display.set_caption('Plaid Madness!!!')
	side_bar_rect = Rectangle(0,0,swatch_0_x + swatch_w*1.25,screen_height,0, SKY)
	mousex = 0
	mousey = 0
	mouseClicked = False

	while True:
		pygame.time.wait(wait_time_ms)

		screen.fill(SLATE)
		side_bar_rect.draw()
		swatch_0.draw()
		draw_picker()

		for event in pygame.event.get(): 
			keys = pygame.key.get_pressed() 
			if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()	
			if event.type == MOUSEBUTTONUP:
				new_color = color_picker()
				print new_color
				mousex, mousey = event.pos
				sw0_offset = (mousex - swatch_0.x)
				swatch_0.add_stripe(sw0_offset, True, new_color)

		# create some new swatches
		for i in range (0,7):
			new_swatch = copy.deepcopy(swatch_0)
			#create evenly spaced swatches
			new_swatch.x = (swatch_array_start_x + i*(swatch_w -1))

			# if stripe has been copied, update stripe locations, by taking the difference between (the x locations of the new swatch and swatch_0) and adding the position of the same stripe in swatch_0.  This could probably be simpler
			for i in range (0, len(new_swatch.stripe_array)):
				new_swatch.stripe_array[i].start_pos = (new_swatch.x - swatch_0.x + swatch_0.stripe_array[i].start_pos[0], new_swatch.y)
				new_swatch.stripe_array[i].end_pos = (new_swatch.x - swatch_0.x + swatch_0.stripe_array[i].start_pos[0], new_swatch.bottom)

			new_swatch.draw()
			# swatch_array.append(new_swatch)

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


box_height = 100
box_width = 100

rect_size = 2
rect_spacer = 0

num_row = int(box_height/(rect_size+ rect_spacer))
num_col = int(box_width/(rect_size+ rect_spacer))

array_of_rows = []
array_of_elements =[]
color = [50,0,00]

red_min = 0
red_max = 255
red_range = (red_max - red_min)

green_min = 255
green_max = 0
green_range = (green_max - green_min)

blue_min = 0
blue_max = 255
blue_range = (blue_max - blue_min)


def draw_picker():
	#create array
	# for each row
	for x in range (0,num_row):
		array_of_elements = []
		color[0] = int(red_min + x*(red_range/(num_row-1))) # create s spetrcum that goes from red_min to red_max as it moves from top to bottom on the screen
		for y in range (0,num_col):
			color[1] = int(green_min + y*(green_range/(num_col-1))) # create s spetrcum that goes from green_min to green_max as it moves from left to right on the screen
			color[2] = int(blue_min + y*(blue_range/(num_col-1))) # create s spetrcum that goes from blue_min to blue_max as it moves from left to right on the screen
			color_new = tuple(color)
			rect = Rect(y * (rect_size + rect_spacer), x * (rect_size + rect_spacer), rect_size, rect_size, 0, color_new)
			array_of_elements.append(rect)
		array_of_rows.append(array_of_elements)

	# draw screen objects
	background = Rectangle(0, 0, box_height, box_width, 0, BLACK)
	background.draw()
	array_of_rows[1][1].draw()
	for x in range (0,num_row):
		for y in range (0,num_col):
			array_of_rows[x][y].draw()
	pygame.display.update()


def color_picker():

	draw_picker()
	while True:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		mouse_x = int(mouse_x)
		mouse_y = int(mouse_y)

		pygame.time.wait(50)

		#wait for ESCAPE keypress
		for event in pygame.event.get(): 
			keys = pygame.key.get_pressed()
			if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
				return color_pick
			if event.type == MOUSEBUTTONUP:
				if mouse_x > 0 and mouse_x < box_width and mouse_y > 0 and mouse_y < box_height:
					color_pick = array_of_rows[int(mouse_y/rect_size)][int(mouse_x/rect_size)].color
					return color_pick

run_game()
