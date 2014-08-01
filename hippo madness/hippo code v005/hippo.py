#started 26Dec2013
#test
from __future__ import division
import pygame, sys, random, math
from hippo_SETTINGS import *
from hippo_CLASS_Poly import *


#create instances of screen objects
# eyeball_image = pygame.image.load("eye_002_100p_v001.png")
# iris_image = pygame.image.load("iris_v002.png")

hippo_image_open = pygame.image.load("hippov001_open.png")
hippo_image_closed = pygame.image.load("hippov001_closed2.png")
iris_image = pygame.image.load("iris_v003.png")
rt_eyeball_image_back = pygame.image.load("rt_eye_back_002_100p.png")
rt_eyeball_front_image = pygame.image.load("rt_eye_front_002_100p.png")

eye_array = []
num_eyes = 4

for i in range (0,num_eyes):
	new_eye = Eye_image(eye_image_x + i* 100, eye_image_y, eye_image_w, eye_image_h, rt_eyeball_image_back, rt_eyeball_front_image, iris_image)
	eye_array.append (new_eye)

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
		# draw screen objects
		screen.fill(GREEN)
		sky_rect.draw()
		pygame.draw.circle(screen, YELLOW, (sun_x,sun_y), sun_diameter, 0)
		my_hippo.draw(main_loop_iteration)
		food_rect_shadow.draw()

		for i in eye_array:
		#update eye target (the point that is to be followed)
			i.target_x = food_rect.x
			i.target_y = food_rect.y
			i.draw()
			pygame.draw.line(screen, BLACK, (food_rect.x, food_rect.y), (i.center_x, i.center_y))
		food_rect.draw()
		pygame.display.update()
		pygame.time.wait(50)

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
