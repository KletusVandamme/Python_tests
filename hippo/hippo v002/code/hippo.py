#started 26Dec2013

import pygame, sys, random, math
from hippo_SETTINGS import *
from hippo_CLASS_Poly import *

#create instances of screen objects
my_rect = Rect(side_bar_w/2, my_rect_x, rect_w, rect_w, 0, my_rect_color)
side_bar_rect =  Rect(0,0, side_bar_w, screen_height,0, side_bar_color)
my_rect_shadow = Rect(side_bar_w/2,my_rect_x, rect_w, rect_w, 1, BLACK)
rect_hippo = Rect(screen_width/2,screen_height/2, 200, 200, 1, BLACK)
hippo_image = pygame.image.load("hippov001.png")

def run_game():
	#define screen objects

	#place all screen objects into an array, so they can be acted on as a group
	all_obj = (side_bar_rect, my_rect, my_rect_shadow, rect_hippo)

	pygame.init()
	pygame.display.set_caption('Hippo Madness!!!')
	draw_fixed_objects(all_obj)
	pygame.display.update()	


	run = 1
	while run == 1:
		#wait for ESCAPE keypress
		look_for_quit()
		pygame.time.wait(wait_time_ms)

		#detect mouse actions and color, move polygon accordingly
		detect_mouse_actions()
		#draw all objects on screen
		draw_fixed_objects(all_obj)
		#draw variables on screen for debugging
		# draw_var_watches()
		#publish screen to monitor
		screen.blit(hippo_image, (500,200))
		pygame.display.update()
		# check for ESC keypress or window close		


def draw_var_watches():
	a = "hover = " + str(my_rect.hover)
	b = "grab = " + str(my_rect.grab)
	c =  "drop = " + str(my_rect.drop)
	d =  "click = " + str(my_rect.click)

	spacing = 30
	button_text(a, (200, 200 + 1*spacing), color=BLACK, font_size=30)
	button_text(b, (200, 200 + 2*spacing), color=BLACK, font_size=30)
	button_text(c, (200, 200 + 3*spacing), color=BLACK, font_size=30)
	button_text(d, (200, 200 + 4*spacing), color=BLACK, font_size=30)
	print a
	print b
	print c
	print d
	print "----------"
def detect_mouse_actions():
		#detect mouse actions and color polygon accordingly
		my_rect.detect_hover()
		if my_rect.hover == True:
			my_rect.color = my_rect_hover_color

		my_rect.detect_grab()
		if my_rect.grab == True:
			my_rect.color = my_rect_grab_color

		if my_rect.hover == False and my_rect.grab == False and my_rect.drop == False:
			my_rect.color = my_rect_color

		#if the polygon has been grabbed, move it with the mouse
		if my_rect.grab == True:
			my_rect.x = pygame.mouse.get_pos()[0] - my_rect.w/2
			my_rect.y = pygame.mouse.get_pos()[1] - my_rect.h/2

		#look for drop action
		my_rect.detect_drop()
		if my_rect.drop ==True:
			my_rect.color = my_rect_drop_color
			#reset drop to False, since it is a momentary action
			my_rect.drop = False

def draw_fixed_objects(all_obj):
	screen.fill(GRAY)
	for i in range (0, len(all_obj)):
		all_obj[i].draw()

def look_for_quit():
	for event in pygame.event.get(): 
		keys = pygame.key.get_pressed()
		if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()

def button_text(text_display, (location_x, location_y), color=BLACK, font_size=30):
	myfont = pygame.font.SysFont("Arial", font_size)
	label = myfont.render(text_display, 1, color)
	screen.blit(label, (location_x, location_y))

run_game()
