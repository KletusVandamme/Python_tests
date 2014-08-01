#started 26Dec2013
#test
from __future__ import division
import pygame, sys, random, math
from eyeballs_SETTINGS import *
from eyeballs_CLASS import *
# from matt_stuff import *

# from matt_stuff import *from matt_stuff import *

#create instances of screen objects

iris_image = pygame.image.load("iris_v003.png")
rt_eyeball_image_back = pygame.image.load("rt_eye_back_002_100p.png")
rt_eyeball_front_image = pygame.image.load("rt_eye_front_002_100p.png")
fur_ball = pygame.image.load("eyeball_v003.png")
fur_ball2 = pygame.image.load("eyeball_v003.png")

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
print screen.get_size()

new_rect = Rect(500,500,50,50,0, YELLOW)
new_rect.x_move = 50
new_rect.y_move = 15

#create multiple rows
for j in range (0,num_y):
	#create single row
	for i in range (0,num_x):
		new_eye = Eye_image(x_start + i* (eye_image_w + border), y_start + j*(eye_image_h + border), eye_image_w, eye_image_h, rt_eyeball_image_back, rt_eyeball_front_image, iris_image)
		eye_array.append (new_eye)

food_rect = Rect(food_rect_x, food_rect_y, food_rect_w, food_rect_w, 0, food_rect_color)
food_rect_shadow = Rect(food_rect_x, food_rect_y, food_rect_w, food_rect_w, 1, BLACK)
sky_rect = Rect(sky_rect_x, sky_rect_y, sky_rect_w, sky_rect_h, 0, sky_rect_color)
side_bar_rect =  Rect(0,0, side_bar_w, screen_height,0, side_bar_color)
side_bar_rect_outline =  Rect(0,0, side_bar_w, screen_height,1, BLACK)

init_loop = True
main_loop_iteration = 0

def run_game():
	#define screen objects

	#place all screen objects into an array, so they can be acted on as a group
	# all_obj = (side_bar_rect, food_rect, food_rect_shadow, rect_hippo)
	pygame.init()
	pygame.display.set_caption('Eyeball Madness!!!')
	pygame.display.update()	
	global main_loop_iteration
	
	#initialize local variables
	init_loop = False

	run = 1
	while run == 1:
		main_loop_iteration += 1
		#wait for ESCAPE keypress
		look_for_quit()
		pygame.time.wait(wait_time_ms)

		#detect mouse actions and color, move polygon accordingly
		detect_mouse_actions()
		# draw screen objects
		screen.fill(YELLOW)
		# pygame.draw.circle(screen, YELLOW, (sun_x,sun_y), sun_diameter, 0)

		for i in eye_array:
		#update eye target (the point that is to be followed)
			i.target_x = new_rect.x
			i.target_y = new_rect.y
			i.draw()

		# new_rect.draw()
		new_rect.x += new_rect.x_move
		new_rect.y += new_rect.y_move
		if new_rect.x - 1*fur_ball_w < 0 or new_rect.x + 1*fur_ball_w > screen_width:
			new_rect.x_move *= -1
		if new_rect.y - 1*fur_ball_h < 0 or new_rect.y + 1*fur_ball_h > screen_height:
			new_rect.y_move *= -1

		screen.blit(fur_ball, (new_rect.x - fur_ball_w/2, new_rect.y - fur_ball_h/2))
		screen.blit(fur_ball, (new_rect.x - fur_ball_w/2, new_rect.y - fur_ball_h/2))
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
