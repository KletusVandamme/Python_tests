#started 26Dec2013

import pygame, sys, random, math
from hippo_SETTINGS import *
from hippo_CLASS_Poly import *

#create instances of screen objects
hippo_image_open = pygame.image.load("hippov001_open.png")
hippo_image_closed = pygame.image.load("hippov001_closed2.png")
my_hippo = Hippo(hippo_x, hippo_y, hippo_image_open, hippo_image_closed)
food_rect = Rect(food_rect_x, food_rect_y, food_rect_w, food_rect_w, 0, food_rect_color)
food_rect_shadow = Rect(food_rect_x, food_rect_y, food_rect_w, food_rect_w, 1, BLACK)
sky_rect = Rect(sky_rect_x, sky_rect_y, sky_rect_w, sky_rect_h, 0, sky_rect_color)
side_bar_rect =  Rect(0,0, side_bar_w, screen_height,0, side_bar_color)
side_bar_rect_outline =  Rect(0,0, side_bar_w, screen_height,1, BLACK)
rect_hippo = Rect(rect_hippo_x,rect_hippo_y, rect_hippo_w, rect_hippo_h, 1, BLACK)

init_loop = True
main_loop_iteration = 0

def run_game():
	#define screen objects

	#place all screen objects into an array, so they can be acted on as a group
	# all_obj = (side_bar_rect, food_rect, food_rect_shadow, rect_hippo)
	pygame.init()
	pygame.display.set_caption('Hippo Madness!!!')
	pygame.display.update()	
	global main_loop_iteration
	
	#initialize local variables
	hippo_open = True
	hippo_image = hippo_image_open
	init_loop = False

	run = 1
	while run == 1:
		main_loop_iteration += 1
		#wait for ESCAPE keypress
		look_for_quit()
		pygame.time.wait(wait_time_ms)

		my_hippo.is_beg == True

		#detect mouse actions and color, move polygon accordingly
		detect_mouse_actions()

		#draw all objects on screen
		screen.fill(GREEN)
		sky_rect.draw()
		pygame.draw.circle(screen, YELLOW, (800,100), 30, 0)
		my_hippo.draw(main_loop_iteration)
		# rect_hippo.draw()
		food_rect.draw()
		food_rect_shadow.draw()

		# draw_var_watches()
		#publish screen to monitor
		pygame.display.update()
		# check for ESC keypress or window close		

#------------------------------------------------------------------------------

def detect_mouse_actions():
		#detect mouse actions and color polygon accordingly
		food_rect.detect_hover()
		food_rect.detect_grab()

		if food_rect.hover == False and food_rect.grab == False and food_rect.drop == False:
			food_rect.color = food_rect_color

		#if the polygon has been grabbed, move it with the mouse
		if food_rect.grab == True:
			food_rect.x = pygame.mouse.get_pos()[0] - food_rect.w/2
			food_rect.y = pygame.mouse.get_pos()[1] - food_rect.h/2

		#look for drop action
		food_rect.detect_drop()
		if food_rect.drop ==True:
			food_rect.color = food_rect_color
			#reset drop to False, since it is a momentary action
			food_rect.drop = False

		#look for food in hippo mouth
		food_rect.detect_in_mouth(rect_hippo)
		if food_rect.is_in_mouth ==True:
			food_rect.color = LIME
			
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
