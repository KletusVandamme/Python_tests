# this code tests numpy array funtions

from __future__ import division
import pygame, sys, random, math
from numpy import *
pygame.init()
# threed_array[0,0,0]

def reverse_image(threed_array):
	print threed_array[1]

def run_game():
	# run some basic tests of numpy array operations
	# basic_tests()
	# Screen parameters
	screen_width, screen_height = 500, 500
	screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
	rt_eyeball_image_back = pygame.image.load("eye_back_002_100p.png")

	screen.fill(WHITE)
	screen.blit(rt_eyeball_image_back, (100,100))

	#convert screen into 3D array of pixels
	threed_array = pygame.surfarray.pixels3d(screen)
	twod_array = pygame.surfarray.pixels2d(screen)
	#change the color of a single pixel
	# threed_array[1,1] = [0,0,0]
	for i in range (0,screen_height):
		threed_array[i,i] = [0,0,0]
	new = transpose(twod_array)
	# reverse_image(threed_array)

	# print threed_array
	pygame.surfarray.blit_array(screen, twod_array)

	pygame.display.update()


	# print my_array

	while True:
		look_for_quit()


def basic_tests():
	def print_array():
		print "print array"
		print new_array
		print ""

	# initialize array
	num_row = 3
	num_col = 5
	new_array = zeros((num_row,num_col))
	print_array()

	# programatically replace values
	place(new_array, new_array==0, 5)

	#set single value
	new_array[2,2] = 8

	# get single value
	print "get single value"
	print new_array[2,2]
	print ""

	print_array()

def look_for_quit():
	for event in pygame.event.get(): 
		keys = pygame.key.get_pressed()
		if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()


BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 153, 0)
BLUE = (51, 51, 255)
YELLOW = (255, 255, 100)
run_game()
