# this code tests numpy array funtions

from __future__ import division
import pygame, sys, random, math
from numpy import *
pygame.init()

def run_game():
	# run some basic tests of numpy array operations
	# basic_tests()
	# Screen parameters
	screen_width, screen_height = 1000, 500
	screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
	screen.fill(WHITE)

	#convert screen into a 2D array of pixels, modify a pixel in the array, then blit array
	# my_array = pygame.surfarray.array2d(screen)
	# my_array[5,5] = 0
	# pygame.surfarray.blit_array(screen, my_array)


	#convert screen into 3D array of pixels
	threed_array = pygame.surfarray.pixels3d(screen)
	#change the color of a single pixel
	# threed_array[1,1] = [0,0,0]
	for i in range (0,screen_height - 0):
		threed_array[i,i] = [0,0,0]

	# print threed_array
	pygame.surfarray.blit_array(screen, threed_array)

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
